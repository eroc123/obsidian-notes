- Sender and reciever agrees to use EVEN or ODD parity
- there is one bit reserved at the end of a string that ensures ODD or EVEN parity
![[parity check]]
- If a value gets flipped, then there will be a mismatch between parity bit and whether the number of bits is even or odd. 
	- e.g. if the last bit gets flipped, then there will be an odd number of 1's yet the parity bit still stays as 1 (even)
	- limitation is that if two bits get flipped, the binary string continues to have an even number of 1's and the parity bit stays as 1 (even), meaning that error goes undetected