- Passing by reference - when the variable is changed within a function or a procedure, the variable outside is also changed

- Passing by value, when the variable is changed within a function or a procedure, the variable outside does not change


##### Pseudocode to pass by reference
PROCEDURE \<identifier> (BYREF \<parameter1>:\<datatype>, \<parameter2>:\<datatype...>)
	\<statements>
ENDPROCEDURE


default is pass by value


e.g. in python
> def consoleprint(x):
> 	x=5
> 	print(x)
>x=2
>consoleprint(x)
>print(x)

##### Terminal
> 5
> 2

- the variable outside the function isn't modified.
- x within the function is in its own local scope