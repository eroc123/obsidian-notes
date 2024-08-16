##### General explanation
- Takes an input of variable size to produce an output of fixed size
- High quality hash algorithm should:
	- Reduce number of collisions (same hash value produced from different values)
	- Have uniform spread over problem space - basically all hashes are equally different from each other.

##### Uses
- Allows for efficient location and retrieval of data (e.g. file records)
- Used to read and write data from/to [[Random files|random]]/[[Sequential access files]]
- Used in [[File access types|direct access]], e.g. for random files/sequential access files
- Works with random files and sequential access files which have a key field. 
	- The input key value is divided by a large number
	- (continue)