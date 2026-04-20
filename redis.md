# Redis
System designs can involve a dizzying array of different technologies, concepts and patterns, but one technology (arguably) stands above the rest in terms of its versatility: Redis. This versatility is important in an interview setting becaue it allows you to go deep. Instead of learning about dozens of different technologies. you can learn a few useful ones and learn them deeply, which magnifies the chances that you're able to get to the level your interviewer is expecting.<br>

Beyond versatility, Redis is great for its simplicity. Redis has a ton of features which resemble data structures you're probably used to from coding (hashes, sets, sorted sets, streams, etc) and which, given a few basics, are easy to reason about how they behave in a distributed system. While many databases involve a lot of magic (optimizers, query planners, etc), with only minor exceptions Redis has remained quite simple and good at what it does best: executing simple operations fast.

## Redis Basics
Redis is a self-described "data structure store" written in C. It's in-memory and single threaded making it very fast and easy to reason about.
<pre>
One important reason you might not want to use Redis is because you need durability. While there are some reasonable stratergies for (using Redis' Append-Only Fine (AOF)) to minimize data loss, you don't get the same guarantees you might get from e.g. a relational database about commits being written to disk. This is an intentional tradeoff made by the Redis team in favor of speed, but alternative implementations (e.g. AWS' MemoryDB) will compromise a bit on speed to give you disk-based durability. If you need it, it's there!
</pre>