---
tags:
  - non-composite
  - user-defined
  - datatypes
---
- user defined 
- **non - composite**
	- hence each element in the set has no datatype - no quotes or anything
- maps a **set** of names to a specific number
- is **ordered** and **countable**, with finite values in the set
	- hence when an enumerator is defined, incrementing the enumerator sets its value to the "next" element of the set, and values in the set can be compared to each other. 
- e.g. for a set called months

| name      | enumerator |
| --------- | ---------- |
| jan       | 1          |
| feb       | 2         |
| march     | 3          |
| april     | 4          |
| may       | 5          |
| june      | 6          |
| july      | 7          |
| august    | 8          |
| september | 9          |
| october   | 10         |
| november  | 11         |
| december  | 12         |

pseudocode example:

**To declare**

TYPE \<Datatype> = (\<value1>,\<value2>,\<value3>…) 
DECLARE \<identifier> : \<datatype>


**Example declaration**
e.g.
TYPE Season = (Summer,Winter,Autumn,Spring) 

Note: we are writing Summer intead of "Summer" b/c it is a non-composite data type 

DECLARE ThisSeason : Season
DECLARE NextSeason : Season

ThisSeason <-- Autumn 
NextSeason <-- ThisSeason + 1 // NextSeason is set to Spring - increment the enumerator by one an it takes on the next value of the set. 


