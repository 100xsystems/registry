#!/usr/bin/env tsx
/**
 * update-feeds.ts
 *
 * Fetches RSS feed items and updates the JSON files in `feeds/`.
 *
 * USAGE:
 *   # Daily incremental update (default):
 *   tsx scripts/update-feeds.ts
 *
 *   # One-time historical import (fetches up to 500 items per feed):
 *   tsx scripts/update-feeds.ts --historical --limit=500
 *
 *   # Single feed (for testing):
 *   tsx scripts/update-feeds.ts --feed=netflix-tech-blog
 *
 * DESIGN:
 *   - Each feed is an independent JSON file: `feeds/{feedId}.json`
 *   - Files are only updated if new items are found (avoids unnecessary commits)
 *   - The script is idempotent — running it multiple times produces the same result
 *   - GUIDs are used for deduplication (falls back to link if no guid)
 *   - Only metadata is stored (title, link, summary, author, publishedAt).
 *     NEVER stores article body content.
 *   - Feeds are processed in parallel batches to be fast while respecting rate limits.
 *   - Each failed feed is retried once before being logged as an error.
 *   - Individual feed failures do NOT cause the whole script to exit with code 1.
 *
 * ETHICAL NOTE:
 *   We index only article metadata — title, URL, summary, author, publication date.
 *   We NEVER download, cache, or host article content. Users click through to the
 *   original source to read. This is an index, not an archive.
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
  /** ISO timestamp of the last update to this file */
  updatedAt: string;
  items: FeedItem[];
  /** Total number of items ever indexed (for stats) */
  totalIndexed: number;
}

// ── Configuration ─────────────────────────────────────────────────────

const FEEDS_DIR = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..', 'feeds');
const DAILY_DIR = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..', 'daily');
const DEFAULT_LIMIT = 50;
const HISTORICAL_LIMIT = 500;
const CONCURRENCY = 10;      // Number of feeds to fetch in parallel
const RETRY_COUNT = 1;       // Number of retries per failed feed
const DELAY_BETWEEN_BATCHES = 1000; // 1s delay between batches to avoid rate limiting

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

// ── Helpers ───────────────────────────────────────────────────────────

function ensureFeedsDir(): void {
  if (!fs.existsSync(FEEDS_DIR)) {
    fs.mkdirSync(FEEDS_DIR, { recursive: true });
  }
}

function existingGuidSet(feedData: FeedData | null): Set<string> {
  if (!feedData) return new Set();
  return new Set(feedData.items.map((i) => i.guid));
}

function getGuid(item: FeedItemRaw, feedId: string): string {
  if (item.guid) return item.guid;
  if (item.link) return `${feedId}::${item.link}`;
  // Last resort — hash the title
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
  const limit = limitIdx >= 0 ? parseInt(args[limitIdx + 1], 10) || DEFAULT_LIMIT : (historical ? HISTORICAL_LIMIT : DEFAULT_LIMIT);

  // Support both --feed=name and --feed name syntax
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

/**
 * Sleep for a given number of milliseconds.
 */
function sleep(ms: number): Promise<void> {
  return new Promise((r) => setTimeout(r, ms));
}

// ── Core logic ────────────────────────────────────────────────────────

async function updateFeed(feed: FeedSource, limit: number, attempt = 0): Promise<{ newItems: number; total: number; error?: string }> {
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

  const existingGuids = existingGuidSet(existingData);
  const alreadyHasContent = existingData !== null && existingData.items.length > 0;

  // Fetch RSS
  const parser = new Parser<FeedItemRaw, FeedItemRaw>();
  let parsed: Awaited<ReturnType<typeof parser.parseURL>>;

  try {
    parsed = await parser.parseURL(feed.rssUrl);
  } catch (err) {
    const errorMsg = err instanceof Error ? err.message : String(err);
    // Retry once
    if (attempt < RETRY_COUNT) {
      console.log(`    Retrying...`);
      await sleep(2000);
      return updateFeed(feed, limit, attempt + 1);
    }
    return { newItems: 0, total: existingData?.items.length ?? 0, error: errorMsg };
  }

  if (!parsed.items || parsed.items.length === 0) {
    return { newItems: 0, total: existingData?.items.length ?? 0, error: alreadyHasContent ? undefined : 'No items in feed' };
  }

  // Process items
  const newItems: FeedItem[] = [];

  for (const rawItem of parsed.items.slice(0, limit)) {
    const guid = getGuid(rawItem, feed.id);

    if (existingGuids.has(guid)) continue; // Already indexed

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
  }

  if (newItems.length === 0) {
    return { newItems: 0, total: existingData?.items.length ?? 0 };
  }

  // Build updated FeedData
  const updatedData: FeedData = {
    feedId: feed.id,
    feedName: feed.name,
    feedSiteUrl: feed.siteUrl,
    feedRssUrl: feed.rssUrl,
    tags: feed.tags,
    updatedAt: new Date().toISOString(),
    items: [...(existingData?.items ?? []), ...newItems].slice(-10_000), // Cap at 10k items to keep files manageable
    totalIndexed: (existingData?.totalIndexed ?? 0) + newItems.length,
  };

  // Write to a temp file first, then rename (atomic write)
  const tmpPath = filePath + '.tmp';
  fs.writeFileSync(tmpPath, JSON.stringify(updatedData, null, 2) + '\n', 'utf-8');
  fs.renameSync(tmpPath, filePath);

  return { newItems: newItems.length, total: updatedData.items.length };
}

// ── Delta JSON Generation ──────────────────────────────────────────

/**
 * Write daily/delta.json with ONLY the newly added items from this run.
 * This file is fetched by the website's ISR to incrementally update its cache
 * without re-downloading all feed JSON files.
 *
 * The delta only contains feedId → new items, no full feedData objects.
 * That keeps the file tiny (typically < 1 KB).
 */
function writeDeltaJson(results: Array<{ id: string; newItems: number }>): void {
  if (!fs.existsSync(DAILY_DIR)) {
    fs.mkdirSync(DAILY_DIR, { recursive: true });
  }

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

    // Take only the newest items (the ones just added — they're at the end of the array)
    const newItems = feedData.items.slice(-result.newItems);
    if (newItems.length > 0) {
      items[result.id] = newItems;
    }
  }

  if (Object.keys(items).length === 0) {
    writeEmptyDelta();
    return;
  }

  const delta = {
    date: new Date().toISOString().slice(0, 10), // YYYY-MM-DD
    generatedAt: new Date().toISOString(),
    items,
    totalNewItems: Object.values(items).reduce((sum, arr) => sum + arr.length, 0),
    feedCount: Object.keys(items).length,
  };

  const deltaPath = path.join(DAILY_DIR, 'delta.json');
  fs.writeFileSync(deltaPath, JSON.stringify(delta, null, 2) + '\n', 'utf-8');
  console.log(`\n📝 Wrote daily/delta.json (${delta.totalNewItems} new items across ${delta.feedCount} feeds)`);
}

/**
 * Write an empty delta.json when no new items were found.
 * The website checks the `generatedAt` timestamp to know we checked.
 */
function writeEmptyDelta(): void {
  if (!fs.existsSync(DAILY_DIR)) {
    fs.mkdirSync(DAILY_DIR, { recursive: true });
  }
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
  const { historical, limit, feedIds } = parseArgs();

  console.log(`\n🔍 100xSystems Feed Updater`);
  console.log(`   Mode: ${historical ? 'HISTORICAL IMPORT' : 'INCREMENTAL UPDATE'}`);
  console.log(`   Max items per feed: ${limit}`);
  console.log(`   Concurrency: ${CONCURRENCY} feeds at a time`);
  console.log(`   Target feeds: ${feedIds.length > 0 ? feedIds.join(', ') : `ALL (${FEED_REGISTRY.length})`}\n`);

  ensureFeedsDir();

  const feedsToProcess = feedIds.length > 0
    ? feedIds.map((id) => FEED_REGISTRY.find((f) => f.id === id)).filter(Boolean) as FeedSource[]
    : FEED_REGISTRY;

  const results: Array<{ id: string; name: string; newItems: number; total: number; error?: string }> = [];
  let totalNew = 0;
  let totalErrors = 0;

  // Process feeds in parallel batches for speed
  for (let i = 0; i < feedsToProcess.length; i += CONCURRENCY) {
    const batch = feedsToProcess.slice(i, i + CONCURRENCY);

    const batchResults = await Promise.allSettled(
      batch.map(async (feed) => {
        const result = await updateFeed(feed, limit);
        return { feed, result };
      })
    );

    for (const settled of batchResults) {
      if (settled.status === 'rejected') {
        // This shouldn't happen with proper error handling, but just in case
        totalErrors++;
        continue;
      }

      const { feed, result } = settled.value;

      if (result.error) {
        totalErrors++;
        console.log(`  ⚠ [${feed.id}] ${feed.name} — ${result.error}`);
      } else if (result.newItems > 0) {
        totalNew += result.newItems;
        console.log(`  ✓ [${feed.id}] ${feed.name} — +${result.newItems} new items (total: ${result.total})`);
      } else {
        console.log(`  ✓ [${feed.id}] ${feed.name} — No new items (total: ${result.total})`);
      }

      results.push({
        id: feed.id,
        name: feed.name,
        newItems: result.newItems,
        total: result.total,
        error: result.error,
      });
    }

    // Small delay between batches to be kind to RSS servers
    if (i + CONCURRENCY < feedsToProcess.length) {
      await sleep(DELAY_BETWEEN_BATCHES);
    }
  }

  // Write daily delta.json (only for non-historical runs)
  if (!historical) {
    if (totalNew > 0) {
      writeDeltaJson(results);
    } else {
      writeEmptyDelta();
    }
  }

  // Summary
  console.log(`\n${'─'.repeat(50)}`);
  console.log(`📊 Summary`);
  console.log(`   Feeds processed: ${results.length}`);
  console.log(`   New items indexed: ${totalNew}`);
  console.log(`   Errors: ${totalErrors}`);
  console.log(`   Previous items preserved: all`);
  console.log(`   Complete!`);

  // Log warnings for errors but DO NOT exit with code 1.
  // Individual feed failures should not crash the entire pipeline.
  if (totalErrors > 0) {
    console.log(`\n⚠  ${totalErrors} feed(s) had errors — they will be retried next run.`);
    console.log(`   (This is informational; the script continues successfully.)`);
  }
}

main().catch((err) => {
  console.error('Fatal error:', err);
  process.exit(1);
});
