## System Design - Topics

### 1 Foundations
### 1.1 What is a Distributed System
A distributed system is a collection of independent machines that work together as a single system. These machines communicate over a network and coordinate to provide scalability, fault tolerance, and high availability. In system design interviews, almost every problems assumes a distributed system because a single machine cannot handle millions of users or requests reliably.<br>
<pre>Notebook note: One system, many machines, netwokr communication, partial failures.</pre>

### 1.2 Client-Server Architecutre
In client-server architecture, clients (mobile/web apps) send requests to servers, which process the request and return a response. This separation allows servers to scale independently of clients. Almost all modern systems - from Google Search to Instagram use some form of client-server model.
<pre> Draw: Client --> Server --> Response</pre>

### 1.3 APIs (REST/HTTP Basics)
APIs define how clients communicate with servers. REST APIs typically use HTTP methods like GET, POST, PUT and DELETE. Understanding APIs is important because system design interviews often ask how services communicate with each other.

<pre> Interview relevance: You must explain how data flows, not just where it is stored </pre>

### 2 Networking & Traffic Handling
### 2.1 DNS (Domain Name System)
DNS converts human-readable domain names into IP addresses. When a user types "google.com", DNS helps locate the correct server. DNS is a critical entry point in large-scale systems and is often the first step in request routing.
<pre> Remember DNS = Internet's phonebook</pre>

### 2.2 Load Balancers
Load balancers distribute incoming traffic across multiple servers to prevent overload and improve availability. Without load balancers, one server could become a bottleneck or single point of failure.<br>
Common stratergies include round-robin, least connections, and consistent hashing.
<pre> Interview phrase: "I'll place a load balancer in front my application servers."</pre>

### 3 Storage Systems 
### 3.1 Relational Databases (SQL)
Relational Databases store data in tables with fixed schemas and support ACID transcations. They are best suited for systems requiring strong consistency, complex queries, and relationships between data.<br>
Examples: MySQL, PostgreSQL
<pre> Use when: Transactions + strong consistency are required </pre>

### 3.2 NoSQL Databases
NoSQL databases are designed for scalability and high availability. They often sacrifice strict consistency for performance and scale. They are commonly used in large-scale systems with massive data.<br>
They include:
- Key-Value stores
- Document stores
- Column-family stores
<pre> Use when: Huge scale + simple queries </pre>

### 3.3 Object Storage
Object storage is used for large binary files like images, videos, and documents. Instead of storing files in a database, systems store them in object storage and save references in the DB.<br>
Examples: S3-like systems, GCS
<pre> Interview tip: Never store large files directly in DB </pre>

### 4 Caching
### 4.1 Why Caching is Needed
Caching stores frequently accessed data in fast storage to reduce latency and database load. Without caching, databases become bottlenecks under high read traffic.<br>
<pre> One-liner: Cache = performance booster </pre>

### 4.2 Cache Stratergies
Common stratergies include read-through, write-through, and cache-aside. Understanding these helps you justify how data stays fresh and consistent.
<pre> Interviewers love: Cache invaliation discussion</pre>

### 5 Scalability Concepts
### 5.1 Vertical vs Horizontal Scaling
Vertical scaling means adding more power to a single machine. Horizontal scaling means adding more machines. Modern systems prefer horizontal scaling because it avoids hard limits.
<pre> Remember: Scale out, not up</pre>

### 5.2 Database Replication
Replication creates copies of data to improve read scalability and fault tolerance. Usually, one primary handles writes, and replicas handle reads.
<pre> Better reads vs replication lag </pre>

### 5.3 Sharding (Partitioning)
Sharing splits data across multiple databases. It is essential for massive scale but introducecs complexity in queries and transactions. <br>
<pre> Golden rule: Shard by something evenly distributed (user_id)</pre>

### 6 Consistency & Reliability
### 6.1 CAP Theorm
CAP theorem states that a distributed system can only guarantee two of Consistency, Availablity, and Partition tolerance at a time. Understanding CAP helps you justify design choices.
<pre> Interview gold: Explain which two you choose and why </pre>

### 6.2 Strong vs Eventual Consistency
Strong consistency ensures users always see the latest data. Eventual consistency allows temporary inconsistency for better performance and availability.
<pre> Example: Social media likes --> eventual consistency </pre>

### 7 Asynchronous Processing
### 7.1 Message Queues
Queues decouple services and help handle spikes in traffic. They allow background processing and improve system resilience.<br>
Example: Kafka-like systems, RabbitMQ-like systems
<pre> Interview phrase: "I'll introduce a queue to smooth traffic spikes." </pre>

### 7.2 Background Workers
Workers process tasks asynchronously, such as sending emails or processing videos. This prevents long-running tasks from blocking user requests.

### 8 Reliabilty & Fault Tolerance
### 8.1 Redundancy
Running multiple instances of services ensures the system remains available even if one instance fails.

### 8.2 Timeouts, Retries & Circuit Breakers
These mechanisms prevent cascading failures when downstream services are slow or unavailable.
<pre> Senior-level thinking: Failure is normal, design for it. </pre>

### 9 Security Basics
### 9.1 Authentication & Authorization
Authentication verifies who the user is. Authorization checks what the user is allowed to do.

### 9.2 Rate Limiting
Rate limiting protects systems from abuse and traffic spikes.
<pre> Interview line: "I'll add rate limiting at the API gateway. </pre>

### 10 Observability & Maintenance
### 10.1 Logging
Logs help debug issues and analyze behavior.

### 10.2 Monitoring & Alerts
Monitoring tracks system health and alerts engineers when something goes wrong.