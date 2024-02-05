- Is basically a python function, but the general name is Procedure
- **Is used when the same group of statements perform similar tasks**
	- Same code but repeated
- Procedure can be called many times 
	- e.g. in python it would be Function() where the quotation is call
	- e.g. in pseudocode it would be CALL \<identifier>


**to define a procedure in pseudocode:**
PROCEDURE \<identifier>
	\<statements>
ENDPROCEDURE


**example procedure**
PROCEDURE stars (NUMBER : INTEGER)
	FOR Counter 1 TO NUMBER
		OUTPUT "\*"
	NEXTCOUNTER
ENDPROCEDURE

CALL stars

**calling a procedure with parameters**