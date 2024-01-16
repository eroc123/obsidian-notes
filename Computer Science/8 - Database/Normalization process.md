**Unnormalized (UNF) -> First Normal Form**
- Each column should contain single atomic values (not a list)
| Bob, Alice | (wrong)
vs
| Bob  |
| Alice | (right)

- There are no repeating groups of attributes/columns - each column has a unique name
![[Pasted image 20240115152817.png]]
**First Normal Form (1NF) -> Second Normal Form (2NF)**
- A database must be in the first normal form
- Relation must not contain any partial dependency
	- Any non-primary key attribute must be fully dependent on the primary key for identification
	- e.g. for location data and zip code, both those attributes are dependent on each other, hence they should get a new location table instead of being dependent on another unrelated primary key. 
	- ![[Pasted image 20240115152806.png]]
**Second Normal Form (2NF) -> Third Normal Form (3NF)**
- A database must be in the first and second normal form
- Relations must not contain any transitive dependencies
- A->B and B->C are two FDs then A->C is a transitive dependency
- Solve by breaking up the table 
![[Pasted image 20240115152830.png]]