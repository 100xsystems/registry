#!/usr/bin/env tsx
/**
 * fetch-ph-data.ts — PRODUCT HUNT API v2
 *
 * Fetches Product Hunt products using the official GraphQL API v2.
 * Stores results in day-wise JSON files: producthunt/YYYY-MM-DD.json
 * Maintains a merged catalog: producthunt/products.json
 *
 * SPEED: Completes in ~1-3s for 2 days of data (~20-50 posts per day)
 *
 * USAGE:
 *   PH_API_KEY=xxx PH_API_SECRET=xxx tsx scripts/fetch-ph-data.ts
 *   PH_DEV_TOKEN=xxx tsx scripts/fetch-ph-data.ts
 *
 * ENV VARS:
 *   PH_DEV_TOKEN    — Developer token (simplest, never expires)
 *   PH_API_KEY      — API key (for OAuth2 client credentials)
 *   PH_API_SECRET   — API secret (for OAuth2 client credentials)
 */

import * as fs from 'node:fs';
import * as path from 'node:path';

// ── Config ────────────────────────────────────────────────────────────

const TOKEN_URL = 'https://api.producthunt.com/v2/oauth/token';
const GRAPHQL_URL = 'https://api.producthunt.com/v2/api/graphql';
const PH_CACHE_DIR = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..', 'producthunt');
const FETCH_TIMEOUT_MS = 15_000;
const MAX_PAGES_PER_DAY = 5;       // 50 posts/page × 5 = 250 max per day (typical is 20-50)
const DAILY_FETCH_WINDOW = 1;      // Always fetch today + yesterday (catches late-featured posts)
const PAGE_DELAY_MS = 200;         // 200ms between pages to avoid rate limit bursts

// GraphQL query to fetch posts — optimized for minimal complexity cost
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

interface DayFile {
  date: string;
  fetchedAt: string;
  totalCount: number;
  posts: PhPost[];
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
  // 1. Try Developer Token first (simplest)
  const devToken = process.env.PH_DEV_TOKEN;
  if (devToken) {
    console.log('  Using PH_DEV_TOKEN');
    return devToken;
  }

  // 2. Try OAuth2 Client Credentials
  const apiKey = process.env.PH_API_KEY;
  const apiSecret = process.env.PH_API_SECRET;
  if (apiKey && apiSecret) {
    console.log('  Getting access token via OAuth2...');
    try {
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
    } catch (err) {
      throw new Error(`OAuth2 failed: ${err instanceof Error ? err.message : String(err)}`);
    }
  }

  throw new Error(
    'No PH API credentials found. Set PH_DEV_TOKEN or PH_API_KEY + PH_API_SECRET env vars.',
  );
}

// ── GraphQL Query ───────────────────────────────────────────────────

interface PostsQueryResult {
  posts?: {
    totalCount: number;
    pageInfo: { hasNextPage: boolean; endCursor: string | null };
    edges: Array<{
      node: Record<string, unknown>;
    }>;
  };
}

async function fetchPostsPage(
  token: string,
  after: string | null,
  postedAfter: string,
  postedBefore: string,
): Promise<PostsQueryResult> {
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
    data?: PostsQueryResult;
    errors?: Array<{ message: string; error?: string; error_description?: string }>;
  };

  if (body.errors) {
    throw new Error(`GraphQL error: ${body.errors.map((e) => e.message ?? e.error_description ?? e.error).join('; ')}`);
  }

  return body.data ?? { posts: undefined };
}

// ── Normalize a raw post node into our PhPost format ────────────────

function normalizePost(raw: Record<string, unknown>): PhPost {
  const thumbnailRaw = raw.thumbnail as Record<string, unknown> | null;
  const makersRaw = raw.makers as Array<Record<string, unknown>> | undefined;
  const topicsRaw = (raw.topics as Record<string, unknown> | undefined)?.edges as
    | Array<Record<string, unknown>>
    | undefined;
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

// ── Fetch all posts for a given date ─────────────────────────────────

async function fetchPostsForDate(
  token: string,
  date: string,
): Promise<PhPost[]> {
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

    // Small delay between pages to avoid rate limit bursts
    await new Promise((r) => setTimeout(r, PAGE_DELAY_MS));
  }

  return allPosts;
}

// ── Merge day-wise files into products.json catalog ──────────────────

function mergeIntoCatalog(dates: string[], existingProducts: Record<string, PhPost>): PhPost[] {
  const allProducts = { ...existingProducts };

  for (const date of dates) {
    const filePath = path.join(PH_CACHE_DIR, `${date}.json`);
    try {
      const dayData = JSON.parse(fs.readFileSync(filePath, 'utf-8')) as DayFile;
      for (const post of dayData.posts) {
        allProducts[post.id] = post; // Dedup by ID, latest wins
      }
    } catch {}
  }

  return Object.values(allProducts).sort(
    (a, b) => new Date(b.featuredAt ?? b.createdAt).getTime() - new Date(a.featuredAt ?? a.createdAt).getTime(),
  );
}

// ── Main ──────────────────────────────────────────────────────────────

async function main(): Promise<void> {
  console.log('\n🦊 Fetching Product Hunt data via official API v2...');
  const startTime = Date.now();

  // 1. Authenticate
  const token = await getAccessToken();

  // 2. Determine which dates to fetch: always today + yesterday
  ensureDir(PH_CACHE_DIR);
  const today = new Date();
  const datesToFetch: string[] = [];

  for (let i = DAILY_FETCH_WINDOW; i >= 0; i--) {
    const d = new Date(today);
    d.setDate(d.getDate() - i);
    datesToFetch.push(dateStr(d));
  }

  console.log(`  Fetching ${datesToFetch.length} days of data...`);

  // 3. Fetch posts for each day
  let totalNewPosts = 0;
  let totalUpdated = 0;
  const fetchedDates: string[] = [];

  for (const date of datesToFetch) {
    const filePath = path.join(PH_CACHE_DIR, `${date}.json`);

    console.log(`  📅 ${date}: querying...`);
    const posts = await fetchPostsForDate(token, date);

    const dayFile: DayFile = {
      date,
      fetchedAt: new Date().toISOString(),
      totalCount: posts.length,
      posts,
    };

    const dayJson = JSON.stringify(dayFile, null, 2) + '\n';

    // Check if this day's data changed
    const existing = readExisting(filePath);
    if (existing === dayJson) {
      console.log(`     ${posts.length} posts — unchanged`);
      fetchedDates.push(date);
      continue;
    }

    fs.writeFileSync(filePath, dayJson, 'utf-8');
    totalNewPosts += posts.length;
    if (existing) {
      totalUpdated++;
      console.log(`     ${posts.length} posts — UPDATED`);
    } else {
      totalUpdated++;
      console.log(`     ${posts.length} posts — NEW`);
    }
    fetchedDates.push(date);
  }

  // 4. Rebuild the merged products.json catalog
  console.log(`  Merging catalog...`);
  let existingProducts: Record<string, PhPost> = {};
  const mergedFile = path.join(PH_CACHE_DIR, 'products.json');
  try {
    const existingData = JSON.parse(fs.readFileSync(mergedFile, 'utf-8')) as {
      products: PhPost[];
    };
    for (const p of existingData.products) {
      existingProducts[p.id] = p;
    }
  } catch {}

  const allProducts = mergeIntoCatalog(fetchedDates, existingProducts);

  const mergedJson = JSON.stringify(
    { fetchedAt: new Date().toISOString(), count: allProducts.length, products: allProducts },
    null,
    2,
  );
  writeIfChanged(mergedFile, mergedJson + '\n');

  // 5. Write index
  const allDates = fs
    .readdirSync(PH_CACHE_DIR)
    .filter((f) => /^\d{4}-\d{2}-\d{2}\.json$/.test(f))
    .map((f) => f.replace('.json', ''))
    .sort();

  const firstDate = allDates.length > 0 ? allDates[0] : dateStr();
  const lastDate = allDates.length > 0 ? allDates[allDates.length - 1] : dateStr();

  // Read total unique products from merged file
  let totalProducts = 0;
  try {
    const mergedData = JSON.parse(fs.readFileSync(mergedFile, 'utf-8')) as {
      count: number;
    };
    totalProducts = mergedData.count;
  } catch {}

  const index: PhIndex = {
    type: 'producthunt',
    fetchedAt: new Date().toISOString(),
    lastFetchedDate: lastDate,
    firstFetchedDate: firstDate,
    totalDaysFetched: allDates.length,
    totalProducts,
    availableDates: allDates,
  };
  writeIfChanged(path.join(PH_CACHE_DIR, 'index.json'), JSON.stringify(index, null, 2) + '\n');

  // 6. Summary
  const elapsed = ((Date.now() - startTime) / 1000).toFixed(1);
  console.log(`\n   Done in ${elapsed}s`);
  console.log(`   Days fetched: ${fetchedDates.length}`);
  console.log(`   New/updated posts: ${totalNewPosts}`);
  console.log(`   Catalog: ${totalProducts} products across ${allDates.length} days`);
  console.log('✅ Product Hunt data cached to producthunt/\n');
}

main().catch((err) => {
  console.error('💥 Fatal error:', err);
  process.exit(1);
});
