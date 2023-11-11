---
tags:
  - "#comsci/chapter-2"
---


![[client to server model.png]]
- Devices are either client or server (cannot be both at the same time)
- Servers provide access to resources and data requested by clients
	- Essentially, clients request services and the server provides assistance
	- Server also provides security (as a middleground between other clients)
- Requires dedicated hardware (the server)

**Where to use:**
- Companies with large user base
- Need for good security
- access to network resources needs to be controlled
- Data needs to be backed up
- e.g. Amazon, where a central server handles orders and such

**Advantages:**
- can be scaled very easily
- Uses central security databases (requires passwords and login ID to log in and such)
- Can back up data regularly on a central server
- allows installation of software onto client's computer (and for all clients to have the same software)
- Access to resources can be managed, for example if a user logs into the system, they will only get access to the files of that user.
**Disadvantages:**
- Single point of failure
	- If the server is down, the entire network is down
- Can become bottlenecked if multiple requests are sent at once
