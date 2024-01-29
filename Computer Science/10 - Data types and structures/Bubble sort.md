---
tags:
  - comsci/chapter-10
  - datamanipulation
  - array
---
- Bubble sort allows for a list to be ordered numerically or alphabetically 
- Each element of the array is compared with the next element and swapped if the elements are in the wrong order.
- Upper bound is now in right position
- Comparison is repeated with one less element in the list until there is only one element left or no swaps are made.

DECLARE myList : ARRAY\[0:8] OF INTEGER 
DECLARE upperBound : INTEGER 
DECLARE lowerBound : INTEGER 
DECLARE index : INTEGER 
DECLARE swap : BOOLEAN
DECLARE temp : INTEGER 
DECLARE top : INTEGER 
upperBound ← 8
lowerBound ← 0 
top ← upperBound  - **top index is equivalent to upper bound**
REPEAT 
	FOR index <- lowerBound TO top - 1   **e.g. if there are 5 elements, it will do 4 comparisons that is why it is **
		Swap ← FALSE 
		IF myList\[index] > myList\[index + 1] 
			THEN 
				temp ← myList\[index] 
				myList\[index] ← myList\[index + 1] 
				myList\[index + 1] ← temp 
				swap ← TRUE 
			ENDIF 
		NEXT
		top ← top -1 
UNTIL (NOT swap) OR (top = 0)