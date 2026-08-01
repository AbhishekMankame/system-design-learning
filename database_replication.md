## Database Replication
Database replication is a process where data from one database server (the master or primary) is copied to one or more other database servers (the replica or secondary).<br>
This allows for high availability, load balancing and backup recovery. There are several ways to implement replication, depending on the database system (like MySQL, PostgreSQL, etc.) and your use case (synchronous vs asynchronous, master-slave, master-master).

### Basic Concepts of Database Replication
1. Master (Primary) Server: The server where the original data is stored. All write operations occur here.
2. Slave (Replica) Server: One or more servers that replicate the data from the master. These can handle read operations to distribute load, but in a typical setup, they don't handle writes.
3. Replication Types:
- Synchronous Replication: Data is written to both the master and the replica at the same time. It is slow but provides a guarantee that data is available on all servers.
- Asynchronous Replication: Data is written to the master first, and the replica is updated after the fact. This is faster but has a small risk of data inconsistency during network failures or crashes.