- **[[Single linked list]]:** Navigation is forward only
- **[[Doubly linked list:]]** Forward and backward navigation is possible
- **[[Circular linked list:]]** Last element is linked to first element

startPointer = -1 as the list has no elements

### Stage 1 - set up 
###### Empty linked list elements

- When set up, there are technically two linked lists, one for free space and one for actual data storage
![[Linked List Stage 1]]

- heapPointer points to node 0 of the list (heapPointer = 0)
- startPointer points to -1 since it points to NULL (any pointer with value of -1 points to null)

| Index | Value |
| ---- | ---- |
| 0 > heapPointer |  |
| 1 |  |
| 2 |  |
| 3 |  |
| 4 |  |
| 5 |  |
| 6 |  |
| 7 |  |
| 8 |  |
| 9 |  |
| 10 |  |

###### Empty linked list pointers
| Index | Value |
| ---- | ---- |
| 0 | 1 |
| 1 | 2 |
| 2 | 3 |
| 3 | 4 |
| 4 | 5 |
| 5 | 6 |
| 6 | 7 |
| 7 | 8 |
| 8 | 9 |
| 9 | 10 |
| 10 | -1 |


### Stage 2 - adding value to the list

###### Empty linked list elements

- heapPointer points to the index 1 (heapPointer = 1) of the list 
- startPointer set to heapPointer value
	- heapPointer takes the **linked pointer list** value of whatever was stored in the **same index** as the previous element it pointed to.
	- Previous element it pointed to was where value 37 is now with **index 0**. Hence heapPointer takes value stored in **index - of the linked list pointer** which was 1
	- Now heapPointer points to value 1

| Index | Value |
| ---- | ---- |
| 0 > *startPointer* | 37 |
| 1 > *heapPointer* |  |
| 2 |  |
| 3 |  |
| 4 |  |
| 5 |  |
| 6 |  |
| 7 |  |
| 8 |  |
| 9 |  |
| 10 |  |
|  |  |

###### Empty linked list pointers
- The element in index 0 (number 37) has its pointer changed to point to -1 
	- It is the last element in the list, hence it points 

| Index | Value |
| ---- | ---- |
| 0 > identified by heapPointer <- *startPointer*  | -1 > heapPointer took value of 1 from index 0 and changed it to -1  **as it is the last element of the list** |
| 1 <- *heapPointer* | 2 |
| 2 | 3 |
| 3 | 4 |
| 4 | 5 |
| 5 | 6 |
| 6 | 7 |
| 7 | 8 |
| 8 | 9 |
| 9 | 0 |
| 10 | -1 |