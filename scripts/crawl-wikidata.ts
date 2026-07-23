#!/usr/bin/env tsx
/**
 * crawl-wikidata.ts
 *
 * Bootstraps a knowledge graph of software engineering concepts from Wikidata.
 *
 * HOW IT WORKS:
 *   1. Define seed concepts by label names (e.g. "ACID", "CAP theorem")
 *   2. Resolve each to its Wikidata QID via the entity search API
 *   3. Fetch relationships (parents, children, instances, aliases, descriptions)
 *      via SPARQL queries
 *   4. Recursively expand to discover new concepts (up to a configurable limit)
 *   5. Store each entity as a JSON file in registry/knowledge/entities/
 *   6. Generate a manifest.json for fast lookups
 *
 * USAGE:
 *   npm run crawl-wikidata
 *   npm run crawl-wikidata -- --limit=500       # Max total entities to index
 *   npm run crawl-wikidata -- --dry-run         # Preview without writing
 *   npm run crawl-wikidata -- --concept=ACID    # Fetch a single concept
 *
 * ETHICAL NOTE:
 *   We store only metadata from Wikidata (labels, descriptions, relationships).
 *   All content is sourced from Wikidata's CC0-licensed dataset.
 *   We respect Wikidata's rate limits and include delays between queries.
 */

import * as fs from 'node:fs';
import * as path from 'node:path';

// ── Types ────────────────────────────────────────────────────────────

interface KnowledgeEntity {
  /** Wikidata QID (e.g. "Q215616") */
  id: string;
  /** Entity type: concept, technology, pattern, language, etc. */
  type: string;
  /** Display label */
  label: string;
  /** Short description from Wikidata */
  description: string | null;
  /** Alternative labels / aliases */
  aliases: string[];
  /** Parent concept IDs (wdt:P279 - subclass of) */
  parents: string[];
  /** Child concept IDs (inverse of P279) */
  children: string[];
  /** Instance of IDs (wdt:P31) */
  instanceOf: string[];
  /** Related concept IDs (wdt:P361 - part of, wdt:P527 - has part, wdt:P155/P156 follows/followed by) */
  related: string[];
  /** External URLs */
  externalUrls: Record<string, string>;
  /** When this entity was indexed */
  indexedAt: string;
}

interface KnowledgeManifest {
  totalEntities: number;
  generatedAt: string;
  byType: Record<string, number>;
  topLevel: Array<{ id: string; label: string; entityCount: number }>;
}

interface WikidataEntity {
  id: string;
  label: string;
  description: string | null;
  aliases: string[];
  parents: string[];
  instanceOf: string[];
  related: string[];
  externalUrls: Record<string, string>;
}

// ── Configuration ─────────────────────────────────────────────────────

const KNOWLEDGE_DIR = path.resolve(
  path.dirname(new URL(import.meta.url).pathname),
  '..',
  'knowledge',
);

const ENTITIES_DIR = path.join(KNOWLEDGE_DIR, 'entities');

const WIKIDATA_API = 'https://www.wikidata.org/w/api.php';
const WIKIDATA_SPARQL = 'https://query.wikidata.org/sparql';
const USER_AGENT = '100xSystems/1.0 (knowledge-crawler; contact@100xsystems.com)';

/**
 * Seed concepts — foundational engineering topics to bootstrap the graph.
 * Each will be resolved to its Wikidata QID via the entity search API.
 * These cover: databases, distributed systems, networking, architecture, security, AI, etc.
 */
const SEED_CONCEPTS: string[] = [
  // Computing Foundations
  'Computer science',
  'Software engineering',
  'Computer engineering',
  'Computer programming',
  'Algorithm',
  'Data structure',

  // Databases
  'Database',
  'Relational database',
  'NoSQL',
  'SQL',
  'Transaction processing',
  'ACID',
  'CAP theorem',
  'Index (database)',
  'Database replication',
  'Shard (database architecture)',
  'B-tree',
  'Hash table',
  'Cache (computing)',
  'Data warehouse',
  'OLAP',
  'OLTP',
  'Object–relational mapping',
  'Data modeling',

  // Distributed Systems
  'Distributed computing',
  'Distributed system',
  'Consensus (computer science)',
  'Paxos (computer science)',
  'Raft (computer science)',
  'MapReduce',
  'Publish–subscribe pattern',
  'Message queue',
  'Load balancing (computing)',
  'Microservices',
  'Service mesh',
  'Event-driven architecture',
  'Consistent hashing',
  'Content delivery network',

  // Networking
  'Computer network',
  'OSI model',
  'TCP/IP',
  'HTTP',
  'DNS',
  'Transport Layer Security',
  'API',
  'REST',
  'gRPC',
  'WebSocket',
  'Domain Name System',
  'Reverse proxy',
  'API gateway',

  // System Design & Architecture
  'Systems design',
  'Software architecture',
  'Design Patterns',
  'Monolithic application',
  'Model–view–controller',
  'Domain-driven design',
  'Test-driven development',
  'CI/CD',
  'Scalability',
  'High availability',
  'Fault tolerance',
  'Observability (software)',

  // Operating Systems & Infrastructure
  'Operating system',
  'Linux',
  'Virtualization',
  'Containerization (computing)',
  'Docker (software)',
  'Kubernetes',
  'Serverless computing',
  'Infrastructure as code',

  // Security
  'Computer security',
  'Authentication',
  'OAuth',
  'Identity management',
  'Encryption',
  'Zero trust security',

  // Programming Languages & Compilers
  'Programming language',
  'Compiler',
  'Type system',
  'Garbage collection (computer science)',
  'Interpreter (computing)',
  'Assembly language',
  'Functional programming',
  'Object-oriented programming',
  'Reactive programming',

  // AI / ML
  'Artificial intelligence',
  'Machine learning',
  'Deep learning',
  'Neural network',
  'Natural language processing',
  'Computer vision',
  'Large language model',
  'Reinforcement learning',
  'Recommendation system',
  'Vector database',
];

// ── Wikidata API ──────────────────────────────────────────────────────

async function fetchJson(url: string, body?: string): Promise<any> {
  const options: RequestInit = {
    headers: {
      'User-Agent': USER_AGENT,
      Accept: 'application/json',
    },
  };

  if (body) {
    options.method = 'POST';
    options.headers = { ...options.headers, 'Content-Type': 'application/sparql-query' };
    options.body = body;
  }

  const res = await fetch(url, options);
  if (!res.ok) {
    throw new Error(`HTTP ${res.status}: ${res.statusText} for ${url}`);
  }
  return res.json();
}

/**
 * Search Wikidata for an entity by label.
 * Returns the top match or null.
 */
async function searchEntityByLabel(
  label: string,
): Promise<{ id: string; label: string; description: string | null } | null> {
  const url = `${WIKIDATA_API}?action=wbsearchentities&search=${encodeURIComponent(label)}&language=en&limit=3&format=json`;
  const data = await fetchJson(url);

  if (!data?.search?.length) return null;

  // Pick the best match: prefer exact label match, then first result
  const exact = data.search.find(
    (s: any) => s.label?.toLowerCase() === label.toLowerCase(),
  );
  const match = exact || data.search[0];

  return {
    id: match.id,
    label: match.label || label,
    description: match.description || null,
  };
}

/**
 * Fetch an entity's full data from Wikidata via SPARQL.
 * Gets: label, description, aliases, subclass-of parents, instance-of, related concepts.
 */
async function fetchEntitySparql(qid: string): Promise<WikidataEntity> {
  // Query for relationships
  const sparql = `
    SELECT ?parent ?parentLabel ?instance ?instanceLabel ?related ?relatedLabel ?relatedProp WHERE {
      VALUES ?entity { wd:${qid} }

      # Subclass of (parent)
      OPTIONAL { ?entity wdt:P279 ?parent . }

      # Instance of
      OPTIONAL { ?entity wdt:P31 ?instance . }

      # Part of
      OPTIONAL { ?entity wdt:P361 ?related . BIND("partOf" AS ?relatedProp) }

      # Has part
      OPTIONAL { ?entity wdt:P527 ?hasPart . BIND("hasPart" AS ?relatedProp) }

      # Follows / Followed by
      OPTIONAL { ?entity wdt:P155 ?follows . BIND("follows" AS ?relatedProp) }
      OPTIONAL { ?entity wdt:P156 ?followedBy . BIND("followedBy" AS ?relatedProp) }

      SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
    }
  `;

  const data = await fetchJson(WIKIDATA_SPARQL, sparql);
  const bindings = data?.results?.bindings || [];

  const parents: string[] = [];
  const instanceOf: string[] = [];
  const related: string[] = [];
  const childRefs: Set<string> = new Set();

  for (const b of bindings) {
    if (b.parent) {
      const pid = b.parent.value.split('/').pop()!;
      if (!parents.includes(pid)) parents.push(pid);
    }
    if (b.instance) {
      const iid = b.instance.value.split('/').pop()!;
      if (!instanceOf.includes(iid)) instanceOf.push(iid);
    }
    if (b.related && b.relatedProp?.value === 'partOf') {
      const rid = b.related.value.split('/').pop()!;
      if (!related.includes(rid)) related.push(rid);
    }
    if (b.related && b.relatedProp?.value === 'child') {
      const cid = b.related.value.split('/').pop()!;
      childRefs.add(cid);
    }
  }

  // Fetch aliases via the entity data API (SPARQL doesn't easily return aliases)
  let aliases: string[] = [];
  let label = qid;
  let description: string | null = null;
  let wikipediaTitle: string | null = null;

  try {
    const entData = await fetchJson(
      `${WIKIDATA_API}?action=wbgetentities&ids=${qid}&props=labels|descriptions|aliases|sitelinks&languages=en&format=json`,
    );
    const entity = entData?.entities?.[qid];
    if (entity) {
      label = entity.labels?.en?.value || qid;
      description = entity.descriptions?.en?.value || null;
      aliases = (entity.aliases?.en || []).map((a: any) => a.value);
      wikipediaTitle = entity.sitelinks?.enwiki?.title || null;
    }
  } catch {
    // Non-fatal — we can use the SPARQL-derived data
  }

  // Build external URLs with real Wikipedia title if available
  const externalUrls: Record<string, string> = {
    wikidata: `https://www.wikidata.org/wiki/${qid}`,
  };
  if (wikipediaTitle) {
    externalUrls.wikipedia = `https://en.wikipedia.org/wiki/${encodeURIComponent(
      wikipediaTitle.replace(/ /g, '_'),
    )}`;
  }

  return {
    id: qid,
    label,
    description,
    aliases,
    parents,
    instanceOf,
    related,
    externalUrls,
  };
}

/**
 * Fetch child concepts (inverse of P279 — subclass of this entity).
 */
async function fetchChildren(qid: string): Promise<Array<{ id: string; label: string }>> {
  const sparql = `
    SELECT ?child ?childLabel WHERE {
      ?child wdt:P279 wd:${qid} .
      SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
    }
    LIMIT 200
  `;

  const data = await fetchJson(WIKIDATA_SPARQL, sparql);
  const bindings = data?.results?.bindings || [];

  return bindings
    .filter((b: any) => b.child)
    .map((b: any) => ({
      id: b.child.value.split('/').pop()!,
      label: b.childLabel?.value || b.child.value.split('/').pop()!,
    }));
}

// ── Entity Type Detection ────────────────────────────────────────────

/**
 * Determine the entity type based on instance-of / parent classes.
 */
function detectEntityType(entity: WikidataEntity): string {
  const labels = [...entity.instanceOf, ...entity.parents];

  // These are QIDs for common top-level types
  const typeMap: Array<{ qids: string[]; type: string }> = [
    { qids: ['Q9143'], type: 'programming-language' },
    { qids: ['Q8513'], type: 'database-concept' },
    { qids: ['Q203105', 'Q177625'], type: 'distributed-systems-concept' },
    { qids: ['Q1301371', 'Q1325973'], type: 'networking-concept' },
    { qids: ['Q16560', 'Q896238'], type: 'api-concept' },
    { qids: ['Q2539', 'Q11660'], type: 'ai-concept' },
    { qids: ['Q9135'], type: 'os-concept' },
    { qids: ['Q47506'], type: 'compiler-concept' },
    { qids: ['Q8366', 'Q192371'], type: 'algorithm-data-structure' },
    { qids: ['Q2976309'], type: 'design-pattern' },
    { qids: ['Q539330'], type: 'architecture-pattern' },
    { qids: ['Q7067606'], type: 'architecture-pattern' },
    { qids: ['Q141090', 'Q152759'], type: 'security-concept' },
    { qids: ['Q10773'], type: 'memory-management' },
    { qids: ['Q171147'], type: 'virtualization-concept' },
  ];

  for (const { qids, type } of typeMap) {
    if (qids.some((q) => labels.includes(q))) return type;
  }

  return 'concept';
}

// ── Storage ───────────────────────────────────────────────────────────

function ensureKnowledgeDirs(): void {
  if (!fs.existsSync(ENTITIES_DIR)) {
    fs.mkdirSync(ENTITIES_DIR, { recursive: true });
  }
}

function writeEntity(entity: KnowledgeEntity, dryRun: boolean): void {
  if (dryRun) {
    console.log(`  [dry-run] Would write: entities/${entity.id}.json (${entity.label})`);
    return;
  }
  const filePath = path.join(ENTITIES_DIR, `${entity.id}.json`);
  const tmpPath = filePath + '.tmp';
  fs.writeFileSync(tmpPath, JSON.stringify(entity, null, 2) + '\n', 'utf-8');
  fs.renameSync(tmpPath, filePath);
}

function writeManifest(allEntities: KnowledgeEntity[], dryRun: boolean): void {
  const byType: Record<string, number> = {};
  for (const e of allEntities) {
    byType[e.type] = (byType[e.type] || 0) + 1;
  }

  // Top-level concepts: entities with no parents
  const topLevel = allEntities
    .filter((e) => e.parents.length === 0)
    .slice(0, 50)
    .map((e) => ({
      id: e.id,
      label: e.label,
      entityCount: allEntities.filter((c) => c.parents.includes(e.id)).length,
    }));

  const manifest: KnowledgeManifest = {
    totalEntities: allEntities.length,
    generatedAt: new Date().toISOString(),
    byType,
    topLevel,
  };

  if (dryRun) {
    console.log(`  [dry-run] Would write: manifest.json (${manifest.totalEntities} entities)`);
    return;
  }

  ensureKnowledgeDirs();
  const manifestPath = path.join(KNOWLEDGE_DIR, 'manifest.json');
  const tmpPath = manifestPath + '.tmp';
  fs.writeFileSync(tmpPath, JSON.stringify(manifest, null, 2) + '\n', 'utf-8');
  fs.renameSync(tmpPath, manifestPath);
}

// ── Main ─────────────────────────────────────────────────────────────

async function main(): Promise<void> {
  const args = process.argv.slice(2);
  const dryRun = args.includes('--dry-run');
  const maxEntities = parseInt(getArgValue(args, '--limit') || '200', 10);
  const singleConcept = getArgValue(args, '--concept');

  console.log(`\n🧠  Wikidata Knowledge Graph Crawler`);
  console.log(`   Mode: ${dryRun ? 'DRY RUN (no writes)' : 'LIVE'}`);
  console.log(`   Max entities: ${maxEntities}`);
  console.log();

  if (singleConcept) {
    console.log(`   Single concept: "${singleConcept}"\n`);
  }

  // Step 1: Resolve seed concepts to QIDs
  const conceptsToResolve = singleConcept ? [singleConcept] : SEED_CONCEPTS;
  const resolvedQids: Map<string, { id: string; label: string; description: string | null }> = new Map();

  console.log('📡 Resolving seed concepts to Wikidata QIDs...\n');

  for (let i = 0; i < conceptsToResolve.length; i++) {
    const name = conceptsToResolve[i];
    process.stdout.write(`  [${i + 1}/${conceptsToResolve.length}] ${name}... `);

    try {
      const result = await searchEntityByLabel(name);
      if (result) {
        resolvedQids.set(result.id, result);
        console.log(`✅ ${result.id}`);
      } else {
        console.log(`⚠  Not found`);
      }
    } catch (err) {
      console.log(`❌ Error: ${err instanceof Error ? err.message : 'Unknown'}`);
    }

    // Delay to be kind to Wikidata
    await new Promise((r) => setTimeout(r, 200));
  }

  console.log(`\n   Resolved ${resolvedQids.size}/${conceptsToResolve.length} concepts to QIDs.\n`);

  if (resolvedQids.size === 0) {
    console.error('   No concepts resolved. Exiting.');
    process.exit(1);
  }

  // Step 2: Fetch relationships for each resolved QID
  const allEntities: Map<string, KnowledgeEntity> = new Map();
  const queue = [...resolvedQids.keys()];
  const seen = new Set<string>();
  let childrenToExplore: string[] = [];

  console.log('🔗 Fetching relationships...\n');

  while (queue.length > 0 && allEntities.size < maxEntities) {
    const qid = queue.shift()!;
    if (seen.has(qid)) continue;
    seen.add(qid);
    const seedInfo = resolvedQids.get(qid);

    process.stdout.write(`  [${allEntities.size + 1}/${maxEntities}] ${seedInfo?.label || qid}... `);

    try {
      const entity = await fetchEntitySparql(qid);

      // Fetch children (subclasses) for this entity
      let children: Array<{ id: string; label: string }> = [];
      try {
        children = await fetchChildren(qid);
      } catch {
        // Non-fatal
      }

      const knowledgeEntity: KnowledgeEntity = {
        id: entity.id,
        type: detectEntityType(entity),
        label: entity.label,
        description: entity.description || seedInfo?.description || null,
        aliases: entity.aliases,
        parents: entity.parents,
        children: children.map((c) => c.id),
        instanceOf: entity.instanceOf,
        related: entity.related,
        externalUrls: entity.externalUrls,
        indexedAt: new Date().toISOString(),
      };

      allEntities.set(qid, knowledgeEntity);
      writeEntity(knowledgeEntity, dryRun);

      // Add children to the exploration queue (up to limit)
      for (const child of children) {
        if (!seen.has(child.id) && !queue.includes(child.id) && allEntities.size < maxEntities) {
          childrenToExplore.push(child.id);
        }
      }

      console.log(`✅ ${entity.label} (${entity.children?.length || 0} children)`);
    } catch (err) {
      console.log(`❌ Error: ${err instanceof Error ? err.message : 'Unknown'}`);
    }

    // Delay
    await new Promise((r) => setTimeout(r, 300));

    // When the current queue is exhausted, move children into queue
    if (queue.length === 0 && childrenToExplore.length > 0) {
      // Deduplicate and limit
      const unique = [...new Set(childrenToExplore)]
        .filter((id) => !seen.has(id))
        .slice(0, maxEntities - allEntities.size);
      queue.push(...unique);
      childrenToExplore = [];
      console.log(`\n   📦 Expanding to ${queue.length} children...\n`);
    }
  }

  // Write manifest
  const entities = [...allEntities.values()];
  if (entities.length > 0) {
    writeManifest(entities, dryRun);
  }

  // Summary
  console.log(`\n${'─'.repeat(50)}`);
  console.log(`📊 Summary`);
  console.log(`   Seed concepts resolved: ${resolvedQids.size}`);
  console.log(`   Total entities indexed: ${entities.length}`);

  const byType: Record<string, number> = {};
  for (const e of entities) {
    byType[e.type] = (byType[e.type] || 0) + 1;
  }
  for (const [type, count] of Object.entries(byType).sort((a, b) => b[1] - a[1])) {
    console.log(`   ${type}: ${count}`);
  }

  console.log(`   Mode: ${dryRun ? 'DRY RUN (no files written)' : `LIVE → ${KNOWLEDGE_DIR}`}`);
  console.log(`   Complete!`);
}

// ── Utility ──────────────────────────────────────────────────────────

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
