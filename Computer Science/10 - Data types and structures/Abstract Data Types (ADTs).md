---
tags:
  - "#array"
  - "#comsci/chapter-10"
  - "#datatypes"
---
- **abstract data type (ADT)** is a collection of data and a set of operations on that data

##### Three abstract data types:
- [[Computer Science/10 - Data types and structures/Stack|Stack]] - list containing several items operating on last in, first out (LIFO) principle**
	- First item added to the list is last item to be removed (imagine stacking tires on each other, first tire will be the last one to be removed as all other tires must be removed first)
	- items can be added (push) or removed (pop) from the stack - the top gets manipulated
		- e.g. if push, a new item is placed on top of stack
		- e.g. if pop, an item is taken from the top of stack (top pointer)
	- **Base pointer always has same value**
	- ![[Computer Science/Excalidraw/stack]]
- **[[Queue]] - list containing several items operating on the first in, first out principle**
	- Items can be added to the queue (enqueue) and removed from the queue (dequeue)
	- First item to queue is first item removed
	- ![[Computer Science/Excalidraw/queue]]
- **[[Linked List]] - list containing several items in which each item in the list points to the next item in the list**
	- New items are always added to the start of the list. 
	- Each item in a linked list is stored with a pointer to the next item called a node.
	- ![[Computer Science/Excalidraw/linked list]]