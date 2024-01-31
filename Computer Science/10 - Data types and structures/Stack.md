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
		OUTPUT "Stack is empty, cannot pop" 
	ELSE
		Item <- stack\[topPointer]