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