# Introduction to Data Bases
John [[Von Neumann]] architecture contemplates the principal meory.
The standard of representation for the Entity-Relation diagram is the [[chen-notation]].


##### RDBMS
**R**elational **D**ata**b**ase **M**anagement **S**ystem are tools that help us to manage a Data Base.


### [[relational data bases|Relational Data Bases]]
They use [[sql|SQL]] to comunicate to the data base.

Created by **Edgar Cood**, who of course left us a few rules to follow to get a consistent standard, known as the [[12 Codd's Rules]]. Besides he created the **Relational Algebra**, that's about how we can manage, merge data using different characteristics.

-  **MySQL** from **Oracle**
 - **MariaDB** fork from MySQL to be an open source DB
 - **SQL Server**
 - **[[PostgreSQL]]**


### [[nosql|Non-Relational Database]]
They use a [[nosql|NOSQL]] to make `complete this...`
**MongoDB**
**Elasticsearch**
**Cassandra**


### [[data types|Data Types]]:
They are a little bit different from usual Data Types, they're completely designed to be efficient in a Data Base. To use less memory and accelerate Querys.

##### Text:
+ **CHAR**(n): Only have the lenght that you specified.
+ **VARCHAR**(n): Dynamic lenght, usefull when the **text lenght is unknown**. It becomes useless with different lenghts cause the motor calculate it individually.
+ **TEXT**: To large arrays of text.

##### Numbers:
+ **Integer**: Belongs to $N$
	+ BigInt 
	+ Smalllnt
+ **Numeric**(p,s):
	**p = precision**, or the maximum total number of digits to be stored including both sides of the decimal point.
	**s = scale**, or the number of digits to the right of the decimal point. It can be specified only when the precision (p) is specified. The default is 0.
+ **Decimal**(n,s):
	**p = precision**. It’s similar to the precision specified for NUMERIC, but the number of digits can be actually greater than p.
	**s = scale**, exactly like the scale specified for NUMERIC. There can be a maximum of s digits to the right of the decimal point.

##### Date/Hour:
+ **Date**: year/month/day.
+ **Time**: Indicates hour of the day.
+ **DateTime** (8 bytes): Contains **date** and **hour**.
+ **TimeStamp** (4 bytes): Contains **date** and **hour**.

##### Logic
+ **Boolean**: True or False, usually used to validate data.


### Constraints (Restrictions)
It add some rules to the data types that the Data Base table can accept.
+ **Null**: Default value from a DB table.
+ **Not Null**: Makes sure that column **is not a Null** value.
+ **Unique**: Makes sure that column value can't be repeted.
+ **Primary Key**: This data is specified in the Entity-Relation diagram for being an **underlined attribute**. Is essensial to make the relation between Entitys, so it is $Not Null$ and $Unique$.
+ **Foreign Key**: Is like a $Primary Key$ borrowed by another table. So it uses a Key from another table to be identified in a Query.
+ **Check**: Make sure that column always needs to fulfill a specific condition.
+ **Default**: Is a substitute of $Null$ to be the new default value of a table.
+ **Index**: ... It allow us the possibility to add some restrictions to a Query and thus filter the data that we don't want to be shown.


### Normalization
Steps to get a normalizated table that fulfill the [[12 Codd's Rules]].
- **1NF**: Atomic attributes (without repeated attributes).
- **2NF**: Fulfill 1NF and any table column **can't repeat a Primary Key**.
- **3NF**: Fulfill 1NF and 2NF. Any field of the table **can't** have dependences. This means that every field of the table can only b related to the **Primary field**.
- **4NF**: Fulfill 1NF, 2NF and  3NF. Multivariable fields are identified by a $Unique$ key. When we relate two independent tables we need to create a third one that only have the **Primary Keys** from which we want to relate.

### DB Instance
![[db instance.png]]