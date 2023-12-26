---
tags:
  - comsci/chapter-4
---

-  Program Counter (PC) ^PC
	- Stores [[address]] of next [[instruction]] to be read
-  Memory Data Register (MDR) ^MDR
	- Stores data that has just been read from memory or just about to be written to [[memory]]
-  Memory Address Register (MAR) ^MAR
	- Stores address of a memory location (on the [[ram]]) that is about to have a value read from or written to (kind of like the current address of the task that the [[processor]] intends to fetch)
-  The Accumulator (ACC) ^ACC
	- Where the output of an arithmetic operation is stored
-  Index Register (IX) ^IX
	- Stores a value for [[Types of memory addressing#^bbb593|index addressing]]
-  Current Instruction Register (CIR) ^CIR
	- Stores the current instruction whilst its being [[Computer Science/4 - Processor Fundamentals/FE cycle|decoded and executed]] 
	- "current instruction" in the name suggests its the instruction being run
-  Status Register ^statusRegister
	- Contains bits representing [[flags]] that are set or cleared after ALU (arithmetic logic unit) operations
	- Flags can consist of whether an arithmetic operation produced a negative number, a [[carry]] or an [[overflow]].
	- The status register shows these flags which the [[OS]] can then take into account when dealing with a [[program]].
-  IAS Immediate Access Store ^IAS
	- Stores information current in use by the processor that needs to be accessed quickly
%%Help what does this stand for???%%