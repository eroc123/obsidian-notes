Direction is a variable
If direction has value of N, S, E or W the program will execute the code required by the condition accoringly
If direction does not have those values, it will output whatever is in the OTHERWISE line

CASE OF Direction
	"N": Y ← Y + 1
	"S": Y ← Y – 1
	"E": X ← X + 1
	"W": X ← X – 1
OTHERWISE : OUTPUT "Error"
ENDCASE