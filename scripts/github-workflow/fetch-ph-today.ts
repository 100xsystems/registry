#!/usr/bin/env tsx
/**
 * fetch-ph-today.ts — DAILY PRODUCT HUNT TODAY FETCHER
 *
 * Fetches today's Product Hunt posts using the official API v2.
 * Saves to a day-wise JSON file: producthunt/YYYY-MM-DD.json
 *
 * USAGE:
 *   PH_API_KEY=xxx PH_API_SECRET=xxx tsx scripts/github-workflow/fetch-ph-today.ts
 *   PH_DEV_TOKEN=xxx tsx scripts/github-workflow/fetch-ph-today.ts
 *
 * ENV VARS:
 *   PH_DEV_TOKEN    — Developer token (simplest, never expires)
 *   PH_API_KEY      — API key (for OAuth2 client credentials)
 *   PH_API_SECRET   — API secret (for OAuth2 client credentials)
 *
 * NOTE: The initial products.json catalog must be seeded first
 * via scripts/one-time/fetch-ph-bulk.ts.
 */

import * as fs from 'node:fs';
import * as path from 'node:path';

// ── Config ────────────────────────────────────────────────────────────

const TOKEN_URL = 'https://api.producthunt.com/v2/oauth/token';
const GRAPHQL_URL = 'https://api.producthunt.com/v2/api/graphql';
const PH_CACHE_DIR = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..', '..', 'producthunt');
const FETCH_TIMEOUT_MS = 15_000;
const MAX_PAGES_PER_DAY = 5;       // 50 posts/page × 5 = 250 max per day
const PAGE_DELAY_MS = 200;

const POSTS_QUERY = `
query GetPosts($after: String, $postedBefore: DateTime, $postedAfter: DateTime, $first: Int) {
  posts(first: $first, after: $after, postedAfter: $postedAfter, postedBefore: $postedBefore) {
    totalCount
    pageInfo { hasNextPage endCursor }
    edges {
      node {
        id
        name
        tagline
        description
        url
        website
        slug
        votesCount
        commentsCount
        reviewsCount
        reviewsRating
        dailyRank
        featuredAt
        createdAt
        makers { name username }
        topics(first: 5) {
          edges { node { name slug } }
        }
        thumbnail { type url(width: 640) }
        media {
          type url videoUrl
        }
      }
    }
  }
}
`.trim();

// ── Types ────────────────────────────────────────────────────────────

interface PhPost {
  id: string;
  name: string;
  tagline: string;
  description: string | null;
  url: string;
  website: string;
  slug: string;
  votesCount: number;
  commentsCount: number;
  reviewsCount: number;
  reviewsRating: number;
  dailyRank: number | null;
  featuredAt: string | null;
  createdAt: string;
  makers: { name: string; username: string }[];
  topics: { name: string; slug: string }[];
  thumbnail: { type: string; url: string } | null;
  media: Array<{ type: string; url: string; videoUrl: string | null }>;
}

interface PhIndex {
  type: 'producthunt';
  fetchedAt: string;
  lastFetchedDate: string;
  firstFetchedDate: string;
  totalDaysFetched: number;
  totalProducts: number;
  availableDates: string[];
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

// ── Authentication ──────────────────────────────────────────────────

async function getAccessToken(): Promise<string> {
  const devToken = process.env.PH_DEV_TOKEN;
  if (devToken) {
    console.log('  Using PH_DEV_TOKEN');
    return devToken;
  }

  const apiKey = process.env.PH_API_KEY;
  const apiSecret = process.env.PH_API_SECRET;
  if (apiKey && apiSecret) {
    console.log('  Getting access token via OAuth2...');
    const response = await fetch(TOKEN_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: new URLSearchParams({
        grant_type: 'client_credentials',
        client_id: apiKey,
        client_secret: apiSecret,
      }),
      signal: AbortSignal.timeout(10_000),
    });
    if (!response.ok) {
      const text = await response.text();
      throw new Error(`HTTP ${response.status}: ${text}`);
    }
    const data = (await response.json()) as { access_token: string };
    console.log('  ✓ Access token obtained');
    return data.access_token;
  }

  throw new Error(
    'No PH API credentials found. Set PH_DEV_TOKEN or PH_API_KEY + PH_API_SECRET env vars.',
  );
}

// ── GraphQL Query ───────────────────────────────────────────────────

async function fetchPostsPage(
  token: string,
  after: string | null,
  postedAfter: string,
  postedBefore: string,
): Promise<{ posts?: { totalCount: number; pageInfo: { hasNextPage: boolean; endCursor: string | null }; edges: Array<{ node: Record<string, unknown> }> } }> {
  const variables: Record<string, unknown> = {
    first: 50,
    postedAfter,
    postedBefore,
  };
  if (after) variables.after = after;

  const response = await fetch(GRAPHQL_URL, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'User-Agent': '100xSystems-PHFetcher/1.0',
    },
    body: JSON.stringify({ query: POSTS_QUERY, variables }),
    signal: AbortSignal.timeout(FETCH_TIMEOUT_MS),
  });

  if (!response.ok) {
    const text = await response.text();
    throw new Error(`GraphQL HTTP ${response.status}: ${text}`);
  }

  const body = (await response.json()) as {
    data?: { posts?: unknown };
    errors?: Array<{ message: string; error?: string; error_description?: string }>;
  };

  if (body.errors) {
    throw new Error(`GraphQL error: ${body.errors.map((e) => e.message ?? e.error_description ?? e.error).join('; ')}`);
  }

  return body.data as { posts?: { totalCount: number; pageInfo: { hasNextPage: boolean; endCursor: string | null }; edges: Array<{ node: Record<string, unknown> }> } } ?? {};
}

function normalizePost(raw: Record<string, unknown>): PhPost {
  const thumbnailRaw = raw.thumbnail as Record<string, unknown> | null;
  const makersRaw = raw.makers as Array<Record<string, unknown>> | undefined;
  const topicsRaw = (raw.topics as Record<string, unknown> | undefined)?.edges as Array<Record<string, unknown>> | undefined;
  const mediaRaw = raw.media as Array<Record<string, unknown>> | undefined;

  return {
    id: String(raw.id ?? ''),
    name: String(raw.name ?? ''),
    tagline: String(raw.tagline ?? ''),
    description: (raw.description as string) ?? null,
    url: String(raw.url ?? ''),
    website: String(raw.website ?? ''),
    slug: String(raw.slug ?? ''),
    votesCount: Number(raw.votesCount ?? 0),
    commentsCount: Number(raw.commentsCount ?? 0),
    reviewsCount: Number(raw.reviewsCount ?? 0),
    reviewsRating: Number(raw.reviewsRating ?? 0),
    dailyRank: (raw.dailyRank as number) ?? null,
    featuredAt: (raw.featuredAt as string) ?? null,
    createdAt: String(raw.createdAt ?? ''),
    makers: (makersRaw ?? []).map((m) => ({
      name: String(m.name ?? ''),
      username: String(m.username ?? ''),
    })),
    topics: (topicsRaw ?? []).map((t) => {
      const node = t.node as Record<string, unknown> | undefined;
      return { name: String(node?.name ?? ''), slug: String(node?.slug ?? '') };
    }),
    thumbnail: thumbnailRaw
      ? { type: String(thumbnailRaw.type ?? ''), url: String(thumbnailRaw.url ?? '') }
      : null,
    media: (mediaRaw ?? []).map((m) => ({
      type: String((m as Record<string, unknown>)?.type ?? ''),
      url: String((m as Record<string, unknown>)?.url ?? ''),
      videoUrl: ((m as Record<string, unknown>)?.videoUrl as string) ?? null,
    })),
  };
}

async function fetchPostsForDate(token: string, date: string): Promise<PhPost[]> {
  const postedAfter = `${date}T00:00:00Z`;
  const postedBefore = `${date}T23:59:59Z`;
  const allPosts: PhPost[] = [];
  let cursor: string | null = null;
  let pages = 0;

  while (pages < MAX_PAGES_PER_DAY) {
    const result = await fetchPostsPage(token, cursor, postedAfter, postedBefore);
    const postsData = result.posts;
    if (!postsData?.edges?.length) break;

    for (const edge of postsData.edges) {
      allPosts.push(normalizePost(edge.node));
    }

    if (!postsData.pageInfo?.hasNextPage || !postsData.pageInfo.endCursor) break;
    cursor = postsData.pageInfo.endCursor;
    pages++;
    await new Promise((r) => setTimeout(r, PAGE_DELAY_MS));
  }

  return allPosts;
}

// ── Main ──────────────────────────────────────────────────────────────

async function main(): Promise<void> {
  console.log('\n🦊 Fetching Product Hunt today\'s data via official API v2...');
  const startTime = Date.now();

  // 1. Authenticate
  const token = await getAccessToken();

  // 2. Fetch today's posts only
  ensureDir(PH_CACHE_DIR);
  const today = dateStr();

  console.log(`  📅 ${today}: querying...`);
  const posts = await fetchPostsForDate(token, today);

  // 3. Save day-wise file
  const dayFile = {
    date: today,
    fetchedAt: new Date().toISOString(),
    totalCount: posts.length,
    posts,
  };
  const dayJson = JSON.stringify(dayFile, null, 2) + '\n';
  const changed = writeIfChanged(path.join(PH_CACHE_DIR, `${today}.json`), dayJson);

  if (changed) {
    console.log(`     ${posts.length} posts — ${posts.length > 0 ? 'UPDATED' : 'empty'}`);
  } else {
    console.log(`     ${posts.length} posts — unchanged`);
  }

  // 4. Update index.json
  const allDates = fs
    .readdirSync(PH_CACHE_DIR)
    .filter((f) => /^\d{4}-\d{2}-\d{2}\.json$/.test(f))
    .map((f) => f.replace('.json', ''))
    .sort();

  const firstDate = allDates.length > 0 ? allDates[0] : today;
  const lastDate = allDates.length > 0 ? allDates[allDates.length - 1] : today;

  const index: PhIndex = {
    type: 'producthunt',
    fetchedAt: new Date().toISOString(),
    lastFetchedDate: lastDate,
    firstFetchedDate: firstDate,
    totalDaysFetched: allDates.length,
    totalProducts: allDates.length > 0
      ? posts.length // approximate — products.json has the full count
      : posts.length,
    availableDates: allDates,
  };
  writeIfChanged(path.join(PH_CACHE_DIR, 'index.json'), JSON.stringify(index, null, 2) + '\n');

  // 5. Summary
  const elapsed = ((Date.now() - startTime) / 1000).toFixed(1);
  console.log(`\n   Done in ${elapsed}s`);
  console.log(`   Today's posts: ${posts.length}`);
  if (posts.length > 0) {
    console.log(`   Top: ${posts[0].name} (${posts[0].votesCount} votes)`);
  }
  console.log(`   Archive: ${allDates.length} days indexed`);
  console.log('✅ Product Hunt today\'s data cached\n');
}

main().catch((err) => {
  console.error('💥 Fatal error:', err);
  process.exit(1);
});
