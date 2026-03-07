## Message Queue
Message Queue is a communication mechanism used in distributed systems where messages are stored in a queue and processed asynchronously by consumers.<br>
<b>Definition:</b> A message queue is a software component that enables asynchronous communication between different services or applications by temporarily storing messages sent by producers until they are processed by consumers.
<br>It works like a waiting line for messages.
<pre>
Producer -> Message Queue -> Consumer
</pre>

- Producer: sends the message
- Queue: stores the message
- Consumer: processes the message

<br>
Example: When a user places an order in an e-commerece system:
<pre>
Order Service -> Message Queue -> Payment Service
                               -> Inventory Service
                               -> Email Service 

</pre>
The queue ensures that messages are delivered reliably and processed even if some services are temporarily busy or unavailable.