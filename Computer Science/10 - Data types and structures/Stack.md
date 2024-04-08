---
tags:
  - "#pseudocode"
  - "#array"
  - "#comsci/chapter-10"
  - "#datatypes"
---
DECLARE stack ARRAY\[1:10] OF INTEGER - create [[Data types|identifier]] "stack" for an array which only takes int
DECLARE topPointer : INTEGER - create [[Data types|identifier]] "topPointer" which only takes int
DECLARE basePointer : INTEGER
DECLARE stackful : INTEGER
basePointer <- 1   - **define base pointer value (always points to the first index no matter if there is a value)**
topPointer <- 0  - **define number of values currently stored (0 as default)**
stackful <- 10 - **upper bound is 10**

##### Push - an item stored in *item*, onto a stack

IF topPointer < stackful   - if the number of values is less than upper bound 
	THEN
		topPointer <- topPointer + 1  - **increment number of items by 1 (as you just stored another item)**
		stack\[topPointer] <- item  - **the index that topPointer is pointing to gets assigned a value**
	ELSE
		OUTPUT "Stack is full, cannot push"
ENDIF

##### Pop an item, stored in *item*, from a stack

IF topPointer = basePointer - 1 **- checks if there are values in the stack (topPointer = 0)**
	THEN
		OUTPUT "Stack is empty, cannot pop" **- cannot remove values if there are none left**
	ELSE
		Item <- stack\[topPointer] 
		 topPointer <- topPointer - 1 - **decrement 1 down from old index to show that topPointer is now pointing at the item below. The item to pop will now be overwritten the next time the stack is pushed to**
ENDIF
![[Stack Pop]]



#### NOTE
- **When answering questions describing how to create a stack, DECLARE THE VARIABLES ITS FREE MARKS**

##### Example Mark scheme
- Declare a (1D) array of data type STRING 
- 2 The number of elements in that array corresponds to the size of the required stack 
- 3 Declare an integer / variable for StackPointer 
- 4 Declare an integer / variable for the size of the stack // for the max value of StackPointer 
- 5 Use the StackPointer as an index to the array 
- 6 Pointers and variables initialised to indicate empty stack 
- 7 Store each item on the stack as one array element / Each stack item maps to one array element 
- 8 Attempt to describe Push and Pop operations 9 Push and Pop routines need to check for full or empty conditions