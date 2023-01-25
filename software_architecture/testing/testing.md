# Testing
It is a practice that help us to check if the $project$ that we are developing works properly, if it doesn't we have done some changes that are changes our $project$ behavior.

Testing help us to:
- Verify our apps requirments
- Is a way to show us the way we expect it to work. Of course is a good way to documentate the code with some examples.
- Help us in the design **[[test driven development|Test-Driven-Development]]**.
- It's easeier to refactorize.


###  Tests
They can be automatic or manual, this will only change the development time. It's always preferable to use Automatic Test.
- **Benefits**: They are automatic, fast, and viable.
- **Cons**: Not always simple, development time.


### Test Types
Used to test the project at different abstraction levels.

- **Unit Test**: Verifies the properly work of an specific part(a class or a method) of the $project$.
- **Integration**: Test how different parts of our application are connected.
	- script-API
	- script-dataBase
	- script-etc...
 - **Funcitonal**: Test a complete part of the system, could be the User Interface, a specific branch, etc.
- **End to End**: A complete test of an action in the project (request, proccess and saing data) or in some cases the complete project behavior.
- **Stress**: Tests the effitiency of the project excecuting lots of processes and requests at the same time.

