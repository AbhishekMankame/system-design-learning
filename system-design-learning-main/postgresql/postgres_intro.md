# PostgresSQL

## Introduction
PostgreSQL (often called Postgres) is an open-source, object-relational database management system (ORDBMS). It's known for:
- ACID compilance (Atomicity, Consistency, Isolation, Durability)
- Extensibility (custom functions, types, operators)
- Advanced SQL features (window functions, CTEs, JSON support)
- Strong community support and enterprise-level reliability<br>
Use cases:
- Web applications (e.g., Django, Rails, Node.js apps)
- Analytics and OLAP workloads
- Geospatial applications (PostGIS)<br>
Key features:
- MVCC (Multi-Version Concurrency Control)
- JSON/JSONB storage for semi-structured data
- Full-text search
- Paritioning, indexing, and parallel query execution

## PostgreSQL Architecture
Understanding architecture is crucial for interviews and repo documentation. PostgreSQL is a client-server system:
### Process Architecture
- Postmaster: Main server process managing connections.
- Backend processes: One per client connection.
- Auxilliary processes:
    - Autovaccum: Cleans up dead tuples.
    - Checkpointer: Writes dirty pages to disk.
    - WAL writer: Handles Write-Ahed Logging.

### Storage Architecture
- Tablespaces: Logical storage locations.
- Data Files: Store tables, indexes, and transaction logs.
- WAL (Write-Ahead Log): Ensures durability (crash recovery)

### MVCC (Multi-Version Concurrency Control)
- Each transaction sees a snapshot of the database.
- Writers don't block readers.
- Dead tuples are cleaned up by VACCUM.