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
3. The result tells us which database should store that event.<br>

In code, it looks like this:
<pre>
database_id = hash(event_id)%number_of_databases
</pre>

For a concrete examples with 3 databases:
<pre>
Event #1234 -> hash(1234)%3=1 -> Database 1
Event #5678 -> hash(5678)%3=0 -> Database 0
Event #9012 -> hash(9012)%3=2 -> Database 2
</pre>