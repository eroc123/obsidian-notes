Total <- 0 
FOR Counter ← 1 TO 10 
	OUTPUT "Enter a number " 
	INPUT Number 
	Total ← Total + Number 
NEXT Counter
OUTPUT "The total is: ", Total

FOR Counter ← 1 TO 10 STEP 2 
	OUTPUT Counter 
NEXT Counter


- **FOR** is a loop with a fixed number of repeats 
- **STEP** specifies with what increment the index increases by, e.g. step 2 means it increases by 2 each iteration until counter = 10 (the index)
- MUST INCLUDE **NEXT Counter** (same indent as the **FOR**) so that
- The for loop repeats until the index arrives to the number specified, in this case 10. The condition is inclusive of 10, hence the counter will run one more time even when it has hit 10. 
- After 10 however it will stop.
- Hence:
	- FOR Counter <- 1 TO 10 will run 10 times 
	- FOR Counter <- 0 TO 10 will run 11 times
	- FOR Counter <- 1 TO 10 STEP 2 will run 5 times
	- FOR Counter <- 0 TO 10 STEP 2 will run 6 times
