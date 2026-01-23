// Consistent Hashing
/*
Consistent hashing is a technique to distribute keys across server such that:
- When a server is added or removed, only a small fraction of keys move
- Avoids massive rehashing (key%N problem)
- Used in distributed caches, databases, sharded systems

Key property: With 'N' servers, adding/removing one server only reassigns about '1/N' of the keys.
*/