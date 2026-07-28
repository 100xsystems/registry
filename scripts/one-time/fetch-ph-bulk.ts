#!/usr/bin/env tsx
/**
 * fetch-ph-bulk.ts — ONE-TIME PRODUCT HUNT BULK FETCHER
 *
 * Downloads the historical Product Hunt products CSV from the community
 * scraper and converts it into the standardized PhPost JSON format.
 *
 * USAGE:
 *   tsx scripts/one-time/fetch-ph-bulk.ts
 *
 * OUTPUT:
 *   producthunt/products.json — Catalog of all historical products
 *   producthunt/index.json    — Index for the website
 *
 * NOTE: The CSV scraper data is limited (name, upvotes, links, description, tags).
 * The daily workflow (fetch-ph-today.ts) enriches with official API data.
 */

import * as fs from 'node:fs';
import * as path from 'node:path';

// ── Config ────────────────────────────────────────────────────────────

const CSV_URL = 'https://raw.githubusercontent.com/bennyblanco4/producthunt-scraper/refs/heads/main/output/products.csv';
const PH_CACHE_DIR = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..', '..', 'producthunt');
const FETCH_TIMEOUT_MS = 30_000;

// ── Types ────────────────────────────────────────────────────────────

interface PhBulkProduct {
  id: string;
  name: string;
  tagline: string;
  description: string | null;
  url: string;
  website: string;
  slug: string;
  votesCount: number;
  commentsCount: number;
  reviewsCount: number;
  reviewsRating: number;
  dailyRank: number | null;
  featuredAt: string | null;
  createdAt: string;
  makers: { name: string; username: string }[];
  topics: { name: string; slug: string }[];
  thumbnail: { type: string; url: string } | null;
  media: Array<{ type: string; url: string; videoUrl: string | null }>;
}

// ── Helpers ───────────────────────────────────────────────────────────

function ensureDir(dir: string): void {
  if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
}

function writeFile(filePath: string, data: unknown): void {
  fs.writeFileSync(filePath, JSON.stringify(data, null, 2) + '\n', 'utf-8');
  const size = fs.statSync(filePath).size;
  console.log(`  ✓ ${path.basename(filePath)} — ${(size / 1024 / 1024).toFixed(1)}MB`);
}

/**
 * Parse a quoted CSV field, handling commas inside quotes.
 */
function parseCsvLine(line: string): string[] {
  const fields: string[] = [];
  let current = '';
  let inQuotes = false;

  for (let i = 0; i < line.length; i++) {
    const char = line[i];
    if (char === '"') {
      inQuotes = !inQuotes;
    } else if (char === ',' && !inQuotes) {
      fields.push(current.trim());
      current = '';
    } else {
      current += char;
    }
  }
  fields.push(current.trim());
  return fields;
}

/**
 * Extract slug from a producthunt_link like:
 *   https://www.producthunt.com/posts/trickle-4            → trickle-4
 *   https://www.producthunt.com/products/foo#foo           → foo
 */
function extractSlug(productHuntLink: string): string {
  try {
    const url = new URL(productHuntLink);
    const parts = url.pathname.split('/').filter(Boolean);
    // Could be /posts/<slug> or /products/<slug>
    return parts[parts.length - 1] ?? '';
  } catch {
    return '';
  }
}

/**
 * Parse comma-separated tags like '#web-app, #productivity, #artificial-intelligence'
 * into topic-like objects.
 */
function parseTags(tagsStr: string): Array<{ name: string; slug: string }> {
  if (!tagsStr) return [];
  return tagsStr
    .split(',')
    .map((t) => t.trim().replace(/^#/, ''))
    .filter(Boolean)
    .map((name) => ({
      name,
      slug: name.toLowerCase().replace(/[^a-z0-9]+/g, '-'),
    }));
}

// ── Main ──────────────────────────────────────────────────────────────

async function main(): Promise<void> {
  console.log('\n🦊 [ONE-TIME] Fetching Product Hunt bulk data from CSV...');
  const startTime = Date.now();

  ensureDir(PH_CACHE_DIR);

  // 1. Download CSV
  console.log(`  Downloading CSV from producthunt-scraper...`);
  const res = await fetch(CSV_URL, {
    signal: AbortSignal.timeout(FETCH_TIMEOUT_MS),
  });
  if (!res.ok) throw new Error(`CSV download failed: HTTP ${res.status}`);
  const csvText = await res.text();
  const lines = csvText.split('\n').filter(Boolean);
  console.log(`  Downloaded ${lines.length - 1} rows (${(csvText.length / 1024).toFixed(0)}KB)`);

  // 2. Parse CSV
  const products: PhBulkProduct[] = [];
  const seen = new Set<string>();

  for (let i = 1; i < lines.length; i++) {
    const fields = parseCsvLine(lines[i]);
    if (fields.length < 5) continue;

    const [name, upvotesStr, link, productHuntLink, description, tagsStr] = fields;
    if (!name) continue;

    const slug = extractSlug(productHuntLink);
    const id = slug || `csv-${i}`;

    // Deduplicate by slug
    if (seen.has(id)) continue;
    seen.add(id);

    products.push({
      id,
      name: name.trim(),
      tagline: (description || '').trim().substring(0, 140),
      description: (description || '').trim() || null,
      url: productHuntLink || link || '',
      website: link || '',
      slug,
      votesCount: parseInt(upvotesStr, 10) || 0,
      commentsCount: 0,
      reviewsCount: 0,
      reviewsRating: 0,
      dailyRank: null,
      featuredAt: null,
      createdAt: new Date(0).toISOString(), // unknown date for bulk
      makers: [],
      topics: parseTags(tagsStr || ''),
      thumbnail: null,
      media: [],
    });
  }

  // Sort by votesCount descending
  products.sort((a, b) => b.votesCount - a.votesCount);

  console.log(`  Parsed ${products.length} unique products`);

  // 3. Write products.json
  writeFile(
    path.join(PH_CACHE_DIR, 'products.json'),
    {
      fetchedAt: new Date().toISOString(),
      count: products.length,
      isBulkImport: true,
      source: 'bennyblanco4/producthunt-scraper',
      products,
    },
  );

  // 4. Write index.json
  writeFile(
    path.join(PH_CACHE_DIR, 'index.json'),
    {
      type: 'producthunt',
      fetchedAt: new Date().toISOString(),
      isBulkImport: true,
      source: 'bennyblanco4/producthunt-scraper',
      totalProducts: products.length,
      firstFetchedDate: 'bulk-import',
      lastFetchedDate: 'bulk-import',
      availableDates: [],
    },
  );

  // 5. Summary
  const elapsed = ((Date.now() - startTime) / 1000).toFixed(1);
  console.log(`\n   ✅ Done in ${elapsed}s`);
  console.log(`   Products: ${products.length}`);
  console.log(`   Top product: ${products[0]?.name ?? 'N/A'} (${products[0]?.votesCount ?? 0} votes)`);
  console.log('\n⚠  This is a ONE-TIME seed script. Do NOT run in CI.\n');
}

main().catch((err) => {
  console.error('💥 Fatal error:', err);
  process.exit(1);
});
