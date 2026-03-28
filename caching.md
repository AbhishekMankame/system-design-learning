# Caching

In system design interviews, caching comes up almost everytime you need to handle high read traffic. Your database becomes bottleneck, latency starts creeping up, and the interviewer is waiting for you to say the word: cache.<br>

Reading a user profile from Postgres may take 50 milliseconds, but reading from an in-memory cache like Redis takes just 1 millisecond. That's a 50x improvement in latency. Databases store data on disk, and every query pays the cost of disk accecss. Memory sits just closer to the CPU and avoids that entirely.<br>

Caches are essential for scalable systems. They reduce load on the database and cut latency dramatically. But they also create new challenges around invalidation and failure handling.<br>

This breakdown covers the basics of caching, when and where to use it, common pitfalls, and how to talk about caching clearly in interviews.

### Where to cache?
When most engineers hear caching, they immediately think of Redis or Memcached sitting between the application and the database. It is the most common type of cache and the one interviewers care about the most.<br>

But caching shows up in multiple layers of a system. Browsers cache. CDNs cache. Applications cache. Even databases have built-in cache layers. <br>

Let's look at the main places you can cache data, why each one exists, and when it makes sense to use it.

### External Caching
An external cache is a standalone cache service that your application talks to over the network. This is what most people think of when they head caching. You store frequently accessed data in something like 'Redis' or 'Memcached' so you do not have to hit the database every time.

<pre>
Client <----> Application Servers <---- 1. Check cache ----> Cache
                            ^
                            |
                            --- 2. Read from DB as fallback ----> Database

</pre>
External caches scale well because every application server can share the same cache. They also support eviction policies like LRU and expiration via TTL so your memory footprint stays controlled.<br>

- VV IMP Note: In system design interviewers, external caching with Redis is the default answer when discussing caching stratergies. Interviewers expect you to mention it for any high-traffic system. Start here, then layer on other caching types such as CDN or client-side caching only if the problem calls for them.


### CDN (Content Delivery Network)
A CDN is a geographically distributed network of servers that caches content close to users. Instead of every request travelling to your original server, a CDN stores copies of your content at edge servers around the world.
<pre> Modern CDNs like Clourflare, Fastly and Akamai can cache much more than static files. They can also cache public API responses, HTML pages, and even run edge logic to personalize content or enforce security rules before requests reach your servers. But the most common and most impactful use of a CDN is still media delivery.</pre>

How it works:
1. A user requests an image from your app.
2. The request goes to the nearest CDN edge server.
3. If the image is cached there, it returned immediately.
4. If not, the CDN fetches it from your origin server, stores it, and returns it.
5. Future users in that region get the image instantly from the CDN.
<br>

Without a CDN, every image request travels to your origin. If your server is in Virginia and the user is in India, that adds 250-300ms of latency per request. With a CDN, the same image is server from a nearby edge server in 20-40ms. That is massive performance difference.

<pre> Even though modern CDNs can cache API responses and dynamic content, in system design interviews the safest time to introduce a CDN is when your system serves static media at scale. Start with that reason first, then expand only if the problem calls for more.</pre>

### Client-Side Caching
Client-Side caching stores the data close to the requester to avoid unnecessary network calls. This usually means the user's device, like a browser (HTTP cache, localStorage) or mobile app using local memory or on-device storage.<br>

But it can also mean caching within a client library For example, Redis clients cache cluster metadata like which nodes are in the cluster and which slots are assigned to them. That way, the client can route requests directly to the right node without querying the cluster on every operation.<br>

For user-facing caching, you have limited control from the backend. Data can go stale and invalidation is harder. The 'Strava app' keeps your run data on the disk while you are offline and syncs it later. A browser reusing a previously downloaded image from disk is also caching.

<pre>
Client (It has cache) <---> Application Servers <---> Databse
</pre>

### In-Process Caching
Most candiditaes, and engineers, overlook the fact that servers run on machines with a lot of memory. As hardware improves, this becomes increasingly true. You can use that memory to cache data directly inside the application process instead of always calling out to Redis or the database.<br>

The idea is simple: if your service keeps requesting the same small piece of data again and again, store them in a local cache inside the process. Reads from local memory are even faster than reads from Redis because they avoid any network call.<br>

This light-weight form of caching makes sense for small pieces of data that are requested frequently like:
- Configuration values
- Feature flags
- Small reference datasets
- Hot keys
- Rate limiting counters
- Precomputed values

<pre>

Client ----> Application Servers (With cache) ----> Database
</pre>

In-process caching is blazing fast, but it comes with obvious limitations. Each instance of your application has its own cache, so cached data is not shared across servers. If one instance updates or invalidates a cached value, the others will not know.

<pre>
Note: Use in-process caching for small, freqently accessed values that rarely change. It is great for speed but not a replacement for Redis. In system design interviews, mention this only as an <b>optimization layer</b> after you have already introduced an external cache.
</pre>

## Cache Architectures
Not all caching works the same way. How you read from and write to the cache changes performance, consistency, and complexity.<br>
These are the four core cache patterns you should know for system design interviews.

### Cache-Aside (Lazy Loading)
This is the most common caching pattern and the one you should default to in interviews.<br>
How it works:
1. Application checks the cache.
2. If the data is there, return it.
3. If not, fetch from the database, store it in the cache, and return it.<br>
Cache-aside only caches data when needed, which keeps the cache lean. The downside is that a cache miss cause extra latency.
<pre>
Very Very Important Note: <b> If you only remember one caching pattern for interviews, make it cache-aside.</b>
</pre>

### Write-Through Caching
With write-through caching, the application writes only to the cache. The cache then synchronously writes to the database before returning to the application. The write operation does not complete until both the cache and database are updated.<br>

In practice, this requires a cache implementation that supports write-through, like a caching library with a data store plugin. Where you write to the cache, the library handles calling your database write logic before acknowledging the write. Redis itself does not natively support write through, so you need application code or a framework to implement this pattern.<br>

The tradeoff is slower writes because the application must wait for both the cache update and the database write to complete. Write-through can also pollute cache with data that may never be read again.<br>

Write through still suffers from the dual-write problem. If the cache update succeeds but the database write fails, or vice-versa, the systems can end up inconsistent. You need retry logic, error handling, or eventually accept that perfect consistency is difficult without distributed transactions. <br>

In system design interviews, write-through is less common than cache-aside because it requires specialized caching infrastructure and still has consistency edge cases. <br>

Use this when <b>reads must always return fresh data</b> and your system can tolerate slightly slower writes.

### Write-Behind (Write-Back) Caching
With write-behind caching, the application writes only to the cache. The cache batches and writes the data to the database asynchronously in the background. <br>

This makes writes very fast, but introduces risk. If the cache crashes before flushing, you can lose data. This is best for workloads where occasional data loss is acceptable. <br>

Use this when <b>you need high write throughput</b> and <b> eventual consistency is acceptable.</b> Common in analytics and metrics pipelines.

### Read-Through Caching
With read-through caching, the cache acts as a smart proxy. Your application never talks to the database directly. On a cache miss, the cache itself fetches from the database, stores the data, and returns it. <br>

This is the read equivalent of write-through. In both patterns, the cache acts as an intermediary that handles database operations. Read-through manages reads, write-through manages writes. Systems often combine both patterns.<br>

This centralizes caching logic but adds complexity and usually requires a specialized caching library or service. It is less common in practice than cache-aside. <br>

CDNs are a form of read-through cache. When a CDN gets a cache miss, it fetches from your origin server, caches the result, and returns it. But for application-level caching with Redis, cache-aside is far more common. <br>

Generally speaking, there are very few reasons to propose this pattern in system design interviews unless you're discussing CDNs or similar infrastructure.

## Cache Eviction Policies:
Caches have limited memory, so they need a stratergy for deciding which entries to remove when full. These stratergies are called cache eviction policies.

### LRU (Least Recently Used)
LRU evicts the item that has not been accessed for the longest time. It tracks access order using a linked list or ring buffer so the least recently used item can be removed in constant time.<br>

It is the default in many systems because it adapts well to mos workloads where recently used data is likely to be used agin.

### LFU (Least Frequently Used)
LFU evicts the item that has been accessed the least. It maintains a counter for each key and removes the one with the lowest frequency. Some implementations use approximate LFU to avoid the cost of precise frequency tracking. <br>

This works well when certain keys are consistently popular over time, like trending videos or top playlists.

### FIFO (First In First Out)
FIFO evicts the oldest item in the cache based only on insertion time. It can be implemented with a simple queue, but it ignores usage patterns. <br>

Because it may evict items that are still hot, it is rarely used in real systems beyond simple caching layers.

### TTL (Time To Live)
TTL is not an eviction policy by itself. Instead, it sets an expiration time for each key and removes entries that are too old. It is often combined with LRU or LFU to balance freshenss and memory usage. <br>

TTL is a must havve when data must eventually refresh, like API responses or sessions tokens.

## Common Cache Problems
Caching makes system faster, but it also introduces new failure modes. These problems show up in real systems at scale, and interviewers often use them to test whether you understand the trade-offs of caching, not just the benefits. If you bring up caching in an interview, you should also show that you can handle these edge cases.

### Cache Stampede (Thundering Herd)
A cache stampede happpens when a popular cache entry expires and many requests try to rebuild it at the same time. There is a brief window, even if only a second, where every request misses the cache and goes straight to the database. Instead of one query, you suddenly have hundreds or thousands, which can overload the database.<br>

For example, imagine your system caches the homepage feed with a TTL of 60 seconds. When the cache expires at exactly 12:01:00, every request at that moment misses the cache queries the database. If traffic is high, this spike can overwhelm the database and cause cascading failures.
<br>

How to handle it:
- <b> Request coalescing (single fault):</b> Allow only one request to rebuild the cache while others wait for the result. This is the most effective solution.
- <b> Cache warming: </b> Refresh popular keys proactively before they expire. This only helps when using TTL-based expiration. If you invalidate cache on writes instead, warming does not prevent stampedes.