#!/usr/bin/env tsx
/**
 * crawl-sitemap.ts
 *
 * Fetches an XML sitemap (or sitemap index), extracts all article URLs
 * with their last-modified dates, and merges them into the existing
 * feeds/{feedId}.json format.
 *
 * USAGE:
 *   # Crawl sitemap and merge into feed JSON:
 *   tsx scripts/crawl-sitemap.ts --feed=cloudflare-blog
 *
 *   # Crawl ALL feeds that have sitemap-based historical import:
 *   tsx scripts/crawl-sitemap.ts --all
 *
 *   # Dry run (show what would be imported without writing):
 *   tsx scripts/crawl-sitemap.ts --all --dry-run
 *
 * DESIGN:
 *   - Sitemaps are the primary source for historical article data
 *   - RSS only provides the latest 10-50 articles (not an archive)
 *   - Sitemaps provide ALL article URLs + last-modified dates
 *   - Title is extracted from the URL slug (kebab-case → Title Case)
 *     as a placeholder; proper titles come from RSS incremental updates
 *   - Deduplication by URL (not GUID, since sitemaps don't have GUIDs)
 *   - Sitemap index files are automatically followed recursively
 *
 * ETHICAL NOTE:
 *   We extract only article URLs and publication dates from the sitemap.
 *   We do NOT download article content, HTML pages, or images.
 *   This is metadata — not content.
 */

import * as fs from 'node:fs';
import * as path from 'node:path';
import { XMLParser } from 'fast-xml-parser';
import { FEED_REGISTRY, type FeedSource, type HistoricalImport } from './feed-registry.js';

// ── Types ────────────────────────────────────────────────────────────

interface SitemapUrlEntry {
  loc: string;
  lastmod?: string;
}

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

// ── Configuration ─────────────────────────────────────────────────────

const FEEDS_DIR = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..', 'feeds');

// ── Helpers ───────────────────────────────────────────────────────────

/**
 * Extract a reasonable title from a URL slug.
 * Example: "https://blog.cloudflare.com/ddos-trends-july-2026"
 *          → "Ddos Trends July 2026"
 */
function titleFromUrl(url: string): string {
  try {
    const pathname = new URL(url).pathname;
    // Get the last meaningful segment of the URL path
    const segments = pathname.replace(/\/$/, '').split('/');
    const lastSegment = segments[segments.length - 1] || segments[segments.length - 2] || '';
    // Convert kebab-case to Title Case
    return lastSegment
      .replace(/[-_]/g, ' ')
      .replace(/\//g, '')
      .replace(/\b\w/g, (c) => c.toUpperCase())
      .trim() || url;
  } catch {
    return url;
  }
}

/**
 * Parse a date from various sitemap date formats.
 * Sitemaps use ISO 8601: YYYY-MM-DD or YYYY-MM-DDThh:mm:ss±hh:mm
 */
function parseSitemapDate(dateStr: string | undefined): string | null {
  if (!dateStr) return null;
  try {
    const d = new Date(dateStr);
    if (isNaN(d.getTime())) return null;
    return d.toISOString();
  } catch {
    return null;
  }
}

// ── Sitemap Fetcher ───────────────────────────────────────────────────

/**
 * Fetch and parse a sitemap XML file.
 * Handles both single sitemaps and sitemap indexes.
 * Maximum depth: 2 (index → sub-sitemap → URLs)
 */
async function fetchSitemapUrls(
  sitemapUrl: string,
  depth = 0,
  maxDepth = 2,
): Promise<SitemapUrlEntry[]> {
  if (depth > maxDepth) {
    console.warn(`    ⚠ Max sitemap depth (${maxDepth}) reached at ${sitemapUrl}`);
    return [];
  }

  console.log(`    Fetching: ${sitemapUrl} (depth ${depth})`);

  let xml: string;
  try {
    const res = await fetch(sitemapUrl, {
      headers: { 'User-Agent': '100xSystems/1.0 (sitemap-crawler)' },
      signal: AbortSignal.timeout(30_000),
    });
    if (!res.ok) {
      console.warn(`    ⚠ HTTP ${res.status} for ${sitemapUrl}`);
      return [];
    }
    xml = await res.text();
  } catch (err) {
    console.warn(`    ⚠ Fetch failed: ${err instanceof Error ? err.message : String(err)}`);
    return [];
  }

  // Parse XML
  const parser = new XMLParser({
    ignoreAttributes: false,
    attributeNamePrefix: '@_',
    isArray: (name) => ['url', 'sitemap', 'loc'].includes(name),
  });

  let parsed: any;
  try {
    parsed = parser.parse(xml);
  } catch (err) {
    console.warn(`    ⚠ XML parse error: ${err instanceof Error ? err.message : String(err)}`);
    return [];
  }

  // Handle sitemap index (contains <sitemap> children)
  if (parsed.sitemapindex) {
    const childSitemaps = parsed.sitemapindex.sitemap || [];
    const childUrls = childSitemaps.map((s: any) => s.loc?.[0]).filter(Boolean);
    console.log(`    Found sitemap index with ${childUrls.length} child sitemaps`);

    // Fetch all child sitemaps in parallel (up to 10 at a time)
    const allUrls: SitemapUrlEntry[] = [];
    const chunks: string[][] = [];
    for (let i = 0; i < childUrls.length; i += 10) {
      chunks.push(childUrls.slice(i, i + 10));
    }

    for (const chunk of chunks) {
      const results = await Promise.allSettled(
        chunk.map((url: string) => fetchSitemapUrls(url, depth + 1, maxDepth))
      );
      for (const r of results) {
        if (r.status === 'fulfilled') {
          allUrls.push(...r.value);
        }
      }
      // Small delay between chunks to be kind to servers
      if (chunks.length > 1) await new Promise((r) => setTimeout(r, 500));
    }

    return allUrls;
  }

  // Handle single sitemap (contains <url> children)
  if (parsed.urlset) {
    const urlList = parsed.urlset.url || [];
    const entries = urlList
      .map((u: any) => ({
        loc: u.loc?.[0] || '',
        lastmod: u.lastmod?.[0],
      }))
      .filter((e: SitemapUrlEntry) => e.loc);

    console.log(`    → ${entries.length} URLs found in sitemap`);
    return entries;
  }

  console.warn(`    ⚠ Unknown sitemap format at ${sitemapUrl}`);
  return [];
}

// ── Merge into Feed JSON ──────────────────────────────────────────────

/**
 * Convert sitemap URL entries into the FeedData format and merge into
 * the existing feed JSON file.
 */
function mergeIntoSitemapFeed(
  feed: FeedSource,
  sitemapEntries: SitemapUrlEntry[],
  dryRun: boolean,
): { totalInSitemap: number; newItems: number; alreadyHad: number } {
  const filePath = path.join(FEEDS_DIR, `${feed.id}.json`);

  // Read existing data
  let existingData: FeedData | null = null;
  if (fs.existsSync(filePath)) {
    try {
      existingData = JSON.parse(fs.readFileSync(filePath, 'utf-8')) as FeedData;
    } catch {
      console.warn(`  ⚠ Corrupt file for ${feed.id}, starting fresh`);
    }
  }

  // Build a set of existing URLs for deduplication
  const existingUrls = new Set(existingData?.items.map((i) => i.link) ?? []);
  let alreadyHad = 0;
  let newItems = 0;

  const convertedItems: FeedItem[] = [];

  for (const entry of sitemapEntries) {
    if (!entry.loc) continue;

    if (existingUrls.has(entry.loc)) {
      alreadyHad++;
      continue;
    }

    const title = titleFromUrl(entry.loc);
    if (!title) continue;

    convertedItems.push({
      guid: `${feed.id}::${entry.loc}`,
      title,
      link: entry.loc,
      summary: null,
      author: null,
      publishedAt: parseSitemapDate(entry.lastmod),
    });

    existingUrls.add(entry.loc);
    newItems++;
  }

  if (newItems === 0) {
    return { totalInSitemap: sitemapEntries.length, newItems: 0, alreadyHad };
  }

  // Build merged feed data
  const updatedData: FeedData = {
    feedId: feed.id,
    feedName: feed.name,
    feedSiteUrl: feed.siteUrl,
    feedRssUrl: feed.rssUrl,
    tags: feed.tags,
    updatedAt: new Date().toISOString(),
    // Sitemap items first (covers older articles), then RSS items (covers newer ones)
    // But within sitemap items, sort by date (newest first)
    items: [
      ...convertedItems,
      ...(existingData?.items ?? []),
    ]
      .sort((a, b) => {
        const dateA = a.publishedAt ? new Date(a.publishedAt).getTime() : 0;
        const dateB = b.publishedAt ? new Date(b.publishedAt).getTime() : 0;
        return dateB - dateA;
      })
      .slice(0, 10_000), // Keep cap at 10k
    totalIndexed: (existingData?.totalIndexed ?? 0) + newItems,
  };

  if (!dryRun) {
    const tmpPath = filePath + '.tmp';
    fs.writeFileSync(tmpPath, JSON.stringify(updatedData, null, 2) + '\n', 'utf-8');
    fs.renameSync(tmpPath, filePath);
  }

  return { totalInSitemap: sitemapEntries.length, newItems, alreadyHad };
}

// ── Main ──────────────────────────────────────────────────────────────

interface CrawlResult {
  feedId: string;
  name: string;
  sitemapUrl: string;
  totalInSitemap: number;
  newItems: number;
  alreadyHad: number;
  error?: string;
}

async function main(): Promise<void> {
  const args = process.argv.slice(2);
  const dryRun = args.includes('--dry-run');
  const shouldRunAll = args.includes('--all');

  // Get single feed from --feed=name or --feed name
  let targetFeedId: string | null = null;
  for (let i = 0; i < args.length; i++) {
    const arg = args[i];
    if (arg.startsWith('--feed=')) {
      targetFeedId = arg.slice(7);
    } else if (arg === '--feed' && i + 1 < args.length) {
      targetFeedId = args[++i];
    }
  }

  if (!shouldRunAll && !targetFeedId) {
    console.error('Usage: tsx scripts/crawl-sitemap.ts --feed=<id> | --all [--dry-run]');
    process.exit(1);
  }

  // Determine which feeds to process
  const feedsToProcess = shouldRunAll
    ? FEED_REGISTRY.filter((f) => f.historicalImport?.strategy === 'sitemap')
    : FEED_REGISTRY.filter((f) => f.id === targetFeedId);

  if (feedsToProcess.length === 0) {
    console.error(`No feeds found with sitemap strategy${targetFeedId ? ` for ID "${targetFeedId}"` : ''}`);
    process.exit(1);
  }

  console.log(`\n🗺️  Sitemap Crawler`);
  console.log(`   Mode: ${dryRun ? 'DRY RUN (no writes)' : 'LIVE (will write)'}`);
  console.log(`   Target feeds: ${feedsToProcess.length}\n`);

  const results: CrawlResult[] = [];
  let totalNew = 0;
  let totalErrors = 0;

  for (const feed of feedsToProcess) {
    const hi = feed.historicalImport!;
    console.log(`  [${feed.id}] ${feed.name}...`);

    if (hi.strategy !== 'sitemap' || !hi.sitemapUrl) {
      console.log(`    ⚠ No sitemap URL configured, skipping`);
      continue;
    }

    try {
      const sitemapEntries = await fetchSitemapUrls(hi.sitemapUrl);

      if (sitemapEntries.length === 0) {
        console.log(`    ⚠ No entries found in sitemap`);
        results.push({ feedId: feed.id, name: feed.name, sitemapUrl: hi.sitemapUrl, totalInSitemap: 0, newItems: 0, alreadyHad: 0 });
        continue;
      }

      const result = mergeIntoSitemapFeed(feed, sitemapEntries, dryRun);

      if (result.newItems > 0) {
        totalNew += result.newItems;
        console.log(`    ✓ +${result.newItems} new items from sitemap (${result.alreadyHad} already existed, ${result.totalInSitemap} total in sitemap)`);
      } else if (result.alreadyHad > 0) {
        console.log(`    ✓ All ${result.alreadyHad} sitemap URLs already in feed (no new items)`);
      } else {
        console.log(`    ✓ No new items (sitemap had ${result.totalInSitemap} entries)`);
      }

      results.push({ feedId: feed.id, name: feed.name, sitemapUrl: hi.sitemapUrl, ...result });
    } catch (err) {
      totalErrors++;
      const errMsg = err instanceof Error ? err.message : String(err);
      console.log(`    ⚠ Error: ${errMsg}`);
      results.push({ feedId: feed.id, name: feed.name, sitemapUrl: hi.sitemapUrl, totalInSitemap: 0, newItems: 0, alreadyHad: 0, error: errMsg });
    }

    // Delay between feeds
    if (feedsToProcess.length > 1) {
      await new Promise((r) => setTimeout(r, 1000));
    }
  }

  // Summary
  console.log(`\n${'─'.repeat(50)}`);
  console.log(`📊 Summary`);
  console.log(`   Feeds processed: ${results.length}`);
  console.log(`   New items from sitemaps: ${totalNew}`);
  console.log(`   Errors: ${totalErrors}`);
  console.log(`   Mode: ${dryRun ? 'DRY RUN (no files written)' : 'LIVE'}`);
  console.log(`   Complete!`);

  if (totalErrors > 0) {
    console.error(`\n⚠  ${totalErrors} feed(s) had errors — see above for details.`);
    process.exit(1);
  }
}

main().catch((err) => {
  console.error('Fatal error:', err);
  process.exit(1);
});
