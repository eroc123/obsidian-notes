**Features included by a database management system**
- data management, including maintaining a data dictionary 
	- stores data about the data
		- e.g. fields, types, validation, no.records in each file
- Data modelling
	- analysis of data objects used in the database, identifying relationships among them
- Query Processor
	- Retrieve data matching criteria using SQL/QBE
	- Can be used to perform calculations on extracted data
- logical schema 
	- overall view of the entire database, includes entities, attributes and relationships
- data integrity 
	- entire block copied to user's area when being changed
- data security, including backup procedures and the use of access rights to individuals / groups of users
	- Access rights - user accounts: restrict actions of specific users/ unauthorized users cannot access database
	- Views - restrict which parts of the database specific users can see
	- Password - prevents unauthorized access
	- Automatic backup - create regular copies of data in case of loss
	- Encryption - data is incomprehensible to unauthorized users
**Tools in a DBMS**
- Developed Interface: 
	- allows creating and manipulating databases in SQL rather than graphically
- Query processor: 
	- handles high-level queries. It parses, validates, optimizes and compiles or interprets a query which results in the query plan