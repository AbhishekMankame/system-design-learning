## What is System Design?
At its core, system design is about making decisions that affect the overall structure of a system, keeping in mind how different parts of the system will interact with each other.
<br>The goal is to build a solution that meets the business requirements while being efficient, scalable, and easy to maintain.

### Key Concepts in System Design
1. Scalability: How well the system can handle an increasing number of users, requests, or data.
2. Reliability: How dependable the system is in terms of uptime and consistency.
3. Fault Tolerance: The system's ability to continue functioning correctly even if parts of it fail.
4. Maintainability: How easy it is to update and modify the system.
5. Latency: The time delay before a transfer of data begins following an instruction for its transfer.
6. Throughput: The amount of data processed by the system in a given period.
7. Load Balancing: Distributing incoming network traffic across multiple servers to ensure no single server becomes a bottleneck.
8. Availability: The percentage of time the system remains operational and accessible.
- High availability systems aim for minimal downtime.
- Often achieved using redundancy and replication.
9. Consistency: Ensures that all users see the same data at the same time after an update.
- Strong consistency
- Eventual consistency
10. CAP Theorem: States that a distributed system can only guarantee two of the following three:
- Consistency
- Availability
- Partition Tolerance
11. Caching: Storing frequently accessed data in memory to reduce latency and database load.
- In-memory cache (Redis, Memcached)
- CDN caching
12. Database Design: Choosing the right database type and schema for the use case.
- SQL vs NoSQL
- Indexing and normalization
13. Data Partitioning (Sharding): Splitting large datasets into smaller, more manageable pieces across multiple databases or servers.
- Horizontal partitioning
- Vertical partitioning
14. Replication: Maintaining multiple copies of data across different nodes to improve availability and fault tolerance.
- Leader-follower replication
- Multi-leader replication
15. Security: Protecting the system against unauthorized access and attacks.
- Authentication and authorization
- Encryption (data at rest and in transit)
16. Monitoring and Logging: Tracking system performance and behavior to detect issues early.
- Metrics (CPU, memory, latency)
- Centralized logging
