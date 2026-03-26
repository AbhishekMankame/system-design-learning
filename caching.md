## Caching

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
Client ----> Application Servers ---- 1. Check cache ----> Cache
                                   |
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