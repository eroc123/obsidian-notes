---
tags:
  - comsci/chapter-10
  - array
---
- Uses tables with rows and columns

Example:

MyArray

|  | \[r,0] | \[r,1] | \[r,2] |
| ---- | ---- | ---- | ---- |
| \[0,c] | 27 | 31 | 17 |
| \[1,c] | 19 | 67 | 48 |
| \[2,c] | 36 | 98 | 29 |
| \[3,c] | 42 | 22 | 95 |
| \[4,c] | 16 | 35 | 61 |
| \[5,c] | 89 | 46 | 47 |
| \[6,c] | 21 | 71 | 28 |
| \[7,c] | 16 | 23 | 13 |
| \[8,c] | 55 | 11 | 77 |

- Leftmost column is lower bound for column index
- Rightmost column is upper bound for column index
- Top row is lower bound for row index
- Bottom row is upper bound for row index

##### Declaring 2D arrays in Pseudocode

> Declare \<identifier> : ARRAY\[LBR:UBR, LBC:UBC] OF \<data type>

- row always comes first in the index, then column. 