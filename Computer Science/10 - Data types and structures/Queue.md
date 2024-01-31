- frontPointer changes after dequeue (index + 1 since an item is removed) and rearPointer changes after enqueue (index +1 since an item is added).
##### Stage 1
![[queue operation stage 1]]
##### Stage 2
![[queue pointer stage 2]] 

##### Stage 3
![[queue operation stage 3]]

- Arranged as a circular queue, where if the index of either rearPointer or frontPointer exceeds the upper bound, it cycles back to the