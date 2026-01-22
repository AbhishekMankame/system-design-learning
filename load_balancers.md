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