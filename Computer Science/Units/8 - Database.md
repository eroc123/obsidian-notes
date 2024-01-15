#### 8.1 Database Concepts
- Show understanding of the limitations of using a [[flat file|file-based]] approach for the storage and retrieval of data 
- Describe the features of a [[relational database]] that address the limitations of a file-based approach
- Show understanding of and use the [[terminology]] associated with a relational database model
	- Including entity, table, record, field, tuple, attribute, primary key, candidate key, secondary key, foreign key, relationship (one-to-many, one-to-one, many-to-many), referential integrity, indexing 
- Use an [[entity-relationship (E-R)]] diagram to document a database design
- Show understanding of the normalisation process 
	- [[First Normal Form (1NF)]], 
	- [[Second Normal Form (2NF)]] and 
	- [[Third Normal Form (3NF)]]
- Explain why a given set of database tables are, or are not, in 3NF 
- [[Produce a normalized database]] design for a description of a database, a given set of data, or a given set of tables

#### 8.2 Database Management Systems (DBMS)

- Show understanding of the features provided by a Database Management System (DBMS) that address the issues of a file based approach
	- data management, including maintaining a data dictionary 
	- data modelling 
	- logical schema 
	- data integrity 
	- data security, including backup procedures and the use of access rights to individuals / groups of users
- Show understanding of how software tools found within a DBMS are used in practice
	- developer interface 
	- query processor

#### 8.3 Data Definition Language (DDL) and Data Manipulation Language (DML)
- Show understanding that the DBMS carries out all creation/modification of the database structure using its Data Definition Language (DDL)
- Show understanding that the DBMS carries out all queries and maintenance of data using its DML
- Show understanding that the industry standard for both DDL and DML is Structured Query Language (SQL)
	- Understand a given SQL statement
- Understand given SQL (DDL) statements and be able to write simple SQL (DDL) statements using a sub-set of statements
	- Create a database (CREATE DATABASE) 
	- Create a table definition (CREATE TABLE), including the creation of attributes with appropriate data types:
	- CHARACTER 
	- VARCHAR(n) 
	- BOOLEAN 
	- INTEGER 
	- REAL 
	- DATE 
	- TIME change a table definition (ALTER TABLE) add a primary key to a table (PRIMARY KEY (field)) add a foreign key to a table (FOREIGN KEY (field) REFERENCES Table (Field))
- Write an SQL script to query or modify data (DML) which are stored in (at most two) database tables
	- Queries including SELECT... FROM, WHERE, ORDER BY, GROUP BY, INNER JOIN, SUM, COUNT, AVG Data maintenance including. INSERT INTO, DELETE FROM, UPDATE