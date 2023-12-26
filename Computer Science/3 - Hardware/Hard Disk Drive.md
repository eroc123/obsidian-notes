
- Data is stored in a digital format (1's and 0's) on the magnetic surface of a hard disk drive.
- Contains one or more platters made of aluminium coated with magnetized metal grains (ferrous oxides).
- Platters rotate around a central spindle at high speed (up to 7000 times a second)
- Read write heads access the two surfaces on a hard disk drive and go up and down the radius of the disk around 50 times a second.
- electronic circuits the movement of arm and heads.
**Arrangement"**
- HDD is split up into tracks and sectors storing a number of bytes.
![[Hard Disk Drive.png]]

**Reading data**
- Actuator head moves to the track that will be read from
- Each grain will have a magnetic field either pointing north to south or south to north (this can represent 0 or 1).
	- The [[Electric Current|current]] going through the read head will depend on the [[magnetic field]] direction, allowing digital data to be read.
	- When data sector has run under the actuator arm, the data will have been read.
**Writing data**
- Actuator head moves to the track it will write to
- Change in current going through the [[electromagnet|electromagnetic]] write head causes direction of magnetic field of grains to change.
	- When data sector has run under the actuator arm, the data will have been written.
![[Pasted image 20230925150112 1.png]]

**Advantages:**
- Random access (data doesn't need to be read in a sequence to access the intended data)
- High capacities
- Low cost per megabyte
- Long longevity - more read/write operations than an SSD 
**Disadvantage:**
- Latency, since head needs time to move to the correct track to access the block of data.
- Susceptible to physical shock
- Can undergo fragmentation, sectors are constantly read and written to and some data may be allocated to two non-adjacent sectors. Makes data take longer to be written and read (reduce efficiency)