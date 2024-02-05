- **[[Single linked list]]:** Navigation is forward only
- **[[Doubly linked list:]]** Forward and backward navigation is possible
- **[[Circular linked list:]]** Last element is linked to first element

startPointer = -1 as the list has no elements

### Stage 1 - set up 
###### Empty linked list elements

- When set up, there are technically two linked lists, one for free space and one for actual data storage
![[Linked List Stage 1]]

- **heapPointer** points to node 0 of the list (heapPointer = 0)
- **startPointer** points to -1 since it points to NULL (any pointer with value of -1 points to NULL)
- null is the end of the list

###### Empty linked list DATA
| Node | Value |
| ---- | ---- |
| 0   |  |
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

###### Empty linked list pointers - heapPointer used for empty space linked list
| Node | Value |
| ---- | ---- |
| **heapPointer** | **0** |
| 0  | 1 |
| 1 | 2 |
| 2 | 3 |
| 3 | 4 |
| 4 | 5 |
| 5 | 6 |
| 6 | 7 |
| 7 | 8 |
| 8 | 9 |
| 9 | 10 |
| 10 | -1 (**NULL**) |


### Stage 2 - adding value to the list

###### Empty linked list elements

- heapPointer points to the index 1 (heapPointer = 1) of the empty data linked list
	- this is because free space is taken from the front of the list - **node 0 is sacrificed first**
	- heapPointer then **points to node 1** as node 0 has been removed.
- startPointer set to value 0
	- this is because the empty node - **which is node 0** is taken from the empty data linked list and put at the **beginning of the data linked list.** 
	- startPointer then points to **node 0** instead of NULL (-1).

##### Linked list
| Node | Value |
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