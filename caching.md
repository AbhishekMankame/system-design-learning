## Caching

In system design interviews, caching comes up almost everytime you need to handle high read traffic. Your database becomes bottleneck, latency starts creeping up, and the interviewer is waiting for you to say the word: cache.<br>

Reading a user profile from Postgres may take 50 milliseconds, but reading from an in-memory cache like Redis takes just 1 millisecond. That's a 50x improvement in latency. Databases store data on disk, and every query pays the cost of disk accecss. Memory sits just closer to the CPU and avoids that entirely.<br>

Caches are essential for scalable systems. They reduce load on the database and cut latency dramatically. But they also create new challenges around invalidation and failure handling.<br>

This breakdown covers the basics of caching, when and where to use it, common pitfalls, and how to talk about caching clearly in interviews.

