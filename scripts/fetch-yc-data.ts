#!/usr/bin/env tsx
/**
 * fetch-yc-data.ts
 *
 * Clones the yc-oss/api repository and caches Y Combinator company data
 * as JSON files in the registry's yc/ directory.
 *
 * The yc-oss/api repo: https://github.com/yc-oss/api
 * Individual company files are inside batches/{batch}/ directories.
 * Batch summary files (batches/{batch}.json) contain full company arrays.
 *
 * USAGE:
 *   tsx scripts/fetch-yc-data.ts
 *
 * This script should run daily via GitHub Actions.
 */

import { execSync } from 'node:child_process';
import * as fs from 'node:fs';
import * as path from 'node:path';

// ── Config ────────────────────────────────────────────────────────────

const YC_API_REPO = 'https://github.com/yc-oss/api.git';
const YC_CACHE_DIR = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..', 'yc');
const TMP_CLONE_DIR = '/tmp/yc-api-clone';
const RECENT_BATCHES = ['summer-2026', 'winter-2026', 'summer-2025', 'winter-2025'];
const FEATURED_COUNT = 50;

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

function cleanClone(): boolean {
  if (fs.existsSync(TMP_CLONE_DIR)) {
    fs.rmSync(TMP_CLONE_DIR, { recursive: true, force: true });
  }
  console.log('  Cloning yc-oss/api...');
  try {
    execSync(`git clone --depth=1 ${YC_API_REPO} ${TMP_CLONE_DIR}`, { stdio: 'pipe', timeout: 60000 });
    return true;
  } catch (err) {
    console.error(`  ✗ Clone failed: ${err instanceof Error ? err.message : String(err)}`);
    return false;
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

function main(): void {
  console.log('\n🔬 Fetching YC Combinator data...');
  const startTime = Date.now();

  if (!cleanClone()) {
    process.exit(1);
  }

  ensureDir(YC_CACHE_DIR);

  // 1. Copy meta.json
  const metaSrc = path.join(TMP_CLONE_DIR, 'meta.json');
  if (fs.existsSync(metaSrc)) {
    const meta = JSON.parse(fs.readFileSync(metaSrc, 'utf-8')) as YcMeta;
    const cachedMeta = { ...meta, fetchedAt: new Date().toISOString() };
    fs.writeFileSync(path.join(YC_CACHE_DIR, 'meta.json'), JSON.stringify(cachedMeta, null, 2), 'utf-8');
    console.log(`  ✓ meta.json — ${meta.total_companies} companies, ${meta.total_batches} batches`);
  }

  // 2. Read batch summary JSON files → collect featured companies
  const batchesSrc = path.join(TMP_CLONE_DIR, 'batches');
  const featuredCompanies: YcCompany[] = [];

  if (fs.existsSync(batchesSrc)) {
    for (const batchName of RECENT_BATCHES) {
      const batchFile = path.join(batchesSrc, `${batchName}.json`);
      if (!fs.existsSync(batchFile)) continue;

      try {
        const batchData = JSON.parse(fs.readFileSync(batchFile, 'utf-8')) as Record<string, unknown>[];
        if (!Array.isArray(batchData)) continue;

        const batchFeatured = batchData
          .map((raw) => slimCompany(raw))
          .sort((a, b) => Number(b.top_company) - Number(a.top_company))
          .slice(0, 12);

        featuredCompanies.push(...batchFeatured);
        console.log(`  ✓ ${batchName}.json — ${batchData.length} companies`);
      } catch {
        console.warn(`  ⚠ Could not parse ${batchName}.json`);
      }
    }

    // 3. Copy batch directories (individual company JSON files for detailed access)
    const batchesDest = path.join(YC_CACHE_DIR, 'batches');
    ensureDir(batchesDest);

    const batchDirs = fs.readdirSync(batchesSrc, { withFileTypes: true }).filter(d => d.isDirectory());
    let copiedBatches = 0;
    for (const dir of batchDirs) {
      const batchDirSrc = path.join(batchesSrc, dir.name);
      const batchDirDest = path.join(batchesDest, dir.name);
      fs.mkdirSync(batchDirDest, { recursive: true });

      const batchFiles = fs.readdirSync(batchDirSrc).filter(f => f.endsWith('.json'));
      for (const file of batchFiles.slice(0, 30)) {
        try {
          const raw = JSON.parse(fs.readFileSync(path.join(batchDirSrc, file), 'utf-8')) as Record<string, unknown>;
          const slim = slimCompany(raw);
          fs.writeFileSync(path.join(batchDirDest, file), JSON.stringify(slim), 'utf-8');
        } catch { /* skip corrupt files */ }
      }
      copiedBatches++;
    }
    console.log(`  ✓ batches/ — ${copiedBatches} batch dirs copied (${batchDirs.length} total)`);
  }

  // 4. Write featured-companies.json (used by HomeYC component)
  const featuredPath = path.join(YC_CACHE_DIR, 'featured.json');
  fs.writeFileSync(featuredPath, JSON.stringify({
    fetchedAt: new Date().toISOString(),
    count: featuredCompanies.length,
    companies: featuredCompanies.slice(0, FEATURED_COUNT),
  }, null, 2), 'utf-8');
  console.log(`  ✓ featured.json — ${Math.min(featuredCompanies.length, FEATURED_COUNT)} featured companies`);

  // 5. Also cache the latest changes
  const changesSrc = path.join(TMP_CLONE_DIR, 'changes', 'latest.json');
  if (fs.existsSync(changesSrc)) {
    fs.copyFileSync(changesSrc, path.join(YC_CACHE_DIR, 'changes-latest.json'));
    console.log('  ✓ changes-latest.json');
  }

  // 6. Write index
  const index = {
    type: 'yc-combinator',
    fetchedAt: new Date().toISOString(),
    source: YC_API_REPO,
    featuredCount: Math.min(featuredCompanies.length, FEATURED_COUNT),
  };
  fs.writeFileSync(path.join(YC_CACHE_DIR, 'index.json'), JSON.stringify(index, null, 2), 'utf-8');

  // Cleanup
  fs.rmSync(TMP_CLONE_DIR, { recursive: true, force: true });

  const elapsed = ((Date.now() - startTime) / 1000).toFixed(1);
  console.log(`   Done in ${elapsed}s`);
  console.log('✅ YC data cached to yc/\n');
}

main();
