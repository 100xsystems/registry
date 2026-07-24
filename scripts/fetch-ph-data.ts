#!/usr/bin/env tsx
/**
 * fetch-ph-data.ts
 *
 * Clones the producthunt-scraper repository and converts the CSV data
 * into structured JSON files in the registry's producthunt/ directory.
 *
 * USAGE:
 *   tsx scripts/fetch-ph-data.ts
 *
 * Source repo: https://github.com/bennyblanco4/producthunt-scraper
 */

import { execSync } from 'node:child_process';
import * as fs from 'node:fs';
import * as path from 'node:path';

const PH_REPO = 'https://github.com/bennyblanco4/producthunt-scraper.git';
const PH_CACHE_DIR = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..', 'producthunt');
const TMP_CLONE_DIR = '/tmp/ph-scraper-clone';

function ensureDir(dir: string): void {
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
  }
}

function cleanClone(): boolean {
  if (fs.existsSync(TMP_CLONE_DIR)) {
    fs.rmSync(TMP_CLONE_DIR, { recursive: true, force: true });
  }
  console.log('  Cloning producthunt-scraper...');
  try {
    execSync(`git clone --depth=1 ${PH_REPO} ${TMP_CLONE_DIR}`, { stdio: 'pipe', timeout: 60000 });
    return true;
  } catch (err) {
    console.error(`  ✗ Clone failed: ${err instanceof Error ? err.message : String(err)}`);
    return false;
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

function main(): void {
  console.log('\n🦊 Fetching Product Hunt data...');
  const startTime = Date.now();

  if (!cleanClone()) {
    process.exit(1);
  }

  ensureDir(PH_CACHE_DIR);

  const csvPath = path.join(TMP_CLONE_DIR, 'output', 'products.csv');
  if (!fs.existsSync(csvPath)) {
    console.error('  ✗ products.csv not found in cloned repo');
    process.exit(1);
  }

  const lines = fs.readFileSync(csvPath, 'utf-8').split('\n').filter(Boolean);
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
    source: PH_REPO,
    productCount: products.length,
  }, null, 2), 'utf-8');

  // Cleanup
  fs.rmSync(TMP_CLONE_DIR, { recursive: true, force: true });

  const elapsed = ((Date.now() - startTime) / 1000).toFixed(1);
  console.log(`   Done in ${elapsed}s`);
  console.log('✅ Product Hunt data cached to producthunt/\\n');
}

main();
