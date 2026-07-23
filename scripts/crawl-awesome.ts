#!/usr/bin/env tsx
/**
 * crawl-awesome.ts
 *
 * Crawls GitHub Awesome lists, parses their README files, and extracts
 * categorized link metadata as JSON files in registry/awesome/.
 *
 * USAGE:
 *   # Crawl all predefined awesome lists:
 *   GITHUB_TOKEN=ghp_xxx npm run crawl-awesome
 *
 *   # Crawl specific lists only:
 *   GITHUB_TOKEN=ghp_xxx tsx scripts/crawl-awesome.ts --list=awesome-distributed-systems
 *
 *   # Auto-discover awesome lists by topic (GitHub search):
 *   GITHUB_TOKEN=ghp_xxx tsx scripts/crawl-awesome.ts --discover --topic=distributed-systems
 *
 *   # Dry run (show what would be stored without writing files):
 *   GITHUB_TOKEN=ghp_xxx npm run crawl-awesome -- --dry-run
 *
 * DESIGN:
 *   - Each Awesome list becomes one JSON file in awesome/{repo-name}.json
 *   - Links are deduplicated by URL across all crawled lists
 *   - A global index.json is generated for fast lookups
 *   - Only the README.md is fetched, never the actual linked resources
 *   - Runs at the registry level (local or GitHub Action), not at the website
 *
 * ETHICAL NOTE:
 *   We store only link metadata (URL, title, description, category, source list).
 *   We do NOT download or host the content of linked resources.
 *   Users click through to the original source to read.
 */

import * as fs from 'node:fs';
import * as path from 'node:path';

// ── Types ────────────────────────────────────────────────────────────

/** A single link extracted from an Awesome list */
interface AwesomeLink {
  /** The URL of the linked resource */
  url: string;
  /** The title/name of the resource */
  title: string;
  /** Short description (text after the dash) */
  description: string | null;
  /** Category name from the ## heading */
  category: string;
  /** Which awesome list this came from */
  source: string;
  /** When this was indexed */
  indexedAt: string;
}

/** An entire awesome list */
interface AwesomeList {
  /** Owner/repo (e.g., "ligurio/awesome-distributed-systems") */
  repoId: string;
  /** Display name */
  name: string;
  /** Description from GitHub repo */
  description: string;
  /** GitHub URL */
  repoUrl: string;
  /** Star count (for ranking) */
  stars: number;
  /** Topics from GitHub */
  topics: string[];
  /** Parsed links */
  links: AwesomeLink[];
  /** Categories found in the README */
  categories: string[];
  /** When this was last crawled */
  crawledAt: string;
}

/** Aggregated index of all awesome lists */
interface AwesomeIndex {
  /** Total awesome lists crawled */
  listCount: number;
  /** Total unique links across all lists */
  totalLinks: number;
  /** When the index was generated */
  generatedAt: string;
  /** Summary by topic */
  topicSummary: Record<string, number>;
  /** All list names and their link counts */
  lists: Array<{ repoId: string; name: string; linkCount: number; stars: number }>;
}

// ── Configuration ─────────────────────────────────────────────────────

const GITHUB_TOKEN = process.env.GITHUB_TOKEN;
const GITHUB_API_BASE = 'https://api.github.com';
const AWESOME_DIR = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..', 'awesome');

/**
 * Predefined list of Awesome engineering repos to crawl.
 * These are hand-curated high-quality lists relevant to engineering.
 */
const AWESOME_REPOS: Array<{ owner: string; repo: string }> = [
  // Distributed Systems & Databases
  { owner: 'dhamaniasad', repo: 'awesome-databases' },
  { owner: 'danluu', repo: 'post-mortems' },

  // Architecture & Design
  { owner: 'binhnguyennus', repo: 'awesome-scalability' },
  { owner: 'madd86', repo: 'awesome-system-design' },

  // Programming Languages
  { owner: 'sindresorhus', repo: 'awesome' }, // The original awesome list
  { owner: 'avelino', repo: 'awesome-go' },
  { owner: 'rust-unofficial', repo: 'awesome-rust' },
  { owner: 'vinta', repo: 'awesome-python' },

  // DevOps & Infrastructure
  { owner: 'veggiemonk', repo: 'awesome-docker' },
  { owner: 'ramitsurana', repo: 'awesome-kubernetes' },

  // Tools & Platforms
  { owner: 'fffaraz', repo: 'awesome-cpp' },
  { owner: 'akullpp', repo: 'awesome-java' },
  { owner: 'agile6v', repo: 'awesome-nginx' },
  { owner: 'zoidbergwill', repo: 'awesome-ebpf' },

  // Security
  { owner: 'qazbnm456', repo: 'awesome-web-security' },
  { owner: 'paragonie', repo: 'awesome-appsec' },

  // AI / ML
  { owner: 'josephmisiti', repo: 'awesome-machine-learning' },
  { owner: 'ChristosChristofidis', repo: 'awesome-deep-learning' },
];

// ── GitHub API ────────────────────────────────────────────────────────

const GITHUB_HEADERS: Record<string, string> = {
  Accept: 'application/vnd.github.v3+json',
  'User-Agent': '100xSystems/1.0 (awesome-crawler)',
};

if (GITHUB_TOKEN) {
  GITHUB_HEADERS['Authorization'] = `Bearer ${GITHUB_TOKEN}`;
}

/** Fetch JSON from GitHub API with auth */
async function ghFetch(url: string): Promise<any> {
  const res = await fetch(url, { headers: GITHUB_HEADERS });

  if (!res.ok) {
    if (res.status === 403) {
      const reset = res.headers.get('X-RateLimit-Reset');
      const remaining = res.headers.get('X-RateLimit-Remaining');
      throw new Error(
        `GitHub API 403 (rate limit). Remaining: ${remaining}, Reset at: ${reset ? new Date(parseInt(reset) * 1000).toISOString() : 'unknown'}`
      );
    }
    if (res.status === 404) {
      return null; // Not found
    }
    throw new Error(`GitHub API ${res.status}: ${res.statusText}`);
  }

  return res.json();
}

/** Search GitHub for awesome repos by topic */
async function searchAwesomeByTopic(topic: string, limit = 20): Promise<Array<{ owner: string; repo: string }>> {
  const query = encodeURIComponent(`topic:awesome ${topic} in:name awesome`);
  const url = `${GITHUB_API_BASE}/search/repositories?q=${query}&sort=stars&order=desc&per_page=${limit}`;
  const data = await ghFetch(url);
  if (!data?.items) return [];
  return data.items
    .filter((item: any) => !item.archived && !item.fork)
    .map((item: any) => ({
      owner: item.owner.login,
      repo: item.name,
    }));
}

/** Fetch repo metadata (stars, topics, description) */
async function fetchRepoMeta(owner: string, repo: string): Promise<{
  description: string;
  stars: number;
  topics: string[];
  url: string;
} | null> {
  const data = await ghFetch(`${GITHUB_API_BASE}/repos/${owner}/${repo}`);
  if (!data) return null;
  return {
    description: data.description || '',
    stars: data.stargazers_count || 0,
    topics: data.topics || [],
    url: data.html_url || `https://github.com/${owner}/${repo}`,
  };
}

/** Fetch the README.md content (decoded from base64) */
async function fetchReadme(owner: string, repo: string): Promise<string | null> {
  const data = await ghFetch(`${GITHUB_API_BASE}/repos/${owner}/${repo}/readme`);
  if (!data?.content) return null;
  return Buffer.from(data.content, 'base64').toString('utf-8');
}

// ── Markdown Parser ──────────────────────────────────────────────────

interface ParsedSection {
  name: string;
  links: Array<{ title: string; url: string; description: string | null }>;
}

/**
 * Parse an Awesome list README and extract categorized links.
 *
 * Supported formats:
 *   ## Section Name ... ###### Section Name   (ATX h2-h6)
 *   Section Name                              (setext headings with
 *   ------------                                --- or === underline)
 *   - [Title](url) - Description              (hyphen list)
 *   * [Title](url) - Description              (asterisk list)
 *   1. [Title](url) - Description             (ordered list)
 *   | [Title](url) | Description |            (markdown table cell)
 *   <a href="url">Text</a>                    (HTML table cell)
 *   [Title](url) - Description                (bare inline link)
 *
 * The parser:
 *   - Handles nested lists (trimmed to match)
 *   - Skips TOC / contributing / license sections
 *   - Strips HTML tags from titles
 *   - Only captures http/https URLs (skips relative links and anchors)
 *   - Deduplicates by normalized URL
 */
function parseReadme(readme: string, debug = false): ParsedSection[] {
  const sections: ParsedSection[] = [];
  const lines = readme.split('\n');
  let currentSection: ParsedSection | null = null;

  const SKIP_SECTIONS = new Set([
    'contents', 'table of contents', 'toc', 'contributing',
    'license', 'footnotes', 'references',
  ]);

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i].trim();

    if (debug && i < 60) {
      // Debug: print first 60 lines to show format
      if (line.startsWith('#')) console.log(`  [debug:L${i}] ${line.substring(0, 120)}`);
    }

    // ── Detect ATX headings (## through ######) ──
    const sectionMatch = line.match(/^#{2,6}\s+(.+)/);
    if (sectionMatch) {
      const sectionName = sectionMatch[1].trim().toLowerCase();
      if (currentSection && currentSection.links.length > 0) {
        if (debug) console.log(`  [debug] Closing section "${currentSection.name}" (${currentSection.links.length} links)`);
        sections.push(currentSection);
      }
      if (!SKIP_SECTIONS.has(sectionName) && !sectionName.startsWith('#')) {
        currentSection = { name: sectionMatch[1].trim(), links: [] };
        if (debug) console.log(`  [debug] Opened section "${currentSection.name}"`);
      } else {
        if (debug) console.log(`  [debug] Skipping section "${sectionName}"`);
        currentSection = null;
      }
      continue;
    }

    // ── Detect setext headings (text followed by --- or ===) ──
    if (i + 1 < lines.length) {
      const nextLine = lines[i + 1];
      if (nextLine && /^[-=]{3,}\s*$/.test(nextLine)) {
        // Current line is text, next line is --- or ===
        if (currentSection && currentSection.links.length > 0) {
          if (debug) console.log(`  [debug] Closing section "${currentSection.name}" (${currentSection.links.length} links) for setext heading`);
          sections.push(currentSection);
        }
        const sectionName = line.toLowerCase();
        if (!SKIP_SECTIONS.has(sectionName) && !sectionName.startsWith('#')) {
          currentSection = { name: line, links: [] };
          if (debug) console.log(`  [debug] Opened setext section "${currentSection.name}"`);
        } else {
          if (debug) console.log(`  [debug] Skipping setext section "${sectionName}"`);
          currentSection = null;
        }
        i++; // Skip the ---/=== line
        continue;
      }
    }

    // ── Detect link in list item ──
    // Supports: - [Title](url), * [Title](url), 1. [Title](url)
    if (currentSection && (/^[-*]\s+\[/.test(line) || /^\d+\.\s+\[/.test(line))) {
      const linkMatch = line.match(/^(?:[-*]|\d+\.)\s+\[([^\]]+)\]\(([^)]+)\)(?:\s*[-–—:]\s+(.+))?/);
      if (linkMatch) {
        let title = linkMatch[1].trim();
        const url = linkMatch[2].trim();
        let description = linkMatch[3]?.trim() || null;

        // Clean up title (remove HTML, extra spaces)
        title = title.replace(/<[^>]+>/g, '').trim();
        if (!title) continue;

        // Skip non-http URLs and anchors
        if (!url.startsWith('http')) continue;

        currentSection.links.push({ title, url, description });
      }
      continue;
    }

    // ── Detect links in HTML table cells ──
    // Matches: <a href="https://url.com">Link Text</a>
    if (currentSection && line.includes('<a href=')) {
      const tableLinkRegex = /<a\s+href="([^"]+)"[^>]*>([^<]+)<\/a>/g;
      let tableMatch;
      let hasMatch = false;
      while ((tableMatch = tableLinkRegex.exec(line)) !== null) {
        const url = tableMatch[1].trim();
        const title = tableMatch[2].trim();
        if (url.startsWith('http') && title) {
          if (debug && !hasMatch) console.log(`  [debug] Parsed HTML table <a> in ${currentSection.name}`);
          hasMatch = true;
          currentSection.links.push({ title, url, description: null });
        }
      }
      if (hasMatch) continue;
    }

    // ── Detect links in markdown table cells ──
    // Format: | [Title](url) | Description |
    // The links might be relative paths - only capture http/https URLs
    if (currentSection && line.startsWith('|') && line.includes('[') && line.includes('](http')) {
      const tableCellRegex = /\[([^\]]+)\]\(([^)]+)\)/g;
      let cellMatch;
      let hasMatch = false;
      while ((cellMatch = tableCellRegex.exec(line)) !== null) {
        const url = cellMatch[2].trim();
        if (url.startsWith('http') || url.startsWith('https')) {
          let title = cellMatch[1].trim();
          title = title.replace(/<[^>]+>/g, '').trim();
          if (title) {
            if (debug && !hasMatch) console.log(`  [debug] Parsed markdown table link in ${currentSection.name}`);
            hasMatch = true;
            currentSection.links.push({ title, url, description: null });
          }
        }
      }
      if (hasMatch) continue;
    }

    // ── Baseline: detect inline markdown links without list prefix ──
    // Some repos use: "[Title](url) - description" on its own line
    if (currentSection && line.startsWith('[') && line.includes('](http')) {
      const bareLink = line.match(/^\[([^\]]+)\]\(([^)]+)\)(?:\s*[-–—:]\s+(.+))?/);
      if (bareLink) {
        const url = bareLink[2].trim();
        if (url.startsWith('http')) {
          let title = bareLink[1].trim();
          title = title.replace(/<[^>]+>/g, '').trim();
          if (title) {
            if (debug) console.log(`  [debug] Parsed bare markdown link in ${currentSection.name}`);
            currentSection.links.push({ title, url, description: bareLink[3]?.trim() || null });
          }
        }
      }
    }
  }

  // Push last section
  if (currentSection && currentSection.links.length > 0) {
    if (debug) console.log(`  [debug] Closing final section "${currentSection.name}" (${currentSection.links.length} links)`);
    sections.push(currentSection);
  }

  return sections;
}

// ── URL Normalization & Dedup ────────────────────────────────────────

/** Normalize a URL for deduplication (strip protocol, www, trailing slashes) */
function normalizeUrl(url: string): string {
  try {
    const u = new URL(url);
    // Remove trailing slashes, lower case hostname, strip www
    u.pathname = u.pathname.replace(/\/+$/, '');
    const hostname = u.hostname.replace(/^www\./, '');
    return hostname.toLowerCase() + u.pathname.toLowerCase();
  } catch {
    return url.toLowerCase();
  }
}

// ── Storage ──────────────────────────────────────────────────────────

function ensureAwesomeDir(): void {
  if (!fs.existsSync(AWESOME_DIR)) {
    fs.mkdirSync(AWESOME_DIR, { recursive: true });
  }
}

/** Write a single awesome list JSON file */
function writeAwesomeList(list: AwesomeList, dryRun: boolean): void {
  ensureAwesomeDir();
  if (dryRun) {
    console.log(`  [dry-run] Would write: ${list.repoId.replace('/', '-')}.json (${list.links.length} links, ${list.categories.length} categories)`);
    return;
  }
  const filePath = path.join(AWESOME_DIR, `${list.repoId.replace('/', '-')}.json`);
  const tmpPath = filePath + '.tmp';
  fs.writeFileSync(tmpPath, JSON.stringify(list, null, 2) + '\n', 'utf-8');
  fs.renameSync(tmpPath, filePath);
}

/** Generate and write the aggregated index */
function writeAwesomeIndex(allLists: AwesomeList[], dryRun: boolean): void {
  // Build topic summary
  const topicSummary: Record<string, number> = {};
  for (const list of allLists) {
    for (const topic of list.topics) {
      topicSummary[topic] = (topicSummary[topic] || 0) + 1;
    }
  }

  const index: AwesomeIndex = {
    listCount: allLists.length,
    totalLinks: allLists.reduce((sum, l) => sum + l.links.length, 0),
    generatedAt: new Date().toISOString(),
    topicSummary,
    lists: allLists.map((l) => ({
      repoId: l.repoId,
      name: l.name,
      linkCount: l.links.length,
      stars: l.stars,
    })),
  };

  if (dryRun) {
    console.log(`  [dry-run] Would write: index.json (${index.listCount} lists, ${index.totalLinks} links)`);
    return;
  }

  ensureAwesomeDir();
  const indexPath = path.join(AWESOME_DIR, 'index.json');
  const tmpPath = indexPath + '.tmp';
  fs.writeFileSync(tmpPath, JSON.stringify(index, null, 2) + '\n', 'utf-8');
  fs.renameSync(tmpPath, indexPath);
}

// ── Main ─────────────────────────────────────────────────────────────

async function main(): Promise<void> {
  const args = process.argv.slice(2);
  const dryRun = args.includes('--dry-run');
  const debug = args.includes('--debug');
  const specificList = getArgValue(args, '--list');
  const discoverTopic = getArgValue(args, '--topic');
  const limit = parseInt(getArgValue(args, '--limit') || '50', 10);

  console.log(`\n⭐  GitHub Awesome List Crawler`);
  console.log(`   Token: ${GITHUB_TOKEN ? '✅ Provided' : '❌ NOT PROVIDED (will hit rate limits)'}`);
  console.log(`   Mode: ${dryRun ? 'DRY RUN (no writes)' : 'LIVE (will write)'}`);
  console.log(`   Debug: ${debug ? 'ON' : 'OFF'}`);
  console.log();

  if (!GITHUB_TOKEN) {
    console.warn('  ⚠  No GITHUB_TOKEN set. Set GITHUB_TOKEN env var to avoid rate limiting.');
    console.warn('     Without a token: 10 requests/hour. With a token: 5,000 requests/hour.\n');
  }

  // Determine which repos to crawl
  let reposToCrawl: Array<{ owner: string; repo: string }> = [];

  if (specificList) {
    // Single list: --list=awesome-distributed-systems or --list=owner/repo
    const parts = specificList.includes('/') ? specificList.split('/') : ['sindresorhus', specificList];
    reposToCrawl = [{ owner: parts[0], repo: parts[1] }];
    console.log(`   Target: ${parts[0]}/${parts[1]}\n`);
  } else if (discoverTopic) {
    // Auto-discover by topic
    console.log(`   Searching for awesome lists related to: ${discoverTopic}\n`);
    const discovered = await searchAwesomeByTopic(discoverTopic, limit);
    reposToCrawl = discovered;
    console.log(`   Found ${discovered.length} awesome lists\n`);
  } else {
    // Use predefined list
    reposToCrawl = AWESOME_REPOS;
    console.log(`   Target: ${reposToCrawl.length} predefined awesome lists\n`);
  }

  if (reposToCrawl.length === 0) {
    console.error('   No repos to crawl. Exiting.');
    process.exit(1);
  }

  // Process each repo
  const allLists: AwesomeList[] = [];
  let totalErrors = 0;
  const allUrls = new Set<string>(); // For global dedup

  for (const { owner, repo } of reposToCrawl) {
    process.stdout.write(`  [${owner}/${repo}]... `);

    try {
      // Fetch metadata
      const meta = await fetchRepoMeta(owner, repo);
      if (!meta) {
        console.log(`❌ Not found`);
        totalErrors++;
        continue;
      }

      // Fetch README
      const readme = await fetchReadme(owner, repo);
      if (!readme) {
        console.log(`⚠  No README`);
        totalErrors++;
        continue;
      }

      // Parse sections
      const sections = parseReadme(readme, debug);
      if (sections.length === 0) {
        console.log(`⚠  No links found in README`);
        totalErrors++;
        continue;
      }

      // Build links with dedup
      const links: AwesomeLink[] = [];
      const seenLocal = new Set<string>();
      const now = new Date().toISOString();

      for (const section of sections) {
        for (const link of section.links) {
          const nurl = normalizeUrl(link.url);
          if (seenLocal.has(nurl) || allUrls.has(nurl)) continue;
          seenLocal.add(nurl);
          allUrls.add(nurl);
          links.push({
            url: link.url,
            title: link.title,
            description: link.description,
            category: section.name,
            source: `${owner}/${repo}`,
            indexedAt: now,
          });
        }
      }

      const awesomeList: AwesomeList = {
        repoId: `${owner}/${repo}`,
        name: meta.description.split('\n')[0] || repo,
        description: meta.description,
        repoUrl: meta.url,
        stars: meta.stars,
        topics: meta.topics,
        links,
        categories: sections.map((s) => s.name),
        crawledAt: now,
      };

      allLists.push(awesomeList);

      writeAwesomeList(awesomeList, dryRun);
      console.log(`✅ ${links.length} links (${sections.length} categories)`);
    } catch (err) {
      totalErrors++;
      console.log(`❌ Error: ${err instanceof Error ? err.message : String(err)}`);
    }

    // Small delay between API calls to be polite
    await new Promise((r) => setTimeout(r, 500));
  }

  // Write aggregated index
  if (allLists.length > 0) {
    writeAwesomeIndex(allLists, dryRun);
  }

  // Summary
  console.log(`\n${'─'.repeat(50)}`);
  console.log(`📊 Summary`);
  console.log(`   Successfully crawled: ${allLists.length}`);
  console.log(`   Errors: ${totalErrors}`);
  const totalUnique = allLists.reduce((sum, l) => sum + l.links.length, 0);
  console.log(`   Total unique links: ${totalUnique}`);
  console.log(`   Mode: ${dryRun ? 'DRY RUN (no files written)' : 'LIVE'}`);
  console.log(`   Complete!`);

  if (totalErrors > 0) {
    console.error(`\n⚠  ${totalErrors} feed(s) had errors — see above.`);
  }
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
