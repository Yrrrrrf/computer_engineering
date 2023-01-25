# Object Oriented Programming
Is a programming paradigm based on the concept of Objects, which may contain data, in the form of fields, often known as **attributes**; and **code**, in the form of procedures, often known as methods.

There are comncepts that are the **pillar of this Programming paragim**. Does are:
-    **Abstraction:** It refers to, providing only essential information to the outside world and hiding their background details.
-    **[[#Encapsulation]]:** Is a process of binding data members (variables, properties) and member functions into a single unit. It is also a way of restricting access to certain properties or component.
-    **[[#Inheritance]]:** Is the ability to create a new class from an existing class is called Inheritance. Using inheritance, we can create a Child class from a Parent class such that it inherits the properties and methods of the parent class and can have its own additional properties and methods.
-    **[[#Polymorphism]]:** The word polymorphism means having many forms. Typically, polymorphism occurs when there is a hierarchy of classes and they are related by inheritance. C++ polymorphism means that a call to a member function will cause a different function to be executed depending on the type of object that invokes the function.

![[Object.png]]


### Encapsulation
Sometimes referred to as the **first pillar** of [[object oriented programming]].
A class or struct can specify how accessible each of its members is to code outside of the class or struct. Methods and variables that aren't intended to be used from outside of the class or assembly can be hidden to limit the potential for coding errors or malicious exploits.

### Inheritance

Known as the  **second pillar** of [[object oriented programming]].
Inheritance enables you to create new classes that reuse, extend, and modify the behavior defined in other classes. The class whose members are inherited is called the $base$ $class$, and the class that inherits those members is called the $derived$ $class$.


### Polymorphism

Is often referred to as the **third pillar** of [[object oriented programming]].
Polymorphism is a Greek word that means $many-shaped$ and it has two distinct aspects:
- At run time, objects of a $derived$ $class$ may be treated as objects of a $base$ $class$ in places such as method parameters and collections or arrays. When this polymorphism occurs, the object's declared type is no longer identical to its run-time type.
- Base classes may define and implement [virtual](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/virtual) _methods_, and derived classes can [override](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/override) them, which means they provide their own definition and implementation.
