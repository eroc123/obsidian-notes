---
tags:
  - comsci/chapter-2
---

TCP : Transmission Control Protocol

TCP manages the sending and receiving of all packets. It ensures that all packets are send and received. TCP keeps an inventory of all the packets that it received. It sends the inventory check back to the original server for confirmation. If there are packets missing, the server will send the missing packets again until all packets arrive. 