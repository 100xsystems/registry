/**
 * FEED_REGISTRY for the registry repo.
 *
 * Mirrors the website's `src/feed/feed.constants.ts` so the registry scripts
 * know which RSS feeds to fetch. The FEED_REGISTRY in the website repo is
 * the canonical source of truth — update both when adding/removing feeds.
 */
export interface HistoricalImport {
  /** Strategy for fetching ALL historical articles (beyond RSS's 10-50 limit) */
  strategy: 'sitemap' | 'archive-crawl' | 'rss-all' | 'none';
  /** URL of the sitemap (for 'sitemap' strategy) */
  sitemapUrl?: string;
  /** URL of the archive page (for 'archive-crawl' strategy) */
  archiveUrl?: string;
  /** Pagination pattern like '/page/{page}' (for 'archive-crawl' strategy) */
  paginationPattern?: string;
}

export interface FeedSource {
  id: string;
  name: string;
  rssUrl: string;
  siteUrl: string;
  tags: string[];
  /** Strategy for historical import of all articles (beyond RSS's 10-50 limit) */
  historicalImport?: HistoricalImport;
}

export const FEED_REGISTRY: FeedSource[] = [
  {
    id: 'netflix-tech-blog',
    name: 'Netflix Tech Blog',
    rssUrl: 'https://netflixtechblog.com/feed',
    siteUrl: 'https://netflixtechblog.com',
    tags: ['distributed-systems', 'infrastructure', 'streaming'],
    historicalImport: { strategy: 'none' }, // Medium-hosted, no sitemap
  },
  {
    id: 'stripe-engineering',
    name: 'Stripe Engineering',
    rssUrl: 'https://stripe.com/blog/feed.rss',
    siteUrl: 'https://stripe.com/blog',
    tags: ['payments', 'architecture', 'api-design'],
    historicalImport: { strategy: 'none' }, // No sitemap found
  },
  {
    id: 'cloudflare-blog',
    name: 'Cloudflare Blog',
    rssUrl: 'https://blog.cloudflare.com/rss',
    siteUrl: 'https://blog.cloudflare.com',
    tags: ['networking', 'security', 'performance', 'edge-computing'],
    historicalImport: { strategy: 'sitemap', sitemapUrl: 'https://blog.cloudflare.com/sitemap-posts.xml' },
  },
  {
    id: 'discord-engineering',
    name: 'Discord Engineering',
    rssUrl: 'https://discord.com/blog/rss.xml',
    siteUrl: 'https://discord.com/category/engineering',
    tags: ['backend', 'infrastructure', 'real-time'],
    historicalImport: { strategy: 'none' }, // No sitemap found
  },
  {
    id: 'uber-engineering',
    name: 'Uber Engineering',
    rssUrl: 'https://www.uber.com/en-IN/blog/engineering/feed',
    siteUrl: 'https://www.uber.com/blog/engineering',
    tags: ['distributed-systems', 'infrastructure', 'mobile'],
    historicalImport: { strategy: 'none' }, // Sitemap covers entire Uber site, not just engineering blog
  },
  {
    id: 'meta-engineering',
    name: 'Engineering at Meta',
    rssUrl: 'https://engineering.fb.com/feed',
    siteUrl: 'https://engineering.fb.com',
    tags: ['infrastructure', 'ai', 'performance', 'distributed-systems'],
    historicalImport: { strategy: 'sitemap', sitemapUrl: 'https://engineering.fb.com/sitemap.xml' },
  },
  {
    id: 'martin-fowler',
    name: 'Martin Fowler',
    rssUrl: 'https://martinfowler.com/feed.atom',
    siteUrl: 'https://martinfowler.com',
    tags: ['architecture', 'patterns', 'refactoring', 'design'],
    historicalImport: { strategy: 'none' }, // No sitemap found
  },
  {
    id: 'aws-architecture',
    name: 'AWS Architecture Blog',
    rssUrl: 'https://aws.amazon.com/blogs/architecture/feed',
    siteUrl: 'https://aws.amazon.com/blogs/architecture',
    tags: ['cloud', 'architecture', 'aws'],
    historicalImport: { strategy: 'none' }, // No sitemap found
  },
  {
    id: 'grafana-labs',
    name: 'Grafana Labs',
    rssUrl: 'https://grafana.com/blog/index.xml',
    siteUrl: 'https://grafana.com/blog',
    tags: ['observability', 'monitoring', 'data-visualization'],
    historicalImport: { strategy: 'sitemap', sitemapUrl: 'https://grafana.com/sitemap.xml' },
  },
  {
    id: 'slack-engineering',
    name: 'Slack Engineering',
    rssUrl: 'https://slack.engineering/feed',
    siteUrl: 'https://slack.engineering',
    tags: ['backend', 'infrastructure', 'real-time'],
    historicalImport: { strategy: 'none' }, // No sitemap found (301)
  },
  {
    id: 'figma-engineering',
    name: 'Figma Engineering',
    rssUrl: 'https://www.figma.com/blog/feed',
    siteUrl: 'https://www.figma.com/blog',
    tags: ['frontend', 'systems', 'webassembly', 'collaboration'],
    historicalImport: { strategy: 'sitemap', sitemapUrl: 'https://www.figma.com/sitemap.xml' },
  },
  {
    id: 'tailscale-blog',
    name: 'Tailscale Blog',
    rssUrl: 'https://tailscale.com/blog/index.xml',
    siteUrl: 'https://tailscale.com/blog',
    tags: ['networking', 'security', 'vpn', 'wireguard'],
    historicalImport: { strategy: 'sitemap', sitemapUrl: 'https://tailscale.com/sitemap.xml' },
  },
  {
    id: 'cockroachdb',
    name: 'CockroachDB',
    rssUrl: 'https://www.cockroachlabs.com/blog/index.xml',
    siteUrl: 'https://www.cockroachlabs.com/blog',
    tags: ['databases', 'distributed-systems', 'sql'],
    historicalImport: { strategy: 'sitemap', sitemapUrl: 'https://www.cockroachlabs.com/sitemap.xml' },
  },
  {
    id: 'apple-ml-research',
    name: 'Apple Machine Learning Research',
    rssUrl: 'https://machinelearning.apple.com/rss.xml',
    siteUrl: 'https://machinelearning.apple.com',
    tags: ['machine-learning', 'ai', 'research'],
    historicalImport: { strategy: 'none' }, // No sitemap found
  },
  {
    id: 'svelte-blog',
    name: 'Svelte Blog',
    rssUrl: 'https://svelte.dev/blog/rss.xml',
    siteUrl: 'https://svelte.dev/blog',
    tags: ['frontend', 'javascript', 'compiler'],
    historicalImport: { strategy: 'none' }, // No sitemap found
  },
  {
    id: 'vercel-blog',
    name: 'Vercel Blog',
    rssUrl: 'https://vercel.com/blog/rss.xml',
    siteUrl: 'https://vercel.com/blog',
    tags: ['frontend', 'infrastructure', 'edge-computing', 'nextjs'],
    historicalImport: { strategy: 'none' }, // No sitemap found (301)
  },
  {
    id: 'github-engineering',
    name: 'GitHub Engineering',
    rssUrl: 'https://github.blog/engineering/feed',
    siteUrl: 'https://github.blog/engineering',
    tags: ['infrastructure', 'developer-tools', 'platform'],
    historicalImport: { strategy: 'none' }, // No sitemap found (301)
  },
  {
    id: 'datadog-engineering',
    name: 'Datadog Engineering',
    rssUrl: 'https://www.datadoghq.com/feed',
    siteUrl: 'https://www.datadoghq.com/blog/engineering',
    tags: ['observability', 'monitoring', 'infrastructure'],
    historicalImport: { strategy: 'sitemap', sitemapUrl: 'https://www.datadoghq.com/sitemap.xml' },
  },
  {
    id: 'clickhouse',
    name: 'ClickHouse Blog',
    rssUrl: 'https://clickhouse.com/blog/rss',
    siteUrl: 'https://clickhouse.com/blog',
    tags: ['databases', 'analytics', 'performance'],
    historicalImport: { strategy: 'sitemap', sitemapUrl: 'https://clickhouse.com/sitemap.xml' },
  },
  {
    id: 'pinecone-engineering',
    name: 'Pinecone Engineering',
    rssUrl: 'https://www.pinecone.io/rss',
    siteUrl: 'https://www.pinecone.io/blog',
    tags: ['ai', 'vector-databases', 'infrastructure'],
    historicalImport: { strategy: 'sitemap', sitemapUrl: 'https://www.pinecone.io/sitemap.xml' },
  },
  {
    id: 'cloudflare-workers',
    name: 'Cloudflare Workers Blog',
    rssUrl: 'https://blog.cloudflare.com/tag/workers/rss',
    siteUrl: 'https://blog.cloudflare.com/tag/workers',
    tags: ['serverless', 'edge-computing', 'javascript'],
    historicalImport: { strategy: 'sitemap', sitemapUrl: 'https://blog.cloudflare.com/sitemap-posts.xml' }, // Same sitemap as parent
  },
  {
    id: 'postgresql',
    name: 'PostgreSQL Blog',
    rssUrl: 'https://planet.postgresql.org/rss20.xml',
    siteUrl: 'https://www.postgresql.org/blog',
    tags: ['databases', 'sql', 'open-source'],
    historicalImport: { strategy: 'rss-all' }, // Planet PG RSS aggregates many sources
  },
  {
    id: 'redis-blog',
    name: 'Redis Engineering',
    rssUrl: 'https://redis.io/blog/feed',
    siteUrl: 'https://redis.io/blog',
    tags: ['databases', 'caching', 'performance'],
    historicalImport: { strategy: 'none' }, // No sitemap found
  },
  {
    id: 'nasa-software',
    name: 'NASA Software Engineering',
    rssUrl: 'https://www.nasa.gov/feeds/technology',
    siteUrl: 'https://www.nasa.gov/technology',
    tags: ['software-engineering', 'research', 'systems'],
    historicalImport: { strategy: 'none' },
  },
  {
    id: 'traefik',
    name: 'Traefik Labs',
    rssUrl: 'https://traefik.io/blog/rss',
    siteUrl: 'https://traefik.io/blog',
    tags: ['networking', 'cloud-native', 'infrastructure'],
    historicalImport: { strategy: 'none' },
  },
  {
    id: 'istio',
    name: 'Istio Blog',
    rssUrl: 'https://istio.io/latest/blog/feed.xml',
    siteUrl: 'https://istio.io/latest/blog',
    tags: ['networking', 'cloud-native', 'service-mesh'],
    historicalImport: { strategy: 'none' },
  },
  {
    id: 'deno-blog',
    name: 'Deno Blog',
    rssUrl: 'https://deno.com/blog/feed.xml',
    siteUrl: 'https://deno.com/blog',
    tags: ['javascript', 'runtime', 'security'],
    historicalImport: { strategy: 'none' },
  },
  {
    id: 'bun-blog',
    name: 'Bun Blog',
    rssUrl: 'https://bun.sh/blog/rss.xml',
    siteUrl: 'https://bun.sh/blog',
    tags: ['javascript', 'performance', 'runtime'],
    historicalImport: { strategy: 'none' },
  },
  {
    id: 'rust-blog',
    name: 'Rust Blog',
    rssUrl: 'https://blog.rust-lang.org/feed.xml',
    siteUrl: 'https://blog.rust-lang.org',
    tags: ['systems-programming', 'compiler', 'performance'],
    historicalImport: { strategy: 'sitemap', sitemapUrl: 'https://blog.rust-lang.org/sitemap.xml' },
  },
  {
    id: 'airbnb-engineering',
    name: 'Airbnb Engineering',
    rssUrl: 'https://medium.com/feed/airbnb-engineering',
    siteUrl: 'https://medium.com/airbnb-engineering',
    tags: ['infrastructure', 'platform', 'mobile'],
    historicalImport: { strategy: 'none' }, // Medium-hosted
  },
  {
    id: 'dropbox-engineering',
    name: 'Dropbox Engineering',
    rssUrl: 'https://dropbox.tech/feed',
    siteUrl: 'https://dropbox.tech',
    tags: ['distributed-systems', 'storage', 'infrastructure'],
    historicalImport: { strategy: 'sitemap', sitemapUrl: 'https://dropbox.tech/sitemap.xml' },
  },
  {
    id: 'spotify-engineering',
    name: 'Spotify Engineering',
    rssUrl: 'https://engineering.atspotify.com/feed/',
    siteUrl: 'https://engineering.atspotify.com',
    tags: ['backend', 'infrastructure', 'platform'],
    historicalImport: { strategy: 'none' }, // No sitemap found
  },
  {
    id: 'linkedin-engineering',
    name: 'LinkedIn Engineering',
    rssUrl: 'https://www.linkedin.com/blog/engineering/feed',
    siteUrl: 'https://engineering.linkedin.com/blog',
    tags: ['infrastructure', 'ai', 'distributed-systems'],
    historicalImport: { strategy: 'none' },
  },
  {
    id: 'hashicorp',
    name: 'HashiCorp Blog',
    rssUrl: 'https://www.hashicorp.com/blog/feed.xml',
    siteUrl: 'https://www.hashicorp.com/blog',
    tags: ['cloud-native', 'infrastructure', 'devops'],
    historicalImport: { strategy: 'sitemap', sitemapUrl: 'https://www.hashicorp.com/sitemap.xml' },
  },
  {
    id: 'mongodb',
    name: 'MongoDB Blog',
    rssUrl: 'https://www.mongodb.com/blog/rss',
    siteUrl: 'https://www.mongodb.com/blog',
    tags: ['databases', 'performance', 'cloud'],
    historicalImport: { strategy: 'none' },
  },
  {
    id: 'elastic',
    name: 'Elastic Blog',
    rssUrl: 'https://www.elastic.co/blog/feed',
    siteUrl: 'https://www.elastic.co/blog',
    tags: ['search', 'observability', 'security'],
    historicalImport: { strategy: 'none' },
  },
  {
    id: 'julia-evans',
    name: 'Julia Evans',
    rssUrl: 'https://jvns.ca/atom.xml',
    siteUrl: 'https://jvns.ca',
    tags: ['systems-programming', 'networking', 'debugging'],
    historicalImport: { strategy: 'sitemap', sitemapUrl: 'https://jvns.ca/sitemap.xml' },
  },
  {
    id: 'dan-luu',
    name: 'Dan Luu',
    rssUrl: 'https://danluu.com/atom.xml',
    siteUrl: 'https://danluu.com',
    tags: ['systems-programming', 'performance', 'software-engineering'],
    historicalImport: { strategy: 'sitemap', sitemapUrl: 'https://danluu.com/sitemap.xml' },
  },
  {
    id: 'sentry',
    name: 'Sentry Blog',
    rssUrl: 'https://blog.sentry.io/feed.xml',
    siteUrl: 'https://blog.sentry.io',
    tags: ['observability', 'debugging', 'performance'],
    historicalImport: { strategy: 'none' }, // No sitemap found
  },
  {
    id: 'posthog',
    name: 'PostHog Blog',
    rssUrl: 'https://posthog.com/blog/rss.xml',
    siteUrl: 'https://posthog.com/blog',
    tags: ['startups', 'open-source', 'product-engineering'],
    historicalImport: { strategy: 'none' }, // No sitemap found
  },
  {
    id: 'sourcegraph',
    name: 'Sourcegraph Blog',
    rssUrl: 'https://about.sourcegraph.com/blog/rss.xml',
    siteUrl: 'https://about.sourcegraph.com/blog',
    tags: ['developer-tools', 'code-search', 'platform'],
    historicalImport: { strategy: 'none' },
  },
  {
    id: 'stack-overflow',
    name: 'Stack Overflow Blog',
    rssUrl: 'https://stackoverflow.blog/feed',
    siteUrl: 'https://stackoverflow.blog',
    tags: ['developer-tools', 'community', 'platform'],
    historicalImport: { strategy: 'sitemap', sitemapUrl: 'https://stackoverflow.blog/sitemap.xml' },
  },
  {
    id: 'jetbrains',
    name: 'JetBrains Blog',
    rssUrl: 'https://blog.jetbrains.com/feed',
    siteUrl: 'https://blog.jetbrains.com',
    tags: ['developer-tools', 'ide', 'programming-languages'],
    historicalImport: { strategy: 'none' }, // No sitemap found (301)
  },
  {
    id: 'docker',
    name: 'Docker Blog',
    rssUrl: 'https://www.docker.com/blog/feed/',
    siteUrl: 'https://www.docker.com/blog',
    tags: ['containers', 'devops', 'cloud-native'],
    historicalImport: { strategy: 'none' }, // No sitemap found (301)
  },
  {
    id: 'digitalocean',
    name: 'DigitalOcean Blog',
    rssUrl: 'https://www.digitalocean.com/blog/feed',
    siteUrl: 'https://www.digitalocean.com/blog',
    tags: ['cloud', 'infrastructure', 'devops'],
    historicalImport: { strategy: 'none' },
  },
  {
    id: 'confluent',
    name: 'Confluent Blog',
    rssUrl: 'https://www.confluent.io/feed',
    siteUrl: 'https://www.confluent.io/blog',
    tags: ['distributed-systems', 'streaming', 'kafka'],
    historicalImport: { strategy: 'sitemap', sitemapUrl: 'https://www.confluent.io/sitemap.xml' },
  },
  {
    id: 'databricks',
    name: 'Databricks Blog',
    rssUrl: 'https://www.databricks.com/feed',
    siteUrl: 'https://www.databricks.com/blog',
    tags: ['ai', 'data-platform', 'spark'],
    historicalImport: { strategy: 'none' }, // No sitemap found (301)
  },
  {
    id: 'nginx',
    name: 'NGINX Blog',
    rssUrl: 'https://www.nginx.com/blog/feed/',
    siteUrl: 'https://www.nginx.com/blog',
    tags: ['networking', 'web-server', 'performance'],
    historicalImport: { strategy: 'none' }, // No sitemap found (301)
  },
  {
    id: 'redhat',
    name: 'Red Hat Blog',
    rssUrl: 'https://www.redhat.com/rss/blog',
    siteUrl: 'https://www.redhat.com/en/blog',
    tags: ['open-source', 'linux', 'cloud-native'],
    historicalImport: { strategy: 'sitemap', sitemapUrl: 'https://www.redhat.com/sitemap.xml' },
  },
];
