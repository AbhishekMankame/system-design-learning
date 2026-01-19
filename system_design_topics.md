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