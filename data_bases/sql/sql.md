# Structured Query Language SQL
Is the must stantarized language to administrate data **into one or more data tables** in which **[[data bases#RDB Relational Data Bases||data types may be related]] to each other**. These relations help structure the data.

SQL is a language programmers use to create, modify and extract data from the relational database, as well as control user access to the database. In addition to relational databases and **SQL**, an [[data bases#RDBMS|RDBMS]] like MySQL works with an operating system to **implement** a **relational database** in a computer's storage system, **manages users**, allows for **network access** and **facilitates testing database integrity** and **creation of backups**.

**SQL** divides in many branches with different usages:
![[SQL Commands.png]]

### DDL [[data definition language]]
Deals with database schemas and descriptions, of how the data should reside in the database.
- **CREATE**: Create create a database and its objects like (table, index, views, store procedure, function, and triggers).
- **ALTER**: Modify or alterate the strcucture entities.
- **DROP**: Delete objects from data base. **Must be careful** when use it, **is irreversible**.
- **TRUNCATE**: Remove all records from a table, including all spaces allocated for the records are removed.
- **COMMENT**: Add comments to the data dictionary.
- **RENAME**: Rename an object.

### DML [[data manipulation language]] 
Deals with **data manipulation** and **includes most** common **SQL statements**, it is used to store, modify, retrieve, delete and update data in a database.
- **SELECT**: Retrieve data from a database.
- **INSERT**: Insert data into a table.
- **UPDATE**: Updates existing data within a table.
- **DELETE**: Delete all records from a database table.
- **MERGE**: UPSERT operation (insert or update).
- **CALL**: Call a PL/SQL or Java subprogram.
- **EXPLAIN PLAN**: Interpretation of the data access path.
- **LOCK TABLE**: Concurrency Control.

##### Tipos de operadores
[[#DML Data Manipulation Language]] us based on **Relational Algebra**, developed by Edgar Codd.
-   **Operadores unarios**: Requiere una relación o tabla para funcionar.  
	- **Proyección (π):** `π<name, surname, mail>(User_table)`
	Equivale al comando Select. Saca un número de columnas o atributos sin necesidad de hacer una unión con una segunda tabla.
    - **Selección (σ):** `σ<name="Yrrrrrf">(User_Table)`
    Equivale al comando Where. Consiste en el filtrado de de tuplas.
- **Operadores binarios**: Requiere más de una tabla para operar.  
    - **Producto cartesiano (x):** `Table_1 x Table_2`
    Toma todos los elementos de una tabla y los combina con los elementos de la segunda tabla.  
    - **Unión (∪):** `Table_1 U Table_2`
    Obtiene los elementos que existen en una de las tablas o en la otra de las tablas.  
    - **Diferencia (-):** `Table1 - Table2`
    Obtiene los elementos que existe en una de las tablas pero que no corresponde a la otra tabla.  

### DCL [[data control language|Data Control Language]]
Includes permissions and other controls of the database system.
- **GRANT**: Allow users access privileges to the database.
- **REVOKE**: Withdraw users access privileges given by using the GRANT command.

### TCL [[transaction control language|Transaction Control Language]]
Deals with a transaction within a database.
- **COMMIT**: Commits a Transaction.
- **ROLLBACK**: Rollback a transaction in case of any error occurs.
- **SAVEPOINT**: Rollback the transaction making points within groups.
- **SET TRANSACTION**: Specify characteristics of the transaction.


`Complete the syntax part using the must used SQL query instructions`
### [Syntax](https://www.w3schools.com/sql/sql_syntax.asp)
**Create a new Data Base**:
```SQL
CREATE DATABASE 'databaseName' DEFAULT CHARACTER SET utf8;
```
Where `utf8` is one of the most standarized characters in [[data bases]].



`Pending:
`See Administrative Systems class from Fundamentos de Base de Datos in Platzi`
