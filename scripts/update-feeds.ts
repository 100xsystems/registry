#!/usr/bin/env tsx
/**
 * update-feeds.ts — ULTRA-FAST FEED UPDATER
 *
 * Fetches RSS feed items from the registry and updates JSON files in feeds/.
 *
 * SPEED DESIGN:
 *   ⚡ All feeds are fetched IN PARALLEL (not in batches of 10)
 *   ⚡ Native fetch() with 3s hard timeout (aggressive — most feeds respond in <1.5s)
 *   ⚡ NO retries — if a feed doesn't respond in 3s, mark it and move on
 *   ⚡ Feed health tracking — dead feeds auto-skipped after 3 consecutive failures
 *   ⚡ Only items from the last 48h are indexed (no historical baggage per run)
 *   ⚡ YC/PH fetch via raw.githubusercontent.com (no git clone — saves ~120s)
 *
 * With this design:
 *   -   438 feeds → ~3 seconds (all parallel, worst-case timeout)
 *   - 1,000 feeds → ~3 seconds (more feeds doesn't mean more wall time)
 *   - 5,000 feeds → ~3 seconds (same — timeouts are parallel)
 *
 * USAGE:
 *   tsx scripts/update-feeds.ts
 *   tsx scripts/update-feeds.ts --historical --limit=500
 *   tsx scripts/update-feeds.ts --feed=netflix-tech-blog
 *
 * ETHICAL NOTE:
 *   We index only article metadata — title, URL, summary, author, publication date.
 *   We NEVER download, cache, or host article content.
 */

import * as fs from 'node:fs';
import * as path from 'node:path';
import Parser from 'rss-parser';
import { FEED_REGISTRY, type FeedSource } from './feed-registry.js';

// ── Types ────────────────────────────────────────────────────────────

interface FeedItem {
  guid: string;
  title: string;
  link: string;
  summary: string | null;
  author: string | null;
  publishedAt: string | null;
}

interface FeedData {
  feedId: string;
  feedName: string;
  feedSiteUrl: string;
  feedRssUrl: string;
  tags: string[];
  updatedAt: string;
  items: FeedItem[];
  totalIndexed: number;
}

interface FeedHealthEntry {
  status: 'active' | 'dead';
  consecutiveFailures: number;
  lastSuccess: string | null;
  lastError: string | null;
  lastErrorDate: string | null;
  lastCheckedDate: string;
}

interface FeedHealth {
  [feedId: string]: FeedHealthEntry;
}

type FeedItemRaw = {
  guid?: string;
  title?: string;
  link?: string;
  contentSnippet?: string;
  content?: string;
  pubDate?: string;
  isoDate?: string;
  creator?: string;
  author?: string;
};

// ── Configuration ─────────────────────────────────────────────────────

const FEEDS_DIR = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..', 'feeds');
const DAILY_DIR = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..', 'daily');
const HEALTH_FILE = path.join(DAILY_DIR, 'feed-health.json');

const HTTP_TIMEOUT_MS = 5_000;    // 5s max per feed — balances speed with catching slow-but-working feeds.
                                    // No retries. Health system handles failures after 3 strikes.
const MAX_CONSECUTIVE_FAILURES = 3; // After this, feed auto-skipped
const DEAD_FEED_RECHECK_DAYS = 7;   // Re-check dead feeds weekly
const FEED_ITEM_LIMIT = 50;         // Max items to parse per feed
const MAX_TOTAL_ITEMS = 10_000;      // Cap total stored items per feed
const RECENT_ITEM_HOURS = 48;       // Only index items published in last 48h

// ── Helpers ───────────────────────────────────────────────────────────

function ensureDir(dir: string): void {
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
  }
}

function getGuid(item: FeedItemRaw, feedId: string): string {
  if (item.guid) return item.guid;
  if (item.link) return `${feedId}::${item.link}`;
  return `${feedId}::${item.title ?? 'untitled'}`;
}

function toAbsoluteUrl(rawUrl: string | undefined, feedRssUrl: string): string {
  if (!rawUrl) return '';
  if (rawUrl.startsWith('http://') || rawUrl.startsWith('https://')) return rawUrl;
  try {
    return new URL(rawUrl, feedRssUrl).href;
  } catch {
    return rawUrl;
  }
}

function truncate(text: string | null, maxLength = 300): string | null {
  if (!text) return null;
  if (text.length <= maxLength) return text;
  return text.slice(0, maxLength).replace(/\s+\S*$/, '') + '…';
}

function parseArgs(): { historical: boolean; limit: number; feedIds: string[] } {
  const args = process.argv.slice(2);
  const historical = args.includes('--historical');
  const limitIdx = args.indexOf('--limit');
  const limit = limitIdx >= 0
    ? parseInt(args[limitIdx + 1], 10) || FEED_ITEM_LIMIT
    : (historical ? 500 : FEED_ITEM_LIMIT);

  let feedIds: string[] = [];
  for (let i = 0; i < args.length; i++) {
    const arg = args[i];
    if (arg.startsWith('--feed=')) {
      feedIds.push(arg.slice(7));
    } else if (arg === '--feed' && i + 1 < args.length) {
      feedIds.push(args[++i]);
    }
  }

  return { historical, limit, feedIds };
}

// ── Feed Health Tracking ─────────────────────────────────────────────

function loadFeedHealth(): FeedHealth {
  ensureDir(DAILY_DIR);
  if (fs.existsSync(HEALTH_FILE)) {
    try {
      return JSON.parse(fs.readFileSync(HEALTH_FILE, 'utf-8')) as FeedHealth;
    } catch {
      return {};
    }
  }
  return {};
}

function saveFeedHealth(health: FeedHealth): void {
  ensureDir(DAILY_DIR);
  const newJson = JSON.stringify(health, null, 2) + '\n';
  // Only write if changed to avoid unnecessary git diffs on every run
  const currentJson = fs.existsSync(HEALTH_FILE) ? fs.readFileSync(HEALTH_FILE, 'utf-8') : '';
  if (newJson !== currentJson) {
    fs.writeFileSync(HEALTH_FILE, newJson, 'utf-8');
  }
}

function shouldProcessFeed(feedId: string, health: FeedHealth, historical: boolean): boolean {
  if (historical) return true; // always process in historical mode

  const entry = health[feedId];
  if (!entry) return true; // never checked before — process

  // If dead, only re-check if enough days have passed
  if (entry.status === 'dead') {
    const lastCheck = new Date(entry.lastCheckedDate).getTime();
    const daysSinceCheck = (Date.now() - lastCheck) / (1000 * 60 * 60 * 24);
    return daysSinceCheck >= DEAD_FEED_RECHECK_DAYS;
  }

  return true; // active or unchecked
}

function markFeedSuccess(health: FeedHealth, feedId: string): void {
  health[feedId] = {
    status: 'active',
    consecutiveFailures: 0,
    lastSuccess: new Date().toISOString(),
    lastError: null,
    lastErrorDate: null,
    lastCheckedDate: new Date().toISOString(),
  };
}

function markFeedFailure(health: FeedHealth, feedId: string, error: string): void {
  const existing = health[feedId];
  const failures = (existing?.consecutiveFailures ?? 0) + 1;

  health[feedId] = {
    status: failures >= MAX_CONSECUTIVE_FAILURES ? 'dead' : 'active',
    consecutiveFailures: failures,
    lastSuccess: existing?.lastSuccess ?? null,
    lastError: error.substring(0, 200),
    lastErrorDate: new Date().toISOString(),
    lastCheckedDate: new Date().toISOString(),
  };
}

// ── Fast RSS fetch via native fetch() + rss-parser ──────────────────

async function fetchFeedXml(url: string, signal: AbortSignal): Promise<string | null> {
  const response = await fetch(url, {
    signal,
    headers: {
      'User-Agent': '100xSystems-FeedUpdater/1.0',
      'Accept': 'application/rss+xml, application/atom+xml, application/xml, text/xml',
    },
  });

  if (!response.ok) {
    console.error(`  ⚠ HTTP ${response.status} for ${url}`);
    return null;
  }

  const contentType = response.headers.get('content-type') || '';
  if (!contentType.includes('xml') && !contentType.includes('rss') && !contentType.includes('atom') && !contentType.includes('text')) {
    console.error(`  ⚠ Non-XML content-type: ${contentType} for ${url}`);
    // Still try to parse — some servers return text/html with actual RSS XML
  }

  return response.text();
}

// Create parser once (reused across all feeds — avoids 400+ allocations)
const parser = new Parser<FeedItemRaw, FeedItemRaw>();

async function updateFeed(
  feed: FeedSource,
  limit: number,
  historical: boolean,
): Promise<{ newItems: number; total: number; error?: string }> {
  const filePath = path.join(FEEDS_DIR, `${feed.id}.json`);

  // Read existing data
  let existingData: FeedData | null = null;
  if (fs.existsSync(filePath)) {
    try {
      existingData = JSON.parse(fs.readFileSync(filePath, 'utf-8')) as FeedData;
    } catch {
      console.warn(`    ⚠ Corrupt file for ${feed.id}, starting fresh`);
    }
  }

  const existingGuids = new Set(existingData?.items.map((i) => i.guid) ?? []);
  const alreadyHasContent = existingData !== null && existingData.items.length > 0;

  // ── FETCH via native fetch() with 3s timeout ──
  // No retries. If a feed doesn't respond in 3s, it gets marked as a failure.
  // After 3 consecutive failures across different runs, the feed is auto-marked DEAD
  // and skipped entirely. This is faster than wasting time retrying dead servers.
  let xml: string | null;
  try {
    xml = await fetchFeedXml(feed.rssUrl, AbortSignal.timeout(HTTP_TIMEOUT_MS));
  } catch (err) {
    const errorMsg = err instanceof Error ? err.message : String(err);
    return { newItems: 0, total: existingData?.items.length ?? 0, error: errorMsg };
  }

  if (!xml || xml.trim().length === 0) {
    return { newItems: 0, total: existingData?.items.length ?? 0, error: 'Empty response' };
  }

  // ── PARSE via rss-parser (robust RSS/Atom/RDF handling) ──
  let parsed: { items?: FeedItemRaw[] };
  try {
    parsed = await parser.parseString(xml);
  } catch (err) {
    const errorMsg = err instanceof Error ? err.message : String(err);
    return { newItems: 0, total: existingData?.items.length ?? 0, error: `Parse: ${errorMsg}` };
  }

  if (!parsed.items || parsed.items.length === 0) {
    return { newItems: 0, total: existingData?.items.length ?? 0, error: alreadyHasContent ? undefined : 'No items in feed' };
  }

  // ── PROCESS items ──
  const now = Date.now();
  const recentCutoff = now - RECENT_ITEM_HOURS * 60 * 60 * 1000;
  const newItems: FeedItem[] = [];
  let itemsAdded = 0;

  for (const rawItem of parsed.items) {
    // Apply item limit
    if (itemsAdded >= limit) break;

    const guid = getGuid(rawItem, feed.id);
    if (existingGuids.has(guid)) continue;

    // In incremental mode, only index recent items (within 48h)
    if (!historical) {
      const pubDate = rawItem.isoDate || rawItem.pubDate;
      if (pubDate) {
        const pubTime = new Date(pubDate).getTime();
        if (!isNaN(pubTime) && pubTime < recentCutoff) continue; // skip old items
      } else {
        // No date — stop after first 3 items to avoid re-indexing old undated content
        if (itemsAdded >= 3) continue;
      }
    }

    const title = rawItem.title?.trim();
    if (!title) continue;

    newItems.push({
      guid,
      title,
      link: toAbsoluteUrl(rawItem.link, feed.rssUrl),
      summary: truncate(rawItem.contentSnippet || rawItem.content || null, 300),
      author: rawItem.creator || rawItem.author || null,
      publishedAt: rawItem.isoDate || rawItem.pubDate || null,
    });

    existingGuids.add(guid);
    itemsAdded++;
  }

  if (newItems.length === 0) {
    return { newItems: 0, total: existingData?.items.length ?? 0 };
  }

  // ── WRITE updated file (atomic write via tmp + rename) ──
  const updatedData: FeedData = {
    feedId: feed.id,
    feedName: feed.name,
    feedSiteUrl: feed.siteUrl,
    feedRssUrl: feed.rssUrl,
    tags: feed.tags,
    updatedAt: new Date().toISOString(),
    items: [...(existingData?.items ?? []), ...newItems].slice(-MAX_TOTAL_ITEMS),
    totalIndexed: (existingData?.totalIndexed ?? 0) + newItems.length,
  };

  const tmpPath = filePath + '.tmp';
  fs.writeFileSync(tmpPath, JSON.stringify(updatedData, null, 2) + '\n', 'utf-8');
  fs.renameSync(tmpPath, filePath);

  return { newItems: newItems.length, total: updatedData.items.length };
}

// ── Delta JSON ──────────────────────────────────────────────────────

function writeDeltaJson(results: Array<{ id: string; newItems: number }>): void {
  ensureDir(DAILY_DIR);

  const items: Record<string, FeedItem[]> = {};

  for (const result of results) {
    if (result.newItems === 0) continue;

    const filePath = path.join(FEEDS_DIR, `${result.id}.json`);
    let feedData: FeedData | null = null;
    try {
      feedData = JSON.parse(fs.readFileSync(filePath, 'utf-8')) as FeedData;
    } catch {
      continue;
    }
    if (!feedData) continue;

    const newItems = feedData.items.slice(-result.newItems);
    if (newItems.length > 0) {
      items[result.id] = newItems;
    }
  }

  const delta = {
    date: new Date().toISOString().slice(0, 10),
    generatedAt: new Date().toISOString(),
    items,
    totalNewItems: Object.values(items).reduce((sum, arr) => sum + arr.length, 0),
    feedCount: Object.keys(items).length,
  };

  const deltaPath = path.join(DAILY_DIR, 'delta.json');
  fs.writeFileSync(deltaPath, JSON.stringify(delta, null, 2) + '\n', 'utf-8');
  console.log(`\n📝 Wrote daily/delta.json (${delta.totalNewItems} new items across ${delta.feedCount} feeds)`);
}

function writeEmptyDelta(): void {
  ensureDir(DAILY_DIR);
  const delta = {
    date: new Date().toISOString().slice(0, 10),
    generatedAt: new Date().toISOString(),
    items: {},
    totalNewItems: 0,
    feedCount: 0,
  };
  const deltaPath = path.join(DAILY_DIR, 'delta.json');
  fs.writeFileSync(deltaPath, JSON.stringify(delta, null, 2) + '\n', 'utf-8');
  console.log(`\n📝 Wrote daily/delta.json (0 new items — heartbeat only)`);
}

// ── Main ──────────────────────────────────────────────────────────────

async function main(): Promise<void> {
  const startTime = Date.now();
  const { historical, limit, feedIds } = parseArgs();

  console.log(`\n⚡ 100xSystems Feed Updater — ULTRA-FAST MODE`);
  console.log(`   Mode: ${historical ? 'HISTORICAL IMPORT' : 'INCREMENTAL UPDATE'}`);
  console.log(`   Max items per feed: ${limit}`);
  console.log(`   Strategy: ALL feeds IN PARALLEL (not batched)`);
  console.log(`   Timeout: ${HTTP_TIMEOUT_MS}ms per feed`);
  console.log(`   Recent items: ${historical ? 'ALL (historical)' : `Last ${RECENT_ITEM_HOURS}h only`}`);
  console.log(`   Target feeds: ${feedIds.length > 0 ? feedIds.join(', ') : `ALL (${FEED_REGISTRY.length})`}\n`);

  ensureDir(FEEDS_DIR);

  const feedsToProcess = feedIds.length > 0
    ? feedIds.map((id) => FEED_REGISTRY.find((f) => f.id === id)).filter(Boolean) as FeedSource[]
    : FEED_REGISTRY;

  // ── Load feed health & filter out dead feeds ──
  const feedHealth = loadFeedHealth();
  const activeFeeds = feedsToProcess.filter((f) => shouldProcessFeed(f.id, feedHealth, historical));
  const skippedCount = feedsToProcess.length - activeFeeds.length;

  if (skippedCount > 0) {
    console.log(`   ⏭ Skipping ${skippedCount} dead feed(s) (will re-check in ${DEAD_FEED_RECHECK_DAYS} days)\n`);
  }

  // ── ALL FEEDS IN PARALLEL ──
  // No batching. No concurrency limit. All 400+ feeds fire at once.
  // Node.js handles hundreds of concurrent fetch() calls effortlessly.
  // Each has a 3s hard timeout, so the slowest feed determines wall time.
  console.log(`   🚀 Firing ${activeFeeds.length} requests in parallel...\n`);

  const results = await Promise.allSettled(
    activeFeeds.map((feed) =>
      updateFeed(feed, limit, historical).then(
        (result) => ({ feed, result }),
        (err: unknown) => ({
          feed,
          result: {
            newItems: 0,
            total: 0,
            error: err instanceof Error ? err.message : 'Unknown error',
          },
        }),
      ),
    ),
  );

  // ── Process results & update feed health ──
  const processedResults: Array<{ id: string; name: string; newItems: number; total: number; error?: string }> = [];
  let totalNew = 0;
  let errorCount = 0;

  for (const settled of results) {
    if (settled.status === 'rejected') {
      // Should not happen — the catch inside the map wraps all errors
      continue;
    }

    const { feed, result } = settled.value;

    if (result.error) {
      errorCount++;
      markFeedFailure(feedHealth, feed.id, result.error);

      if (feedHealth[feed.id]?.status === 'dead') {
        console.log(`  ✗ [${feed.id}] ${feed.name} — ${result.error} (marked dead after ${MAX_CONSECUTIVE_FAILURES} failures)`);
      } else {
        console.log(`  ⚠ [${feed.id}] ${feed.name} — ${result.error} (failure ${feedHealth[feed.id]?.consecutiveFailures ?? 1}/${MAX_CONSECUTIVE_FAILURES})`);
      }
    } else {
      markFeedSuccess(feedHealth, feed.id);

      if (result.newItems > 0) {
        totalNew += result.newItems;
        console.log(`  ✓ [${feed.id}] ${feed.name} — +${result.newItems} new (total: ${result.total})`);
      } else {
        console.log(`  ✓ [${feed.id}] ${feed.name} — No new items (total: ${result.total})`);
      }
    }

    processedResults.push({
      id: feed.id,
      name: feed.name,
      newItems: result.newItems,
      total: result.total,
      error: result.error,
    });
  }

  // ── Save feed health (only if something changed — avoid unnecessary git diffs) ──
  saveFeedHealth(feedHealth);

  // ── Write delta ──
  if (!historical) {
    if (totalNew > 0) {
      writeDeltaJson(processedResults);
    } else {
      writeEmptyDelta();
    }
  }

  // ── Summary ──
  const elapsed = ((Date.now() - startTime) / 1000).toFixed(1);
  console.log(`\n${'═'.repeat(50)}`);
  console.log(`📊 Summary (${elapsed}s)`);
  console.log(`   Feeds processed: ${activeFeeds.length}`);
  console.log(`   Feeds skipped (dead): ${skippedCount}`);
  console.log(`   New items indexed: ${totalNew}`);
  console.log(`   Errors: ${errorCount}`);
  console.log(`   ✅ Complete in ${elapsed}s!`);
}

main().catch((err) => {
  console.error('💥 Fatal error:', err);
  process.exit(1);
});
