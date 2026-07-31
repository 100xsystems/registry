#!/usr/bin/env python3
"""Deep curriculum data batch 5: lru-cache, lsm-tree, mapreduce, mediator, memento, multi-leader."""

TOPICS = {}


def _t(slug, topics):
    TOPICS[slug] = topics
    return topics


# ─────────────────────────────────────────────────────────────────────────────
# LRU CACHE
# ─────────────────────────────────────────────────────────────────────────────
_t('lru-cache', [
    {
        'title': 'LRU Cache: Evict What You Use Least Recently',
        'desc': 'A bounded cache that drops the least-recently-used entry when it runs out of room.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain the LRU eviction policy',
            'Implement O(1) get and put',
            'Understand why hash + list',
            'Know when LRU fits',
        ],
        'prereqs': ['principles/caching', 'patterns/flyweight'],
        'sections': [
            {'heading': 'The Policy', 'paras': [
                'An LRU cache has a capacity. Every get or put marks its key most-recently-used; when the cache is full, the least-recently-used entry is evicted. The assumption: if you have not used it recently, you probably will not use it soon — temporal locality.',
            ], 'code': {'lang': 'python', 'body': '''
# LRU: dict (O(1) lookup) + doubly linked list (O(1) reorder/evict)
class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}          # key -> [value, prev, next]
        self.head = self.tail = None     # most-recent .. least-recent

    def _remove(self, key):
        _, p, n = self.cache[key]
        if p is not None: self.cache[p][2] = n
        else: self.head = n
        if n is not None: self.cache[n][1] = p
        else: self.tail = p

    def _push_front(self, key):
        self.cache[key][1] = None
        self.cache[key][2] = self.head
        if self.head is not None: self.cache[self.head][1] = key
        self.head = key
        if self.tail is None: self.tail = key

    def get(self, key):
        if key not in self.cache: return -1
        self._remove(key); self._push_front(key)
        return self.cache[key][0]

    def put(self, key, value):
        if key in self.cache:
            self.cache[key][0] = value
            self._remove(key); self._push_front(key); return
        if len(self.cache) >= self.cap:
            del self.cache[self.tail]      # evict least-recent
            if self.tail is not None:      # fix tail pointer
                self._remove(self.tail)
        self.cache[key] = [value, None, None]
        self._push_front(key)'''}},
            {'heading': 'Why LRU Wins', 'paras': [
                'LRU adapts to the workload: hot keys stay hot by being touched. FIFO evicts regardless of use; random is unpredictable; LFU tracks frequency but can keep a once-hot key forever. LRU needs one touch per access — O(1) with the right structures — and is the default for most page caches.',
            ]},
        ],
        'practice': {
            'title': 'Build and Test the LRU',
            'intro': 'A cache of 3 entries receives a workload that repeats some keys and scans others.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Implement the O(1) LRU with the hash + list structure.'},
                {'label': 'Task 2', 'text': 'Trace a workload: put a,b,c then get a then put d — what is evicted?'},
                {'label': 'Task 3', 'text': 'Compare hit rates: LRU vs FIFO vs random on the same workload.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why LRU needs both a hash and a list. Start with the O(1) requirements.'},
            {'label': 'Compare & Contrast', 'text': 'Compare LRU with LFU and with TTL-based expiry. When does a once-hot key poison LFU?'},
            {'label': 'Boundary Testing', 'text': 'The workload is a full sequential scan — LRU thrashes. Design the scan-resistant variant (like CLOCK or ARC).'},
        ],
        'takeaways': [
            'LRU evicts the least-recently-used entry',
            'Hash + doubly linked list gives O(1) operations',
            'LRU assumes temporal locality',
            'Scan workloads need resistant variants',
        ],
        'further': [
            {'title': 'Cache replacement policies — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Cache_replacement_policies'},
            {'title': 'Redis — eviction policies', 'url': 'https://redis.io/docs/reference/eviction/'},
        ],
    },
    {
        'title': 'LRU in Production: Page Caches and Memcached',
        'desc': 'Real LRUs in OS page caches, Redis, and CDNs — and their eviction knobs.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Configure eviction policies in Redis',
            'Understand OS page cache LRU approximation',
            'Design CDN edge caching',
            'Monitor hit and eviction rates',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Redis Eviction', 'paras': [
                'Redis maxmemory policies are LRU families: allkeys-lru evicts any key, volatile-lru only keys with TTL, and LFU variants exist for frequency-shaped workloads. The choice shapes the cache: allkeys-lru protects hot keys globally; volatile-lru lets you pin the important ones by omitting TTL.',
            ], 'code': {'lang': 'config', 'body': '''
# Redis eviction configuration
maxmemory 512mb
maxmemory-policy allkeys-lru   # evict least-recently-used key
# Alternatives:
#   volatile-lru   only evict keys WITH a TTL (others are pinned)
#   allkeys-lfu    evict least-frequently-used (hot keys stay hot)
#   noeviction     return errors instead of evicting (for queues)'''}},
            {'heading': 'Approximation at Scale', 'paras': [
                'The OS page cache and huge caches cannot maintain a perfect LRU list — they approximate with CLOCK-style bit scans (Linux uses an aging approximation of LRU). CDNs combine LRU with popularity tiers: hot objects pinned, warm objects in LRU, cold objects evicted fast.',
            ]},
        ],
        'practice': {
            'title': 'Tune the Cache',
            'intro': 'A Redis cache serves 90% of reads; the workload has a 5% long tail of one-hit wonders.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Choose the policy: allkeys-lru vs allkeys-lfu, and justify with the workload.'},
                {'label': 'Task 2', 'text': 'Set the maxmemory budget as a fraction of dataset and traffic.'},
                {'label': 'Task 3', 'text': 'Design the monitoring: hit rate, eviction rate, and the alert when evictions spike.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why real systems approximate LRU at scale. Ask me what breaks with a perfect LRU on millions of keys.'},
            {'label': 'Implementation Design', 'text': 'Design a CDN cache: object size classes, pinning rules, and the LRU tier per class. How does a viral video behave?'},
            {'label': 'Boundary Testing', 'text': 'Evictions suddenly spike after a deploy. Design the diagnosis: what metrics and what fix?'},
        ],
        'takeaways': [
            'Redis offers LRU and LFU policy families',
            'Perfect LRU is approximated at scale (CLOCK aging)',
            'TTL pinning lets you protect important keys',
            'Eviction rate is an operational alarm',
        ],
        'further': [
            {'title': 'Redis — eviction policy docs', 'url': 'https://redis.io/docs/reference/eviction/'},
            {'title': 'Linux page cache — LWN', 'url': 'https://lwn.net/Articles/380931/'},
        ],
    },
    {
        'title': 'Advanced LRU: Segmented and Adaptive Caches',
        'desc': 'Segmented LRU, ARC, and cache-aware system design.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Design a two-tier LRU',
            'Explain ARC adaptation',
            'Handle cache poisoning',
            'Co-design caches and data flow',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Segmented LRU', 'paras': [
                'Two-tier LRU splits the cache: a small probationary segment for new entries and a protected segment for entries that survive. On a hit in probation, the entry promotes. This resists scan poisoning — a one-time sweep cannot evict the protected hot set, because scans only churn probation.',
            ], 'code': {'lang': 'python', 'body': '''
# Two-tier LRU: probation + protected segments
class SegLRU:
    def __init__(self, capacity):
        self.protected = LRUCache(int(capacity * 0.8))
        self.probation = LRUCache(capacity - int(capacity * 0.8))

    def get(self, key):
        if key in self.protected.cache:
            return self.protected.get(key)
        if key in self.probation.cache:
            self.probation.remove(key)
            self.protected.put(key, value)     # promote on second hit
        return None

# A full sequential scan only fills probation; the protected set
# survives untouched. Cold churn never reaches the hot segment.'''}},
            {'heading': 'ARC and Cache-Aware Design', 'paras': [
                'ARC (Adaptive Replacement Cache) maintains four lists — recent and frequent, ghost and real — and adapts the split between recency and frequency based on which direction the misses point. It often beats plain LRU on mixed workloads. The deeper lesson: cache design must be co-designed with the data access pattern.',
            ]},
        ],
        'practice': {
            'title': 'Resist the Scan',
            'intro': 'A nightly batch job scans 100x the cache capacity, thrashing the hot set for other tenants.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Model the damage: what the scan evicts from plain LRU.'},
                {'label': 'Task 2', 'text': 'Design the two-tier cache and measure hot-set survival.'},
                {'label': 'Task 3', 'text': 'Optionally size an ARC variant and compare on the mixed workload.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why a probation segment absorbs scan churn.'},
            {'label': 'Implementation Design', 'text': 'Design a cache for a database fronting: hot rows protected, range scans in probation. What is the promotion rule?'},
            {'label': 'Boundary Testing', 'text': 'Two tenants share a cache; one scans constantly. Design the isolation (per-tenant segments) that stops the bleed.'},
        ],
        'takeaways': [
            'Two-tier LRU resists scan poisoning',
            'ARC adapts between recency and frequency',
            'Cache design follows the access pattern',
            'Multi-tenant caches need isolation',
        ],
        'further': [
            {'title': 'ARC — the paper', 'url': 'https://www.usenix.org/legacy/publications/library/proceedings/fast03/tech/full_papers/megiddo/megiddo.pdf'},
            {'title': 'Cache replacement policies — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Cache_replacement_policies'},
        ],
    },
    {
        'title': 'LRU Cache: Review & Mastery Quiz',
        'desc': 'Scenario questions on policies, tuning, and resistance.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate LRU concepts',
            'Tune eviction policies',
            'Design scan resistance',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: LRU evicts? (A: the least-recently-used / B: the oldest inserted / C: the smallest)',
                'Q2: O(1) LRU needs? (A: hash + list / B: array only / C: a database)',
                'Q3: A full scan workload causes LRU to? (A: thrash / B: shine / C: compress)',
                'Q4: True or false: LFU can keep a once-hot key forever.',
                'Q5: Two-tier LRU resists? (A: scan poisoning / B: disk full / C: network loss)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A recommendation feed cache serves 99% of traffic but a crawler sweeps it hourly. Design the policy that keeps the hot set.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why eviction policy is a product decision, not just plumbing.'},
        ],
        'takeaways': [
            'Q1: A; Q2: A; Q3: A; Q4: true; Q5: A',
            'LRU assumes locality; adapt when the workload does not',
            'Eviction policy shapes user-visible latency',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# LSM TREE
# ─────────────────────────────────────────────────────────────────────────────
_t('lsm-tree', [
    {
        'title': 'LSM Trees: Writes First, Compaction Later',
        'desc': 'Append-only structure that turns random writes into sequential ones and merges in the background.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain the LSM structure',
            'Describe memtable, SSTable, compaction',
            'Understand write amplification',
            'Know the read cost',
        ],
        'prereqs': ['patterns/b-tree', 'patterns/bloom-filter'],
        'sections': [
            {'heading': 'The Structure', 'paras': [
                'An LSM tree keeps writes in an in-memory memtable, flushes it to immutable sorted files (SSTables), and merges files in the background. Because writes only append, they are sequential — fast on HDD and SSD. The cost moves to reads: a key may live in several files, so reads check memtable then files, newest first.',
            ], 'code': {'lang': 'python', 'body': '''
# LSM essentials: memtable -> flush -> merge
class Memtable:
    def __init__(self):
        self.data = {}          # sorted structure in practice (skip list)

    def put(self, key, value):
        self.data[key] = value

    def flush(self):            # write as a sorted immutable SSTable
        sstable = SSTable(sorted(self.data.items()))
        self.data = {}
        return sstable

class LSMTree:
    def __init__(self):
        self.mem = Memtable()
        self.levels = [[]]      # level 0 newest; deeper = older/merged

    def put(self, key, value):
        self.mem.put(key, value)
        if len(self.mem.data) > 4096:     # flush on size trigger
            self.levels[0].append(self.mem.flush())

    def get(self, key):
        if key in self.mem.data: return self.mem.data[key]
        for level in self.levels:          # newest files first
            for sst in reversed(level):
                if sst.bloom.might_contain(key):
                    v = sst.get(key)
                    if v is not None: return v
        return None'''}},
            {'heading': 'Compaction', 'paras': [
                'Compaction merges overlapping SSTables into sorted runs and drops dead versions, reclaiming space and bounding the read amplification. Leveled compaction (RocksDB default) keeps files in strict levels for predictable reads but pays on every merge; size-tiered (Cassandra) merges similar-size runs, cheaper writes, messier reads.',
            ]},
        ],
        'practice': {
            'title': 'Trace the Lifecycle',
            'intro': 'A key is written, updated twice, and read — trace it through memtable and files.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Trace the three versions of the key through flush and compaction.'},
                {'label': 'Task 2', 'text': 'Count the files a read must check with no compaction vs after.'},
                {'label': 'Task 3', 'text': 'Measure write amplification: bytes written to disk per byte of user data.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why appending beats in-place update on disk. Start with random vs sequential IO.'},
            {'label': 'Compare & Contrast', 'text': 'Compare LSM with B-trees: write cost, read cost, space, and when each wins.'},
            {'label': 'Boundary Testing', 'text': 'Compaction falls behind and files pile up. Design the backpressure that slows writes before space runs out.'},
        ],
        'takeaways': [
            'LSM turns random writes into sequential appends',
            'Memtable + SSTables + background compaction',
            'Reads pay for the write win (amplification)',
            'Compaction strategy shapes the trade-offs',
        ],
        'further': [
            {'title': 'The Log-Structured Merge-Tree — the paper', 'url': 'https://www.cs.umb.edu/~poneil/lsm.pdf'},
            {'title': 'RocksDB — wiki', 'url': 'https://github.com/facebook/rocksdb/wiki'},
        ],
    },
    {
        'title': 'LSM in Production: RocksDB, Cassandra, and LevelDB',
        'desc': 'How real engines tune memtables, compaction, and bloom filters.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Tune memtable size and flush',
            'Choose leveled vs size-tiered compaction',
            'Use bloom filters to cut reads',
            'Configure write stalls',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'The Tuning Knobs', 'paras': [
                'RocksDB exposes every trade: memtable size (bigger = fewer flushes, more memory), write buffer count, compaction style, bloom filter bits per key, and soft/hard write stall limits. Cassandra defaults to size-tiered and uses bloom filters per SSTable so point reads skip files entirely.',
            ], 'code': {'lang': 'text', 'body': '''
Key LSM tuning decisions:
  - write_buffer_size: bigger memtable = fewer flushes = longer
    recovery after crash (memtable is replayed from the WAL)
  - max_write_buffer_number: more buffers = absorb write bursts,
    but each is memory
  - compaction_style: level vs size-tiered
  - bloom filter bits_per_key: ~10 bits = ~1% false positives;
    point reads skip non-matching SSTables entirely
  - soft_pending_compaction_bytes / hard: stall writes when
    compaction lags, trading throughput for stability'''}},
            {'heading': 'Write Path and WAL', 'paras': [
                'A write is ack\'d after the WAL (write-ahead log) is durable, then applied to the memtable — so a crash only costs memtable contents since the last flush. WAL is sequential append; group commit batches fsyncs to amortize the cost. The read path leans on bloom filters and block caches.',
            ]},
        ],
        'practice': {
            'title': 'Tune for the Workload',
            'intro': 'A telemetry ingest: 200k writes/s, occasional point reads, 8GB memory budget.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Size the memtable and write buffers for the burst profile.'},
                {'label': 'Task 2', 'text': 'Choose compaction style and bloom filter size for the read ratio.'},
                {'label': 'Task 3', 'text': 'Set the stall thresholds and simulate a compaction lag.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me the WAL role: why a crash loses only the memtable and how group commit helps.'},
            {'label': 'Implementation Design', 'text': 'Design an LSM-backed time-series store: how are timestamps ordered, and how do range reads exploit the sort?'},
            {'label': 'Boundary Testing', 'text': 'Compaction storms starve reads on a busy box. Design the IO budget (rate limiting compaction) that protects the read path.'},
        ],
        'takeaways': [
            'Memtable, buffers, and compaction are the tunables',
            'Bloom filters make point reads skip files',
            'WAL durability + group commit define the write cost',
            'Write stalls protect stability when compaction lags',
        ],
        'further': [
            {'title': 'RocksDB — Tuning Guide', 'url': 'https://github.com/facebook/rocksdb/wiki/RocksDB-Tuning-Guide'},
            {'title': 'Cassandra — Compaction', 'url': 'https://cassandra.apache.org/doc/stable/cassandra/operating/compaction/index.html'},
        ],
    },
    {
        'title': 'Advanced LSM: Merge Policies and Range Reads',
        'desc': 'Compaction strategies in depth, range reads across files, and LSM for time-series.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Compare leveled and size-tiered deeply',
            'Design range read merging',
            'Exploit LSM for time-ordered data',
            'Analyze amplification costs',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Leveled vs Size-Tiered', 'paras': [
                'Leveled compaction keeps one sorted run per level with exponentially growing sizes; reads touch at most one file per level — predictable. Size-tiered merges runs of similar size; writes are cheaper but a read may scan many files. Cassandra and HBase differ exactly here, and the choice is workload-shaped.',
            ], 'code': {'lang': 'text', 'body': '''
Compaction styles compared:
  Leveled (RocksDB default):
    - each level has one sorted run; reads hit <= one file/level
    - write amplification higher (every write merged many times)
    - predictable read latency, compact space
  Size-tiered (Cassandra default):
    - merge runs of similar size; fewer merges -> lower write amp
    - reads may scan many overlapping files
    - better for write-heavy, read-light, or time-series
  Time-series twist: range-merge on time-ordered keys, compact old
  runs rarely — hot recent data compact, cold history untouched'''}},
            {'heading': 'Range Reads and Time-Series', 'paras': [
                'Range reads merge across files like a k-way merge, streaming rows in order. Time-series workloads shine: writes are time-ordered appends, hot recent data lives in the memtable and first files, and old history stays compacted and rarely touched — LSM is the natural shape for metrics and logs.',
            ]},
        ],
        'practice': {
            'title': 'Design the Merge Strategy',
            'intro': 'A metrics store ingests 1M points/s, keeps 90 days, reads last-hour ranges heavily.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Choose the compaction style for the hot-recent/cold-history split.'},
                {'label': 'Task 2', 'text': 'Design the range read that merges memtable + recent files + compacted history.'},
                {'label': 'Task 3', 'text': 'Compute write and read amplification for the chosen layout.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain the write-amplification vs read-predictability trade between the two compaction styles.'},
            {'label': 'Implementation Design', 'text': 'Design a log store: partition by time, LSM per partition, and the retention compaction that drops old partitions.'},
            {'label': 'Boundary Testing', 'text': 'A time-series key skews: one hot series grows the level 0 files. Design the split or priority that isolates the hot series.'},
        ],
        'takeaways': [
            'Leveled: predictable reads, higher write amplification',
            'Size-tiered: cheaper writes, messy reads',
            'Range reads are k-way merges across files',
            'Time-series is LSM\'s natural workload',
        ],
        'further': [
            {'title': 'RocksDB — Compaction', 'url': 'https://github.com/facebook/rocksdb/wiki/Compaction'},
            {'title': 'HBase — compaction', 'url': 'https://hbase.apache.org/book.html#_compaction'},
        ],
    },
    {
        'title': 'LSM Trees: Review & Mastery Quiz',
        'desc': 'Scenario questions on structure, tuning, and strategies.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate LSM concepts',
            'Tune engines',
            'Choose compaction',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: LSM turns random writes into? (A: sequential appends / B: in-place updates / C: deletes)',
                'Q2: The in-memory write buffer is the? (A: memtable / B: SSTable / C: WAL)',
                'Q3: Bloom filters make point reads? (A: skip files / B: slower / C: impossible)',
                'Q4: True or false: leveled compaction has predictable reads.',
                'Q5: After a crash, the memtable is recovered from? (A: the WAL / B: compaction / C: the network)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A chat history store writes 50k msgs/s, reads conversations. Design the LSM layout, compaction, and bloom settings.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why LSM trades read cost for write speed and how bloom filters pay it back.'},
        ],
        'takeaways': [
            'Q1: A; Q2: A; Q3: A; Q4: true; Q5: A',
            'Write-optimized by design; reads tuned with filters',
            'Compaction strategy is the main dial',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# MAPREDUCE
# ─────────────────────────────────────────────────────────────────────────────
_t('mapreduce', [
    {
        'title': 'MapReduce: Parallelize Batch by Divide and Conquer',
        'desc': 'Splitting a large computation into a parallel map phase and a grouped reduce phase.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain the map-reduce model',
            'Describe shuffle and group',
            'Identify map-reduce workloads',
            'Write a word-count job',
        ],
        'prereqs': ['patterns/iterator', 'principles/fail-fast'],
        'sections': [
            {'heading': 'The Model', 'paras': [
                'MapReduce runs in three phases: map (each input record produces key-value pairs, in parallel), shuffle (pairs are grouped by key and routed), and reduce (each group is processed by one reduce task, in parallel). The framework hides distribution, failure, and scheduling — the programmer writes two pure functions.',
            ], 'code': {'lang': 'python', 'body': '''
# Word count: the canonical MapReduce
def map_fn(line):
    for word in line.split():
        yield (word.lower(), 1)

def reduce_fn(word, counts):
    yield (word, sum(counts))

# Framework: partition -> shuffle by key -> group -> reduce per key
def run_mapreduce(lines, n_reducers):
    mapped = []
    for line in lines:                       # map phase, parallelizable
        mapped.extend(map_fn(line))
    groups = {}
    for key, val in mapped:                  # shuffle + group by hash
        groups.setdefault(hash(key) % n_reducers, []).append((key, val))
    return {k: v for g in groups.values()
            for k, v in reduce_fn(g[0][0], (v for _, v in g))}'''}},
            {'heading': 'Why Map and Reduce Are Pure', 'paras': [
                'Map and reduce functions must be pure — no shared state, deterministic output — because the framework may retry any task on another node. Purity is what makes failure recovery trivial: re-run the task. Side effects and hidden orderings are the classic MapReduce bugs.',
            ]},
        ],
        'practice': {
            'title': 'Count the Log Lines',
            'intro': 'A 100GB log must be summarized by error type across 20 machines.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Define map (extract type) and reduce (count) functions.'},
                {'label': 'Task 2', 'text': 'Design the partitioning so counts are correct regardless of retries.'},
                {'label': 'Task 3', 'text': 'Identify the phase that must be pure and why.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why pure functions make retries safe. Start with a crashed task.'},
            {'label': 'Compare & Contrast', 'text': 'Compare MapReduce with streaming (Kafka) and with SQL GROUP BY. When is batch the right tool?'},
            {'label': 'Boundary Testing', 'text': 'A reduce task sees keys in different order after a retry. Design the deterministic grouping that keeps output identical.'},
        ],
        'takeaways': [
            'Map + shuffle + reduce parallelizes batch data',
            'Pure functions make failure recovery trivial',
            'The framework hides distribution and scheduling',
            'Determinism across retries is mandatory',
        ],
        'further': [
            {'title': 'MapReduce — the paper', 'url': 'https://static.googleusercontent.com/media/research.google.com/en//archive/mapreduce-osdi04.pdf'},
            {'title': 'MapReduce — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/MapReduce'},
        ],
    },
    {
        'title': 'MapReduce in Production: Hadoop and SQL Engines',
        'desc': 'Hadoop MR, Hive, and how modern engines compile GROUP BY to the same shape.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Describe Hadoop job execution',
            'Recognize SQL compiles to map-reduce',
            'Handle skew',
            'Design combiners',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'From SQL to MapReduce', 'paras': [
                'GROUP BY, COUNT, and JOIN compile to map-reduce shapes: Hive translates SQL to MR jobs; modern engines (Spark, Trino) do the same in memory. The map side pushes filters and projections; the reduce side aggregates per group. Understanding the shape lets you predict job behavior from a query.',
            ], 'code': {'lang': 'sql', 'body': '''
-- This SQL compiles to a map-reduce job:
SELECT status, COUNT(*) AS cnt
FROM orders
WHERE created_at > '2026-01-01'
GROUP BY status;

-- Map phase:  for each row -> emit (status, 1), after the WHERE filter
-- Shuffle:    group all (status, 1) pairs by status
-- Reduce:     sum the counts per status
-- A JOIN compiles to a map-side emit per side + a reduce-side merge,
-- or a broadcast join when one side is small.'''}},
            {'heading': 'Combiners and Skew', 'paras': [
                'A combiner is a mini-reduce on the map side, shrinking the shuffle volume (sum partial counts before shipping). Skew is the killer: one key dominates (a hot word, a famous user), overloading one reducer. Salting splits hot keys across reducers, then a final pass merges.',
            ]},
        ],
        'practice': {
            'title': 'Tune the Job',
            'intro': 'A daily aggregation of 10B events has one hot key with 60% of the data.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Add the combiner and measure shuffle bytes before/after.'},
                {'label': 'Task 2', 'text': 'Design the salt-and-merge for the hot key.'},
                {'label': 'Task 3', 'text': 'Predict: which phase is the bottleneck and what parallelism fixes it?'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why a combiner shrinks shuffle and why skew breaks one reducer. Ask me to trace a hot key.'},
            {'label': 'Implementation Design', 'text': 'Design a daily recommendation aggregation with a hot user. Show the salting plan and the final merge.'},
            {'label': 'Boundary Testing', 'text': 'A reducer task fails twice and must retry. Design the determinism that makes the retry identical.'},
        ],
        'takeaways': [
            'SQL GROUP BY/JOIN compile to map-reduce shapes',
            'Combiners shrink shuffle traffic',
            'Key skew overloads single reducers',
            'Salt-and-merge tames hot keys',
        ],
        'further': [
            {'title': 'Hadoop MapReduce tutorial', 'url': 'https://hadoop.apache.org/docs/current/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html'},
        ],
    },
    {
        'title': 'Advanced MapReduce: Iterative and Incremental Jobs',
        'desc': 'Iterative algorithms (PageRank), incremental pipelines, and materialized views.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Express iterative algorithms',
            'Design incremental updates',
            'Avoid recomputing everything',
            'Choose engine for the job',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Iteration Is the Pain Point', 'paras': [
                'PageRank and k-means iterate: each pass needs the previous output as input, and naive MapReduce re-reads and re-shuffles the entire dataset every iteration. Systems like Spark cache RDDs in memory to keep iteration fast, and Pregel (vertex-centric) specializes graph iteration. The lesson: know your iteration pattern before choosing the engine.',
            ], 'code': {'lang': 'scala', 'body': '''
// Spark: cache keeps iterative algorithms fast
val links = sc.textFile("links.tsv")
    .map(parse).distinct().groupByKey().cache()   // cached across iters

var ranks = links.mapValues(_ => 1.0)
for (i <- 1 to 10) {                              // iterative loop
  val contribs = links.join(ranks).values.flatMap {
    case (urls, rank) => urls.map(url => (url, rank / urls.size))
  }
  ranks = contribs.reduceByKey(_ + _).mapValues(0.15 + 0.85 * _)
}
// Without the cache(), every iteration re-reads and re-shuffles
// the whole graph from disk.'''}},
            {'heading': 'Incremental Aggregation', 'paras': [
                'When inputs change by a fraction, full recompute is wasteful. Incremental pipelines (Lambda/Kappa) keep base aggregates and apply deltas; streaming stages (Kafka Streams, Flink) maintain rolling windows as the map-reduce shape runs continuously. Materialized views in warehouses do this declaratively.',
            ]},
        ],
        'practice': {
            'title': 'Iterate Without Recomputation',
            'intro': 'A PageRank job over a 10B-edge graph runs nightly and the edges change 2% per day.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the cached iteration and count the bytes saved.'},
                {'label': 'Task 2', 'text': 'Design the incremental delta path for the 2% change.'},
                {'label': 'Task 3', 'text': 'Choose the engine (Spark vs Flink vs warehouse SQL) and justify with the update pattern.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why iteration without caching re-reads the world every pass.'},
            {'label': 'Implementation Design', 'text': 'Design a streaming map-reduce for real-time per-user aggregations with exactly-once semantics. Where do the windows live?'},
            {'label': 'Boundary Testing', 'text': 'A delta arrives out of order. Design the watermark or the idempotent apply that keeps the aggregate correct.'},
        ],
        'takeaways': [
            'Iteration without caching is re-reading the world',
            'Engine choice follows the iteration pattern',
            'Deltas beat full recompute for slowly changing data',
            'Streaming runs the map-reduce shape continuously',
        ],
        'further': [
            {'title': 'Spark — RDD programming guide', 'url': 'https://spark.apache.org/docs/latest/rdd-programming-guide.html'},
            {'title': 'Pregel — Google paper', 'url': 'https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/37252.pdf'},
        ],
    },
    {
        'title': 'MapReduce: Review & Mastery Quiz',
        'desc': 'Scenario questions on the model, tuning, and iteration.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate map-reduce concepts',
            'Tune jobs',
            'Design incremental pipelines',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: Map and reduce must be? (A: pure / B: stateful / C: interactive)',
                'Q2: The shuffle phase? (A: groups by key / B: sorts by size / C: drops data)',
                'Q3: A combiner runs? (A: on the map side / B: on the client / C: in the DB)',
                'Q4: True or false: one dominant key overloads a single reducer.',
                'Q5: Iterative algorithms stay fast with? (A: caching / B: re-reading / C: compression)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A daily user-activity rollup of 50B events has celebrity users. Design the job: combiner, salting, and the merge pass.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why pure functions are what make a 10,000-machine job recoverable.'},
        ],
        'takeaways': [
            'Q1: A; Q2: A; Q3: A; Q4: true; Q5: A',
            'Map-reduce is divide-and-conquer batch done right',
            'Purity, skew, and iteration define the hard parts',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# MEDIATOR
# ─────────────────────────────────────────────────────────────────────────────
_t('mediator', [
    {
        'title': 'Mediator: One Hub for Many Collaborators',
        'desc': 'Centralizing interactions between many objects so they talk to the hub, not to each other.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain the mediator intent',
            'Replace many-to-many with hub-and-spoke',
            'Build a UI mediator',
            'Compare with observer',
        ],
        'prereqs': ['patterns/observer', 'patterns/facade'],
        'sections': [
            {'heading': 'The Problem', 'paras': [
                'A form has 20 widgets; every widget reacts to changes in others. Direct wiring creates a many-to-many tangle. The mediator becomes the hub: widgets notify the mediator, and the mediator decides what to update. Widgets stay reusable and know nothing about each other.',
            ], 'code': {'lang': 'typescript', 'body': '''
// Mediator: the dialog coordinates its widgets
class DialogMediator {
    constructor(private input: Input, private button: Button) {
        input.onChange = (v) => this.inputChanged(v);
        button.onClick = () => this.submit();
    }
    private inputChanged(v: string) {
        this.button.setEnabled(v.length > 2);   // hub decides
    }
    private submit() {
        if (this.button.enabled) save(this.input.value);
    }
}
// Input and Button have no reference to each other.
// A new widget joins by wiring it in the mediator only.'''}},
            {'heading': 'Mediator vs Observer', 'paras': [
                'Observer is a one-to-many notification: subjects announce, observers listen. Mediator is many-to-many coordination through one hub: it is the observer plus control flow. They combine well — widgets fire events, the mediator subscribes to all of them and orchestrates.',
            ]},
        ],
        'practice': {
            'title': 'Untangle the Form',
            'intro': 'A settings dialog: theme, font size, and preview update each other across 6 widgets.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Draw the current many-to-many wiring and count the links.'},
                {'label': 'Task 2', 'text': 'Build the mediator and move every link through it.'},
                {'label': 'Task 3', 'text': 'Add a new widget and count the changes under both designs.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why the mediator centralizes control flow, not just notifications.'},
            {'label': 'Compare & Contrast', 'text': 'Compare mediator with observer and with facade. Where does each belong in a UI or service layer?'},
            {'label': 'Boundary Testing', 'text': 'Two widgets update each other in a loop through the mediator. Design the cycle guard.'},
        ],
        'takeaways': [
            'Mediator turns many-to-many into hub-and-spoke',
            'Widgets stay decoupled and reusable',
            'Mediator owns the coordination logic',
            'Guard against update cycles',
        ],
        'further': [
            {'title': 'Mediator — Refactoring Guru', 'url': 'https://refactoring.guru/design-patterns/mediator'},
            {'title': 'Mediator Pattern — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Mediator_pattern'},
        ],
    },
    {
        'title': 'Mediator in Production: Event Buses and Orchestrators',
        'desc': 'Message buses, workflow orchestrators, and transaction managers as mediators.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Design an event bus mediator',
            'Orchestrate workflows centrally',
            'Coordinate transactions',
            'Avoid mediator bloat',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'The Event Bus', 'paras': [
                'An in-process event bus (or a message broker) is a mediator: producers publish, the bus routes to subscribers, and no producer knows its consumers. The bus centralizes routing, ordering, and fan-out policy. The risk is the mediator becoming a god object — every rule flowing through one hub.',
            ], 'code': {'lang': 'go', 'body': '''
// Event bus as mediator: publishers and subscribers never meet
type Bus struct {
    subs map[string][]func(Event)
}
func (b *Bus) Publish(topic string, e Event) {
    for _, h := range b.subs[topic] { h(e) }   // hub routes to handlers
}
func (b *Bus) Subscribe(topic string, h func(Event)) {
    b.subs[topic] = append(b.subs[topic], h)
}
// Order service publishes OrderPlaced; inventory and billing
// subscribe. Neither service imports the other — the bus mediates.'''}},
            {'heading': 'Orchestration', 'paras': [
                'A workflow orchestrator (Temporal, Step Functions) is a mediator for services: it decides the sequence, retries, and compensations. A transaction coordinator mediates distributed commits. The pattern scales up from dialogs to distributed systems — one hub, clear rules, decoupled participants.',
            ]},
        ],
        'practice': {
            'title': 'Orchestrate the Order Flow',
            'intro': 'Order placement touches inventory, payment, and shipping; failures need compensating actions.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the orchestrator state machine and its events.'},
                {'label': 'Task 2', 'text': 'Wire the services to the bus without any service importing another.'},
                {'label': 'Task 3', 'text': 'Add the compensation flow for a payment failure mid-order.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why an orchestrator is a mediator and how it stays decoupled from the services it coordinates.'},
            {'label': 'Implementation Design', 'text': 'Design a saga orchestrator: the hub, the per-step handlers, and the compensation table. Where does retry live?'},
            {'label': 'Boundary Testing', 'text': 'The bus itself fails. Design the durable queue or the retry contract that keeps the workflow alive.'},
        ],
        'takeaways': [
            'Event buses mediate between producers and consumers',
            'Orchestrators mediate across services',
            'The hub must not become a god object',
            'Durability of the hub is a first-class concern',
        ],
        'further': [
            {'title': 'Temporal — durable workflows', 'url': 'https://docs.temporal.io/'},
            {'title': 'Mediator — Refactoring Guru', 'url': 'https://refactoring.guru/design-patterns/mediator'},
        ],
    },
    {
        'title': 'Advanced Mediator: Choreography vs Orchestration',
        'desc': 'When to choreograph with events instead of orchestrating with a hub.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Contrast orchestration and choreography',
            'Design event choreography',
            'Handle compensation without a hub',
            'Choose the coordination model',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'The Trade-Off', 'paras': [
                'Choreography drops the hub: each service reacts to events and emits its own, passing control along. It removes the single point of failure and keeps services fully independent, but the flow is implicit — harder to trace, test, and reason about. Orchestration is explicit and recoverable but concentrates coordination.',
            ], 'code': {'lang': 'text', 'body': '''
Orchestration vs choreography:
  Orchestration (central hub):
    + explicit flow, easy to trace, retry, and compensate
    - hub is a dependency and a bottleneck
    Example: Temporal workflow coordinates order -> payment -> ship
  Choreography (event chain):
    + services fully independent, no hub to fail
    - flow is implicit; tracing needs an event store
    Example: OrderPlaced -> InventoryReserved -> PaymentCharged
      -> ShipmentDispatched, each step reacts and emits
  Hybrid: choreograph the happy path, orchestrate the failures.'''}},
            {'heading': 'Choosing the Model', 'paras': [
                'Pick orchestration when the flow is long, has complex error handling, or must be resumable. Pick choreography when services must evolve independently and the happy path is linear. Compensation in choreography spreads across services — each emits a compensating event — and tracing requires an event log.',
            ]},
        ],
        'practice': {
            'title': 'Choose the Coordination',
            'intro': 'A signup flow: validate, create account, send email, provision workspace — with retries on each step.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the orchestrated version with a state machine.'},
                {'label': 'Task 2', 'text': 'Design the choreographed version as an event chain.'},
                {'label': 'Task 3', 'text': 'Compare failure handling and choose one, justifying the retry story.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain why choreography makes flows implicit and tracing harder.'},
            {'label': 'Implementation Design', 'text': 'Design a hybrid: choreographed happy path, orchestrated compensations. Where does the compensation hub live?'},
            {'label': 'Boundary Testing', 'text': 'An event is lost in choreography. Design the outbox pattern or the reconciliation that makes the chain reliable.'},
        ],
        'takeaways': [
            'Orchestration is explicit and recoverable',
            'Choreography is decoupled but implicit',
            'Flows with complex errors favor the hub',
            'Hybrids choreograph happy paths, orchestrate failures',
        ],
        'further': [
            {'title': 'Saga pattern — microservices.io', 'url': 'https://microservices.io/patterns/data/saga.html'},
            {'title': 'Temporal — durable workflows', 'url': 'https://docs.temporal.io/'},
        ],
    },
    {
        'title': 'Mediator: Review & Mastery Quiz',
        'desc': 'Scenario questions on hubs, buses, and coordination models.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate mediator concepts',
            'Design buses and orchestrators',
            'Choose coordination',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: A mediator turns many-to-many into? (A: hub-and-spoke / B: one-to-one / C: a tree)',
                'Q2: Observer is? (A: one-to-many / B: many-to-many / C: zero-to-zero)',
                'Q3: An orchestrator is a mediator? (A: for services / B: for users / C: for browsers)',
                'Q4: True or false: choreography has no central hub.',
                'Q5: The main choreography risk is? (A: implicit flow / B: too fast / C: too many hubs)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A checkout flow spans 5 services with refund paths. Choose orchestration or choreography and justify the retry design.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why decoupling collaborators can still create a god object.'},
        ],
        'takeaways': [
            'Q1: A; Q2: A; Q3: A; Q4: true; Q5: A',
            'Hubs centralize coordination; use them deliberately',
            'Choreography trades control for independence',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# MEMENTO
# ─────────────────────────────────────────────────────────────────────────────
_t('memento', [
    {
        'title': 'Memento: Snapshots Without Breaking Encapsulation',
        'desc': 'Capturing and restoring an object state without exposing its internals.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain the memento intent',
            'Capture state without breaking encapsulation',
            'Implement undo/redo',
            'Know the memory cost',
        ],
        'prereqs': ['patterns/command', 'patterns/state'],
        'sections': [
            {'heading': 'The Problem', 'paras': [
                'Undo needs the previous state, but reading all fields to snapshot them either exposes internals or couples the undo logic to every field. The memento is an opaque snapshot created by the originator itself — only the originator can read and restore it, so encapsulation survives.',
            ], 'code': {'lang': 'java', 'body': '''
// Memento: the editor snapshots itself; caretaker holds history
class Editor {
    private String text;
    Memento save() { return new Memento(text); }        // snapshot
    void restore(Memento m) { this.text = m.getText(); }
}

class Memento {                    // opaque to everyone but Editor
    private final String text;
    Memento(String t) { this.text = t; }
    String getText() { return text; }   // package-private access
}

// History: a stack of Mementos, all opaque
Stack<Memento> history = new Stack<>();
history.push(editor.save());
editor.type("hello");
editor.restore(history.pop());     // undo'''}},
            {'heading': 'Undo/Redo', 'paras': [
                'Undo = pop a memento and restore; redo = push back. Two stacks make both work. The memento pattern is the textbook undo — but snapshots are copies: a large document snapshot per keystroke is memory-heavy, which is why real editors use deltas or persistent data structures.',
            ]},
        ],
        'practice': {
            'title': 'Build Undo for the Editor',
            'intro': 'A text area needs undo/redo across 1000 edits without exposing its internal buffer.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Implement the memento and the two-stack undo/redo.'},
                {'label': 'Task 2', 'text': 'Bound the history: drop the oldest snapshots beyond a limit.'},
                {'label': 'Task 3', 'text': 'Measure memory for full snapshots and propose the delta alternative.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why the memento keeps encapsulation while saving state.'},
            {'label': 'Compare & Contrast', 'text': 'Compare memento with command (the other undo approach) and with event sourcing. Which restores what?'},
            {'label': 'Boundary Testing', 'text': 'A snapshot is taken mid-edit and restored later, corrupting an invariant. Design the state validation on restore.'},
        ],
        'takeaways': [
            'Mementos capture state without breaking encapsulation',
            'Undo/redo = two stacks of snapshots',
            'Snapshots cost memory — bound the history',
            'Deltas or persistent structures scale undo',
        ],
        'further': [
            {'title': 'Memento — Refactoring Guru', 'url': 'https://refactoring.guru/design-patterns/memento'},
            {'title': 'Memento Pattern — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Memento_pattern'},
        ],
    },
    {
        'title': 'Memento in Production: Checkpoints and Serialization',
        'desc': 'Database checkpoints, workflow state, and serialized snapshots for recovery.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Design checkpoint-based recovery',
            'Serialize snapshots durably',
            'Restore workflow state',
            'Manage snapshot size',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Checkpoints', 'paras': [
                'Systems checkpoint periodically: serialize a consistent state to durable storage so recovery starts from the checkpoint plus the log since it. Streaming engines checkpoint offsets and state to Kafka; databases checkpoint the WAL. The memento is the design: the originator (the engine) knows its own state layout.',
            ], 'code': {'lang': 'python', 'body': '''
# Checkpoint + log replay: recovery from the snapshot
class Processor:
    def __init__(self):
        self.state = {}
        self.log = []                     # operations since checkpoint
        self.checkpoint = None            # last durable snapshot

    def apply(self, op):
        self.state[op.key] = op.value
        self.log.append(op)

    def checkpoint_now(self):
        self.checkpoint = dump(self.state)   # serialized memento
        self.log = []                        # log restarts from here

    def recover(self):
        if self.checkpoint is not None:
            self.state = load(self.checkpoint)   # restore
        for op in self.log:                      # replay the tail
            self.apply(op)'''}},
            {'heading': 'Workflow State', 'paras': [
                'Long-running workflows serialize their state between steps so a crash resumes exactly where it stopped. Temporal stores the workflow state and events; each step is a checkpoint. Snapshot size is the dial: full snapshots are simple but heavy, incremental snapshots (diff against the last) are lighter but need the base.',
            ]},
        ],
        'practice': {
            'title': 'Design the Checkpointing',
            'intro': 'A stream processor must resume exactly-once after crashes, checkpointing every 10 seconds.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the snapshot format and the checkpoint trigger.'},
                {'label': 'Task 2', 'text': 'Design recovery: snapshot + log replay, exactly-once.'},
                {'label': 'Task 3', 'text': 'Compare full vs incremental snapshots for a 10GB state.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why checkpoint plus replay beats replay-from-the-beginning.'},
            {'label': 'Implementation Design', 'text': 'Design a workflow engine checkpoint: what is stored, when, and how a mid-step crash resumes.'},
            {'label': 'Boundary Testing', 'text': 'A checkpoint is corrupted on disk. Design the validation (checksums) and the fallback to the previous checkpoint.'},
        ],
        'takeaways': [
            'Checkpoints make recovery replay only the tail',
            'The originator owns the snapshot format',
            'Workflow steps are natural checkpoints',
            'Snapshot size drives full vs incremental choice',
        ],
        'further': [
            {'title': 'Flink — checkpointing', 'url': 'https://nightlies.apache.org/flink/flink-docs-stable/docs/concepts/stateful-stream-processing/'},
            {'title': 'Temporal — durable execution', 'url': 'https://docs.temporal.io/'},
        ],
    },
    {
        'title': 'Advanced Memento: Persistent Structures and Deltas',
        'desc': 'Structural sharing, delta snapshots, and time travel.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Use persistent data structures for undo',
            'Design delta snapshots',
            'Implement time travel queries',
            'Reason about snapshot cost',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Persistent Structures', 'paras': [
                'A persistent data structure shares structure between versions: modifying one element creates a new version that shares everything else. Undo becomes keeping the old root pointer — O(1) per snapshot instead of O(n) copies. Git is the canonical example: commits are mementos sharing unchanged trees.',
            ], 'code': {'lang': 'python', 'body': '''
# Persistent list via structural sharing (concept)
# v0 = Node(1, Node(2, Node(3)))
# v1 = prepend(v0, 0) -> Node(0, v0)   # shares v0 entirely
#
# Undo = keep a stack of version roots:
history = [root_v0]
root_v1 = prepend(root_v0, 0)          # shares old tail
history.append(root_v1)
root_v2 = prepend(root_v1, -1)         # shares v1's tail (v0 again)
history.append(root_v2)
# Pop the stack to undo: O(1), no copying.
# This is how Git, Clojure's persistent vectors, and
# immutable.js keep history cheap.'''}},
            {'heading': 'Deltas and Time Travel', 'paras': [
                'Delta snapshots store only what changed against the base; restore applies deltas in order. Time travel — querying state as of an instant — is mementos at scale: a database\'s MVCC keeps version chains; systems with full history (Git, temporal stores) let you inspect any past version cheaply.',
            ]},
        ],
        'practice': {
            'title': 'Design Cheap History',
            'intro': 'A collaborative document keeps 10k snapshots per session; full copies blow memory.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the persistent-structure undo and measure per-edit cost.'},
                {'label': 'Task 2', 'text': 'Design the delta snapshot chain with periodic full bases.'},
                {'label': 'Task 3', 'text': 'Implement a time-travel query: state as of edit #4820.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain how structural sharing makes version history nearly free.'},
            {'label': 'Implementation Design', 'text': 'Design a Git-like store for configuration files with branch, merge, and revert. What are the mementos?'},
            {'label': 'Boundary Testing', 'text': 'A delta chain grows 10,000 deep and restore is slow. Design the base-compaction trigger and the worst-case restore.'},
        ],
        'takeaways': [
            'Persistent structures share state between versions',
            'Undo becomes O(1) root-pointer swaps',
            'Delta chains need periodic full bases',
            'Time travel is mementos kept forever',
        ],
        'further': [
            {'title': 'Git internals — the object model', 'url': 'https://git-scm.com/book/en/v2/Git-Internals-Git-Objects'},
            {'title': 'Persistent data structures — Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Persistent_data_structure'},
        ],
    },
    {
        'title': 'Memento: Review & Mastery Quiz',
        'desc': 'Scenario questions on snapshots, checkpoints, and history.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate memento concepts',
            'Design recovery',
            'Scale history',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: A memento preserves? (A: encapsulation / B: speed / C: coupling)',
                'Q2: Undo/redo uses? (A: two stacks / B: one list / C: a database)',
                'Q3: Checkpoint recovery replays? (A: only the tail / B: everything / C: nothing)',
                'Q4: True or false: persistent structures share unchanged state between versions.',
                'Q5: Git commits are? (A: mementos / B: commands / C: caches)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A stream processor with 20GB state must recover in under 30s. Design the checkpoint interval, format, and replay path.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why snapshotting must not break the encapsulation that made the object safe.'},
        ],
        'takeaways': [
            'Q1: A; Q2: A; Q3: A; Q4: true; Q5: A',
            'Snapshots + replay = recovery',
            'Structural sharing makes history cheap',
        ],
    },
])

# ─────────────────────────────────────────────────────────────────────────────
# MULTI-LEADER
# ─────────────────────────────────────────────────────────────────────────────
_t('multi-leader', [
    {
        'title': 'Multi-Leader Replication: Many Writers, One Log Each',
        'desc': 'Several leaders accept writes and replicate to each other, trading consistency for locality.',
        'dur': '45 min', 'diff': 'Beginner',
        'objs': [
            'Explain the multi-leader model',
            'Describe topologies',
            'Understand write conflicts',
            'Know the use cases',
        ],
        'prereqs': ['patterns/leader-follower', 'patterns/replication'],
        'sections': [
            {'heading': 'The Model', 'paras': [
                'Multi-leader has several nodes that each accept writes; each leader replicates to the others. Use cases: multi-datacenter (write near users, async cross-DC sync), offline-first apps (device is a leader), and collaborative editing. The price is that two leaders can accept the same key concurrently — write conflicts.',
            ], 'code': {'lang': 'text', 'body': '''
Multi-leader topology: every leader replicates to every other
  [DC1 leader] <----> [DC2 leader]
        ^                  ^
     writes near        writes near
     users in 1         users in 2
  Conflict example:
    DC1: user edits profile name -> "Alice"
    DC2: user edits profile name -> "Alicia"
    Both accepted concurrently; replication delivers both.
    Resolution (LWW, merge, CRDT, or surface-to-user) is REQUIRED.
  Compare single-leader: one writer, no conflicts, one region.'''}},
            {'heading': 'Topologies', 'paras': [
                'All-to-all replicates everywhere (simple, ordered). Circular and star topologies reduce links but forward through intermediates — a failure can stop propagation, and ordering across the chain is hard to guarantee. All-to-all with conflict-free data models (per-key single-writer) is the safest.',
            ]},
        ],
        'practice': {
            'title': 'Trace the Conflict',
            'intro': 'A shopping cart syncs between phone and laptop, both leaders, both offline.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Trace two concurrent edits to the same item count.'},
                {'label': 'Task 2', 'text': 'Apply LWW and show the lost update.'},
                {'label': 'Task 3', 'text': 'Design the CRDT merge that loses nothing.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me one question at a time about why two leaders make conflicts inevitable. Start with the offline window.'},
            {'label': 'Compare & Contrast', 'text': 'Compare multi-leader with single-leader and leaderless. Which fits an offline-first notes app and why?'},
            {'label': 'Boundary Testing', 'text': 'A partition splits the leaders and both serve writes. Design the reconciliation that converges when they reconnect.'},
        ],
        'takeaways': [
            'Multi-leader trades consistency for write locality',
            'Conflicts are inevitable with multiple writers',
            'Resolution must be explicit: LWW, merge, or CRDT',
            'Topologies trade links for ordering guarantees',
        ],
        'further': [
            {'title': 'Multi-leader replication — DDIA Ch. 5', 'url': 'https://dataintensive.net/'},
            {'title': 'CRDTs — an introduction', 'url': 'https://crdt.tech/'},
        ],
    },
    {
        'title': 'Multi-Leader in Production: Conflict Resolution',
        'desc': 'LWW, CRDTs, custom merges, and conflict-free schema design.',
        'dur': '60 min', 'diff': 'Intermediate',
        'objs': [
            'Apply LWW correctly',
            'Design CRDT merges',
            'Build conflict-free schemas',
            'Test conflict resolution',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Resolution Strategies', 'paras': [
                'Last-writer-wins uses timestamps — simple, but clock skew silently loses updates. CRDTs merge deterministically (counters, sets, registers) and converge without a coordinator. Custom merges understand the domain (merge concurrent list edits by position). The right strategy depends on the semantic cost of losing an update.',
            ], 'code': {'lang': 'typescript', 'body': '''
// CRDT examples that merge without a coordinator:
//  G-Counter (grow-only): merge = elementwise max; value = sum
//  G-Set / OR-Set: merge = union (removes tracked via tombstones)
//  LWW-Register: merge = take the higher (value, timestamp) pair
//  Convergent by construction: same inputs in any order, same result

// A merge for concurrent set edits (OR-Set style):
function mergeSets(a: Set<string>, b: Set<string>): Set<string> {
    // union of adds minus union of removes (both tracked with IDs)
    const adds = union(a.adds, b.adds);
    const removes = union(a.removes, b.removes);
    return new Set([...adds].filter(x => !removes.has(x)));
}'''}},
            {'heading': 'Schema Design', 'paras': [
                'The best conflict handling is avoiding conflicts: assign each key a single writing leader (shard by user), or design data as CRDT-friendly operations (add/remove with IDs rather than whole-list overwrites). Conflict-free schemas beat clever resolution every time.',
            ]},
        ],
        'practice': {
            'title': 'Design the Conflict-Free Schema',
            'intro': 'A shared grocery list syncs across family phones; items are added and checked off concurrently.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Design the item-level operations (add id, check id) instead of list overwrites.'},
                {'label': 'Task 2', 'text': 'Implement the merge and prove convergence with concurrent edits.'},
                {'label': 'Task 3', 'text': 'Test the LWW alternative and document which update it loses.'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Teach me why operation-based CRDTs beat state-based ones for lists, and what tombstones are for.'},
            {'label': 'Implementation Design', 'text': 'Design a multi-leader calendar where the same slot is booked from two devices. What merge policy serves both users?'},
            {'label': 'Boundary Testing', 'text': 'Clocks skew 30s between two leaders. Design the hybrid logical clock that fixes LWW ordering.'},
        ],
        'takeaways': [
            'LWW is simple but loses updates under skew',
            'CRDTs converge deterministically',
            'Conflict-free schemas beat clever resolution',
            'Concurrent operation design matters more than merge code',
        ],
        'further': [
            {'title': 'CRDT — crdt.tech', 'url': 'https://crdt.tech/'},
            {'title': 'Yjs — CRDTs for collaborative editing', 'url': 'https://docs.yjs.dev/'},
        ],
    },
    {
        'title': 'Advanced Multi-Leader: Hybrid Logical Clocks and Ordering',
        'desc': 'Ordering concurrent writes, HLCs, and multi-leader for collaborative editing.',
        'dur': '75 min', 'diff': 'Advanced',
        'objs': [
            'Order writes with hybrid logical clocks',
            'Design causal delivery',
            'Resolve collaborative edits',
            'Analyze convergence guarantees',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Ordering Writes', 'paras': [
                'Replica clocks drift, so timestamps cannot order concurrent writes. Hybrid logical clocks (HLC) combine a physical timestamp with a logical counter, capturing causality while staying close to wall time. Causal delivery — deliver operations in causal order — plus CRDT convergence gives collaborative systems their guarantees.',
            ], 'code': {'lang': 'go', 'body': '''
// Hybrid logical clock: physical time + logical counter
type HLC struct {
    mu    sync.Mutex
    pt    int64   // physical ms
    ct    int64   // logical counter
}
func (h *HLC) Now() int64 {
    h.mu.Lock(); defer h.mu.Unlock()
    now := time.Now().UnixMilli()
    if now > h.pt { h.pt = now; h.ct = 0 } else { h.ct++ }
    return h.pt<<16 | h.ct    // sortable, causal
}
// When receiving an event with a higher pt, adopt it and bump ct.
// Events that are causally related get increasing HLCs; concurrent
// events tie-break deterministically (e.g. by origin id).'''}},
            {'heading': 'Collaborative Editing', 'paras': [
                'Real-time editors are multi-leader: every client is a leader, operations replicate, and CRDTs (Yjs, Automerge) or OT (Operational Transformation) merge concurrent edits into a consistent document. The difference: CRDTs converge by construction; OT transforms operations against each other — both are multi-leader conflict resolution refined to text.',
            ]},
        ],
        'practice': {
            'title': 'Build the Editor Merge',
            'intro': 'Two users edit the same paragraph concurrently on a shared doc.',
            'tasks': [
                {'label': 'Task 1', 'text': 'Implement the HLC and order the two edits causally.'},
                {'label': 'Task 2', 'text': 'Design the CRDT merge and prove both edits survive.'},
                {'label': 'Task 3', 'text': 'Compare with the LWW approach: which characters does it lose?'},
            ],
        },
        'prompts': [
            {'label': 'Socratic Tutor', 'text': 'Ask me questions until I can explain what a hybrid logical clock adds over a wall clock.'},
            {'label': 'Implementation Design', 'text': 'Design a distributed todo list where two users reorder the same item list concurrently. What operation-based CRDT handles reordering?'},
            {'label': 'Boundary Testing', 'text': 'A client replays an old operation after reconnecting. Design the idempotent apply that prevents double-effects.'},
        ],
        'takeaways': [
            'HLCs give causality to timestamp ordering',
            'Causal delivery + CRDTs = collaborative guarantees',
            'CRDTs converge; OT transforms',
            'Idempotent apply protects against replays',
        ],
        'further': [
            {'title': 'Hybrid Logical Clocks — the paper', 'url': 'https://cse.buffalo.edu/tech-reports/2014-04.pdf'},
            {'title': 'Automerge — CRDTs for apps', 'url': 'https://automerge.org/'},
        ],
    },
    {
        'title': 'Multi-Leader: Review & Mastery Quiz',
        'desc': 'Scenario questions on topologies, conflicts, and ordering.',
        'dur': '30 min', 'diff': 'Intermediate', 'type': 'quiz',
        'objs': [
            'Consolidate multi-leader concepts',
            'Resolve conflicts',
            'Order concurrent writes',
        ],
        'prereqs': [],
        'sections': [
            {'heading': 'Quiz', 'paras': [
                'Answer these, then check against the key takeaways.',
            ], 'bullets': [
                'Q1: Multi-leader trades consistency for? (A: write locality / B: read speed / C: storage)',
                'Q2: Two leaders accepting the same key causes? (A: a conflict / B: nothing / C: a lock)',
                'Q3: LWW resolution is vulnerable to? (A: clock skew / B: disk full / C: caching)',
                'Q4: True or false: CRDTs converge deterministically without a coordinator.',
                'Q5: Hybrid logical clocks combine? (A: physical time + logical counter / B: two clocks / C: GPS + NTP)',
            ]},
        ],
        'prompts': [
            {'label': 'Scenarios', 'text': 'A note app syncs between laptop and phone with concurrent edits. Design the CRDT ops, the HLC ordering, and the merge.'},
            {'label': 'Open-Ended', 'text': 'Explain to a junior engineer why "last writer wins" is a data-loss policy in disguise.'},
        ],
        'takeaways': [
            'Q1: A; Q2: A; Q3: A; Q4: true; Q5: A',
            'Many writers need explicit conflict semantics',
            'CRDTs + causal ordering make convergence real',
        ],
    },
])
