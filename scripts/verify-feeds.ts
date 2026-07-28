#!/usr/bin/env tsx
/**
 * verify-feeds.ts -- ONE-TIME FEED VERIFICATION
 *
 * Pings every RSS URL in feed-registry.ts and reports which feeds are dead.
 * Output is in two formats:
 *   1. Console report showing status for all feeds
 *   2. A copy-pasteable list of dead feed entries for removal from feed-registry.ts
 *
 * USAGE:
 *   tsx scripts/verify-feeds.ts
 *
 * OUTPUT:
 *   - Live feeds: (2xx)
 *   - Dead feeds: (4xx, 5xx)
 *   - Errors: (timeout, DNS failure)
 *   - Summary: X live, Y dead of Z total
 *
 * After running, copy the dead entries from the output and remove them from
 * feed-registry.ts manually.
 */

import { FEED_REGISTRY } from './feed-registry.js';

const PING_TIMEOUT_MS = 5_000;
const MAX_CONCURRENT = 50;

interface PingResult {
  feedId: string;
  name: string;
  rssUrl: string;
  status: 'alive' | 'redirect' | 'dead' | 'error';
  statusCode?: number;
  error?: string;
}

async function checkFeed(url: string, signal: AbortSignal): Promise<{ ok: boolean; status: number }> {
  // Try HEAD first (faster), fall back to GET if 405
  const response = await fetch(url, {
    method: 'HEAD',
    signal,
    headers: {
      'User-Agent': '100xSystems-Verifier/1.0',
      'Accept': 'application/rss+xml, application/atom+xml, application/xml, text/xml',
    },
  });

  if (response.status === 405) {
    // HEAD not supported - try GET
    const getResponse = await fetch(url, {
      signal,
      headers: {
        'User-Agent': '100xSystems-Verifier/1.0',
        'Accept': 'application/rss+xml, application/atom+xml, application/xml, text/xml',
      },
    });
    return { ok: getResponse.ok, status: getResponse.status };
  }

  return { ok: response.ok, status: response.status };
}

async function verifyFeed(feed: typeof FEED_REGISTRY[number]): Promise<PingResult> {
  try {
    const { ok, status } = await checkFeed(feed.rssUrl, AbortSignal.timeout(PING_TIMEOUT_MS));

    if (ok) {
      return { feedId: feed.id, name: feed.name, rssUrl: feed.rssUrl, status: 'alive', statusCode: status };
    }

    if (status >= 400) {
      return { feedId: feed.id, name: feed.name, rssUrl: feed.rssUrl, status: 'dead', statusCode: status };
    }

    return { feedId: feed.id, name: feed.name, rssUrl: feed.rssUrl, status: 'redirect', statusCode: status };
  } catch (err) {
    const errorMsg = err instanceof Error ? err.message : String(err);
    return { feedId: feed.id, name: feed.name, rssUrl: feed.rssUrl, status: 'error', error: errorMsg.substring(0, 100) };
  }
}

async function main(): Promise<void> {
  console.log('\nFeed Registry Verification\n');
  console.log('  Total feeds: ' + FEED_REGISTRY.length);
  console.log('  Timeout: ' + PING_TIMEOUT_MS + 'ms per feed');
  console.log('  Concurrency: ' + MAX_CONCURRENT + ' at a time\n');

  const totalBatches = Math.ceil(FEED_REGISTRY.length / MAX_CONCURRENT);
  const allResults: PingResult[] = [];
  const startTime = Date.now();

  // Process in batches
  for (let i = 0; i < FEED_REGISTRY.length; i += MAX_CONCURRENT) {
    const batchNum = Math.floor(i / MAX_CONCURRENT) + 1;
    console.log('  Batch ' + batchNum + '/' + totalBatches + '...');
    const batch = FEED_REGISTRY.slice(i, i + MAX_CONCURRENT);
    const batchResults = await Promise.all(batch.map(verifyFeed));
    allResults.push(...batchResults);
  }

  const elapsed = ((Date.now() - startTime) / 1000).toFixed(1);
  console.log('\n  Done in ' + elapsed + 's\n');

  // Categorize results
  const alive = allResults.filter((r: PingResult) => r.status === 'alive');
  const redirects = allResults.filter((r: PingResult) => r.status === 'redirect');
  const dead = allResults.filter((r: PingResult) => r.status === 'dead');
  const errors = allResults.filter((r: PingResult) => r.status === 'error');

  // Print report
  const bar = '='.repeat(60);
  console.log('\n' + bar);
  console.log('VERIFICATION RESULTS');
  console.log(bar);
  console.log('  Alive:     ' + alive.length);
  console.log('  Redirects: ' + redirects.length);
  console.log('  Dead:      ' + dead.length);
  console.log('  Errors:    ' + errors.length);
  console.log('  Total:     ' + allResults.length);
  console.log(bar);

  // Print dead feeds (4xx/5xx)
  if (dead.length > 0) {
    console.log('\nDEAD FEEDS (' + dead.length + ') - REMOVE THESE:');
    console.log('(4xx/5xx responses - permanently dead)');
    console.log('');
    for (const r of dead) {
      const entry = JSON.stringify({
        id: r.feedId,
        name: r.name,
        rssUrl: r.rssUrl,
        statusCode: r.statusCode,
      });
      console.log('  ' + entry + ',');
    }
  }

  // Print errors (timeouts, DNS issues)
  if (errors.length > 0) {
    console.log('\nTRANSIENT ERRORS (' + errors.length + ') - RETRY BEFORE REMOVING:');
    console.log('(timeout / DNS / network errors - may be temporary)');
    console.log('');
    for (const r of errors) {
      console.log('  ? [' + r.feedId + '] ' + r.name + ' - ' + r.error);
    }
  }

  // Print redirects
  if (redirects.length > 0) {
    console.log('\nREDIRECTS (' + redirects.length + ') - MAY NEED URL UPDATES:');
    console.log('');
    for (const r of redirects) {
      console.log('  -> [' + r.feedId + '] ' + r.name + ' - HTTP ' + r.statusCode);
      console.log('     ' + r.rssUrl);
    }
  }

  // Overall health
  const healthPct = Math.round((alive.length / allResults.length) * 100);
  console.log('\n' + bar);
  console.log('  Registry health: ' + healthPct + '% alive');
  console.log('  Recommendation: ' + (dead.length > 0 ? 'Remove ' + dead.length + ' dead entries from feed-registry.ts' : 'Registry is healthy'));
  console.log('  Error entries: ' + errors.length + ' (retry before removing)');
  console.log(bar + '\n');
}

main().catch((err) => {
  console.error('Fatal error:', err);
  process.exit(1);
});
