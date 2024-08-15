##### Sequential access
- Read each value in key field until required key of key field is found (record found) OR key value of field being searched for is greater than search key (record not found)
- Used in [[Serial access files]] and [[Sequential access files]]

##### Direct Access
- An index of all key fields is kept
- Index is used to look up address of file location where the record is stored
- Useful for searching individual records
- Much faster than sequential
- Used in [[Sequential access files]] and [[Random files]]


##### Direct vs sequential
- Direct access allows search algorithm to immediately find required record based off a given index. **Only processes and reads one record (the one to be found)**
- Sequential requires an algorithm to open each record and read each record one by one until the required one is found.