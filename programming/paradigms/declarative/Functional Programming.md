# Functional Programming

Is made up of a string of function calls, where each program section can be understood as a function. In functional programming, the functions can take on different forms.

This subsidiary form of declarative programming is very important for computer science in general – and at the same time can be used for a wide range of specific purposes. The special handling of functions enables programmers using the functional method to create and use extensive calculation rules made up of functions.

#### Pure Functions
Only can invoque **pure** funcitons.
- Dont's change a data base
- Don't create a file
- **Don't modify the system**

#### Impure Funcitons
Can invoque a **pure** and **impure**.

### Side Effects
Is every observable change out of the system.

In Functional Programming we're also trying to avois the side effects. But it's inevitable, the thing is that we've to reduce it to the minimum. 
![[Secundary Effects.png]]

### Highe-Order Functions (HOF)
Are functions that **take** another **function as an argument** or **return a funcion**.


### [[lambda functions]]
`Needs some improvements`
They're annonym functions.


### Immutability
- **Advantajes**
	- Once created can be alterateed.
	- Makes it easy to create [[functional programming#Pure Functions|Pure Functions]].
	- Makes it seay to use [[threads]] and concurrency.
- Disadvantajes
	- Every modification needs a new instance of data.
	- Requeries especial attention in design.
	- Mutable objects out of reach.

