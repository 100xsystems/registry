#!/usr/bin/env tsx
/**
 * fetch-yc-bulk.ts — ONE-TIME YC BULK FETCHER
 *
 * Fetches ALL Y Combinator companies from Algolia and saves the full catalog.
 * Run ONCE manually to seed the initial data.
 *
 * USAGE:
 *   tsx scripts/one-time/fetch-yc-bulk.ts
 *
 * OUTPUT:
 *   yc/companies.json     — All 6000+ companies (merged catalog)
 *   yc/featured.json      — Top 50 from recent 4 batches (for homepage)
 *   yc/meta.json          — Metadata (counts, batches, tags, industries)
 *   yc/index.json         — Index for the website
 */

import * as fs from 'node:fs';
import * as path from 'node:path';

// ── Config ────────────────────────────────────────────────────────────

const YC_CACHE_DIR = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..', '..', 'yc');
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
  if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
}

function writeFile(filePath: string, data: unknown): void {
  fs.writeFileSync(filePath, JSON.stringify(data, null, 2) + '\n', 'utf-8');
  const size = fs.statSync(filePath).size;
  console.log(`  ✓ ${path.basename(filePath)} — ${(size / 1024 / 1024).toFixed(1)}MB`);
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

  return allCompanies.sort((a, b) => b.id - a.id);
}

// ── Main ──────────────────────────────────────────────────────────────

async function main(): Promise<void> {
  console.log('\n🔬 [ONE-TIME] Fetching YC Combinator bulk data...');
  const startTime = Date.now();

  ensureDir(YC_CACHE_DIR);

  // 1. Get Algolia API key
  console.log('  Getting Algolia API key...');
  const apiKey = await getAlgoliaKey();
  console.log('  ✓ Algolia key obtained');

  // 2. Fetch all companies
  console.log('  Fetching all companies...');
  const companies = await fetchAllCompanies(apiKey);
  console.log(`  ✓ ${companies.length} companies fetched`);

  // 3. Write companies.json (full merged catalog)
  writeFile(
    path.join(YC_CACHE_DIR, 'companies.json'),
    {
      fetchedAt: new Date().toISOString(),
      count: companies.length,
      companies,
    },
  );

  // 4. Write featured.json (top 50 from recent 4 batches)
  const allBatchNames = Array.from(new Set(companies.map((c) => c.batch)))
    .filter((b) => b !== 'Unspecified')
    .sort((a, b) => {
      const numA = parseInt(a.slice(1), 10);
      const numB = parseInt(b.slice(1), 10);
      if (numB !== numA) return numB - numA;
      const seasonOrder: Record<string, number> = { F: 0, S: 1, W: 2 };
      return (seasonOrder[a[0]] ?? 3) - (seasonOrder[b[0]] ?? 3);
    });
  const recentBatches = allBatchNames.slice(0, 4);
  const featured = companies
    .filter((c) => recentBatches.includes(c.batch))
    .sort((a, b) => (Number(b.top_company) - Number(a.top_company)) || (b.launched_at - a.launched_at))
    .slice(0, 50);
  writeFile(
    path.join(YC_CACHE_DIR, 'featured.json'),
    {
      fetchedAt: new Date().toISOString(),
      count: featured.length,
      companies: featured,
    },
  );

  // 5. Write meta.json
  const uniqueBatches = Array.from(new Set(companies.map((c) => c.batch))).sort();
  const uniqueTags = Array.from(new Set(companies.flatMap((c) => c.tags)));
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
        { name: b, count: companies.filter((c) => c.batch === b).length },
      ]),
    ),
  };
  writeFile(path.join(YC_CACHE_DIR, 'meta.json'), meta);

  // 6. Write index.json
  writeFile(path.join(YC_CACHE_DIR, 'index.json'), {
    type: 'yc-combinator',
    fetchedAt: new Date().toISOString(),
    totalCompanies: companies.length,
    totalBatches: uniqueBatches.length,
    totalTags: uniqueTags.length,
    totalIndustries: uniqueIndustries.length,
  });

  // 7. Summary
  const elapsed = ((Date.now() - startTime) / 1000).toFixed(1);
  console.log(`\n   ✅ Done in ${elapsed}s`);
  console.log(`   Companies: ${companies.length}`);
  console.log(`   Batches: ${uniqueBatches.length}`);
  console.log(`   Tags: ${uniqueTags.length}`);
  console.log(`   Industries: ${uniqueIndustries.length}`);
  console.log('\n⚠  This is a ONE-TIME seed script. Do NOT run in CI.\n');
}

main().catch((err) => {
  console.error('💥 Fatal error:', err);
  process.exit(1);
});
