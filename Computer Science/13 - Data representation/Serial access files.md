- Files with no defined order - can store repeating lines separated with end of line character
- Similar to a [[Computer Science/10 - Data types and structures/Queue|Queue]] abstract datatype - records are added to the end of the file one after another.
- Must search through each record to find a given record [[Computer Science/10 - Data types and structures/Linear Search|Sequential Access]] - similar to linear search
- no defined end of record character 
- think of it as "free files" with no set format
- **Chronological order**


##### Advantages
- Low cost
- Easy to set up

##### Disadvantages
- Slow - have to search through each other record to find given record or search through the whole file to return that the record was not found - because no defined end of file either.

