---
Date: 2023-09-04
tags:
  - comsci/chapter-1
---

**To add numbers in binary, simply add together each digit and [[carry]] if necessary.**

e.g. adding 52 to 61
00110100 + 00111101

|     | 0   | 0   | 1   | 1   | 0   | 1   | 0   | 0   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +   | 0   | 0   | 1   | 1   | 1   | 1   | 0   | 1   |
| =   | 0    | 1   | 1   | 1   | 0   | 0   | 0   | 1   |

**To subtract numbers in [[Binary, Denary and Hexadecimal#^90095a|binary]], first convert the number you are subtracting by to its [[One's and Two's complement#^ba3c97|two's complement]] and then add together the numbers.**
e.g. subtracting 42 from 68

1. Firstly, convert 42 to its two's complement
	- 00101010 (42) turns into 11010110 (-42)
2. Add together the two binary numbers (-42 + 68)

|     | 1   | 1   | 0   | 1   | 0   | 1   | 1   | 0   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| +   | 0   | 1   | 0   | 0   | 0   | 1   | 0   | 0   |
| =   | 0   | 0   | 0   | 1   | 1   | 0   | 1   | 0   |
Note: any excess digits are ignored.

