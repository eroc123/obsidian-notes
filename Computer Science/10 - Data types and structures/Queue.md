- frontPointer changes after dequeue (index + 1 since an item is removed) and rearPointer changes after enqueue (index +1 since an item is added).
##### Stage 1
![[queue operation stage 1]]
##### Stage 2
![[queue pointer stage 2]] 

##### Stage 3
![[queue operation stage 3]]

- Arranged as a circular queue, where if the index of either rearPointer or frontPointer exceeds the upper bound, it cycles back to the first index. 
	- e.g. if rearPointer was 8 and an extra item is added (provided the queue isn't full), the rearPointer will now be 1 (circles back)
	- e.g. if frontPointer was 8 and an extra item is added (provided the queue isn't full), the frontPointer will now be 1 (circles back)

DECLARE queue ARRAY\[1:10] OF INTEGER 
DECLARE  rearPointer : INTEGER 
DECLARE frontPointer : INTEGER 
DECLARE queueful : INTEGER 
DECLARE queueLength : INTEGER 
frontPointer ← 1 
endPointer ← 0 
upperBound ← 10 
queueful ← 10 
queueLength ← 0