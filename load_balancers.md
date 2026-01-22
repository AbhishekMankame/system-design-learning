## Load Balancers

A load balancer is a system component that sits between clients (users) and backend servers and distributes incoming traffic across multiple servers. Instead of all requests hitting a single server (which would quickly fail or become slow), the load balancer ensures that requests are spread efficiently, improving performance, scalability, reliability and availability.<br>
In system design terms, the load balancer is often the first point of contact for external traffic and plays a critical role in preventing single points of failure.

### Why Load Balancers are needed?
Without a load balancer:
- One server handles all traffic
- Server overload causes slow response or crashes
- No easy way to scale horizontally
- Downtime if the server fails

Without a load balancer:
- Traffic is evenly distributed
- System scales by adding/removing servers
- Faulty servers can be isolated automatically
- Zero-downtime deployments become possible<br>
In large-scale systems (Netflix, Amazon, Google), load balancing is non-negotiable.

### Where Load Balancers sit in architecture
A typical request flow looks like:
<pre>
Client -> DNS -> Load Balancer -> Backend Servers -> Database
</pre>
The client never directly talks to backend servers. The load balancer:
- Accepts the request
- Chooses a healthy backend server
- Forward the request
- Return the response<br>
In complex systems, multiple load balancers may exist:
- DNS Load Balancer
- Edge Load Balancer
- Internal Service Load Balancer

### Core responsibilities of a Load Balancer
1. Traffic Distribution: Distributes requests among backend servers using specific algorithms.
2. Health Checks: Continuously monitors backend servers using:
- HTTP endpoints
- TCP checks
- Heartbeats<br>
Unhealthy servers are removed from rotation automatically.
3. Fault tolerance: If a server crashes:
- Requests are rerouted instantly
- Users usually don't notice
4. Scalability: Adding more servers increases capacity linearly in most cases.
5. Security:
- SSL/TLS termination
- DDoS protection
- Rate limiting
- IP filtering

### Types of Load Balancers (By Layer)
1. Layer 4 Load Balancer (Transport Layer)<br>
Operates at TCP/UDP level
- Routes based on IP + Port
- Does not inspect request content
- Extremely fast and lightweight<br>
Example: AWS Network Load Balancer<br>
Use cases:
- High throughput systems
- Real-time apps (gaming, streaming)<br>
Limitation:
- Cannot route based on URL, headers, cookies

2. Layer 7 Load Balancer (Application Layer)<br>
Operates at HTTP/HTTPS level
- Understands request content
- Can route based on:
    - URL path
    - Headers
    - Cookies
    - HTTP method
<br> Example: NGINX, HAProxy, AWS ALB<br>

Use cases:
- Microservices
- APIs
- Web applications<br>
Trade-off:
- Slightly slower than L4
- Much more flexible

### Types of Load Balancers (By Implementation)
1. Hardware Load Balancers:
- Dedicated physical devices
- Very fast
- Very expensive
- Used in legacy enterprise systems

2. Software Load Balancers
- Run on standard servers
- Highly configurable
- Cheaper and flexible<br>

Examples:
- NGINX
- HAProxy
- Envoy
- Traefik

3. Cloud Load Balancers
- Managed by cloud providers
- Auto-scaling
- Built-in health checks<br>

Examples:
- AWS ELB/ALB/NLB
- GCP Load Balancer
- Azure Load Balancer

## Load Balancing Algorithms
1. Round Robin: Requests are sent to servers in sequential order.
<pre>
Request 1 -> Server A
Request 2 -> Server B
Request 3 -> Server C
</pre>
Pros:
- Simple
- Even distribution<br>

Cons:
- Assmes all servers are equal
- Ignores server load<br>

Best for
- Homogenous servers
- Stateless applications

2. Weighted Round Robin: Each server is assigned a weight::
<pre>
Server A (weight 3)
Server B (weight 1)
</pre>
Server A gets 3x traffic compared to B<br>
Use case: Servers with different capacities

3. Least Connections: Traffic goes to the server with the fewest active connections.<pre>
Pros
- Good for long-lived connections
- Handles uneven load<br>
Cons: Slightly more overhead <br>
Best for
- WebSocket
- Streaming
- Chat systems

4. Weighted Least Connections: Like least connection, but considers server capacity. <br>
Common in production systems where machines differ.

5. Least Response Time: Routes requests to the server with:
- Lowest response time
- Fewer active connections<br>
Pros: Optimizes user latency<br>
Cons:
- More complex
- Requires monitoring

6. IP Hash: Client IP is hashed to select a server.
<pre>
Same IP -> Same server
</pre>
Pros: Session persistence without cookies<br>
Cons:
- Uneven distribution
- Problems with NAT users<br>
Best for: Session-based apps (when sticky sessions are needed)

7. Consistent Hashing:
- Minimizes remapping when servers are added/removed
- Used heavily in caches and CDNs<br>
Benefits
- Scalability
- Stability<br>
Used in
- Distributed caches (Redis, Memcached)
- Some advanced load balancers

### Sticky Sessions (Session Persistence)
Sometimes users must always hit the same server.<br>
Techniques
- Cookies
- IP hashing
- Custom headers<br>
Problem
- Reduces load balancing effectiveness
- Makes scaling harder<br>
Better approach: Store session data in shared storage (Redis, DB)

### Health checks (critical topic)
Load balancers continuously check:
- Is the server alive?
- Is it responding correctly?<br>

Types
- Liveness check
- Readiness check<br>

Unhealthy servers:
- Stop receiving traffic
- Rejoin automatically when healthy

### Load balancers as a single point of failure
Ironically, a load balanecer itself can fail.<br>
Solutions:
- Multiple load balancers
- Active-Passive or Active-Active setup
- DNS-based failover
- Anycast IPs<br>
Modern systems never rely on a single LB instance

### Global load balancing
Used when users are worldwide<br>
Techniques:
- DNS-based routing
- Geo-routing
- Latency-based routing<br>
Example
- User in Europe --> EU servers
- User in India --> Asia servers

### Reak=l-World Example (System Design Style)
Example: E-commerce website
- DNS routes to cloud DB
- LB distributes traffic to app servers
- Health checks remove bad instances
- Weighted least connections handles uneven traffic
- SSL terminated at LB
- Auto-scaling adds servers during scale<br>
Result:
- High availability
- Low latency
- Fault tolerance

### Summary:
A load balancer is the backbone of scalable systems. It:
- Improves performance
- Prevent failures
- Enables horizontal scaling
- Acts as traffic manager