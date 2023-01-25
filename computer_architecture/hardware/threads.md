# Threads
Is the **smallest sequence of programmed instructions** that can be managed independently by a [scheduler](https://en.wikipedia.org/wiki/Scheduling_(computing) "Scheduling (computing)"), which is typically a part of the [[operating system]].

The implementation of **threads** and **processes** differs between operating systems, but in most cases a thread is a component of a process. The multiple threads of a given process may be executed [[concurrent programming]] (via multithreading capabilities), sharing resources such as [[memory]], while different processes do not share these resources.

![[threads.png]]

### states
1. **Create**: Can't run yet
2. **Executable/Ready**: Waits for execute
3. **Excetuting**: Executes the process.
4. **Blocked**: Waits until gets the code that needs to execute the process, if it don't recives data the thread aborts that process.
5. **Finished**: The execution had done & can't be restarted.
