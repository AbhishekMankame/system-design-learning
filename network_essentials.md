# Networking Essentials
Networking is a fundamental part of system design: you're nearly always going to be designing systems comprised of independent devices that communicate over a network. But the field of networking is vast and complex, and it's easy to get lost (this was one of the heaviest textbooks in school, gross).<br>

Here we we're going to cover the most important parts of networking that you'll need to know for your system design interviews.<br>

To do this, we will start with the fundamentals of how networks operate, then examine key protocols at different layers of the networking stack. For each concept we will cover its purpose, how it works, and when to apply it in your system designs.<br>

<pre>
Networking tends to be stronger focus in infrastructure and distributed system interviews. For full-stack and product-focused roles, you'll likely only need a surface understanding of networking concepts. Understanding these fundamentals will help you make better decisions, even if the minute details aren't going to be tested in your interviews.<br>

Each interviewer is a little different and if your interviewer just got off an oncall rotation dealing with load balancer problems or CDN issues, you'll want to be prepared to respond to their probes and questions!

</pre>

## Networking 101
As its core, networking is about connecting devices and enabling them to communicate. Networks are built on a layered architecture (the so-called "OSI model") which greately simplifies the world for us application developers who sit on top of it.<br>
Effectively, network layers are just abstractions that allow us to reason about the communication between devices in simpler terms relevant to our application. This way, when you're requesting a webpage, you don't need to know which voltages represent a `1` or `0` on the network wire (modern networking hardware is even more sophisticated than this!) - you just need to know how to use the next layer down the stack. Think of it like how you might use `open` in your langauge of choice instead of manually instructing the disk how to read bytes off a disk.