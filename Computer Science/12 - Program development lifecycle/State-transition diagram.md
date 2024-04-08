- Shows the conditions needed for an event or several events that will cause a transition to occur and the outputs or actions carried out as a result of the transition

##### Represented as:
- States as nodes (circles)
- Transition as interconnecting arrows
- Events are labels on the arrows
- Conditions specified in square brackets after the event label
- Initial state indicated by an arrow with a black dot
- Stopped state indicated with double circle

##### state-transition table
- a way of representing the algorithm in a table, with each state having a connected event which leads it onto the next state
- door lock algorithm with code of 259 to unlock

| Current state | Event | Next state |
| ---- | ---- | ---- |
| locked | 2 input | waiting for input of 2nd digit |
| locked | not 2 input | locked |
| waiting for input of 2nd digit | 5 input | waiting for input of 3rd digit |
| waiting for input of 2nd digit | not 5 input | locked |
| waiting for input of 3rd digit | 9 input | unlocked and stopped |
| waiting for input of 3rd digit | not 9 input | locked |

![[Screen Shot 2567-02-15 at 12.35.07 1.png]]