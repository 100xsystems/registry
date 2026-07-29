#!/usr/bin/env tsx
/**
 * update-feeds.ts — DAILY ULTRA-FAST FEED UPDATER
 *
 * Fetches RSS feed items from the registry and updates JSON files in feeds/.
 * Runs daily via the daily-feed-update.yml GitHub Actions workflow.
 *
 * SPEED DESIGN:
 *   ⚡ All feeds are fetched IN PARALLEL (not in batches)
 *   ⚡ Native fetch() with 30s timeout
 *   ⚡ NO retries — if a feed fails, just log and move on
 *   ⚡ Only items from the last 24h are indexed
 *
 * USAGE:
 *   tsx scripts/github-workflow/update-feeds.ts
 *   tsx scripts/github-workflow/update-feeds.ts --historical --limit=500
 *   tsx scripts/github-workflow/update-feeds.ts --feed=netflix-tech-blog
 */

import * as fs from 'node:fs';
import * as path from 'node:path';
import Parser from 'rss-parser';
import { FEED_REGISTRY, type FeedSource } from '../feed-registry.js';

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

const ROOT_DIR = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..', '..');
const FEEDS_DIR = path.join(ROOT_DIR, 'dynamic-data', 'feeds');

const HTTP_TIMEOUT_MS = 30_000;
const FEED_ITEM_LIMIT = 50;
const MAX_TOTAL_ITEMS = 10_000;
const RECENT_ITEM_HOURS = 24;

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

// ── Fast RSS fetch via native fetch() + rss-parser ──────────────────

const parser = new Parser<FeedItemRaw, FeedItemRaw>();

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
    console.warn(`  ⚠ Non-XML content-type: ${contentType} for ${url}`);
  }

  return response.text();
}

async function updateFeed(
  feed: FeedSource,
  limit: number,
  historical: boolean,
): Promise<{ newItems: number; total: number; error?: string }> {
  const filePath = path.join(FEEDS_DIR, `${feed.id}.json`);

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

  const now = Date.now();
  const recentCutoff = now - RECENT_ITEM_HOURS * 60 * 60 * 1000;
  const newItems: FeedItem[] = [];
  let itemsAdded = 0;

  for (const rawItem of parsed.items) {
    if (itemsAdded >= limit) break;

    const guid = getGuid(rawItem, feed.id);
    if (existingGuids.has(guid)) continue;

    if (!historical) {
      const pubDate = rawItem.isoDate || rawItem.pubDate;
      if (pubDate) {
        const pubTime = new Date(pubDate).getTime();
        if (!isNaN(pubTime) && pubTime < recentCutoff) continue;
      } else {
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



// ── Main ──────────────────────────────────────────────────────────────

async function main(): Promise<void> {
  const startTime = Date.now();
  const { historical, limit, feedIds } = parseArgs();

  console.log(`\n⚡ 100xSystems Feed Updater — ULTRA-FAST MODE`);
  console.log(`   Mode: ${historical ? 'HISTORICAL IMPORT' : 'INCREMENTAL UPDATE'}`);
  console.log(`   Max items per feed: ${limit}`);
  console.log(`   Strategy: ALL feeds IN PARALLEL`);
  console.log(`   Timeout: ${HTTP_TIMEOUT_MS}ms per feed — if feed doesn't respond, skip and move on`);
  console.log(`   Recent items: ${historical ? 'ALL (historical)' : `Last ${RECENT_ITEM_HOURS}h only`}`);
  console.log(`   Target feeds: ${feedIds.length > 0 ? feedIds.join(', ') : `ALL (${FEED_REGISTRY.length})`}\n`);

  ensureDir(FEEDS_DIR);

  const feedsToProcess = feedIds.length > 0
    ? feedIds.map((id) => FEED_REGISTRY.find((f) => f.id === id)).filter(Boolean) as FeedSource[]
    : FEED_REGISTRY;

  console.log(`   🚀 Firing ${feedsToProcess.length} requests in parallel...\n`);

  const results = await Promise.allSettled(
    feedsToProcess.map((feed) =>
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

  let totalNew = 0;
  let errorCount = 0;

  for (const settled of results) {
    if (settled.status === 'rejected') continue;

    const { feed, result } = settled.value;

    if (result.error) {
      errorCount++;
      console.log(`  ⚠ [${feed.id}] ${feed.name} — ${result.error}`);
    } else {
      if (result.newItems > 0) {
        totalNew += result.newItems;
        console.log(`  ✓ [${feed.id}] ${feed.name} — +${result.newItems} new (total: ${result.total})`);
      } else {
        console.log(`  ✓ [${feed.id}] ${feed.name} — No new items (total: ${result.total})`);
      }
    }
  }

  const elapsed = ((Date.now() - startTime) / 1000).toFixed(1);
  console.log(`\n${'═'.repeat(50)}`);
  console.log(`📊 Summary (${elapsed}s)`);
  console.log(`   Feeds processed: ${feedsToProcess.length}`);
  console.log(`   New items indexed: ${totalNew}`);
  console.log(`   Errors: ${errorCount}`);
  console.log(`   ✅ Complete in ${elapsed}s!`);
}

main().catch((err) => {
  console.error('💥 Fatal error:', err);
  process.exit(1);
});
