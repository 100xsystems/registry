/**
 * feed-registry.ts
 *
 * Reads feed sources from feed-registry.json (at repo root) and re-exports
 * them with TypeScript types for use by github-workflow/ scripts.
 *
 * The JSON file at the root is the canonical source of truth — add/remove
 * feeds there. The website's feed.constants.ts must be synced manually.
 */

import * as fs from 'node:fs';
import * as path from 'node:path';

export interface HistoricalImport {
  strategy: 'sitemap' | 'archive-crawl' | 'rss-all' | 'none';
  sitemapUrl?: string;
  archiveUrl?: string;
  paginationPattern?: string;
}

export interface FeedSource {
  id: string;
  name: string;
  rssUrl: string;
  siteUrl: string;
  tags: string[];
  historicalImport?: HistoricalImport;
}

// Path to feed-registry.json in the github-workflow folder
const REGISTRY_PATH = path.resolve(import.meta.dirname, 'github-workflow', 'feed-registry.json');

function loadFeedRegistry(): FeedSource[] {
  try {
    const raw = fs.readFileSync(REGISTRY_PATH, 'utf-8');
    const parsed = JSON.parse(raw) as FeedSource[];
    if (!Array.isArray(parsed)) throw new Error('feed-registry.json must be an array');
    return parsed;
  } catch (err) {
    console.error('[feed-registry] Failed to load feed-registry.json:', err instanceof Error ? err.message : String(err));
    return [];
  }
}

export const FEED_REGISTRY: FeedSource[] = loadFeedRegistry();
