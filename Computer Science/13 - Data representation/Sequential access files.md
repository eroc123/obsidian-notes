- Like a [[Serial access files]] but is ordered with values
- Has a **key field** - similar to database [[DBMS - Database Management Systems|primary keys]] but is both ordered and unique unlike primary keys which are just unique.
- Record is found by reading key field value until required value is found 
- When adding records, they must be inserted in the right place according to their key.
- **binary search can be used - cut search time in half**
- sequential access still requires reading every record.   