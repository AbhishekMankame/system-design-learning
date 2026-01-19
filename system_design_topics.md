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