#!/usr/bin/env tsx
/**
 * fetch-yc-changes.ts — DAILY YC CHANGE TRACKER
 *
 * Fetches ALL Y Combinator companies from Algolia, compares with the stored
 * companies.json, and saves only the CHANGE SET to yc/changes/.
 *
 * If changes are detected:
 *   - Updates yc/companies.json with the latest data
 *   - Saves diff to yc/changes/YYYY-MM-DD.json
 *   - Updates yc/changes/latest.json + latest.md
 *
 * If no changes:
 *   - Saves heartbeat to yc/changes/YYYY-MM-DD.json
 *
 * USAGE:
 *   tsx scripts/github-workflow/fetch-yc-changes.ts
 *
 * Runs daily via the daily-feed-update.yml GitHub Actions workflow.
 *
 * NOTE: The initial companies.json, featured.json, meta.json, index.json
 * must be seeded first via scripts/one-time/fetch-yc-bulk.ts.
 */

import * as fs from 'node:fs';
import * as path from 'node:path';

// ── Config ────────────────────────────────────────────────────────────

const YC_CACHE_DIR = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..', '..', 'yc');
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

// ── Helpers ───────────────────────────────────────────────────────────

function ensureDir(dir: string): void {
  if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
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

async function fetchAllCompanies(apiKey: string): Promise<YcCompany[]> {
  console.log('  Fetching batch facets...');
  const facetResult = await queryAlgolia(apiKey,
    'facets=%5B%22batch%22%5D&hitsPerPage=1&maxValuesPerFacet=1000&query=&tagFilters='
  );
  const facets = facetResult.facets as Record<string, Record<string, number>> | undefined;
  const batches = facets?.batch;
  if (!batches) throw new Error('Algolia response did not include batch facets');
  console.log(`  Found ${Object.keys(batches).length} batches`);

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
      if (key === 'url' || key === 'long_description') continue; // skip computed/large fields
      if (!valuesEqual(prev[key], curr[key])) {
        changes.push({ field: key, before: prev[key], after: curr[key] });
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
  const header = `# YC Company Changes for ${changes.date}\n\n- Previous total: ${changes.previousCount}\n- Current total: ${changes.currentCount}\n- Added: ${changes.added.length}\n- Removed: ${changes.removed.length}\n- Updated: ${changes.updated.length}\n\n`;

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
  console.log('\n🔬 Fetching YC changes via Algolia...');
  const startTime = Date.now();

  ensureDir(YC_CACHE_DIR);
  ensureDir(CHANGES_DIR);

  // 1. Get Algolia API key
  console.log('  Getting Algolia API key...');
  const apiKey = await getAlgoliaKey();
  console.log('  ✓ Algolia key obtained');

  // 2. Fetch all companies from Algolia
  console.log('  Fetching current data...');
  const companies = await fetchAllCompanies(apiKey);
  console.log(`  ✓ ${companies.length} companies fetched`);

  const today = dateStr();

  // 3. Read previous companies.json for change comparison
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
    // First run after seed: companies.json already exists from bulk script,
    // just note this as first tracked date with no changes reported
    const heartbeat = JSON.stringify({
      date: today,
      fetchedAt: new Date().toISOString(),
      message: 'First daily check — no changes since bulk import',
      total: companies.length,
    }, null, 2) + '\n';
    writeIfChanged(path.join(CHANGES_DIR, `${today}.json`), heartbeat);
    writeIfChanged(path.join(CHANGES_DIR, 'latest.json'), heartbeat);
    writeIfChanged(path.join(CHANGES_DIR, 'latest.md'),
      `# YC Company Changes for ${today}\n\nFirst daily check — ${companies.length} companies — no changes since bulk import.\n`
    );
    console.log(`  ✓ First daily check: ${companies.length} companies (no changes tracked)`);
  } else if (hasChanges) {
    const changesJson = JSON.stringify(changeSet, null, 2) + '\n';

    // Write date-stamped change file
    writeIfChanged(path.join(CHANGES_DIR, `${today}.json`), changesJson);
    // Write latest.json
    writeIfChanged(path.join(CHANGES_DIR, 'latest.json'), changesJson);
    // Write latest.md
    writeIfChanged(path.join(CHANGES_DIR, 'latest.md'), renderChangesMarkdown(changeSet));

    // Update companies.json with the latest data (only if changes occurred)
    const catalog = companies.sort((a, b) => b.id - a.id);
    writeIfChanged(
      path.join(YC_CACHE_DIR, 'companies.json'),
      JSON.stringify({
        fetchedAt: new Date().toISOString(),
        count: catalog.length,
        companies: catalog,
      }, null, 2) + '\n',
    );

    console.log(`  ✓ Changes: +${changeSet.added.length} -${changeSet.removed.length} ~${changeSet.updated.length}`);
  } else {
    // No changes — write heartbeat
    const heartbeat = JSON.stringify({
      date: today,
      fetchedAt: new Date().toISOString(),
      message: 'No changes',
      total: companies.length,
    }, null, 2) + '\n';
    writeIfChanged(path.join(CHANGES_DIR, `${today}.json`), heartbeat);
    writeIfChanged(path.join(CHANGES_DIR, 'latest.json'), heartbeat);
    writeIfChanged(path.join(CHANGES_DIR, 'latest.md'),
      `# YC Company Changes for ${today}\n\nNo company records changed. Still ${companies.length} companies.\n`
    );
    console.log('  ✓ No changes detected');
  }

  // 6. Summary
  const elapsed = ((Date.now() - startTime) / 1000).toFixed(1);
  console.log(`\n   Done in ${elapsed}s`);
  console.log(`   Companies: ${companies.length}`);
  console.log(`   Changes: +${changeSet.added.length} -${changeSet.removed.length} ~${changeSet.updated.length}`);
  console.log('✅ YC changes tracked\n');
}

main().catch((err) => {
  console.error('💥 Fatal error:', err);
  process.exit(1);
});
