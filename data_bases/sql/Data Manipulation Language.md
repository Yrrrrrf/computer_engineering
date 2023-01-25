# [[sql#DML Data Manipulation Language|Data Manipulation Language]] 
Deals with **data manipulation** and **includes most** common **SQL statements**, it is used to store, modify, retrieve, delete and update data in a database.


### SELECT
Retrieve data from a database.
```SQL
SELECT column_name "Column alias", column2 -- The alias will be applied only in this query, this doesn't save that alias name anywhere
FROM table_name;
```


### INSERT
Insert data into a table. Fisrt we select in which table we will **insert** the data and then, using the reserved word $values$, we enter as parameter the values for that columns.
```SQL
INSERT INTO table_name (column_name, column2_name, column3_name, column3_name)
VALUES ('value1', value2, value3, value4);
```


### UPDATE
Updates or modifies the existing data within a table.
```SQL
UPDATE table_name
SET column1 = 'newValue', column2 = newValue
WHERE constraint; -- Is necessary to use a constraint otherwise this changes will be applied to all the rows of the table
```


### DELETE
Is similar to [[data definition language#DROP|DROP]] from [[data definition language|DDL]] but it's less powerfull.
This action can only delete records **from a database table**.
```SQL
DELETE FROM table_name
WHERE constraint; -- Is necessary to use a constraint otherwise will delete all the data from the table
```


#Uncomplete
**MERGE**: UPSERT operation (insert or update).
```SQL

```
**CALL**: Call a PL/SQL or Java subprogram.
```SQL

```
**EXPLAIN PLAN**: Interpretation of the data access path.
```SQL

```
**LOCK TABLE**: Concurrency Control.
```SQL

```