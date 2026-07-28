# Product Hunt API — Architecture Design

## Authentication
- **OAuth2 Client Credentials** using API Key + Secret
- Token endpoint: `POST https://api.producthunt.com/v2/oauth/token`
- Token is cached and reused (doesn't expire per session)
- Falls back to `DEVELOPER_TOKEN` env var if provided

## API Details
- **Endpoint**: `https://api.producthunt.com/v2/api/graphql`
- **Auth**: `Authorization: Bearer {access_token}`
- **Rate Limit**: 6,250 complexity points per 15 min
- **Pagination**: Cursor-based (`first: 50`, `after: cursor`)

## Data Storage

### Day-Wise Files: `producthunt/YYYY-MM-DD.json`
```json
{
  "date": "2026-07-28",
  "fetchedAt": "2026-07-28T08:30:00Z",
  "totalCount": 35,
  "posts": [
    {
      "id": "12345",
      "name": "Product Name",
      "tagline": "Short tagline",
      "description": "Full description...",
      "url": "https://www.producthunt.com/posts/...",
      "website": "https://example.com",
      "slug": "product-name",
      "votesCount": 150,
      "commentsCount": 25,
      "reviewsCount": 10,
      "reviewsRating": 4.5,
      "dailyRank": 1,
      "featuredAt": "2026-07-28T08:00:00Z",
      "createdAt": "2026-07-28T07:00:00Z",
      "makers": [
        { "name": "Maker Name", "username": "maker" }
      ],
      "topics": [
        { "name": "Productivity", "slug": "productivity" }
      ],
      "thumbnail": { "type": "image", "url": "..." },
      "media": [
        { "type": "image", "url": "..." }
      ]
    }
  ]
}
```

### Merged Catalog: `producthunt/products.json`
- Appended from all day-wise files
- Deduplicated by post ID
- Sorted by featuredAt DESC
- Used by the website for search/catalog

### Index: `producthunt/index.json`
```json
{
  "type": "producthunt",
  "fetchedAt": "2026-07-28T08:30:00Z",
  "lastFetchedDate": "2026-07-28",
  "firstFetchedDate": "2026-07-01",
  "totalDaysFetched": 28,
  "totalProducts": 980,
  "availableDates": ["2026-07-01", "2026-07-02", ...]
}
```

## Fetch Strategy
1. Each run fetches **last 2 days** (yesterday + today) to catch late-featured posts
2. **30-day backfill** on first run (fetches last 30 days)
3. Pagination: up to 50 posts per page, cursor-based
4. Complexity budget: ~50-100 points per page = 60+ pages per 15 min window
5. Change detection: day file only written if content changed

## Workflow Integration
- Runs after feed update in `daily-feed-update.yml`
- `continue-on-error: true` (non-critical)
- Env vars: `PH_API_KEY`, `PH_API_SECRET`, `PH_DEV_TOKEN`
