## What is the CAP theorem?
CAP theorem, also called Brewer's theorem, is a fundamental concepts in distributed systems. It states that a distributed system can only guarantee at most two of the following three properties at the same time:
1. Consistency (C)
2. Availability (A)
3. Partition Tolerance (P)

### Consistency (C)
- Every read receives the most recent write or an error.
- In other words, all nodes in a distributed system see the same data at the same time.<br>
Example:
- Imagine a banking system. If Alice transfers $100 to Bob, consistency ensures that if you check Alice's account from any server immediately after, you see the updated balance.
- Strong consistency = data is always accurate across all nodes.

### Availability (A)
- Every request (read/write) receives a response (success or failure), without guarantee of the most recent write.
- The system remains operational even if some nodes fail.<br>
Example:
- If a user tries to read a profile and the system responds with something (maybe slightly outdated), that's availability. The system doesn't block the request even if some nodes are lagging.
- High availability = system never goes down for reads/writes

### Partition Tolerance (P)
- The system continues to operate even if there is a network partition (communication breakdown) between nodes.
- In distributed systems, network failures cannot be ignored, so partition tolerance is often a must.<br>
Example:
- A network split occurs between data centres. The system must continue to accept reads/writes in both partitions, even if the nodes cannot communicate with each other temporarily.
- Partition tolerance = system can handle network failures.

### The trade-off: Choose 2 out of 3
The CAP theorem says:
<pre>You cannot have all three: consistency, availability and partition tolerance simultaneously in a distributed system.</pre>
So, when designing systems, we pick two out of three:

| Combination | What it Mean | Use Cases |
| ----------- | ------------ | --------- |
| CA | Consistent & Available (no network partitions) | Single-datacenter systems: SQL DBs like MySQL when network is reliable |
| CP | Consistent & Partition Tolerant | Banking, financial systems where consistency is critical, even if some availability is sacrificed |
| AP | Avai;able & Parition Tolerant | Social media, DNS, caching systems where some stale data is acceptable |

### Why you can't have all three?
Imagine:
- Two database nodes: Node A and Node B.
- A network partition occurs between them.
- You write new data to Node A.<br>

Now:<br>
If Node B receives a read request, it must choose:
| Option | What It Does | What It Sacrifices |
| ------ | ------------ | ------------------ |
| Return old data | System stays available | Breaks Consistency |
| Refusen to respond | Preserves Consistency | Breaks Availability |

Therefore: During a partition, you must choose between Consistency and Availability.<br>
That's the CAP tradeoff.

### Important Clarifications
1. Partition Tolerance is Mandatory<br>
In real distributed system:
- You cannot choose "not P"
- Network failures will happen<br>
So the real tradeoff is:
<pre> During partition -> Choose C or A</pre>

2. CAP Only Applies During Partition<br>
If there is no network failure:
- You can have both consistency and availability<br>
CAP only becomes relevant when partition occurs.

3. Eventual Consistency<br>
Many AP system use: <b>Eventual Consistency</b>
- Data will become consistent over time.
- No guarantee of immediate consistency.<br>
This model powers:
- Social networks
- Large-scale cloud systems

### Real-World Example
- Online Banking (CP)
    - You transfer $100
    - System must ensure:
        - No double spending
        - No inconsistent balance
    - If network splits -> better to reject transaction than allow inconsistency

- Instagram Feed (AP)
    - If one server fails
    - You may see slightly old posts
    - But the app still loads
    - Here availability is more important than strict consistency