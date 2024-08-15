---
tags:
  - user-defined
  - non-composite
  - datatypes
---
- used to reference a memory location
- Does not hold a value but it references a memory address.
- Must be declared using a datatype in format **^\<TypeName>**
	- This defines the datatype found at the memory location that the pointer references. e.g. if a memory location stores string, the pointer must be declared using ^\STRING

##### Example 1

TYPE \<PointerName> = ^\<Typename>

// Declaring a pointer variable

DECLARE \<FirstPointer> : \<PointerName>

\<assignment value> ← \<FirstPointer>^ // This accesses the data stored at the address which FirstPointer points to. This is known as dereferencing.

SecondPointer <-- @\<identifier> //This stores the memory address of the \<identifier> in SecondPointer 


SecondPointer^ <-- MyVariable //This stores the value in MyVariable to the memory location currently pointed by SecondPointer.

basically ^ put at the end like \<address\>^ is basically saying "hey this is referencing the contents of memory at \<address\>, not whatever is stored in the variable \<address\>"

##### Common syntax

IPointer: 4402 // This is the address that IPointer is pointing to.

IPointer^: 33 //This is the value stored at the address (4402) the IPointer is pointing to.

MyInt2 = 33
@MyInt1: 3427 //This is the address of MyInt1

IPointer^ = MyInt2 : TRUE //This compares the value of MyInt2 to the value stored at the address (4402)