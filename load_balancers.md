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