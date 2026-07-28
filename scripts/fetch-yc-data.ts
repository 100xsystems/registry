#!/usr/bin/env tsx
/**
 * fetch-yc-data.ts — ULTRA-FAST YC FETCH
 *
 * Fetches Y Combinator company data from the yc-oss/api repository.
 * Uses raw.githubusercontent.com instead of git clone — saves ~60s.
 *
 * USAGE:
 *   tsx scripts/fetch-yc-data.ts
 *
 * This script should run daily via GitHub Actions.
 */

import * as fs from 'node:fs';
import * as path from 'node:path';

// ── Config ────────────────────────────────────────────────────────────

const RAW_BASE = 'https://raw.githubusercontent.com/yc-oss/api/main';
const API_BASE = 'https://api.github.com/repos/yc-oss/api';

const YC_CACHE_DIR = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..', 'yc');
const RECENT_BATCHES = ['summer-2026', 'winter-2026', 'summer-2025', 'winter-2025'];
const FEATURED_COUNT = 50;
const FETCH_TIMEOUT_MS = 15_000;

// ── Types ────────────────────────────────────────────────────────────

interface YcCompany {
  id: string;
  name: string;
  slug: string;
  website: string;
  one_liner: string;
  batch: string;
  tags: string[];
  top_company: boolean;
  isHiring: boolean;
  team_size: number;
  stage: string;
}

interface YcMeta {
  last_updated: string;
  total_companies: number;
  total_batches: number;
}

// ── Helpers ───────────────────────────────────────────────────────────

function ensureDir(dir: string): void {
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
  }
}

async function fetchJson<T>(url: string, label: string): Promise<T | null> {
  try {
    const response = await fetch(url, {
      signal: AbortSignal.timeout(FETCH_TIMEOUT_MS),
      headers: { 'User-Agent': '100xSystems/1.0' },
    });
    if (!response.ok) {
      console.warn(`  ⚠ ${label}: HTTP ${response.status}`);
      return null;
    }
    return (await response.json()) as T;
  } catch (err) {
    console.warn(`  ⚠ ${label}: ${err instanceof Error ? err.message : String(err)}`);
    return null;
  }
}

/** Extract essential fields from a raw company object. */
function slimCompany(raw: Record<string, unknown>): YcCompany {
  return {
    id: String(raw.id ?? ''),
    name: String(raw.name ?? ''),
    slug: String(raw.slug ?? ''),
    website: String(raw.website ?? ''),
    one_liner: String(raw.one_liner ?? ''),
    batch: String(raw.batch ?? ''),
    tags: ((raw.tags as string[]) || []).slice(0, 5),
    top_company: Boolean(raw.top_company),
    isHiring: Boolean(raw.isHiring),
    team_size: Number(raw.team_size ?? 0),
    stage: String(raw.stage ?? ''),
  };
}

// ── Main ──────────────────────────────────────────────────────────────

async function main(): Promise<void> {
  console.log('\n🔬 Fetching YC Combinator data...');
  const startTime = Date.now();

  ensureDir(YC_CACHE_DIR);
  const errors: string[] = [];

  // 1. Fetch meta.json
  const meta = await fetchJson<YcMeta>(`${RAW_BASE}/meta.json`, 'meta.json');
  if (meta) {
    const cachedMeta = { ...meta, fetchedAt: new Date().toISOString() };
    fs.writeFileSync(path.join(YC_CACHE_DIR, 'meta.json'), JSON.stringify(cachedMeta, null, 2), 'utf-8');
    console.log(`  ✓ meta.json — ${meta.total_companies} companies, ${meta.total_batches} batches`);
  } else {
    errors.push('meta.json');
  }

  // 2. Fetch batch summary JSON files
  const featuredCompanies: YcCompany[] = [];

  for (const batchName of RECENT_BATCHES) {
    const batchUrl = `${RAW_BASE}/batches/${batchName}.json`;
    const batchData = await fetchJson<Record<string, unknown>[]>(batchUrl, `${batchName}.json`);

    if (batchData && Array.isArray(batchData)) {
      const batchFeatured = batchData
        .map((raw) => slimCompany(raw))
        .sort((a, b) => Number(b.top_company) - Number(a.top_company))
        .slice(0, 12);

      featuredCompanies.push(...batchFeatured);
      console.log(`  ✓ ${batchName}.json — ${batchData.length} companies`);
    } else {
      errors.push(`${batchName}.json`);
    }
  }

  // 3. Write featured.json
  const featuredPath = path.join(YC_CACHE_DIR, 'featured.json');
  fs.writeFileSync(featuredPath, JSON.stringify({
    fetchedAt: new Date().toISOString(),
    count: featuredCompanies.length,
    companies: featuredCompanies.slice(0, FEATURED_COUNT),
  }, null, 2), 'utf-8');
  console.log(`  ✓ featured.json — ${Math.min(featuredCompanies.length, FEATURED_COUNT)} featured companies`);

  // 4. Fetch changes/latest.json
  const changes = await fetchJson<Record<string, unknown>>(`${RAW_BASE}/changes/latest.json`, 'changes-latest.json');
  if (changes) {
    fs.writeFileSync(path.join(YC_CACHE_DIR, 'changes-latest.json'), JSON.stringify(changes, null, 2), 'utf-8');
    console.log('  ✓ changes-latest.json');
  }

  // 5. Write index
  const index = {
    type: 'yc-combinator',
    fetchedAt: new Date().toISOString(),
    source: 'https://github.com/yc-oss/api',
    featuredCount: Math.min(featuredCompanies.length, FEATURED_COUNT),
  };
  fs.writeFileSync(path.join(YC_CACHE_DIR, 'index.json'), JSON.stringify(index, null, 2), 'utf-8');

  const elapsed = ((Date.now() - startTime) / 1000).toFixed(1);
  console.log(`   Done in ${elapsed}s`);
  console.log('✅ YC data cached to yc/\n');
}

main().catch((err) => {
  console.error('💥 Fatal error:', err);
  process.exit(1);
});
