# Chen Notation
Is the normilized standard to repreentate [[entity relationship diagram|Entity-Relation diagrams]] in [[data bases]].
These are described in the [[data bases#Constraints Restrictions]].

A **derivated attribute** is one that can be obtainded using another attribute.

An attribute can be compound from other attributes, this will be named as **Compund Attribute**.

The **Key attribute** is $unique$ and can't repeated.
They can be **Natural key**(intrinsic to the object), like a Serial number or ISNB. Or **Artifitial key**(added to the objetc) that we assign it arbitrarily to identify the object.

**Weak Entities** can't exist without a **Entity**. Generally this kind of Entities don't count with a key, so we need to use the Principal **Entity** Key to identify it. But of course is possible to a **weak entity** to have a key.

![[Chen's notation.png]]
