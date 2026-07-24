#!/usr/bin/env tsx
/**
 * fetch-yc-data.ts
 *
 * Clones the yc-oss/api repository and caches Y Combinator company data
 * as JSON files in the registry's yc/ directory.
 *
 * The yc-oss/api repo: https://github.com/yc-oss/api
 * Contains: companies/*.json, batches/*.json, meta.json
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

// ── Types ────────────────────────────────────────────────────────────

interface YcCompany {
  id: string;
  name: string;
  slug: string;
  website: string;
  one_liner: string;
  long_description: string;
  batch: string;
  tags: string[];
  industries: string[];
  top_company: boolean;
  isHiring: boolean;
  team_size: number;
  stage: string;
  status: string;
  regions: string[];
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
  // Remove previous clone if exists
  if (fs.existsSync(TMP_CLONE_DIR)) {
    fs.rmSync(TMP_CLONE_DIR, { recursive: true, force: true });
  }

  console.log('  Cloning yc-oss/api...');
  try {
    execSync(`git clone --depth=1 ${YC_API_REPO} ${TMP_CLONE_DIR}`, {
      stdio: 'pipe',
      timeout: 60000,
    });
    return true;
  } catch (err) {
    console.error(`  ✗ Clone failed: ${err instanceof Error ? err.message : String(err)}`);
    return false;
  }
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
    const cachedMeta = {
      ...meta,
      fetchedAt: new Date().toISOString(),
    };
    fs.writeFileSync(
      path.join(YC_CACHE_DIR, 'meta.json'),
      JSON.stringify(cachedMeta, null, 2),
      'utf-8'
    );
    console.log(`  ✓ meta.json — ${meta.total_companies} companies, ${meta.total_batches} batches`);
  }

  // 2. Copy companies/ directory (limit to key fields to reduce size)
  const companiesSrc = path.join(TMP_CLONE_DIR, 'companies');
  const companiesDest = path.join(YC_CACHE_DIR, 'companies');
  ensureDir(companiesDest);

  if (fs.existsSync(companiesSrc)) {
    const files = fs.readdirSync(companiesSrc).filter(f => f.endsWith('.json'));
    let copied = 0;
    for (const file of files) {
      try {
        const raw = JSON.parse(fs.readFileSync(path.join(companiesSrc, file), 'utf-8')) as YcCompany;
        // Only store essential fields to keep cache light
        const slim = {
          id: raw.id,
          name: raw.name,
          slug: raw.slug,
          website: raw.website,
          one_liner: raw.one_liner,
          batch: raw.batch,
          tags: (raw.tags || []).slice(0, 5),
          top_company: raw.top_company || false,
          isHiring: raw.isHiring || false,
          team_size: raw.team_size,
          stage: raw.stage,
        };
        fs.writeFileSync(
          path.join(companiesDest, file),
          JSON.stringify(slim),
          'utf-8'
        );
        copied++;
      } catch {
        // Skip corrupt files
      }
    }
    console.log(`  ✓ companies/ — ${copied} company profiles`);
  }

  // 3. Copy batches/ structure (just copy batch index files)
  const batchesSrc = path.join(TMP_CLONE_DIR, 'batches');
  const batchesDest = path.join(YC_CACHE_DIR, 'batches');
  ensureDir(batchesDest);

  if (fs.existsSync(batchesSrc)) {
    const batchDirs = fs.readdirSync(batchesSrc, { withFileTypes: true })
      .filter(d => d.isDirectory());
    let copiedBatches = 0;
    for (const dir of batchDirs) {
      const batchDirSrc = path.join(batchesSrc, dir.name);
      const batchDirDest = path.join(batchesDest, dir.name);
      fs.mkdirSync(batchDirDest, { recursive: true });

      const batchFiles = fs.readdirSync(batchDirSrc).filter(f => f.endsWith('.json'));
      for (const file of batchFiles.slice(0, 50)) { // Limit to 50 per batch
        fs.copyFileSync(path.join(batchDirSrc, file), path.join(batchDirDest, file));
      }
      copiedBatches++;
    }
    console.log(`  ✓ batches/ — ${copiedBatches} batch directories`);
  }

  // 4. Also cache the latest changes
  const changesSrc = path.join(TMP_CLONE_DIR, 'changes', 'latest.json');
  if (fs.existsSync(changesSrc)) {
    fs.copyFileSync(changesSrc, path.join(YC_CACHE_DIR, 'changes-latest.json'));
    console.log('  ✓ changes-latest.json');
  }

  // 5. Write index
  const index = {
    type: 'yc-combinator',
    fetchedAt: new Date().toISOString(),
    source: YC_API_REPO,
    companyCount: fs.readdirSync(companiesDest).filter(f => f.endsWith('.json')).length,
  };
  fs.writeFileSync(path.join(YC_CACHE_DIR, 'index.json'), JSON.stringify(index, null, 2), 'utf-8');

  // Cleanup
  fs.rmSync(TMP_CLONE_DIR, { recursive: true, force: true });

  const elapsed = ((Date.now() - startTime) / 1000).toFixed(1);
  console.log(`   Done in ${elapsed}s`);
  console.log('✅ YC data cached to yc/\n');
}

main();
