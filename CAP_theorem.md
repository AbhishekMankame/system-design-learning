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