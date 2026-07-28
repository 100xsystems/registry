#!/usr/bin/env tsx
/**
 * purge-dead-feeds.ts — ONE-TIME DEAD FEED PURGER
 *
 * Parallel-pings every RSS feed in feed-registry.json. For each feed:
 *   1st attempt: 60s timeout
 *   2nd attempt (if 1st fails): 30s timeout
 *   If both fail: permanently DELETE the entry from feed-registry.json
 *
 * This script MODIFIES feed-registry.json at the repo root.
 * After running, commit and push the changes.
 *
 * USAGE:
 *   tsx scripts/one-time/purge-dead-feeds.ts
 *
 * WARNING: This will permanently remove dead feed entries.
 * Make sure you have a clean git state before running.
 */

import * as fs from 'node:fs';
import * as path from 'node:path';

// ── Config ────────────────────────────────────────────────────────────

const REGISTRY_PATH = path.resolve(
  path.dirname(new URL(import.meta.url).pathname),
  '..', 'github-workflow', 'feed-registry.json',
);
const FIRST_ATTEMPT_TIMEOUT_MS = 60_000;
const SECOND_ATTEMPT_TIMEOUT_MS = 30_000;
const MAX_CONCURRENT = 50;

// ── Types ────────────────────────────────────────────────────────────

interface FeedEntry {
  id: string;
  name: string;
  rssUrl: string;
  siteUrl: string;
  tags: string[];
  historicalImport?: {
    strategy: string;
    sitemapUrl?: string;
    archiveUrl?: string;
    paginationPattern?: string;
  };
}

interface PingResult {
  feed: FeedEntry;
  alive: boolean;
  attempts: number;
  errors: string[];
}

// ── Helpers ───────────────────────────────────────────────────────────

function readRegistry(): FeedEntry[] {
  if (!fs.existsSync(REGISTRY_PATH)) {
    console.error(`feed-registry.json not found at ${REGISTRY_PATH}`);
    process.exit(1);
  }
  const raw = fs.readFileSync(REGISTRY_PATH, 'utf-8');
  const parsed = JSON.parse(raw);
  if (!Array.isArray(parsed)) throw new Error('feed-registry.json must be an array');
  return parsed as FeedEntry[];
}

function writeRegistry(entries: FeedEntry[]): void {
  fs.writeFileSync(REGISTRY_PATH, JSON.stringify(entries, null, 2) + '\n', 'utf-8');
  console.log(`\n✍️  Wrote ${entries.length} entries back to feed-registry.json`);
}

/**
 * Ping a single feed URL with a given timeout.
 * Returns { ok: true } if HTTP 2xx, else { ok: false, error }.
 */
async function pingFeed(url: string, timeoutMs: number): Promise<{ ok: boolean; error?: string }> {
  try {
    const response = await fetch(url, {
      signal: AbortSignal.timeout(timeoutMs),
      method: 'GET', // Use GET to ensure we actually reach the server
      headers: {
        'User-Agent': '100xSystems-Purger/1.0',
        'Accept': 'application/rss+xml, application/atom+xml, application/xml, text/xml, */*',
      },
    });

    // Any 2xx or 3xx response means the server is alive
    if (response.status >= 200 && response.status < 400) {
      return { ok: true };
    }

    return { ok: false, error: `HTTP ${response.status}` };
  } catch (err) {
    const msg = err instanceof Error ? err.message : String(err);
    return { ok: false, error: msg };
  }
}

/**
 * Ping a single feed with retry logic.
 */
async function testFeed(feed: FeedEntry, index: number, total: number): Promise<PingResult> {
  const errors: string[] = [];

  // First attempt: 60s
  const result1 = await pingFeed(feed.rssUrl, FIRST_ATTEMPT_TIMEOUT_MS);
  if (result1.ok) {
    console.log(`  ✓ [${index + 1}/${total}] ${feed.id} — OK (1st attempt)`);
    return { feed, alive: true, attempts: 1, errors: [] };
  }
  errors.push(`1st: ${result1.error}`);

  // Second attempt: 30s
  console.log(`  ⚠ [${index + 1}/${total}] ${feed.id} — 1st failed (${result1.error}), retrying...`);
  const result2 = await pingFeed(feed.rssUrl, SECOND_ATTEMPT_TIMEOUT_MS);
  if (result2.ok) {
    console.log(`  ✓ [${index + 1}/${total}] ${feed.id} — OK (2nd attempt)`);
    return { feed, alive: true, attempts: 2, errors };
  }
  errors.push(`2nd: ${result2.error}`);

  // Both failed — dead      console.log(`  ✗ [${index + 1}/${total}] ${feed.id} — DEAD (${result2.error}) — REMOVING`);
  return { feed, alive: false, attempts: 2, errors };
}

// ── Main ──────────────────────────────────────────────────────────────

async function main(): Promise<void> {
  const startTime = Date.now();

  console.log('\n🔍 Feed Registry Dead Feed Purger');
  console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n');

  // 1. Read registry
  const allFeeds = readRegistry();
  console.log(`  Loaded ${allFeeds.length} feeds from feed-registry.json\n`);
  console.log(`  First attempt:  ${FIRST_ATTEMPT_TIMEOUT_MS / 1000}s timeout`);
  console.log(`  Second attempt: ${SECOND_ATTEMPT_TIMEOUT_MS / 1000}s timeout`);
  console.log(`  Concurrency:    ${MAX_CONCURRENT} feeds at a time\n`);

  // 2. Ping all feeds in batches
  const results: PingResult[] = [];
  const totalBatches = Math.ceil(allFeeds.length / MAX_CONCURRENT);

  for (let i = 0; i < allFeeds.length; i += MAX_CONCURRENT) {
    const batch = allFeeds.slice(i, i + MAX_CONCURRENT);
    const batchNum = Math.floor(i / MAX_CONCURRENT) + 1;
    console.log(`  Batch ${batchNum}/${totalBatches} (${batch.length} feeds)...`);

    const batchResults = await Promise.allSettled(
      batch.map((feed, idx) => testFeed(feed, i + idx, allFeeds.length)),
    ).then((settled) =>
      settled.map((s) =>
        s.status === 'fulfilled'
          ? s.value
          : { feed: batch[settled.indexOf(s)], alive: false, attempts: 0, errors: [(s.reason as Error).message] },
      ),
    );
    results.push(...batchResults);
  }

  // 3. Analyze results
  const alive = results.filter((r) => r.alive);
  const dead = results.filter((r) => !r.alive);

  console.log('\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
  console.log(`📊 Results (${((Date.now() - startTime) / 1000).toFixed(0)}s)`);
  console.log(`  Alive: ${alive.length}`);
  console.log(`  Dead:  ${dead.length}`);
  console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');

  // 4. Print dead feed details
  if (dead.length > 0) {
    console.log('\n💀 DEAD FEEDS — REMOVED:\n');
    for (const r of dead) {
      console.log(`  ${r.feed.name} (${r.feed.id})`);
      for (const err of r.errors) {
        console.log(`    ${err}`);
      }
    }
  }

  // 5. Write back only alive feeds
  const survivingFeeds = results
    .filter((r) => r.alive)
    .map((r) => r.feed);

  writeRegistry(survivingFeeds);

  // 6. Final summary
  const removed = allFeeds.length - survivingFeeds.length;
  const elapsed = ((Date.now() - startTime) / 1000).toFixed(0);
  console.log(`\n✅ Purge complete in ${elapsed}s`);
  console.log(`   ${allFeeds.length} → ${survivingFeeds.length} (${removed} removed)`);

  if (removed > 0) {
    console.log('\n⚠  Commit and push the changes to feed-registry.json.');
    console.log('   Then update the website\'s feed.constants.ts to match.\n');
  }
}

main().catch((err) => {
  console.error('💥 Fatal error:', err);
  process.exit(1);
});
