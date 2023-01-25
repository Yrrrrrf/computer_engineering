# [[data bases]] [[programming/data types]]Types
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
