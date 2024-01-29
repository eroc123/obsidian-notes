---
tags:
  - comsci/chapter-10
  - array
---
Example:

| Index | myList |
| ----- | ------ |
| [0]   | 27     |
| [1]   | 19     |
| [2]   | 36     |
| [3]   | 42     |
| [4]   | 16     |
| [5]   | 89     |
| [6]   | 21     |
| [7]   | 16     |
| [8]      | 55       |

##### Declaring Arrays in Pseudocode

DECALRE \<identifier> : ARRAY\[LowerBound:UpperBound] OF \<data type>
DECLARE myList : ARRAY[\0:\8] OF INTEGER

- the lower bound is 0 (index 0 is first element)
- the upper bound is 8 (index 8 is last element)
##### Assigning data to an index within the list

myList\[7] <- 14

(the 7th index changed to 14)

| Index | myList |
| ----- | ------ |
| [0]   | 27     |
| [1]   | 19     |
| [2]   | 36     |
| [3]   | 42     |
| [4]   | 16     |
| [5]   | 89     |
| [6]   | 21     |
| [7]   | **14** |
| [8]   | 55     |
