- A collision occurs when the record key of a searched hash doesn’t match the stored record key
- This means the determined storage location has already been used for another record. 

##### What to do when storing
- Search the file linearly to find the next available storage space if using a closed hash
- Search the overflow area linearly to find next available storage space if its an open hash 
##### What to do when retrieving/searching for a record
- Search the overflow area linearly until the matching record key is found in the case of an open hash
- Search linearly from where you are (closed hash) until the matching record key is found
- If the record is not found in either the overflow area (in the case of an open hash) or in the following records (in the case of a closed hash), the record does not exist.