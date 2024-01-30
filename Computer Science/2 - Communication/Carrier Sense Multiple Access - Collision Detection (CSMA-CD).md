Carrier Sense Multiple Access/Collision Detection (CSMA/CD)

- When transmitting data via ethernet (half duplex - allows for data transmission in only one direction at a time), there is a possibility for two data packets when sent at the same time to collide on the same channel.

- Each device senses whether the cable is idle (no data packets) before transmitting data.

- If there is a collision, a jam signal is sent
- Each device then waits a random period of time before resending data.
	- Random period of time is waited to ensure that signal is sent at different times instead of at the same time again (cause another collision)

- Eventually became less used, as ethernet cables became full duplex (allows for data transmission in both directions at the same time)