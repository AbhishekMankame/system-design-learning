# Sharding
Your app is taking off. Traffic is growing, users are signing up, and your database keeps getting bigger. At first you solve this by upgrading to a larger database instance with more CPU, memory and storage. That works for a while.<br>
But eventually you hit the ceiling of what a single machine can handle. Queries slow down, writes become a bottle neck, and storage approaches the limit. Even powerful cloud databases like Amazon Aurora max out around 256TB.<br>
When a single database can't keep up anymore, you have only one real option:<br>
<b>Split your data across multiple machines.</b> This is called sharding. While it is necessity at scale, it also introduces new challenges. 
<pre>
People often use the words "partitioning" and "sharding" to mean the same thing. Technically they are slightly different. Partitioning usually refers to splitting data within a single database instance, often by table ranges or hash partitions. Sharding means splitting data across multiple machines. In practice most engineers use the terms loosely, so do not get hubg up on the wording. Just be clear about whether your data lives on one machine or many.
</pre>