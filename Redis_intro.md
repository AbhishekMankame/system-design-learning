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