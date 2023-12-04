---
tags:
  - comsci/chapter-4
  - syllabus
---
	
### 4.1 Central Processing Unit (CPU) Architecture

**Candidates should be able to:** 
Show understanding of the basic [[Von Neumann model]] for a computer system and the [[Von Neumann model#Stored Program Concept|stored program concept]]
Show [[Registers|understanding of the purpose and role of registers]], including the difference between general purpose and special purpose registers 
	Special purpose registers including: 
	• Program Counter (PC) 
	• Memory Data Register (MDR) 
	• Memory Address Register (MAR) 
	• The Accumulator (ACC) 
	• Index Register (IX) 
	• Current Instruction Register (CIR) 
	• Status Register 
Show understanding of the purpose and roles of the Arithmetic and Logic Unit (ALU), Control Unit (CU) and system clock, Immediate Access Store (IAS) 
Show understanding of how data are transferred between various components of the computer system using the [[address bus]], [[data bus]] and [[control bus]] 
Show understanding of [[Factors Affecting Performance|how factors contribute]] to the performance of the computer system 
	Including: 
	• processor type and number of cores 
	• the bus width 
	• clock speed 
	• cache memory 
Understand how different ports provide connection to peripheral devices
	Including connection to: 
	• Universal Serial Bus (USB) 
	• High Definition Multimedia Interface (HDMI) 
	• Video Graphics Array (VGA)
Describe the stages of the [[FE cycle|Fetch-Execute (F-E)]] cycle 
Describe and use ‘register transfer’ notation to describe the F-E cycle
Show understanding of the purpose of [[interrupt|interrupts]] 
	Including: 
	• possible causes of interrupts 
	• applications of interrupts 
	• use of an Interrupt Service handling Routine (ISR)
	 • when interrupts are detected during the fetch-execute cycle 
	 • how [[Interrupt Cycle|interrupts are handled]]

### 4.2 Assembly Language

**Candidates should be able to:**
Show understanding of the relationship between assembly language and machine code
Describe the different stages of the [[Assembly instruction sets|assembly process]] for a two-pass assembler
Trace a given simple assembly language program
Show understanding that a set of [[instruction categories|instructions are grouped]]
	Including the following groups: 
	• Data movement 
	• Input and output of data 
	• Arithmetic operations 
	• Unconditional and conditional instructions 
	• Compare instructions
Show understanding of and be able to use different modes of addressing
Including immediate, direct, indirect, indexed, relative
![[Pasted image 20231027092506.png]]
### 4.3 - Bit manipulation

Show [[Bit shifts and bit masking|understanding of and perform binary shifts]]
- Logical, arithmetic and cyclic 
- Left shift, right shift
Show understanding of how bit manipulation can be used to monitor/control a device
- Carry out bit manipulation operations 
- Test and set a bit (using bit masking)
![[Pasted image 20231027092609.png]]