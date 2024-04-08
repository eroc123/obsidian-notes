---
tags:
  - comsci/chapter-2
---

Computer use DNS to look up domain name (part of the url)

DNS stands for Domain Name Server, they are responsible for translating domain names to IP addresses. 

DNS are laid out in a hierarchy 

Frist the computer would ask the local DNS for the IP address, if the local DNS does not have the IP address in its cache, it will ask a higher level DNS. This repeats until either the URL is found (with the top level DNS or other lower level DNS), or an address not found error is returned