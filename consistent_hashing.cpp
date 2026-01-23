// Consistent Hashing
/*
Consistent hashing is a technique to distribute keys across server such that:
- When a server is added or removed, only a small fraction of keys move
- Avoids massive rehashing (key%N problem)
- Used in distributed caches, databases, sharded systems

Key property: With 'N' servers, adding/removing one server only reassigns about '1/N' of the keys.

Why Google cares:
Interviewers expect you to understand:
- Load balancing
- Fault tolerance
- Scalability
- Real-world distributed systems (Bigtable, Spanner, GFS concepts)

## Core Idea (Hash Ring)
1. Hash values lie on a circular ring: [0, 2^32)
2. Both servers and keys are hashed onto the ring
3. A key goes to the first server clockwise

0 -- S1 -- K1 -- S2 -- K2 -- S3 -- 2^32

Virtual Nodes:
Without virtual nodes -> uneven load
Instead:
- Each physical server has multiple virtual nodes
- Each virtual node maps to the same server

Interview buzzword:
"Virtual nodes smooth load distribution."
*/

#include<bits/stdc++.h>
using namespace std;

uint32_t hashFn(const string& s) {
    return std::hash<string>{}(s);
}

// Consistent Hashing Class
class ConsistentHash {
private:
    map<uint32_t, string> ring;;;
    int virtualNodes;

public:
    ConsistentHash(int vNodes=3){
        virtualNodes = vNodes;
    }

    void addServer(const string& serverId) {
        for(int i=0;i<virtualNodes;i++){
            string vnode = serverId + "#" + to_string(i);
            uint32_t hash = hashFn(vnode);
            ring[hash] = serverId;;
        }
    }
}