# Event-Driven Programming

In this [[programming paradigms]] the [[control structures|flow of the program]] is determined by [[events]] such as user actions (mouse, clicks, key presses), [[sensor]] outputs, or **message passing** from other programs or [[threads]].

Is the dominant [[programming paradigms]] used in [[graphical user interface|graphical user interfaces]] and other applications (e.g., JavaScript [[web apps|web applications]] that are centered on performing certain actions in response to user input. In an event-driven application, there is generally a **main loop** that listens for events and then triggers a **callback function** when one of those events is detected.In [[embedded system|embedded systems]], the same may be achieved using [hardware interrupts](https://en.wikipedia.org/wiki/Hardware_interrupt "Hardware interrupt") instead of a constantly running **main loop**.

![[Pasted image 20221216125851.png]]