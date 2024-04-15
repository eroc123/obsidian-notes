1. At the end of each instruction cycle, the processor checks for interrupts
2. If an interrupt flag is set, the processor identifies the source of the interrupt
3. The processor checks the priority
4. If the interrupt priority is high enough, the processor saves the current job on stack (a part of the RAM memory)
5. Processor calls ISR - interrupt service routine to service the interrupt
6. Address of ISR is loaded into PC counter
7. When the servicing of the interrupt is complete, the job from the stack is restored
8. The processor continues with next F-E cycle