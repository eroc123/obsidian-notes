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

**Example:**

TYPE \<PointerName> = ^\<Typename>

// Declaring a pointer variable

DECLARE \<FirstPointer> : \<PointerName>

\<assignment value> ← \<FirstPointer>^ // This accesses the data stored at the address which IntegerPointer points to. This is known
as dereferencing.

SecondPointer <-- @\<identifier> //This stores the memory address of the \<identifier> in SecondPointer 


SecondPointer^ <-- MyVariable //This stores the value in MyVariable to the memory location currently pointed by SecondPointer.
