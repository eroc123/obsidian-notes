---
Date: 2023-09-04
tags:
  - comsci/chapter-1
---

- **Binary-coded Decimal** uses 4 digit binary to represent each denary number
	- 0000 = 0
	- 0001 = 1
	- 0010 = 2
	- 0011 = 3
	- 0100 = 4
	- 0101 = 5
	- 0110 = 6
	- 0111 = 7
	- 1000 = 8
	- 1001 = 9

Can be stored either as half a byte (4-bits) or one byte (2 4-bit numbers)

**One byte**

|0000|0011|3|
|-|-|-|
|0000|0010|2|

**Half a byte**

|0011|3|
|-|-|
|0010|2|

If [[Binary addition and subtraction||binary addition or subtraction]] is done on a BCD value and it exceeds 9 (1010 or above) then add 6 (0110), which makes the BCD value go back to being between (0-9)

## Convert from binary/denary to BCD 

- To convert from binary, first the binary number has to be [[Conversions between number systems|converted into denary]]. 

- The denary number can then be split up into its individual digits
	- e.g. 149 would be split into 1, 4 and 9
- Each digit would then be assigned a 4 digit binary string, equivalent to each denary digit. 

| 1    | 4    | 9    |
| ---- | ---- | ---- |
| 0001 | 0100 | 1001 |

The reverse can be done when converting from BCD to binary/denary
