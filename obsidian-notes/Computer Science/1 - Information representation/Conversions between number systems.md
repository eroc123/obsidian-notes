---
Date: 2023-09-04
tags:
  - comsci/chapter-1
---

## [[Binary, Denary and Hexadecimal|Binary]] to [[Binary, Denary and Hexadecimal|Denary]]

Simply multiply each digit in each column by the place value of the column and add together all the values. 
e.g.

|$2^4$|$2^3$|$2^2$|$2^1$|$2^0$|
|--|--|--|--|--|
|1|0|1|0|1|

$1\times2^4$ + $0\times2^3$+$1\times2^2$+$0\times2^1$ +$1\times2^0$ = 16 + 4 + 1 = 21

- The conversions from **hex** to **denary** are similar to binary, except you multiply by a place value with base 16 instead of base 2.
## Denary to Binary

There are two methods to do this

#### **Method 1**
- Place 1's and 0's into appropriate place value positions to get the equivalent to the denary number
	- e.g. Convert 29 to binary

|$2^4$|$2^3$|$2^2$|$2^1$|$2^0$|
|--|--|--|--|--|
|1|1|1|0|1|

#### **Method 2**
 ![](https://lh5.googleusercontent.com/dpbZYLp6ApbylQ_pLg4oJDLykzS8EezzceauLSChILBkoiqEAn3zjO3Jy_VAIqy-XoYCOpGHhIRK08BwkwsTPXsOwsQR9UrbJRxR4wbl_wWllck_yhu2hZf1yq5C5jzuSP_sGvtn8PTG4kbDYfsNNbo)
Get the denary value and divide it successively by two, logging down the remainder each time (either 1 or 0). Then read the remainders from the bottom up to get the binary number.


- The conversions from **denary** to **hex** are similar to binary, except this time you successively divide by 16 instead of 2 and log down the remainder. If the remainder is between 10 and 15, convert it to a letter. 

## Hex to Binary

**To convert from hex to binary:**
	1. Split the hex number and convert each digit to its denary equivalent. 
	2. Then convert each denary number to a 4 digit binary number. 
	3. String the 4 digit binary numbers together to form the final product

|F|3|A|2|
|--|--|--|--|
|15|3|10|2|
|1111|0011|1010|0010|
= 1111001110100010

- **To convert from binary to hex, do the exact same thing but in reverse.**

