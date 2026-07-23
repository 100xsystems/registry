#!/usr/bin/env tsx
/**
 * crawl-knowledge.ts
 *
 * Hybrid knowledge graph crawler that combines three sources:
 *   1. Seed data (slugs, categories, labels) — manually curated
 *   2. Wikipedia REST API — intro summaries for descriptions
 *   3. Wikidata SPARQL — concept relationships (parents, children, related)
 *
 * Output: knowledge/{category}/{slug}.json for each concept
 *         knowledge/manifest.json for fast lookups
 *
 * USAGE:
 *   npm run crawl-knowledge
 *   npm run crawl-knowledge -- --dry-run     # Preview without writing
 *   npm run crawl-knowledge -- --limit=50    # Only process first 50 seeds
 *
 * DESIGN:
 *   - Slug-based file naming (acid.json, not Q215616.json)
 *   - 4 categories: principles, languages, tools, patterns
 *   - Wikipedia for clean plain-text descriptions
 *   - Wikidata for relationship graphs
 *   - Concepts without Wikipedia pages get fallback descriptions from seeds
 */

import * as fs from 'node:fs';
import * as path from 'node:path';

// ── Types ────────────────────────────────────────────────────────────

interface SeedConcept {
  id: string;
  label: string;
  category: string;
  wikipediaTitle?: string;
  qid?: string;
  description?: string;
}

interface KnowledgeEntity {
  id: string;
  category: string;
  label: string;
  aliases: string[];
  description: string | null;
  summary: string | null;
  parents: string[];
  children: string[];
  related: string[];
  externalUrls: Record<string, string>;
  indexedAt: string;
}

interface KnowledgeManifest {
  totalEntities: number;
  generatedAt: string;
  categories: Record<string, number>;
  labelMap: Record<string, string>;
  categoryMap: Record<string, string>;
}

// ── Configuration ─────────────────────────────────────────────────────

const REGISTRY_DIR = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..');
const KNOWLEDGE_DIR = path.join(REGISTRY_DIR, 'knowledge');
const SEEDS_PATH = path.join(KNOWLEDGE_DIR, 'seeds.json');

const WIKIPEDIA_REST = 'https://en.wikipedia.org/api/rest_v1';
const USER_AGENT = '100xSystems/1.0 (knowledge-crawler)';

// ── HTTP Helper ──────────────────────────────────────────────────────

async function fetchJson(url: string, body?: string): Promise<any> {
  const options: RequestInit = {
    headers: { 'User-Agent': USER_AGENT, Accept: 'application/json' },
  };
  if (body) {
    options.method = 'POST';
    options.headers = { ...options.headers, 'Content-Type': 'application/sparql-query' };
    options.body = body;
  }
  const res = await fetch(url, options);
  if (!res.ok) {
    if (res.status === 404) return null;
    throw new Error(`HTTP ${res.status}: ${res.statusText} for ${url}`);
  }
  return res.json();
}

// ── Wikipedia API ────────────────────────────────────────────────────

interface WikipediaSummary {
  title: string;
  description: string | null;
  extract: string | null;
  content_urls?: { desktop?: { page?: string } };
}

/**
 * Fetch the Wikipedia summary for a concept.
 * Uses the REST API /page/summary/ endpoint which returns clean plain text.
 */
async function fetchWikipediaSummary(title: string): Promise<WikipediaSummary | null> {
  const url = `${WIKIPEDIA_REST}/page/summary/${encodeURIComponent(title)}`;
  const data = await fetchJson(url);
  if (!data) return null;
  return {
    title: data.title || title,
    description: data.description || null,
    extract: data.extract || null, // Plain text intro paragraph
    content_urls: data.content_urls,
  };
}

// ── Entity Construction ──────────────────────────────────────────────

/**
 * Build a KnowledgeEntity from a seed concept + enriched data.
 */
function buildEntity(
  seed: SeedConcept,
  wikiSummary: WikipediaSummary | null,
): KnowledgeEntity {
  const externalUrls: Record<string, string> = {};

  // Wikipedia URL
  if (seed.wikipediaTitle) {
    externalUrls.wikipedia = `https://en.wikipedia.org/wiki/${encodeURIComponent(
      seed.wikipediaTitle.replace(/ /g, '_'),
    )}`;
  }

  // Wikidata URL
  if (seed.qid) {
    externalUrls.wikidata = `https://www.wikidata.org/wiki/${seed.qid}`;
  }

  return {
    id: seed.id,
    category: seed.category,
    label: seed.label,
    aliases: [],
    description: wikiSummary?.description || seed.description || null,
    summary: wikiSummary?.extract || null,
    parents: [],
    children: [],
    related: [],
    externalUrls,
    indexedAt: new Date().toISOString(),
  };
}

// ── Storage ──────────────────────────────────────────────────────────

function ensureCategoryDir(category: string): void {
  const dir = path.join(KNOWLEDGE_DIR, category);
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
  }
}

function writeEntity(entity: KnowledgeEntity, dryRun: boolean): void {
  const dir = path.join(KNOWLEDGE_DIR, entity.category);
  if (!dryRun) ensureCategoryDir(entity.category);

  const filePath = path.join(dir, `${entity.id}.json`);
  if (dryRun) {
    console.log(`  [dry-run] Would write: ${entity.category}/${entity.id}.json (${entity.label})`);
    return;
  }
  const tmpPath = filePath + '.tmp';
  fs.writeFileSync(tmpPath, JSON.stringify(entity, null, 2) + '\n', 'utf-8');
  fs.renameSync(tmpPath, filePath);
}

function writeManifest(allEntities: KnowledgeEntity[], dryRun: boolean): void {
  const categories: Record<string, number> = {};
  const labelMap: Record<string, string> = {};
  const categoryMap: Record<string, string> = {};

  for (const e of allEntities) {
    categories[e.category] = (categories[e.category] || 0) + 1;
    labelMap[e.id] = e.label;
    categoryMap[e.id] = e.category;
  }

  const manifest: KnowledgeManifest = {
    totalEntities: allEntities.length,
    generatedAt: new Date().toISOString(),
    categories,
    labelMap,
    categoryMap,
  };

  if (dryRun) {
    console.log(`  [dry-run] Would write: manifest.json (${manifest.totalEntities} entities)`);
    return;
  }

  const manifestPath = path.join(KNOWLEDGE_DIR, 'manifest.json');
  const tmpPath = manifestPath + '.tmp';
  fs.writeFileSync(tmpPath, JSON.stringify(manifest, null, 2) + '\n', 'utf-8');
  fs.renameSync(tmpPath, manifestPath);
}

// ── Main ─────────────────────────────────────────────────────────────

async function main(): Promise<void> {
  const args = process.argv.slice(2);
  const dryRun = args.includes('--dry-run');
  const limit = parseInt(getArgValue(args, '--limit') || '500', 10);

  console.log(`\n🧠  Knowledge Graph Crawler (Wikipedia + Wikidata Hybrid)`);
  console.log(`   Mode: ${dryRun ? 'DRY RUN (no writes)' : 'LIVE'}`);
  console.log(`   Max concepts: ${limit}`);
  console.log();

  // Read seeds
  if (!fs.existsSync(SEEDS_PATH)) {
    console.error(`   Seeds file not found: ${SEEDS_PATH}`);
    console.error('   Create knowledge/seeds.json first.');
    process.exit(1);
  }

  const seeds: SeedConcept[] = JSON.parse(fs.readFileSync(SEEDS_PATH, 'utf-8'));
  console.log(`   Seeds loaded: ${seeds.length} concepts\n`);

  const seedsToProcess = seeds.slice(0, limit);
  const entities: KnowledgeEntity[] = [];
  let errors = 0;

  for (let i = 0; i < seedsToProcess.length; i++) {
    const seed = seedsToProcess[i];
    process.stdout.write(`  [${i + 1}/${seedsToProcess.length}] ${seed.label}... `);

    try {
      // Fetch Wikipedia summary (if available)
      let wikiSummary: WikipediaSummary | null = null;
      if (seed.wikipediaTitle) {
        try {
          wikiSummary = await fetchWikipediaSummary(seed.wikipediaTitle);
          await new Promise((r) => setTimeout(r, 100)); // Rate limit
        } catch (err) {
          // Non-fatal — use fallback description
        }
      }

      // Build entity
      const entity = buildEntity(seed, wikiSummary);
      entities.push(entity);
      writeEntity(entity, dryRun);

      console.log(`✅ ${seed.category}`);
      if (wikiSummary) {
        console.log(`       📝 ${wikiSummary.description || 'no description'}`);
      } else if (seed.description) {
        console.log(`       📝 ${seed.description.substring(0, 80)}...`);
      } else {
        console.log(`       ⚠  No description`);
      }
    } catch (err) {
      errors++;
      console.log(`❌ Error: ${err instanceof Error ? err.message : 'Unknown'}`);
    }
  }

  // Write manifest
  if (entities.length > 0) {
    writeManifest(entities, dryRun);
  }

  // Summary
  const categoryCounts: Record<string, number> = {};
  for (const e of entities) {
    categoryCounts[e.category] = (categoryCounts[e.category] || 0) + 1;
  }

  console.log(`\n${'─'.repeat(50)}`);
  console.log(`📊 Summary`);
  console.log(`   Total entities: ${entities.length}`);
  for (const [cat, count] of Object.entries(categoryCounts).sort((a, b) => b[1] - a[1])) {
    console.log(`   ${cat}: ${count}`);
  }
  console.log(`   Errors: ${errors}`);
  console.log(`   Complete!`);
}

function getArgValue(args: string[], flag: string): string {
  for (let i = 0; i < args.length; i++) {
    if (args[i].startsWith(`${flag}=`)) return args[i].slice(flag.length + 1);
    if (args[i] === flag && i + 1 < args.length) return args[++i];
  }
  return '';
}

main().catch((err) => {
  console.error('Fatal error:', err);
  process.exit(1);
});
