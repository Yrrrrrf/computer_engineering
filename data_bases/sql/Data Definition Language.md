# [[structured query language#DDL Data Definition Language|Data Definition Language]]
Deals with database schemas and descriptions, of how the data should reside in the database.


### CREATE
Create create a database and its objects like (table, index, views, store procedure, function, and triggers).

**DATABASE**
Database name must be in lowecase.
```SQL
CREATE DATABASE database_name; --Creates a database
USE DATABASE database_name; --Stablish in which scheam/database make the changes
```

**TABLE & PRIMARY KEY**
To create a table, we put as a parameter (_column_name_ _[[data_bases/data types|dataType]]_ _[[data bases#Constraints Restrictions|constraint]]_).
To stablish what column is the **primary key** we use PRIMARY KEY(_column_name_) as a parameter in the table declaration.
``` SQL
-- A table can have as many columns as we want
CREATE TABLE table_name (column_name dataType, second_column_name dataType, ...);
-- To denote what column is our primary key, we use as a parameter the method PRIMARY KEY (pk_name) inside the table creation
CREATE TABLE table_name (pk int, column_name dayaType, PRIMARY KEY (pk));
```

**VIEW**
Take some data from the data base and accomodate it in a way that we can see it easier.
```SQL
-- Create a new view with the gived parametes
CREATE VIEW v_view_name AS
	SELECT columns_to_show
	FROM queried_table
	WHERE query_constraints
;
```
A reccomended practice is to name the view as *v_view_name*.


### ALTER
Modify or alterate the strcucture entities.

**ALTER table columns**
```SQL
ALTER TABLE table_name -- Select the table to alterate
ADD column1, -- Adds a new column
new_column_name AFTER column1; -- Add a new column after another column

-- Alterate that same table...
ALTER TABLE table_name
ALTER COLUMN new_column_name; -- Change the table name

ALTER TABLE table_name
ALTER COLUMN new_column_name; -- Delete column
```

**CHANGE table columns**
Changes a everything from a column.
CHANGE _selected_column_ _new_name_ _dataType_ _constraint_ _defaultValueType_ _defaultValue_
```SQL
ALTER TABLE table_name
CHANGE COLUMN 'column_name' 'new_name' dataType constraint defaultValue value;
```


### DROP
Delete objects from data base. **Must be careful** when use it, **is irreversible**.
```SQL
DROP TABLE table_name; -- Delete that table from data base
DROP DATABASE database_name; -- Delete the selected data base
```


`Complete this`
**TRUNCATE**: Remove all records from a table, including all spaces allocated for the records are removed.
```SQL

```
**COMMENT**: Add comments to the data dictionary.
```SQL

```
**RENAME**: Rename an object.
```SQL

```

