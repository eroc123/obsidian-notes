---
tags:
  - comsci/chapter-2
---

A container for information that are transferred on the internet. 

This works by splitting up large chunks of information into smaller packets, which are then sent through the internet.

The packets does not have to all take the same route and does not have to arrive at the same time. This ensures that even if some routes on the internet are broken or clogged, the information can still be transferred.

e.g. A large image may be split up into many small packets.

Packets are transferred by [[Routers|routers]], which checks the packet to see where the packet is heading. Then it picks the cheapest route and pass the packet onto the next router. 
