Pass 1:
- Removal of comments
- Creation of a names and symbol table containing binary code for symbolic names and labels
- Expansion of [[Macros|macros]] (functions)
	- Essentially, lines where there are macros and functions get expanded and replaced with the full code of the function/macro
Pass 2:
- Generation of object code (generation of machine code from assembly)
- Save or execute program
