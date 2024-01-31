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
basePointer <- 1   - **define base pointer value (index of 1 as its the first value)**
topPointer <- 0  - **define number of values currently stored (0 as default)**
stackful <- 10 - **upper bound is 10**

##### Push

IF topPointer < stackful   - if the 
	THEN
		topPointer <- topPointer + 1
		stack\[topPointer] <- item   
	ELSE
		OUTPUT "Stack is full, cannot push"
ENDIF