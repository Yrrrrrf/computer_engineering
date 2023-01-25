Some of the most usefull sql db commands.


### Startup
- NOMOUNT If there's not database (to create a new one)
```SQL
STARTUP NOMOUNT -- Init an Instance that's not assosiated to a database
```
- MOUNT To give maintainment to the database.
```SQL
STARTUP MOUNT -- Start in mounted
ALTER DATABASE MOUNT;  --Change to mounted 
```
- OPEN a database makes it available for normal operation.
This also initialize the **Oracle Database#Oracle Database Instance|Database Instance]].
```SQL
STARTUP  -- Start the Database Instance
ALTER DATABASE OPEN;
```


### Manage Users
`SHOW USER` will show the actual session (user).
Login: `sql username/password@pdb_name`

###### CRUD
- **Create** user `CREATE USER user_name IDENTIFIED BY password;`
When a new user is created it have not privileges, **so it's necesarry to give them explicitly**.
- **Read** users list: `SELECT * FROM all_users ORDER BY created;`
- **Update** user data: Once created the user, that user can't do anything.
```sql
GRANT CREATE SESSION TO username; -- Grant a session connection
GRANT CREATE TABLE TO username; -- Grant the possibillity to create tables
ALTER USER username DEFAULT TABLESPACE tablespace;
ALTER USER username QUOTA 10M ON tablespace_name; -- On table space
--Object Privilages
GRANT SELECT ON table_name TO username;
GRANT INSERT ON table_name TO username;
GRANT SELECT ON user_1.tablename TO username; -- 
```
- **Delete** user:  `DROP USER user_name CASCADE;`.

##### Connect as  administrator
- `sql user_name/password@pdb_name`
- `sql / as sysdba` will connect the user as the maximmu administrator.
- `sql system/password@pdb_name`

##### Create rol
**DBA** is a role that...
Is a set of [[#CRUD|privilages]] that can be **assigned to a User**. 
``` sql
CREATE ROLE role_name;
GRANT CREATE SESSION TO role_name; -- Assign all privilages
```
`GRANT rol_name TO user_name` will assign that privilages to that user.


### Manage DB
Once initialized the db we can manipulate it by entering in it. There we can use the 
- Default connection path: `CDB$ROOT`
- `SHUTDOWN ABORT` **close** the instance of a databse.
- `STARTUP` **initialize** the instance of a database.
- `SHOW PDBS` will list all the **pdbs inside** this **instance**.
- `SHOW CON_NAME` container's name. ($user\_name@container\_pdb$)

Create a new DB (pdb)
```SQL PLUS
CREATE PLUGGABLE DATABASE pdb_name ADMIN USER mypdb_admin IDENTIFIED BY u_profile;
```
1. Once created, we need to open it using: `ALTER PLUGGABLE DATABASE db_name OPEN;`.
2. Then we can manipulate our [[data bases|database]]. But now we're working with all the PDBs, we need to select one using: `ALTER SESSION SET CONTAINER=pdb_name`

To **change the pdb name** it should be on restricted mode (YES)
```sql
-- To do this the pdb must be on MOUNTED MODE
ALTER PLUGGABLE DATABASE db_name OPEN RESTRICTED; -- Is necessary to change name to db
ALTER PLUGGABLE DATABASE db_name GLOBAL_NAME TO new_db_name; -- Set new name
```


##### FLASHBACK QUERY
```SQL
SELECT COUNT(*) FROM table_name AS OF TIMESTAMP SYSTIMESTAMP-27/1440;
```


### Initialization Parameters
Parameter files `u01/app/oracle/dbs/spfileorcl.orca`
When we initialize the instance, the database read the parameters from the `spfileorcl.orca` file, if it doesn't exist, the instance'll read parameters from `initorcl.ora` & create the `spfileorcl.orca`.
```sql
SHOW PARAMETER
-- Can show all the parameters of a db using a parameter next of this sentence
--- SHOW PARAMETER UNDO

CREATE PFILE FROM SPFILE; -- Create the parameter file from the spfile
SHOW PARAMETER TARGER; -- Show the limit values of the database
-- These parameters define the size of the SGA
```
- Dinamyc parameters: Can be modified with a running instance.
- Static: requierst a SHOUTDOWN to work properly.

`V$PARAMETER` is the VIEW that show all the parameter names.
`DESCRIBE PARAMATER`
- `DICT` Dictionary Index
- `.__.`

Some parameters can be changed at a SESSION lvl.
`ALTER SESSION SET NLS_DATE_FORMAT='DD' 'de' 'MONTH' 'del' 'AAAA'`


### Data tables
Using `SELECT COUNT(*) FROM ____;`
- `V%LOCK` 
- `V$SESSION` Sessions an bg process
- `V$PROCESS` Open connections & background process
- `V$SQL` Total SQL sentences
- `TABLESPACE` Show all the tablespaces
SYSAUX is a Tablespace used to save statistics of the database. We can manually config the time between every update (of this document).
- `SELECT MEMBER FROM V%LOG` List of the REDO LOG FILES & it's corresponding COPIES(used to be sure that these files can be recovered **even if the physic disk fails**).


Look about PL/SQL.

