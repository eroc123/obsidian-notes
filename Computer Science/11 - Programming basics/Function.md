there are often similar calculations or tasks to perform that make use of the same groups of statements and always produce an answer - similar to procedures but it returns a value

**Simple function without parameters:**
FUNCTION \<identifier> RETURNS \<value>
	\<statements>
ENDFUNCTION

**Simple function with parameters:**
FUNCTION \<identifier> (\<parameter1> : \<datatype 1>, \<parameter2> :\<datatype2>)
	RETURNS \<value>
		\<statements>
ENDFUNCTION


RETURN can be placed anywhere in a function and used multiple times like in python
![[pseudocode fnction.png]]