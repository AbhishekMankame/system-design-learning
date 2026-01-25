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