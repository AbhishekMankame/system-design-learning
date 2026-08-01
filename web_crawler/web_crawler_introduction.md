## Web Crawler

### What is a Web Crawler?
A web crawler (spider/bot) is a program that:
- Starts from a set of seed URLs
- Downloads web pages
- Extracts links from those pages
- Adds new links to a queue
- Repeats the process

#### Real-world examples:
- Google uses crawlers to build search index.
- Bing crawler indexes web pages.
- Internet Archive crawls pages for archiving.

### High-Level System Design
<b>Functional Requirements </b>

- Input: Seed URLs
- Download pages
- Extract links
- Avoid duplicate crawling
- Respect robots.txt
- Store crawled pages
- Be scalable and fault tolerant <br>

<b> Non-Functional Requirements</b>

- Scalable to billions of URLs
- Politeness (Don't overload servers)
- High throughput
- Fault tolerance
- Distributed

### High-Level Architecture

            +----------------+
            |   Seed URLs    |
            +--------+-------+
                     |
                     v
            +----------------+
            |   URL Frontier |
            | (Queue System) |
            +--------+-------+
                     |
         +-----------+-----------+
         |                       |
         v                       v
  +-------------+        +-------------+
  |  Crawler    |        |  Crawler    |
  |  Worker 1   |        |  Worker N   |
  +------+------+        +------+------+
         |                       |
         v                       v
  +-------------------------------------+
  |     Page Parser & Link Extractor    |
  +-------------------------------------+
                     |
                     v
         +--------------------------+
         |  Duplicate URL Checker   |
         | (Bloom Filter / DB)      |
         +--------------------------+
                     |
                     v
         +--------------------------+
         | Storage (DB / S3 / HDFS) |
         +--------------------------+

### Core Components Explained

1. URL Frontier (Queue) - Stores URLs to crawl<br>
Can use:
- Kafka
- RabbitMQ
- Redis Queue<br>

Must support:
- Priority
- Domain-based throttling
- Deduplication

2. Crawler Workers<br>
Each worker:
1. Takes URL from queue
2. Downloads page
3. Parses content
4. Extracts links
5. Adds new URLs to queue

3. Duplicate URL Detection<br>
Without this, crawlers loops infinitely.<br>
Solutions:
- Hashset (small scale)
- Redis
- Bloom Filter (large scale)
- Distributed key-value store

4. Politeness & Rate Limiting<br>
We must:
- Respect robots.txt
- Avoid hitting same domain too fast
- Add delay per domain

5. Storage<br>
Options:
- Store raw HTML
- Store parsed data
- Store metadata <br>

Use:
- S3
- HDFS
- Cassandra
- Elasticsearch

5. Database Schema Example:<br>
URLs Table
| Field | Type |
| ----- | ---- |
| id | bigint |
| url | text |
| status | enum |
| crawled_at | timestamp |
| content_hash | string |

6. Scaling Stratergy<br>
For Google-scale crawling:
- Distributed Crawler
       - Use consistent hashing to assign domains
       - Partition by hostname
       - Use multiple machines
       - Central coordinator

- Architecture Upgrade:
       - Distributed queue (Kafka)
       - URL dedupe service
       - Worker autoscaling
       - Monitor system
       - Checkpointing

### Big Picture:
Seed URLs --> URL Frontier --> Crawler Workers --> Throttling --> Dedupe Service --> Storage (S3/HDFS) -> Metadata DB (Cassandra) --> Search Index (Elasticsearch)