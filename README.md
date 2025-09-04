# system-design-learning
Welcome to my little corner of the internet where I try to make sense of all things system design! This repo will be packed with notes, sketches, and some code snippets to help untangle the mysteries of building big, scalable and reliable systems without losing your mind.

## What's inside? (More precisely what will be inside)
- Handy notes that won't put you to sleep
- Architecture diagrams (hopefully)
- Code snippets to get your hand dirty
- Tips and tricks for making systems that don't freak out under pressure

This is a work-in-progress, so expect it to grow and evolve-kind of like a system under constant load!!!


### Key concepts of HLD:

- System: A system is a collection of components working together to perform a specific function.
For example Facebook is a system that lets people connect and share.
- Components: A component is a smaller part of the system that has a specific responsibility
 - A database that stores user data
 - An API server that handles user requests
 - A frontend app that show the UI
- Architecture: Architecture is the overall structure and organization of the system, showing how components interact with each other
- Load balancer: A load balancer is like a traffic cop that directs incoming requests evenly across multiple servers. So no single server gets overwhelmed.
- API (Application Programming Interface): An API is a set of rules that allows different parts of a system (or different systems) to communicate with each other. Think on it as a waiter taking orders between a customer and the kitchen.
- Database: A database is a place where the system stores data permanently, types include:
    - SQL database: Stores data in tables
    - No SQL: Stores unstructured data
- Client: The consumer of your system (cound be a web app, mobile app, or anothe service)
- Server: A backend component that processes data or stores information