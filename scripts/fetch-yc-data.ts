#!/usr/bin/env tsx
/**
 * fetch-yc-data.ts — YC COMBINATOR ALGOLIA FETCHER
 *
 * Fetches ALL Y Combinator companies directly from YC's Algolia search index.
 * Same approach as yc-oss/api but runs in our own registry.
 *
 * ARCHITECTURE:
 *   - Scrapes Algolia API key from YC companies page
 *   - Fetches all 6000+ companies via Algolia search API (paginated by batch)
 *   - Stores day-wise archive: yc/YYYY-MM-DD.json
 *   - Tracks daily changes: yc/changes/latest.json + latest.md
 *   - Merged catalog: yc/companies.json
 *   - Metadata: yc/meta.json
 *
 * SPEED: ~30-40s for all 6000 companies (same as yc-oss/api)
 *
 * USAGE:
 *   tsx scripts/fetch-yc-data.ts
 *
 * Runs once daily via GitHub Actions.
 */

import * as fs from 'node:fs';
import * as path from 'node:path';

// ── Config ────────────────────────────────────────────────────────────

const YC_CACHE_DIR = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..', 'yc');
const CHANGES_DIR = path.join(YC_CACHE_DIR, 'changes');
const ALGOLIA_APP_ID = '45BWZJ1SGC';
const ALGOLIA_INDEX = 'YCCompany_By_Launch_Date_production';
const YC_COMPANIES_URL = 'https://www.ycombinator.com/companies';
const ALGOLIA_API = `https://${ALGOLIA_APP_ID.toLowerCase()}-dsn.algolia.net/1/indexes/*/queries`;
const HITS_PER_PAGE = 1000;
const FETCH_TIMEOUT_MS = 30_000;

// ── Types ────────────────────────────────────────────────────────────

interface YcCompany {
  id: number;
  name: string;
  slug: string;
  former_names: string[];
  small_logo_thumb_url: string;
  website: string;
  all_locations: string;
  long_description: string;
  one_liner: string;
  team_size: number;
  highlight_black: boolean;
  highlight_latinx: boolean;
  highlight_women: boolean;
  industry: string;
  subindustry: string;
  launched_at: number;
  tags: string[];
  tags_highlighted: string[];
  top_company: boolean;
  isHiring: boolean;
  nonprofit: boolean;
  batch: string;
  status: string;
  industries: string[];
  regions: string[];
  stage: string;
  app_video_public: boolean;
  demo_day_video_public: boolean;
  app_answers: null;
  question_answers: boolean;
  url: string;
}

interface YcChangeEntry {
  field: string;
  before: unknown;
  after: unknown;
}

interface YcChangeSet {
  date: string;
  fetchedAt: string;
  previousCount: number;
  currentCount: number;
  added: YcCompany[];
  removed: YcCompany[];
  updated: Array<{
    id: number;
    name: string;
    slug: string;
    batch: string;
    url: string;
    changes: YcChangeEntry[];
  }>;
}

interface YcMeta {
  last_updated: string;
  totalCompanies: number;
  totalBatches: number;
  totalTags: number;
  totalIndustries: number;
  batches: Record<string, { name: string; count: number }>;
}

// ── Helpers ───────────────────────────────────────────────────────────

function ensureDir(dir: string): void {
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
  }
}

function readExisting(filePath: string): string | null {
  try {
    if (fs.existsSync(filePath)) return fs.readFileSync(filePath, 'utf-8');
  } catch {}
  return null;
}

function writeIfChanged(filePath: string, content: string): boolean {
  const existing = readExisting(filePath);
  if (existing === content) return false;
  fs.writeFileSync(filePath, content, 'utf-8');
  return true;
}

function dateStr(d: Date = new Date()): string {
  return d.toISOString().slice(0, 10);
}

/** Stable stringify for deep object comparison */
function stableStringify(value: unknown): string {
  if (Array.isArray(value)) {
    return '[' + value.map((item) => stableStringify(item)).join(',') + ']';
  }
  if (value && typeof value === 'object') {
    const entries = Object.entries(value as Record<string, unknown>)
      .sort(([a], [b]) => a.localeCompare(b));
    return '{' + entries.map(([key, nestedValue]) =>
      JSON.stringify(key) + ':' + stableStringify(nestedValue)
    ).join(',') + '}';
  }
  return JSON.stringify(value);
}

function valuesEqual(a: unknown, b: unknown): boolean {
  return stableStringify(a) === stableStringify(b);
}

// ── Algolia API ──────────────────────────────────────────────────────

/** Scrape Algolia API key from YC companies page */
async function getAlgoliaKey(): Promise<string> {
  const res = await fetch(YC_COMPANIES_URL, {
    signal: AbortSignal.timeout(15_000),
    headers: { 'User-Agent': '100xSystems-YCFetcher/1.0' },
  });
  if (!res.ok) throw new Error(`YC page returned HTTP ${res.status}`);
  const html = await res.text();
  const match = html.match(/window\.AlgoliaOpts\s*=\s*({[^<]+})/);
  if (!match) throw new Error('Could not find AlgoliaOpts on YC companies page');
  const opts = JSON.parse(match[1]) as { app?: string; key?: string };
  if (opts.app !== ALGOLIA_APP_ID || !opts.key) {
    throw new Error('YC page returned unexpected Algolia options');
  }
  return opts.key;
}

/** Query Algolia with given params */
async function queryAlgolia(apiKey: string, params: string): Promise<Record<string, unknown>> {
  const searchParams = new URLSearchParams({
    'x-algolia-agent': 'Algolia for JavaScript (3.35.1); Browser; JS Helper (3.16.1)',
    'x-algolia-application-id': ALGOLIA_APP_ID,
    'x-algolia-api-key': apiKey,
  });
  const res = await fetch(`${ALGOLIA_API}?${searchParams}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ requests: [{ indexName: ALGOLIA_INDEX, params }] }),
    signal: AbortSignal.timeout(FETCH_TIMEOUT_MS),
  });
  if (!res.ok) {
    const body = await res.text();
    throw new Error(`Algolia query failed: HTTP ${res.status} ${body}`);
  }
  const json = (await res.json()) as { results: Record<string, unknown>[] };
  return json.results?.[0] ?? {};
}

// ── Fetch ALL companies from Algolia ────────────────────────────────

async function fetchAllCompanies(apiKey: string): Promise<YcCompany[]> {
  // 1. First, get facets to find all batch names and counts
  console.log('  Fetching batch facets...');
  const facetResult = await queryAlgolia(apiKey,
    'facets=%5B%22batch%22%5D&hitsPerPage=1&maxValuesPerFacet=1000&query=&tagFilters='
  );
  const facets = facetResult.facets as Record<string, Record<string, number>> | undefined;
  const batches = facets?.batch;
  if (!batches) throw new Error('Algolia response did not include batch facets');
  console.log(`  Found ${Object.keys(batches).length} batches`);

  // 2. Fetch companies per batch (paginated)
  const allCompanies: YcCompany[] = [];
  const batchKeys = Object.keys(batches).sort();

  for (const batch of batchKeys) {
    const count = batches[batch];
    let page = 0;
    let fetched = 0;

    while (fetched < count) {
      const result = await queryAlgolia(apiKey,
        `hitsPerPage=${HITS_PER_PAGE}&maxValuesPerFacet=1000&query=&tagFilters=` +
        `&facetFilters=${encodeURIComponent('batch:' + batch)}&page=${page}`
      );
      const hits = result.hits as Record<string, unknown>[] | undefined;
      if (!hits || hits.length === 0) break;

      for (const hit of hits) {
        // Clean Algolia metadata
        if ('_highlightResult' in hit) delete hit._highlightResult;
        if ('objectID' in hit) delete hit.objectID;
        if ('_snippetResult' in hit) delete hit._snippetResult;

        allCompanies.push({
          id: hit.id as number,
          name: hit.name as string,
          slug: hit.slug as string,
          former_names: (hit.former_names as string[]) ?? [],
          small_logo_thumb_url: (hit.small_logo_thumb_url as string) ?? '',
          website: (hit.website as string) ?? '',
          all_locations: (hit.all_locations as string) ?? '',
          long_description: (hit.long_description as string) ?? '',
          one_liner: (hit.one_liner as string) ?? '',
          team_size: (hit.team_size as number) ?? 0,
          highlight_black: (hit.highlight_black as boolean) ?? false,
          highlight_latinx: (hit.highlight_latinx as boolean) ?? false,
          highlight_women: (hit.highlight_women as boolean) ?? false,
          industry: (hit.industry as string) ?? '',
          subindustry: (hit.subindustry as string) ?? '',
          launched_at: (hit.launched_at as number) ?? 0,
          tags: (hit.tags as string[]) ?? [],
          tags_highlighted: (hit.tags_highlighted as string[]) ?? [],
          top_company: (hit.top_company as boolean) ?? false,
          isHiring: (hit.isHiring as boolean) ?? false,
          nonprofit: (hit.nonprofit as boolean) ?? false,
          batch: (hit.batch as string) ?? 'Unspecified',
          status: (hit.status as string) ?? '',
          industries: (hit.industries as string[]) ?? [],
          regions: (hit.regions as string[]) ?? [],
          stage: (hit.stage as string) ?? '',
          app_video_public: (hit.app_video_public as boolean) ?? false,
          demo_day_video_public: (hit.demo_day_video_public as boolean) ?? false,
          app_answers: null,
          question_answers: (hit.question_answers as boolean) ?? false,
          url: `https://www.ycombinator.com/companies/${hit.slug}`,
        });
      }

      fetched += hits.length;
      page++;
    }
  }

  // Sort by ID ascending
  return allCompanies.sort((a, b) => a.id - b.id);
}

// ── Change tracking ─────────────────────────────────────────────────

function buildChangeSet(
  previous: YcCompany[],
  current: YcCompany[],
): YcChangeSet {
  const prevById = new Map(previous.map((c) => [c.id, c]));
  const currById = new Map(current.map((c) => [c.id, c]));

  const added = current.filter((c) => !prevById.has(c.id));
  const removed = previous.filter((c) => !currById.has(c.id));
  const updated: YcChangeSet['updated'] = [];

  for (const curr of current) {
    const prev = prevById.get(curr.id);
    if (!prev) continue;

    const changes: YcChangeEntry[] = [];
    for (const key of Object.keys(curr) as (keyof YcCompany)[]) {
      if (key === 'url') continue; // computed field, always changes
      if (!valuesEqual(prev[key], curr[key])) {
        changes.push({
          field: key,
          before: prev[key],
          after: curr[key],
        });
      }
    }
    if (changes.length > 0) {
      updated.push({
        id: curr.id,
        name: curr.name,
        slug: curr.slug,
        batch: curr.batch,
        url: curr.url,
        changes,
      });
    }
  }

  return {
    date: dateStr(),
    fetchedAt: new Date().toISOString(),
    previousCount: previous.length,
    currentCount: current.length,
    added,
    removed,
    updated,
  };
}

function renderChangesMarkdown(changes: YcChangeSet): string {
  const header = `# YC Company Changes for ${changes.date}

- Previous total: ${changes.previousCount}
- Current total: ${changes.currentCount}
- Added: ${changes.added.length}
- Removed: ${changes.removed.length}
- Updated: ${changes.updated.length}

`;

  if (changes.added.length === 0 && changes.removed.length === 0 && changes.updated.length === 0) {
    return header + 'No company records changed.\n';
  }

  const md: string[] = [header];

  if (changes.added.length > 0) {
    md.push('## Added Companies\n');
    for (const c of changes.added) {
      md.push(`- [${c.name}](${c.url}) (${c.batch}) — ${c.one_liner}`);
    }
    md.push('');
  }

  if (changes.removed.length > 0) {
    md.push('## Removed Companies\n');
    for (const c of changes.removed) {
      md.push(`- ${c.name} (${c.batch})`);
    }
    md.push('');
  }

  if (changes.updated.length > 0) {
    md.push('## Updated Companies\n');
    for (const c of changes.updated) {
      md.push(`### [${c.name}](${c.url})\n`);
      for (const ch of c.changes) {
        const before = String(ch.before ?? 'null').substring(0, 100);
        const after = String(ch.after ?? 'null').substring(0, 100);
        md.push(`- \`${ch.field}\`: ${before} → ${after}`);
      }
      md.push('');
    }
  }

  return md.join('\n');
}

// ── Main ──────────────────────────────────────────────────────────────

async function main(): Promise<void> {
  console.log('\n🔬 Fetching YC Combinator data via Algolia...');
  const startTime = Date.now();

  ensureDir(YC_CACHE_DIR);
  ensureDir(CHANGES_DIR);

  // Clean up stale files from the old approach
  const staleFiles = ['featured.json', 'changes-latest.json', 'index.json'];
  for (const stale of staleFiles) {
    const p = path.join(YC_CACHE_DIR, stale);
    if (fs.existsSync(p)) {
      fs.rmSync(p);
      console.log('  (cleaned up old file: ' + stale + ')');
    }
  }

  // 1. Get Algolia API key
  console.log('  Getting Algolia API key...');
  const apiKey = await getAlgoliaKey();
  console.log('  ✓ Algolia key obtained');

  // 2. Fetch all companies
  console.log('  Fetching companies...');
  const companies = await fetchAllCompanies(apiKey);
  console.log(`  ✓ ${companies.length} companies fetched`);

  const today = dateStr();

  // 3. Read previous snapshot for change tracking (from companies.json, not day file)
  let previousCompanies: YcCompany[] = [];
  let isFirstRun = true;
  const companiesFile = path.join(YC_CACHE_DIR, 'companies.json');
  const existingCompanies = readExisting(companiesFile);
  if (existingCompanies) {
    try {
      const parsed = JSON.parse(existingCompanies) as { companies: YcCompany[] };
      previousCompanies = parsed.companies ?? [];
      isFirstRun = previousCompanies.length === 0;
    } catch {}
  }

  // 4. Build change set
  const changeSet = buildChangeSet(previousCompanies, companies);
  const hasChanges = changeSet.added.length > 0 ||
    changeSet.removed.length > 0 ||
    changeSet.updated.length > 0;

  // 5. Write daily change files
  if (isFirstRun) {
    // First run: just note it as initial snapshot, don't report 6000+ as "added"
    const firstRunJson = JSON.stringify({
      date: today,
      fetchedAt: new Date().toISOString(),
      message: 'Initial snapshot',
      total: companies.length,
    }, null, 2);
    writeIfChanged(path.join(CHANGES_DIR, `${today}.json`), firstRunJson + '\n');
    writeIfChanged(path.join(CHANGES_DIR, 'latest.json'), firstRunJson + '\n');
    writeIfChanged(path.join(CHANGES_DIR, 'latest.md'),
      `# YC Company Changes for ${today}\n\nInitial snapshot — ${companies.length} companies\n`
    );
    console.log(`  ✓ Initial snapshot: ${companies.length} companies`);
  } else if (hasChanges) {
    const changesJson = JSON.stringify(changeSet, null, 2);

    // Write date-stamped change file
    writeIfChanged(path.join(CHANGES_DIR, `${today}.json`), changesJson + '\n');
    // Write latest.json
    writeIfChanged(path.join(CHANGES_DIR, 'latest.json'), changesJson + '\n');
    // Write latest.md
    writeIfChanged(path.join(CHANGES_DIR, 'latest.md'), renderChangesMarkdown(changeSet));

    console.log(`  ✓ Changes: +${changeSet.added.length} -${changeSet.removed.length} ~${changeSet.updated.length}`);
  } else {
    // No changes — write heartbeat
    writeIfChanged(path.join(CHANGES_DIR, `${today}.json`),
      JSON.stringify({
        date: today,
        fetchedAt: new Date().toISOString(),
        message: 'No changes',
        total: companies.length,
      }, null, 2) + '\n'
    );
    console.log('  ✓ No changes detected');
  }

  // 6. Write merged companies.json catalog (from current in-memory data, no day files)
  const catalog = companies.sort((a, b) => b.id - a.id);
  writeIfChanged(
    path.join(YC_CACHE_DIR, 'companies.json'),
    JSON.stringify({
      fetchedAt: new Date().toISOString(),
      count: catalog.length,
      companies: catalog,
    }, null, 2) + '\n',
  );

  // 7. Write featured.json (top recent companies for homepage display)
  const recentBatches = ['S26', 'W26', 'S25', 'W25'];
  const featured = companies
    .filter((c) => recentBatches.includes(c.batch))
    .sort((a, b) => Number(b.top_company) - Number(a.top_company))
    .slice(0, 50);
  writeIfChanged(
    path.join(YC_CACHE_DIR, 'featured.json'),
    JSON.stringify({
      fetchedAt: new Date().toISOString(),
      count: featured.length,
      companies: featured,
    }, null, 2) + '\n',
  );

  // 8. Write meta.json
  const uniqueTags = Array.from(new Set(companies.flatMap((c) => c.tags)));
  const uniqueBatches = Array.from(new Set(companies.map((c) => c.batch))).sort();
  const uniqueIndustries = Array.from(new Set(companies.flatMap((c) => c.industries)));

  const meta: YcMeta = {
    last_updated: new Date().toISOString(),
    totalCompanies: companies.length,
    totalBatches: uniqueBatches.length,
    totalTags: uniqueTags.length,
    totalIndustries: uniqueIndustries.length,
    batches: Object.fromEntries(
      uniqueBatches.map((b) => [
        b.toLowerCase().replace(/\s+/g, '-'),
        {
          name: b,
          count: companies.filter((c) => c.batch === b).length,
        },
      ])
    ),
  };
  writeIfChanged(
    path.join(YC_CACHE_DIR, 'meta.json'),
    JSON.stringify(meta, null, 2) + '\n',
  );

  // 9. Write index
  const index = {
    type: 'yc-combinator',
    fetchedAt: new Date().toISOString(),
    totalCompanies: companies.length,
    totalBatches: uniqueBatches.length,
    totalTags: uniqueTags.length,
    totalIndustries: uniqueIndustries.length,
  };
  writeIfChanged(
    path.join(YC_CACHE_DIR, 'index.json'),
    JSON.stringify(index, null, 2) + '\n',
  );

  // 10. Summary
  const elapsed = ((Date.now() - startTime) / 1000).toFixed(1);
  console.log(`\n   Done in ${elapsed}s`);
  console.log(`   Companies: ${companies.length}`);
  console.log(`   Batches: ${uniqueBatches.length}`);
  console.log(`   Tags: ${uniqueTags.length}`);
  console.log(`   Industries: ${uniqueIndustries.length}`);
  console.log(`   Changes: +${changeSet.added.length} -${changeSet.removed.length} ~${changeSet.updated.length}`);
  console.log('✅ YC data cached to yc/\n');
}

main().catch((err) => {
  console.error('💥 Fatal error:', err);
  process.exit(1);
});
