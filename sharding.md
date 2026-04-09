# Sharding
Your app is taking off. Traffic is growing, users are signing up, and your database keeps getting bigger. At first you solve this by upgrading to a larger database instance with more CPU, memory and storage. That works for a while.<br>
But eventually you hit the ceiling of what a single machine can handle. Queries slow down, writes become a bottle neck, and storage approaches the limit. Even powerful cloud databases like Amazon Aurora max out around 256TB.<br>
When a single database can't keep up anymore, you have only one real option:<br>
<b>Split your data across multiple machines.</b> This is called sharding. While it is necessity at scale, it also introduces new challenges. 