# Not Only [[sql]]
Is a **non-Relational [[data bases|Database]]** provides a mechanism for **storage and retrieval** of **data that is modeled** in means other than the tabular relations used in relational databases.

This type of [[data bases|database]] also support an [[sql|SQL]] query.

##### Non-relational DB Hierarchy
![[NOSQL Hierarchy.png]]

### NoSQL [[data bases|databases]] types
There're a lot of different types of NoSQL [[data bases|databases]] created thinking in a specific purpose.

- **Key - value**
These type is ideal to store & get lots of data using it's associated key. Used in BigData.
Many values can be associated to a same key, so it's difficult to make some more exact queries.
	- DinamoDB (used by AmazonWebServices)
	- Cassandra

- **Based on documents (.json & XML)**
This kind of [[data bases|database]] **is the most used out of the standard [[sql|SQL]]**. Are similar to a $Key-Value$ type, but with a semi-structured form.
This kind is used to store specifications from a webpage, or a game, but have the same problem as the $Key-Value$ types.
	- MongoDB
	- Firestore It's usefull to learn abour [[nosql||Non-Relational Databases]] because of his UI

- **Based on graphs**
These use nodes or entities that have really complex relations.
Used in Artifitial Intelligence  to relate the inputs.
`obsidian uses something similar to connect the documents`
	- neo4j
	- TITAN

- **In memory**
The **principal advantage is that is the quick** but they're **volatile**. So they didn't really store data, but it's good to manage it in a big project.
	- Memcached
	- Redis

- **Optimized for queries**
This have a variety of structures and had been thinked to **complex queries** easilly. is correct?
	- BigQuery
	- Elasticsearch
