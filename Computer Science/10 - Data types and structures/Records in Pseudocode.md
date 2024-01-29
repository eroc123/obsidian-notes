
>TYPE 
>TbookRecord 
>	DECLARE title : STRING 
>	DECLARE author : STRING 
>	DECLARE publisher : STRING 
>	DECLARE noPages : INTEGER 
>	DECLARE fiction : BOOLEAN 
ENDTYPE

- A user-made composite datatype called TbookRecord has just been defined in this statement.
	- The composite datatype "TbookRecord" references several other **built in** data types such as string and int.
- The user can then declare an identifier as such:

> DECLARE Book : TbookRecord


To reference an item from the TBookRecord
