#!/usr/bin/env tsx
/**
 * fetch-ph-data.ts — ULTRA-FAST PH FETCH
 *
 * Fetches Product Hunt data from the bennyblanco4/producthunt-scraper repo.
 * Uses raw.githubusercontent.com instead of git clone — saves ~60s.
 *
 * USAGE:
 *   tsx scripts/fetch-ph-data.ts
 *
 * Source repo: https://github.com/bennyblanco4/producthunt-scraper
 */

import * as fs from 'node:fs';
import * as path from 'node:path';

const RAW_CSV_URL = 'https://raw.githubusercontent.com/bennyblanco4/producthunt-scraper/main/output/products.csv';
const PH_CACHE_DIR = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..', 'producthunt');
const FETCH_TIMEOUT_MS = 15_000;

function ensureDir(dir: string): void {
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
  }
}

function parseCSVLine(line: string): string[] {
  const result: string[] = [];
  let current = '';
  let inQuotes = false;
  for (let i = 0; i < line.length; i++) {
    const char = line[i];
    if (char === '"') {
      inQuotes = !inQuotes;
    } else if (char === ',' && !inQuotes) {
      result.push(current.trim());
      current = '';
    } else {
      current += char;
    }
  }
  result.push(current.trim());
  return result;
}

async function main(): Promise<void> {
  console.log('\n🦊 Fetching Product Hunt data...');
  const startTime = Date.now();

  // Fetch CSV via raw.githubusercontent.com (fast, no git clone)
  console.log('  Fetching products.csv via raw.githubusercontent.com...');
  let csvText: string;
  try {
    const response = await fetch(RAW_CSV_URL, {
      signal: AbortSignal.timeout(FETCH_TIMEOUT_MS),
      headers: { 'User-Agent': '100xSystems/1.0' },
    });
    if (!response.ok) {
      console.error(`  ✗ HTTP ${response.status} for products.csv`);
      process.exit(1);
    }
    csvText = await response.text();
  } catch (err) {
    console.error(`  ✗ Fetch failed: ${err instanceof Error ? err.message : String(err)}`);
    process.exit(1);
  }

  ensureDir(PH_CACHE_DIR);

  const lines = csvText.split('\n').filter(Boolean);
  if (lines.length < 2) {
    console.error('  ✗ No data rows in products.csv');
    process.exit(1);
  }

  const headers = parseCSVLine(lines[0]);
  const products: Record<string, unknown>[] = [];

  for (let i = 1; i < lines.length; i++) {
    const values = parseCSVLine(lines[i]);
    if (values.length !== headers.length) continue;
    const product: Record<string, unknown> = {};
    for (let j = 0; j < headers.length; j++) {
      product[headers[j]] = values[j];
    }
    if (product.name) products.push(product);
  }

  // Write full product list
  const outputPath = path.join(PH_CACHE_DIR, 'products.json');
  fs.writeFileSync(outputPath, JSON.stringify({
    fetchedAt: new Date().toISOString(),
    count: products.length,
    products,
  }, null, 2), 'utf-8');

  console.log(`  ✓ Wrote ${products.length} products to producthunt/products.json`);

  // Write index
  fs.writeFileSync(path.join(PH_CACHE_DIR, 'index.json'), JSON.stringify({
    type: 'producthunt',
    fetchedAt: new Date().toISOString(),
    source: 'https://github.com/bennyblanco4/producthunt-scraper',
    productCount: products.length,
  }, null, 2), 'utf-8');

  const elapsed = ((Date.now() - startTime) / 1000).toFixed(1);
  console.log(`   Done in ${elapsed}s`);
  console.log('✅ Product Hunt data cached to producthunt/\n');
}

main().catch((err) => {
  console.error('💥 Fatal error:', err);
  process.exit(1);
});
