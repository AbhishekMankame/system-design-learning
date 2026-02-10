## Redis (Remote Dictionary Server)

### What is Redis?
- Redis is an in-memory database --> Data is stored on computer's memory.
- Usage of Redis --> Often used as <b>Cache</b> to improve performance.
<pre> Client/Server <--> Cache <--> Database </pre>

- Redis is a fully-fledge <b>primary database</b>
<pre> Client/Server <--> Fast DB </pre>

- Persist multiple data formats
    - RedisSearch
    - RedisGraph
    - RedisBloom
    - RedisJSON
    - RedisAI
    - Redis TimeSeries

- In large-scale systems Redis is typically placed between application servers and persistent databases to reduce database load and improve response time.
- From an internal design perspective, Redis is single-threaded for command execution, which is a deliberate architectural choice. This design avoids race conditions and eliminates the need for complex locking mechanism, ensuring that all operations are atomic.
- Despite being single-threaded, Redis achieves extrememly high performance using non-blocking I/O and event-driven architecture (epoll/kqueue).
- Most Redis operations have O(1) or O(log n) time complexity. To prevent unbounded memory growth, Redis supports TTL (time-to-leave) on keys and configurable eviction policies such as LRU (Least Recently Used) and LFU (Least Frequently Used). These features are critical in cache-heavy, high-traffic systems.

### Challenges of multiple data services
- Data services need to be deployed and maintained
- Know-How needed for each service
- Different Scaling and Infratructure Requirements
- Due to multiple microservices connected or talking to each service and seperate logic and due to more number of services there will be high latency.
- Here each network hop will create latency.

- Having Redis as the database, it will allow us to store different data structures (different types of data).
- No seperate Cache needed

### How Redis works?
- Redis Core: It is a key-value store, that supports storing multiple types of data, modules for different data types which applications needs for different purposes.
- Examples: RedisSearch, RedisGraph, Redis TimeSeries, RedisJSON
- If we are using Redis as primary database we need additional Cache (Out-of-the-Box Cache).
- As an inmemory database Redis is super fast and performant.
- Redis also makes running application test faster as well
- Schemaless

### Data Persistance and Durability
Redis has multiple mechanisms for persisting the data and keeping the data safe.
- Snapshotting (RBD)
    - Produces single-file point-in-time snapshots of your dataset
    - Configure based on time or number of writes passed
    - Stored on disk
    - Great for backups and disaster recovery
    - You may lost the latest minute of data

- Append Only File (AOF)
    - Logs every write operation continuously
    - When restarting Redis, it will re-play the AOF to rebuild the state
    - Much more durable, but can be slower then RDB

- Best: Use both persistence options
    - Redis actually plans to unify AOF and RDB
    - AOF: Persisting all operations one after the other
    - RDB: Regular snapshots for DB backups
    - Even if Redis database itself or the servers with underlying infrastructure were Redis is running fails, we still have all our database safe, and we can easily recreate and restart the database with all the data.<br>

### Where are these persistence files stored?
- Always seperate the persistent storage from Data server.
<pre> Server, where DB service runs     Server, where your data is backed up </pre>

### Storing data in memory expensive?
- We need more servers compared to disk-based databases, means we need more servers compared to database that stores data on disk, simply because memory in limited in size, that's the trade-off between cost and performance.
- Redis actually have a way to optimize this, that is called Redis on Flash (which is a part of Redis Enterprise)
- Redis on Flash extends the RAM to the flash drive or SSD, where frequenty used values (hot values) are stored in RAM and infrequently used values (warm values) are stored on SSD.
- So for Redis, it is more RAM-like (latency & performance) on the server.
- Redis can use more of the underlying infrastructure resources.
- Lower infrastruture costs

### How to scale a Redis Database?
#### How to increase the capacity?
1. Clustering
- We have primary (or master) redis instance for reading and writing
- And we can have multiple replicas for reading
- This way we can scale Redis to handle more requests and increase the high availability of database as if master fails, then one of the replicas can take over and then your database can continue functioning without any issues.
- Replicas hold complete copies of Primary instance's data
- Using one Server for your Redis cluster
    - More replicas, the more memory space
    - Downtime when server crashes
- Distribute the replicas among the nodes/servers, that means master instance will be on one node and replicas will be on different nodes.
- Here, if our dataset grows to large to fit in the memory on a single server

### Sharding
Here in sharding we take our complete datasets and divide it into smaller chunks or subsets of data were each shard is responsible for it's own subset of data.
- That means instead of having one master instance which handles all the write through the complete dataset, you can split it into 4 shards (any 'n' number of shards, 4 in this case for example) each of them responsible for reads and writes to a subset of the data and each shard also needs less memory capacity because they just have one-fourth of the data, this means you can distribute and run shards on smaller nodes and basically scale your cluster horizontally.
- If your dataset grows, you can re-shard it into smaller chunks and create more shards.

### Active-Active Geo Distribution
- Lower latency
- Disaster recovery
- Redis cluster can update data independently
- Once connection is re-established, they can sync up the changes.

### How does Redis resolve changes to the same dataset?
### How does Redis ensure data consistency?
- Redis Enterprise uses something called CRDT (Conflict-Free Replicated Data Types): This is used to resolve any conflicts at database level and without any data loss.
- Redis itself has the mechanism for merghing the changes which were made to the same dataset from multiples sources in a way that none of the data changes are lost, and any conflicts are properly resolved.
- For each datatype, it has its own data conflict resolution rule, the most optimal for that particular data type.
- All the parallel changes are intelligently resolved.

### Running Redis in Kubernetes
- Running Redis on Kubernetes platform is very interesting and common usecase.
- With open source Redis, you can deploy your replicated Redis as Helm Chart or K8s manifest files using the Replication and Scaling rules, setup and run a highly available Redis database.The only difference will be that the hosts where Redis will run will be Kubernetes pods instead of for example EC2 instances or any other physical or virtual servers.