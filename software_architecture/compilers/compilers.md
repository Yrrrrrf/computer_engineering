# [Compiler](https://en.wikipedia.org/wiki/Compiler)

Is a [[software]] that transforms **source code** written in a [[programming language]] (**source language**) into another computer language (**target language**), with the latter often having a binary form known as object code.

The most common reason for converting source code is to create an executable program.


## phases
A compiler is usually divided into several phases, each of which transforms the program in some way. The phases are usually executed in the order shown below, but some phases may be executed in parallel, and some may be omitted.

### Lexical analysis
The first phase of a compiler is called the **lexical analysis** or **lexing**. The input is a sequence of characters called the **source character sequence**. The output is a sequence of tokens called the **token sequence**. The lexical analyzer is often implemented as a **finite state machine**.

### Syntax analysis
The second phase of a compiler is called the **syntax analysis** or **parsing**. The input is the token sequence from the lexical analyzer. The output is a **syntax tree** or **abstract syntax tree** (AST). The syntax analyzer is often implemented as a **recursive descent parser**.

### Semantic analysis
The third phase of a compiler is called the **semantic analysis**. The input is the syntax tree from the syntax analyzer. The output is a **symbol table**. The semantic analyzer is often implemented as a **recursive descent parser**.
