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