
https://www.youtube.com/watch?v=5o8CwafCxnU

Unique assigned identifier for each and every device on the internet

IP : internet protocol

#### Two types of IP addresses:
- Static - an IP address that is permanent and is used for servers and other equipment
- Dynamic - an IP address that does change and is used for consumer equipment (devices)


### IPv4
4 $\times$ 8 bit numbers, separated by a period ".", for a total of 32 bits
e.g. 127.0.0.1

An IP address usually are laid out like below 

| 174 | 129 |  14 | 120 |
| --- | --- | --- | --- |
|Country|Region|Subnetwork|Device|


### IPv6
New standard for IP addresses, as IPv4 only supports around 4 billion unique addresses, IPv6 increases the limit to allow increased unique devices

8 $\times$ 4 hex digits (8x16 bits, 8x2 bytes), for a total 128 bits, separated by a colon ":"
e.g. 3FFE:F200:0234:AB00:0123:4567:8901:ABCD

- **Shortened formats:**
	- Leading 0's within an IPv6 address can be omitted
		- e.g. 1050:0000:0000:0000:0005:0600:300c:326b can be written as 1050:0:0:0:5:600:300c:326b
	- Double colon in place of a series of zero's. Can only be used once
		- e.g. ff06:0:0:0:0:0:0:c3 can be written as ff06::c3
- **IPv4 embed** - allows backward compatibility 
	- First 96 bits (12 bytes or 6 columns of 4 hex digits of IPv6) follow IPv6 format and uses colon between each column
	- Last 32 bits (4 bytes or 4 columns of 2 hex digits of IPv4) follow IPv4 format and uses dots between each column
	- e.g. 0:0:0:0:0:ffff:192.1.56.10
	- 0:0:0:0:0:ffff is IPv6 component
	- 192.1.56.10 is IPv4 component

### How IP works when communicating with a website

A computer visiting a website sends a message to the other websites's IP address
	- Think of it like mailing a letter to an address except in the context of the internet
	- the ip address of the computer is also included in the message, which tells the website which computer communicated with it.
	- This allows for the website to send responses back to the computer which sent the first message.

#### IPv4 address classes 
**Host ID** - The number of devices that can be connected to a network
**Net ID** - The number of networks that can be supported by the IPv4 address class.

Bits from the IPv4 address are reserved for host-ID, netID and the identifier for the class.

**e.g: 11000011 00001100 00011000 00001110** (IPv4 written out in binary)
- if its a class C, then the first 3 bits will be reserved for the identifier.
- The next 21 bits will then be reserved for netID (there can be up to $2^{21}$ different possible networks utilizing class C ip addresses)
- The last 8 bits will then be reserved for host-ID (per network, there can be up to $2^8$ clients that are conencted, or 256 clients)

A custom number of netID can also be specified, using a backslash at the end, e.g.
- **195.12.24.14 / 20**
- written out in bits would be **11000011 00001100 00011000 00001110 / 0001 0100**
	- The suffix is an 8 bit number which will determine how many bits will be allocated for net-ID.
	- E.g. if the suffix is equal to 20 in denary as stated in the example, then there will be 20 bits allocated for net-ID ($2^{20}$ networks utilizing that IP possible)
![[network.png]]

| Network class | Identifier | Number of netID bits | Number of host-ID bits | Types of network |     
| ------------- | ---------- | -------------------- | ---------------------- | ---------------- |
| A             | 0          | 7                    | 24                     | Very large       |     
| B             | 10         | 14                   | 16                     | Medium size      |     
| C             | 110        | 21                   | 8                      | Small networks   | 
- IPv4 addresses have 3 classes, which each have a different number of Net ID's and Host ID's


#### Subnetting
- A network that is created by a router or a gateway can be split up into smaller parts (smaller LANS) using subnetting. ![[subnet.png]]
- Within the host-ID part of the IP address, it can be split up further to represent which subnet (smaller LAN) the IP address is pointing to.
	- e.g. if the hostID part of the IP address has 8 bits allocated and is **00100111**
	- the IP could be split to allocate 3 bits for the subnet (according to example would be 001) and 5 bits for hostID
	- the 5 bit hostID would be able to support 32 devices per network ($2^5$ devices)
	- the 3 bit subnet segment would be able to support 8 subnets ($2^3$) within the larger network created by the router. 
#### Public vs Private IPv4 address
- Public IP address is assigned by the ISP (internet service provider) to a router to access the internet. Web servers will use communicate with the public IP address they were provided (which is your router).
- Private IP address is assigned by the router to the different devices on a network.
	- Devices within a network will use private IP to communicate with each other.
- If a device in a network wants to communicate with a server outside the network, the device's private IP needs to be converted to a public IP and vice versa using a NAT. (Network Address Translation)



#### DNS 


Computer use DNS to look up domain name (part of the [[URL]]) and get the IP address associated with it, kind of like a phone book.

| Website         | IP            |
| --------------- | ------------- |
| www.youtube.com | 207.223.160.0 |
| www.google.com  | 199.223.232.0 |
**Note these aren't the actual IP of these websites, it is just to provide an example of how it works**

DNS stands for Domain Name Server, they are responsible for translating domain names to IP addresses. 

**DNS are laid out in a hierarchy** 


First the computer would ask the local DNS for the IP address, if the local DNS does not have the IP address in its cache, it will ask a higher level DNS. This repeats until either the URL is found (with the top level DNS or other lower level DNS), or an address not found error is returned

- First the computer would ask the local DNS for the IP address, 
- if the local DNS does not have the IP address in its cache, it will ask a higher level DNS. 
- This repeats until either the URL is found (with the top level DNS or other lower level DNS), or an address not found error is returned


##### This note discusses (IP address and DNS server) the process by which a computer looks for the web server requested, the note that discusses what happens after a web server is found is [[HTTP and HTML (web browsing)]]

