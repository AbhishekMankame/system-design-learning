# SDE-2 System Design interivew guide

## 1.What Google Expects at SDE-2 (Reality Check)
For SDE-2, Google is not expecting:
- Huge enterprise architectures
- Memorized buzzwords
- Production-level scaling math
<br>

They do expect:
- Clear problem understanding
- Logical decomposition
- Trade-off discussion
- Basic knowledge of common components
<br>

Think:
<pre>"Can thi person design a clean, reasonable system and explain decisions?"</pre>

## Core System Design Concepts (Minimum You Need)
You should be comfortable with these 10 things:
- Fundamentals
1. Client-Server model 
2. APIs (REST, gRPC - basics)
3. Databases
    - SQL vs NoSQL
4. High-level scalability
    - Load, latency, throughput

- Building Blocks
5. Load Balancer (why it exists)
6. Caching (Redis/in-memory-concepts)
7. Database sharding (what & why)
8. Replication (read vs write replicas)
9. Queues (for async work)
10. Consistency vs Availability (basic CAP idea)

<br>Note: You don't need deep theory. Just when and why.