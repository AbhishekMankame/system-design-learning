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