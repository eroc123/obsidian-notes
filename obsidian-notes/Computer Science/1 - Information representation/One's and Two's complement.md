---
Date: 2023-09-04
tags:
  - comsci/chapter-1
---

**One** and **two's complement** allows binary numbers to be expressed as negative numbers.

## One's complement
To convert to one's complement, simply flip each bit of a binary number (1's turn to 0's and 0's turn to 1's.
- e.g. 0101001 (41) turns into 1010110 (-41 in one's complement) 
## Two's complement 
- To convert to two's complement, flip each bit of a binary number (1's turn to 0's and 0's turn to 1's and then add 1 to the rightmost bit.
-  e.g. 0101001 (41) turns into 1010111 (-41 in two's complement) 

^ba3c97

#### Two's complement format (signed bit)

- Every place value has the same value, except that the leftmost bit is now negative instead of positive. (two's complement of 41, which is -41)

|-128|64 |32 |16 |8  |4  |2  |1  |
|-|-|-|-|-|-|-|-|
|1|0|1|0|1|1|1|1| 

For example, an 8 bit binary number in two's complement format can represent numbers ranging from -127 to +127

Converting to two's complement can allow for easy [[Binary addition and subtraction|addition and subtraction]] of binary numbers


