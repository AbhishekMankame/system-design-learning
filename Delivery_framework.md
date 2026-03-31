# System Design Delivery Framework
The easiest way to sabotage your chances of getting an offer in your system design interview is to fail to deliver a working system. This is the most common reason that mid-level candidates fail these interviews and often manifests as the opaque "time management". This issue isn't (always) that you need to work twice as fast - many times you just need to focus on the right things. <br>

Here is the framework!
<pre>
Requirements --> Core Entities --> API or Interface --> Data Flow --> High-level Design --> Deep Dives

High-Level Design -- Primary Goal: Satisfy Functional Requirements --> Requirements

Deep Dives -- Primary Goal: Satisfy Non-functional Requirements --> Requirements
</pre>

## Requirements (~5 minutes)
The goal of the requirements section is to get a clear understanding of the system that you are being asked to design. To do this, we suggest you break your requirements into two sections.

1. Functional Requirements<br>
Functional requirements are your "Users/Clients should be able to..." statements. These are the core features of your system and should be the first thing you discuss with your interviewer. Oftentimes this is a back and forth with your interviewer. Ask targeted questions as if you were talking to a client, customer, or product manager ("does the system need to do X?", "what would happen if Y?") to arrive at a prioritized list of core features.<br>

For example, if you were designing a system like Twitter, you might have the following functional requirements:
- Users should be able to post tweets
- Users should be able to follow other users
- Users should be able to see tweets from users they follow<br>

A cache meanwhile might have requirements like:
- Clients should be able to insert items
- Clients should be able to set expirations
- Clients should be able to read items<br>

<pre>
Keep your requirements targeted! The main objective in the remainging part of the interview is to develop a system that meets the requirements you've identified -- so it's crucial to be stratergic in your prioritization. Many of these systems have hundreds of features, but it's your job to identify and prioritization. Many of these systems have hundreds of features, but it's your job to identify and prioritize the top 3. Having a long list of requirements will hurt you more than it will help you and many top FAANGs directly evaluate you on your ability to focus on what mattenrs.
</pre>

2. Non-functional Requirements<br>
Non-functional requirements are statements about the system qualitites that are important to your users. These can be phrased as "The system should be able to..." or "The system should be..." statements.<br>

For example, if you were designing a system like Twitter, you might have the following non-functional requirements:
- The system should be highly available, prioritizing availability over consistency.
- The system should be able to scale to support 100M+ DAU (Daily Active Users)
- The system should be low latency, rendering feeds in under 200ms
<pre>
It's important that non-functional requirements are put in the context of the system and, where possible, are quantified. For example, "the system should be low latency" is obvious and not very meaningful - nearly all systems should be low latency. "The system should have low latency search, < 500ms," is much more useful as it identifies the part of the system that most needs to be low latency and provides a target.
</pre>

Coming up with non-functional requirements can be challenging, especially if you're not familiar with the domain. Here is a checklikst of things to consider that might help you identify the most important non-functional requirements for your system. You'll want to identify the top 3-5 that are most relevant to your system.
1. CAP Theorem: Should your system prioritize consistency or availability? Note, partition tolerance is a given in distributed systems.
2. Environment Constraints: Are there any constraints on the environment in which your system will run? For example, are you running on a mobile device with limited battery life? Running on device with limited memory bandwidth (e.g., streaming video on 3G)?
3. Scalability: All systems need to scale, but does the system have unique scaling requirements? For example, does it have bursty traffic at a specific time of day? Are there events, like events, like holidays, that will cause a significant increase in traffic? Also consider the read vs write ratio here. Does your system need to scale reads or write more?
4. Latency: How quickly does the system need to respond to user requests? Specifically consider any requests that require meaningful computation. For example, low latency search when desinging Yelp.
5. Durability: How important is it that the data in your system is not lost? For example, a social network might be able to tolerate some data loss, but a banking system cannot.
6. Security: How secure does the system need to be? Consider data protection, access control, and compilance with regulations.
7. Fault Tolerance: How well does the system need to be? Consider data protection, access control, and compilance with regualtions.
8. Compilance: Are there legal or regulatory requirements the system needs to meet? Consider industry standards, data protection laws, and other regulations.