# Sharding
Your app is taking off. Traffic is growing, users are signing up, and your database keeps getting bigger. At first you solve this by upgrading to a larger database instance with more CPU, memory and storage. That works for a while.<br>
But eventually you hit the ceiling of what a single machine can handle. Queries slow down, writes become a bottle neck, and storage approaches the limit. Even powerful cloud databases like Amazon Aurora max out around 256TB.<br>
When a single database can't keep up anymore, you have only one real option:<br>
<b>Split your data across multiple machines.</b> This is called sharding. While it is necessity at scale, it also introduces new challenges. 
<pre>
People often use the words "partitioning" and "sharding" to mean the same thing. Technically they are slightly different. Partitioning usually refers to splitting data within a single database instance, often by table ranges or hash partitions. Sharding means splitting data across multiple machines. In practice most engineers use the terms loosely, so do not get hubg up on the wording. Just be clear about whether your data lives on one machine or many.
</pre>

## First, what is Partitioning?
Partitioning means splitting a large table into smaller pieces inside a single database instance. It does not add more machines. Instead it organizes data so the database can work more efficiently.<br>

Consider an orders table with 500 million rows and 2 TB of data. A query for last month's order has to scan the entire table. Indexes become huge and slow to maintain while routing operations like vacuuming, analyzing, or rebuilding indexes can lock the whole table and impact performance.<br>

Partitioning solves this problem by breaking that large table into smaller partitions. The data does not move off the machine. It is simply divided into logical pieces the database can manage seperately. Now a query for last month's orders only scans the relevant partition instead of the full table.<br>

There are two common types of partitioning:
1. Horizontal Partitioning: Split rows across partitions. For example, one partition per year of orders. Same columns, fewer rows per partition.
2. Vertical Partitioning: Split columns across partitions. For example, keep frequently accessed columns in one partition and large or rarely used columns in another. Same rows, fewer columns per partition.

## What is Sharding?
Sharding is horizontal partitioning across multiple machines. Each shard holds a subset of the data, and together the shards make up the full dataset. Unlike partitioning, which stays within a single database instance, sharding spreads the load across multiple independent databases.

## How to shard your data?
When you decide to shard, you need to make two decisions that work together:
1. What to shard by: The field or column you use to split the data. It defines how the data is grouped.
2. How to distribute it: The rule for assigning those groups to shards. It defines how the data is distributed across machines.