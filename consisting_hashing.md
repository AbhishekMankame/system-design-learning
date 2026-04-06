# Consistent Hashing
Imagine you're designing a ticketing system like TicketMaster. Initially, your system is simple:
- One database storing all event data
- Client making requests to fetch event information
- Everything works smoothly at first<br>

But success brings challenges. As your platform grows and hosts more events, a single database can longer handle the load. You need to distribute your data across multiple databases - a process called <b>sharding.</b><br>

The question we need to answer is: <b>How do we know which events to store on which database instance?</b>

## First Attempt: Simple Modulo Hashing
The most straightforward approach to distribute data across multiple databases in modulo hashing.
1. First, we take the event ID and run it through a hash function, which converts it into a number.
2. Then, we take the number and perform the modulo operation (%) with the number of databases