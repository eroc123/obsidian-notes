---
tags:
  - comsci/chapter-1
---

- When doing binary addition, for example when using two's complement set up, if the answer is larger than the largest possible number that the available number of bits can represent, it can cause overflow errors.

- For example, when using 8 bit data representation in a [[One's and Two's complement|two's complement]] set up, the largest number that can be represented is +127 and the smallest is -128. If the answer to an addition problem exceeds those bounds, an overflow error occurs as there are not enough bits to represent the larger number (e.g. you get 134 as an answer, that number cannot be represented by 8 bits in a 2's complement setup as it is above 127).

|     | 128 | 64  | 32  | 16  | 8   | 6   | 4   | 2   | 1   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | 1   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   |
|   +  | 1   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   |

you get something larger than 8 bit, that is an overflow