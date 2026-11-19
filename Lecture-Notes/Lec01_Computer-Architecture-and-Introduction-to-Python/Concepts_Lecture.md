# Lecture 1 — Computer Architecture and Introduction to Python

[Repository Guide](../../README.md) | [English](Concepts_Lecture.md) | [한국어](Concepts_Lecture.ko.md)

> **Last Updated:** 2026-11-19

> **Learning Objectives:**
> 1. Explain the components of the von Neumann architecture and the stored-program concept
> 2. Describe step by step how the control unit and the arithmetic logic unit fetch, decode, execute, and store an instruction
> 3. Compare cache memory, main memory, and secondary storage in terms of speed, price, capacity, and volatility, and explain how integers and characters are represented in bits
> 4. Explain how the bus, the operating system, and applications relate to the hardware
> 5. Compare compiled and interpreted languages in terms of execution speed and portability, and explain how a Python program is compiled into bytecode and executed and how syntax errors differ from run-time errors
> 6. Describe the uses of Python with calculation, regression analysis, and deep learning as examples

---

## Table of Contents

- [1. Overview of Learning Python Programming](#1-overview-of-learning-python-programming)
- [2. The von Neumann Architecture](#2-the-von-neumann-architecture)
  - [2.1 Components and the Stored-Program Concept](#21-components-and-the-stored-program-concept)
  - [2.2 Parts of a Real Computer](#22-parts-of-a-real-computer)
- [3. The Central Processing Unit](#3-the-central-processing-unit)
  - [3.1 The Arithmetic Logic Unit and the Control Unit](#31-the-arithmetic-logic-unit-and-the-control-unit)
  - [3.2 How an Instruction Is Executed](#32-how-an-instruction-is-executed)
- [4. Memory](#4-memory)
  - [4.1 Bits, Bytes, and Binary Numbers](#41-bits-bytes-and-binary-numbers)
  - [4.2 Representing Characters](#42-representing-characters)
- [5. Input/Output Devices and the Bus](#5-inputoutput-devices-and-the-bus)
- [6. Operating Systems and Applications](#6-operating-systems-and-applications)
- [7. Programming Languages](#7-programming-languages)
  - [7.1 Programming Languages and Machine Code](#71-programming-languages-and-machine-code)
  - [7.2 Compiled and Interpreted Languages](#72-compiled-and-interpreted-languages)
  - [7.3 How a Python Program Runs](#73-how-a-python-program-runs)
- [8. Uses of Python](#8-uses-of-python)
  - [8.1 A Calculator](#81-a-calculator)
  - [8.2 Statistical Regression Analysis](#82-statistical-regression-analysis)
  - [8.3 Deep Learning](#83-deep-learning)
- [Concept Applications](#concept-applications)
- [Summary](#summary)
- [Self-Check Questions](#self-check-questions)
- [References](#references)

---

<br>

## 1. Overview of Learning Python Programming

**Python** is a general-purpose, high-level programming language created by Guido van Rossum in the early 1990s [1]. Its concise syntax makes code easy to read, and it is a representative programming language used in a wide range of fields such as web development, data analysis, scientific computing, artificial intelligence, and education.

This course aims to develop three abilities. The first is an understanding of the Python language itself, the second is the ability to analyze programs written by others based on an understanding of the basic concepts of programming, and the third is the ability to implement new ideas as programs. To this end, the course starts from the basics of programming and builds up concepts in the order of selection structures (conditional statements), repetition structures (loops), functions, and objects, and each concept is covered together with programs that practice it. Where a comparison with the C language makes a feature of Python clearer, the difference between the two languages is also explained.

| Unit | Topic | Main Contents |
|:-----|:-----|:-----|
| Lecture 1 | Computer architecture and introduction to Python | von Neumann architecture, central processing unit, memory, input/output devices, operating systems, how programming languages are executed, uses of Python |
| Lecture 2 | Getting started with Python | Installing Python and IDLE, `print()` and `input()`, turtle graphics, variables, arithmetic operators, operator precedence |
| Lecture 3 | Kinds of data | Data types and type conversion, string concatenation, repetition, and formatting, indexing and slicing, escape sequences, list basics |
| Lecture 4 | Conditional statements | Basic control structures, relational and logical operators, `if-else` and `if-elif-else` statements, nested `if` statements, random numbers |
| Lecture 5 | Loops | The `for` statement and `range()`, traversing sequences, the accumulation pattern, the `while` statement, nested loops, `break` and `continue` |
| Lecture 6 | Functions | Defining and calling functions, parameters and arguments, return values, the scope of variables, default and keyword arguments, anonymous functions, modules |
| Lecture 7 | Lists and dictionaries | List operations, list comprehensions, two-dimensional lists, tuples and sequence types, copying lists, sets, dictionaries |
| Lecture 8 | Classes and objects | Object-oriented programming, classes and instances, constructors, methods, information hiding, getters and setters |

*Table 1. Topics and main contents of each unit*

Before writing programs in Python, this unit examines the structure of the computer, the stage on which programs run (Sections 2-5), the operating system that connects hardware and programs (Section 6), and the programming languages in which programs are written (Section 7), and then introduces examples of programs that can be built with Python (Section 8).

---

<br>

## 2. The von Neumann Architecture

### 2.1 Components and the Stored-Program Concept

Computers today differ in shape, size, and performance, but their basic structure is almost the same. This is because they follow the structure that John von Neumann described in 1945 in a report summarizing the design of a computer called EDVAC [2]. This structure is called the **von Neumann architecture**. Both the desktop computer on a desk and a smartphone follow it.

```mermaid
graph LR
    subgraph cpu["Central Processing Unit"]
        cu["Control Unit"]
        alu["Arithmetic Logic Unit"]
    end
    mem["Memory"]
    inp["Input Device"]
    outp["Output Device"]
    mem <--> cu
    mem <--> alu
    cu <--> alu
    inp --> cpu
    cpu --> outp
```

*Figure 1. Components of the von Neumann architecture and the flow of data*

The von Neumann architecture consists of the following four parts.

- **Central processing unit (CPU):** The device that performs all computation. It consists of the arithmetic logic unit, which does the calculations, and the control unit, which directs them (Section 3).
- **Memory:** Stores the instructions to execute and the data to process (Section 4).
- **Input device:** Like a keyboard or mouse, it brings information from the outside world into the computer (Section 5).
- **Output device:** Like a monitor or printer, it sends results out to the outside world (Section 5).

> **Definition:** The **stored-program concept** is the approach in which the list of instructions the computer is to perform (the program) is stored in memory in the same way as data, and the central processing unit takes the instructions out of memory one at a time and executes them. A calculating machine without this approach must have its wiring or switches changed to perform a different calculation, but a stored-program computer can do something entirely different simply by changing the program in its memory.

> **Key Point:** A single computer can be used for word processing, games, and running Python programs thanks to the stored-program concept. Programming is, in the end, the work of creating the list of instructions to put into memory.

### 2.2 Parts of a Real Computer

Opening the case of a desktop computer reveals parts that correspond to the components of the von Neumann architecture.

![Figure 2. The CPU, RAM, mainboard, and hard disk of a desktop computer](../../images/Lec01_p03.png)

*Figure 2. The CPU, RAM, mainboard, and hard disk of a desktop computer*

- **CPU:** A part that holds a semiconductor chip in a square package smaller than a palm, connected to the mainboard through the many contacts on its underside. The two chips at the upper left of the figure show the underside and the top of a CPU.
- **RAM:** A module in which several memory chips are mounted on a long board. It is used as main memory.
- **Mainboard:** A large circuit board into which the other parts are plugged. The wiring that connects modules such as the CPU, RAM, and hard disk to one another, that is, the **bus**, is on this board (Section 5).
- **Hard disk:** A secondary storage device that records data on magnetized disks (platters).

| Component of the von Neumann Architecture | Example of a Real Part |
|:-----|:-----|
| Central processing unit | CPU chip |
| Memory | RAM (main memory), hard disk or SSD (secondary storage) |
| Input device | Keyboard, mouse, touchscreen |
| Output device | Monitor, printer, speaker |
| Pathway connecting the components | Bus on the mainboard |

*Table 2. Correspondence between the components of the von Neumann architecture and real parts*

---

<br>

## 3. The Central Processing Unit

### 3.1 The Arithmetic Logic Unit and the Control Unit

All computation that a computer performs is carried out by the **central processing unit (CPU)**. Recently, the processing unit of the graphics card, the **GPU (graphics processing unit)**, is also used for computation. A GPU is designed to perform thousands of simple calculations at the same time, so it is faster than a CPU for graphics processing and deep learning (Section 8.3), which repeat the same calculation over large amounts of data. A CPU consists of the following two units.

- **Arithmetic logic unit (ALU):** Has circuits that perform **arithmetic operations** such as addition, subtraction, multiplication, and division, and **logical operations** that deal with true and false (or 1 and 0). Comparing two numbers to produce true or false is also done by the arithmetic logic unit.
- **Control unit (CU):** Reads and interprets instructions and controls the arithmetic logic unit and memory so that the computation is performed. If the arithmetic logic unit is the hand that calculates, the control unit is the conductor that tells it what to calculate.

> **[Computer Architecture]** Inside the CPU are several small, fast storage locations called **registers**. The arithmetic logic unit usually computes with values in registers and also places its results in registers. In particular, the **program counter (PC)** is a register that holds where in memory (the address) the next instruction to execute is located, and each time the control unit fetches an instruction, it changes this value to the address of the next instruction [3]. The organization of registers and the format of instructions are covered in Computer Architecture.

### 3.2 How an Instruction Is Executed

The control unit and the arithmetic logic unit process one instruction in the following five steps.

1. **Fetch:** The control unit fetches an instruction from memory.
2. **Decode:** The control unit interprets the meaning of the fetched instruction.
3. **Control:** According to the decoded instruction, the control unit moves data to the arithmetic logic unit and tells it which operation to perform.
4. **Execute:** The arithmetic logic unit performs the calculation as instructed by the control unit.
5. **Store:** The result is stored back in memory.

```mermaid
flowchart LR
    F["1. Fetch<br>get the instruction<br>from memory"] --> D["2. Decode<br>interpret the<br>instruction"]
    D --> C["3. Control<br>direct data and the operation<br>to the arithmetic logic unit"]
    C --> E["4. Execute<br>the arithmetic logic<br>unit calculates"]
    E --> S["5. Store<br>store the result<br>in memory"]
    S -->|"next instruction"| F
```

*Figure 3. The five steps of processing one instruction and their repetition*

Steps 1-3 are performed by the control unit and step 4 by the arithmetic logic unit, and in step 5 the result goes back to memory. When the processing of one instruction is finished, the CPU moves on to the next instruction and repeats the same process. This repetition is called the **instruction cycle**, and a modern CPU performs it billions of times per second.

**Example: executing `c = a + b`.** Suppose that memory address 100 holds 3, the value of `a`, address 101 holds 4, the value of `b`, and memory contains an instruction meaning add the values at addresses 100 and 101 and store the sum at address 102. The five steps proceed as follows.

| Step | Unit | What It Does | Action in This Example |
|:-----|:-----|:-----|:-----|
| 1. Fetch | Control unit | Gets the instruction | Reads the addition instruction from memory |
| 2. Decode | Control unit | Interprets the instruction | Finds out that it means add the values at addresses 100 and 101 and put the sum at address 102 |
| 3. Control | Control unit | Moves data and directs the operation | Moves 3 and 4 to the arithmetic logic unit and orders an addition |
| 4. Execute | Arithmetic logic unit | Calculates | Computes 3 + 4 = 7 |
| 5. Store | Arithmetic logic unit → memory | Stores the result | Writes 7 to address 102 (`c`) |

*Table 3. The five steps of processing the instruction corresponding to `c = a + b`*

> **Note:** Table 3 is a simplified model to aid understanding. In a real CPU, this calculation is usually split into several machine instructions, such as reading the value at address 100 into a register, reading the value at address 101 into another register, adding the values of the two registers, and writing the result to address 102, and a result is sometimes kept in a register rather than stored in memory so that the next calculation can use it immediately [3]. A single line of Python is likewise processed as many such machine instructions when it runs.

---

<br>

## 4. Memory

**Memory** stores instructions together with data. Memory is divided as follows according to its distance from the CPU.

- **Cache memory:** The memory closest to the CPU. Recent CPUs place the cache inside the chip. It performs well but is expensive, so its capacity is small. It keeps copies of data that the CPU uses often from main memory, reducing the number of trips to the slower main memory.
- **Main memory:** The memory located below cache memory, usually made of **RAM (random access memory)**. Running programs and the data they handle are loaded here.
- **Secondary storage:** The memory farthest from the CPU. Its performance is low, but so is its price, so it can provide a large capacity. Hard disks were dominant, but as memory technology developed, **flash memory** and the **SSD (solid state drive)** built from it have risen.

```mermaid
graph TD
    R["Registers<br>(inside the CPU)"] --> C["Cache memory"]
    C --> M["Main memory<br>(RAM)"]
    M --> S["Secondary storage<br>(SSD, hard disk)"]
```

*Figure 4. The levels of memory listed in order of closeness to the CPU*

Going down Figure 4, access becomes slower, the price for the same capacity becomes lower, and the capacity that can be provided becomes larger. This arrangement, with a small amount of fast, expensive memory close to the CPU and a large amount of slow, cheap memory farther away, is called the **memory hierarchy**.

Table 4 lists the representative technology used for each kind of memory along with its access time and price as of 2012 [3].

| Memory | Representative Technology | Access Time | Price per GiB (2012) | When Power Is Off |
|:-----|:-----|:-----|:-----|:-----|
| Cache memory | SRAM | 0.5-2.5 ns | 500-1,000 dollars | Contents are lost |
| Main memory | DRAM | 50-70 ns | 10-20 dollars | Contents are lost |
| Secondary storage (SSD) | Flash memory | 5,000-50,000 ns | 0.75-1.00 dollars | Contents remain |
| Secondary storage (hard disk) | Magnetic disk | 5,000,000-20,000,000 ns | 0.05-0.10 dollars | Contents remain |

*Table 4. Representative access time, price, and volatility of each kind of memory*

The ns (nanosecond) in Table 4 is one billionth of a second. The access time of a hard disk is millions to tens of millions of times that of a cache, so if all data were read from the hard disk without a hierarchy, the CPU would spend most of its time waiting.

> **Definition:** **Volatile memory** is memory whose contents are lost when the power is turned off. Cache and RAM are volatile memory.

> **Definition:** **Nonvolatile memory** is memory whose contents remain when the power is turned off. SSDs and hard disks are nonvolatile memory.

> **Key Point:** RAM loses its contents when the power is turned off, so any result of a program that must remain after the power is turned off has to be saved as a file in secondary storage. This is also why Python code is saved as a source file in Lecture 2.

### 4.1 Bits, Bytes, and Binary Numbers

Memory stores numbers, characters, pictures, and instructions alike as two distinguishable electrical states. If the two states are written as 0 and 1, all the information in memory appears as a sequence of 0s and 1s.

> **Definition:** A **bit** is the smallest unit of information, holding one of the values 0 or 1. A group of eight bits is called a byte, and main memory is usually managed by giving each byte a number (an address). The addresses 100 and 101 in Section 3.2 are such addresses.

There are $2^n$ different arrangements of 0s and 1s that n bits can form. Adding one bit produces, from each existing arrangement, one arrangement with a 0 appended and one with a 1 appended, so the number of arrangements doubles. One byte can therefore distinguish 256 values, and when these arrangements are read as nonnegative integers they represent 0 through 255.

| Number of Bits | Number of Different Arrangements | Nonnegative Integers Representable |
|:-----|:-----|:-----|
| 1 | $2^1 = 2$ | 0, 1 |
| 2 | $2^2 = 4$ | 0 through 3 |
| 4 | $2^4 = 16$ | 0 through 15 |
| 8 (1 byte) | $2^8 = 256$ | 0 through 255 |

*Table 5. Number of bits and the number of values they can distinguish*

The numbers of everyday life are written in decimal, with base 10, and numbers inside a computer are written in **binary**, with base 2. Just as the decimal number 413 means $4 \times 10^2 + 1 \times 10^1 + 3 \times 10^0$, each digit of a binary number carries, from the right, the weight $2^0 = 1$, $2^1 = 2$, $2^2 = 4$, $2^3 = 8$. Converting the binary number 1101 to decimal gives the following.

```math
1101_2 = 1 \times 2^3 + 1 \times 2^2 + 0 \times 2^1 + 1 \times 2^0 = 8 + 4 + 0 + 1 = 13
```

Conversely, to convert a decimal number to binary, divide by 2 repeatedly until the quotient becomes 0, and read the remainders backward, starting from the last one obtained. Each remainder tells whether the number at that step is even or odd, that is, the lowest bit, and dividing by 2 is the same as shifting the binary number one place to the right.

```text
13 ÷ 2 = 6  remainder 1   → 2^0 place
 6 ÷ 2 = 3  remainder 0   → 2^1 place
 3 ÷ 2 = 1  remainder 1   → 2^2 place
 1 ÷ 2 = 0  remainder 1   → 2^3 place
Reading the remainders from bottom to top gives 1101
```

*Figure 5. Repeated division converting the decimal number 13 to binary*

Binary numbers quickly become long, so **hexadecimal**, which groups four binary digits into one digit, is used alongside. Four bits have 16 values, so they correspond exactly to one hexadecimal digit, and hexadecimal digits are written with the numerals 0 through 9 and the letters A through F, which stand for 10 through 15. The largest value of one byte, 1111 1111, has 15 (F) in its first four digits and 15 (F) in its last four, so it is FF in hexadecimal and $15 \times 16 + 15 = 255$ in decimal.

Python provides notations and functions for binary and hexadecimal numbers. A number starting with `0b` is a binary integer literal, and a number starting with `0x` is a hexadecimal integer literal. `bin()` and `hex()` convert an integer into a string in binary and hexadecimal notation, and `int(string, base)` conversely converts a string written in the given base into an integer.

```pycon
>>> 0b1101
13
>>> 0xFF
255
>>> bin(13)
'0b1101'
>>> hex(255)
'0xff'
>>> int("1101", 2)
13
>>> int("ff", 16)
255
```

The first two lines show that literals written in binary and hexadecimal are the ordinary integers 13 and 255. Python stores integers in memory in binary, so whichever base a literal is written in, the same value is created, and output shows it in decimal. The result `'0b1101'` of `bin(13)` is a string enclosed in quotes, and `int()` in the last two lines interprets the string according to the base it receives as its second argument.

Missing the fact that `bin()` and `hex()` return strings rather than numbers leads to the following error.

```pycon
>>> bin(13) + 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    bin(13) + 1
    ~~~~~~~~^~~
TypeError: can only concatenate str (not "int") to str
```

The code tried to add an integer to a string, so a `TypeError` occurred (Lecture 3, Section 3.2). Binary notation is used only for showing a value to people; for calculation, use the integer 13 as is, or convert back to an integer as in `int(bin(13), 2)`.

Storage capacity is expressed in multiples of the byte. The GiB (gibibyte) in Table 4 is $2^{30}$ = 1,073,741,824 bytes, and in the same way a KiB is $2^{10}$ = 1,024 bytes and a MiB is $2^{20}$ bytes. The KB, MB, and GB often used to label storage devices usually denote powers of 10, so 1 GB is $10^9$ bytes, and 1 GiB is about 7.4% larger than 1 GB.

### 4.2 Representing Characters

Characters are also stored in bits. Each character is assigned an integer number, and that number is stored in binary; the rule that maps characters to numbers is called a **character code**. ASCII, widely used early on, numbered 128 characters, the English letters, digits, punctuation marks, and control characters, from 0 to 127. The capital letter A is 65, the lowercase letter a is 97, and the digit 0 is 48. **Unicode**, created to handle the characters of the world in a single system, assigns each character a unique number (a code point), including Hangul, Chinese characters, and emoji, and the 128 ASCII characters have the same numbers in Unicode. The number of the Hangul syllable 가 is 44032, AC00 in hexadecimal.

A Python 3 string (Lecture 3) is a sequence of Unicode characters. `ord()` returns the number of a single character, and `chr()` returns the character for a number.

```pycon
>>> ord("A")
65
>>> ord("a")
97
>>> chr(65)
'A'
>>> ord("가")
44032
>>> hex(ord("가"))
'0xac00'
>>> "A".encode("utf-8")
b'A'
>>> "가".encode("utf-8")
b'\xea\xb0\x80'
>>> len("가")
1
>>> len("가".encode("utf-8"))
3
```

The rule that converts character numbers into an actual sequence of bytes for storage is called an **encoding**. UTF-8, the most widely used, stores one character in one to four bytes depending on the size of its number. In the results above, `encode("utf-8")` converts a string into a sequence of bytes (a `bytes` object, shown as `b'...'`); A becomes the single byte `A`, and 가 becomes the three bytes `ea`, `b0`, and `80` in hexadecimal. That is why `len("가")` gives the number of characters, 1, while `len("가".encode("utf-8"))` gives the number of bytes, 3. The same sequence of bytes becomes different characters depending on the encoding used to read it, so characters are garbled when the encoding used to save text to a file differs from the one used to read it (Lecture 10).

---

<br>

## 5. Input/Output Devices and the Bus

Input/output devices are the means by which a computer communicates with the outside world.

| Kind | Examples |
|:-----|:-----|
| Input device | Mouse, keyboard, touchscreen, microphone, gamepad, motion-recognition device |
| Output device | Monitor, printer, 3D printer, speaker, beam projector, E-Ink electronic paper |

*Table 6. Examples of input devices and output devices*

The central processing unit, memory, and input/output devices must exchange data with one another. The computer's information transfer circuit used for this is called a **bus**, and the bus to which input/output devices are connected is called the **I/O bus**. Because all devices are connected to one shared pathway, adding a new device does not require running a separate wire to each of the other devices.

```mermaid
graph TB
    cpu["Central processing unit"] <--> bus["I/O bus"]
    mem["Memory"] <--> bus
    io1["I/O device"] <--> bus
    io2["I/O device"] <--> bus
```

*Figure 6. The I/O bus connecting the central processing unit, memory, and input/output devices*

> **[Computer Architecture]** By function, a bus can be divided into the address bus, which carries the location (address) of a memory cell or device, the data bus, which carries the actual data, and the control bus, which carries control signals such as read and write. When the CPU reads a value from memory, it sends the address over the address bus, sends a read signal over the control bus, and then receives the value over the data bus. The organization of buses and input/output is covered in Computer Architecture.

---

<br>

## 6. Operating Systems and Applications

An **operating system (OS)** is system software that allows applications to run on various hardware (the CPU, memory, input/output devices, and so on). Windows, Linux, macOS, and Android are operating systems, and programs that do what the user wants, such as word processors, games, and music players, are **applications**, that is, application programs.

```mermaid
graph TD
    app["Applications<br>MS Word, StarCraft, iTunes, etc."] --> os["Operating system<br>Windows, Linux, macOS, Android, etc."]
    os --> hw["Hardware<br>CPU, memory, input/output devices"]
```

*Figure 7. The layers of applications, the operating system, and hardware*

The operating system provides applications with an **API (application programming interface)** so that they can use the hardware that the operating system controls. An API is the list of functions defined by the operating system, such as opening a file or writing characters to the screen, together with the rules for using them. Because applications call the API instead of handling the hardware directly, the same application works even if the manufacturer or model of the hardware differs. When Python's `print()` displays characters on the screen, the Python interpreter likewise does not handle the display device directly but calls a function provided by the operating system.

> **[Operating Systems]** Besides wrapping the hardware in a form that applications can use easily, the operating system is responsible for process management and scheduling, which let several programs share the CPU, memory management, which gives each program its share of memory and keeps programs from intruding on one another, and the file system, which organizes the data in secondary storage into files and folders. These policies and techniques are covered in Operating Systems.

---

<br>

## 7. Programming Languages

### 7.1 Programming Languages and Machine Code

Software is made with programming languages. A **programming language** is an artificial language system created for writing programs. However, the only thing a CPU can execute directly is instructions made of 0s and 1s, that is, **machine code**. A program written in a high-level language that people can read and write easily, such as Python or C, must be translated into machine code before it runs, and programming languages are divided into two approaches according to when and how this translation is done.

### 7.2 Compiled and Interpreted Languages

- **Compiled:** A program called a **compiler** translates the entire source code into machine code that the CPU can execute, all at once, before execution. At run time, the translated machine code is executed directly.
- **Interpreted:** A program called an **interpreter** reads the source code and translates it into a form the machine can carry out, while running it, every time the application is executed.

| Approach | Languages | Execution Speed | Portability |
|:-----|:-----|:-----|:-----|
| Compiled | C, C++, Pascal, Ada | Fast, because the program is compiled in advance into machine code that the CPU can execute. | When an application is moved from the CPU and operating system it was developed for to a different CPU and operating system, the code usually cannot be used as is, so portability is low. Languages based on a virtual machine, such as C# and Java, have high portability. |
| Interpreted | BASIC, Python, Ruby, PHP, Perl | Slow, because every time the application runs, the interpreter goes through the process of translating the source code into machine code. | As long as the interpreter supports the target CPU and operating system, the application code runs in any environment without changes, so portability is high. |

*Table 7. Execution speed and portability of compiled and interpreted languages*

> **Definition:** **Portability** is the ease with which a program can be moved to and run on a computer with a different CPU or operating system. Compiled machine code is made for a specific CPU and operating system, so to run it in another environment it must be recompiled for that environment, and parts that use features that differ between operating systems must be modified.

Java and C# mix the two approaches. A compiler translates the source code not into the machine code of a specific CPU but into an intermediate form of code, and a **virtual machine** installed in each environment executes this intermediate code. As long as a virtual machine is present, the same intermediate code runs anywhere, so portability is high.

Python is a representative interpreted language. Python interpreters exist for all major operating systems, including Windows, macOS, and Linux, so a Python program written once usually runs on other operating systems without modification. Programmers also need to worry less about hardware details such as the CPU and memory, and the syntax is close to human language, which makes it familiar to beginners.

> **Note:** **Python bytecode.** The standard Python interpreter (CPython) does not convert source code directly into machine code line by line. It first compiles the entire source code into an intermediate form called **bytecode**, and the Python virtual machine interprets and executes this bytecode one instruction at a time [4]. The bytecode of a module imported from another file (Lecture 6) is saved as a `.pyc` file in the `__pycache__` folder and, as long as the source file has not changed, reused in later runs [5]. Classifying Python as an interpreted language therefore means that no machine-code executable is built in advance, and that the interpreter interprets the program at run time.

### 7.3 How a Python Program Runs

When a Python source file is run, the standard interpreter goes through the following two stages.

1. **Compilation:** It reads the entire source file, checks whether it follows the grammar, and if so converts it into bytecode. If even one place violates the grammar, it stops at this stage, so no statement is executed.
2. **Execution:** The Python virtual machine takes the bytecode instructions one at a time from the beginning and executes them. This works like the instruction cycle of Section 3.2, except that the agent that fetches and executes instructions is not the CPU but a program called the Python virtual machine. The virtual machine itself is a machine-code program executed by the CPU, so one bytecode instruction is ultimately carried out by several machine-code instructions.

```mermaid
flowchart LR
    src["Source file<br>hello.py"] --> comp["Compilation<br>grammar check"]
    comp -->|"follows the grammar"| bc["Bytecode"]
    comp -->|"syntax error"| se["SyntaxError<br>no statement is executed"]
    bc --> vm["Python virtual machine<br>executes instructions one by one"]
    vm --> out["Results of execution<br>or a run-time error"]
```

*Figure 8. How a Python source file is compiled and executed*

The `dis` module of the standard library shows bytecode in a form people can read. The following is the disassembly of `c = a + b` from Section 3.2.

```python
import dis
dis.dis("c = a + b")
```

```text
  0           RESUME                   0

  1           LOAD_NAME                0 (a)
              LOAD_NAME                1 (b)
              BINARY_OP                0 (+)
              STORE_NAME               2 (c)
              RETURN_CONST             0 (None)
```

The number at the far left is the line number in the source code, the middle column is the name of the instruction, and the right column is the value attached to the instruction and its meaning. Each instruction does the following.

- `RESUME`: Marks the point where execution of the code starts and performs no computation.
- `LOAD_NAME 0 (a)`: Finds the value bound to the name `a` and pushes it onto the top of the stack, the virtual machine's working area.
- `LOAD_NAME 1 (b)`: In the same way, pushes the value of `b` onto the stack. The stack now holds the value of `a` and the value of `b`, one on top of the other.
- `BINARY_OP 0 (+)`: Pops the two values at the top of the stack, adds them, and pushes the result back onto the stack.
- `STORE_NAME 2 (c)`: Pops the value at the top of the stack and binds it to the name `c`.
- `RETURN_CONST 0 (None)`: Marks the end of the code.

Compared with Table 3, the two `LOAD_NAME` instructions correspond to fetching the data to compute with, `BINARY_OP` to execution by the arithmetic logic unit, and `STORE_NAME` to storing the result. The Python virtual machine fetches, decodes, and executes these instructions in order from the top.

> **Note:** Bytecode is an implementation detail of CPython, so instructions may be added or changed from one Python version to another [6]. The output above is from Python 3.13, and `BINARY_OP` and `RESUME` were added in Python 3.11, so disassembling the same code in Python 3.7 shows different instruction names.

The fact that there are two stages shows in when errors are found. The following two files are wrong only in their second lines.

```python
# check1.py: the parenthesis on the second line is not closed
print("first line")
print("second line"
```

```python
# check2.py: the name on the second line is misspelled
print("first line")
print(totl)
```

Passing the contents of each file to the interpreter as standard input (`python3 < check1.py`) prints the following. When the file is run in IDLE or with `python3 check1.py`, the path of the source file appears in place of `<stdin>`, and the traceback of the second file also shows the code of the line where the error occurred.

```text
  File "<stdin>", line 2
    print("second line"
         ^
SyntaxError: '(' was never closed
```

```text
first line
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: name 'totl' is not defined
```

The first file did not even print its first line. An unclosed parenthesis is a grammatical error, so it was found at the compilation stage, no bytecode was produced, and the execution stage never began. Such an error is called a **syntax error**. The second file follows the grammar, so it was compiled into bytecode; it executed the first line, printing `first line`, and then stopped on the second line because it could not find the name `totl`. An error like this, which occurs only when execution reaches the statement, is called a **run-time error**, and in Python it is called an exception.

An error message is read from the bottom. The `SyntaxError` or `NameError` on the last line is the kind of error, the text after the colon is its description, and the `File ..., line 2` above it is the file and line where the error occurred. The full message of a run-time error is called a **traceback**, and the `most recent call last` on its first line means that, when an error occurs inside a function, the path of calls is listed from the oldest, with the last entry being where the error occurred (Lecture 6). How a program handles exceptions itself is covered in Lecture 11.

> **Key Point:** A syntax error is found at the compilation stage before execution, so no statement in the file runs. A run-time error occurs when execution reaches that statement, so the statements before it have already run.

> **Note:** **Python 2 and Python 3.** Python 3, released in 2008, intentionally contained changes that are not backward compatible with earlier versions [7]. The `print` statement of Python 2, as in `print "hello"`, became the `print()` function, and `/` between integers now produces a float, as `1/2` is 0.5, instead of the integer quotient, with the quotient computed by `//` [7]. That is why running code written for Python 2 in Python 3.13 gives errors such as `SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?`.

---

<br>

## 8. Uses of Python

### 8.1 A Calculator

With Python, one can build anything from a simple calculator to data analysis and artificial intelligence programs. The simplest example is a calculator. The following is the output of a calculator program written in Python. The program prints a separator line made of `=` and a `=` sign indicating that it is waiting for input, and when the user types `3+10*3=` as if pressing the keys of a desktop calculator, it prints the calculated result after the entered expression, `3+10*3= 39`.

```text
=============
=3+10*3=
3+10*3= 39
```

Like a desktop calculator, this program calculates in the order of input, that is, from the front. It first computes 3 + 10 = 13 and then multiplies by 3 to get 39.

However, entering the same expression into Python gives a different result, because Python, as in mathematics, computes multiplication before addition (operator precedence in Lecture 2). `>>>` indicates that Python is waiting for a command, and the line below it is the result printed by Python.

```pycon
>>> 3 + 10 * 3
33
>>> (3 + 10) * 3
39
```

In the first expression, 10 * 3 = 30 is computed first, giving 3 + 30 = 33. To get 39, as when calculating from the front, parentheses must make 3 + 10 be computed first, as in the second expression. When building a calculator program, the programmer must decide in what order the calculation is done in this way.

### 8.2 Statistical Regression Analysis

Python is widely used for collecting, storing, processing, and analyzing large amounts of data. Data whose storage size (volume), processing speed (velocity), and variety of forms (variety) are too large to handle with conventional methods is called **big data**, and Python has many libraries for handling such data (NumPy, pandas, matplotlib, and others). Statistical **regression analysis** is a representative application.

![Figure 9. Terms related to big data and a graph of a regression line fitted to data](../../images/Lec01_p11.png)

*Figure 9. Terms related to big data and a graph of a regression line fitted to data*

Regression analysis is a statistical technique that expresses as a formula how one variable (x) is related to another variable (y). The graph at the lower right of Figure 9, drawn with matplotlib, shows nine data points with x from 1 to 9 (red dots, data set) and the straight line drawn as close as possible to these points (blue line, regression). This line is called the regression line, and it shows the tendency of y to increase generally as x increases. Once the regression line is found, y can also be predicted for an x that has not yet been observed.

> **[Machine Learning]** The regression line $y = ax + b$ is usually determined by the **least squares method**. The vertical distance $y_i - (ax_i + b)$ from each data point $(x_i, y_i)$ to the line is treated as an error, and the $a$ and $b$ that minimize the sum of squared errors $\sum_i \left(y_i - (ax_i + b)\right)^2$ are chosen. Training and evaluating regression models are covered in Machine Learning.

### 8.3 Deep Learning

**Deep learning** is a machine learning method that learns the features of data by itself using artificial neural networks stacked in many layers, and Python is a language widely used for deep learning research and development (with libraries such as PyTorch and TensorFlow).

![Figure 10. A neural network with two hidden layers and images of handwritten digits](../../images/Lec01_p12.png)

*Figure 10. A neural network with two hidden layers and images of handwritten digits*

The **neural network** at the top of Figure 10 is a structure in which nodes, drawn as circles, are stacked in layers. The **input layer**, where data comes in, has 3 nodes, each of the two **hidden layers**, which perform intermediate calculations, has 4 nodes, and the **output layer**, which produces the result, has 1 node, and arrows connect every node of one layer to every node of the next layer. Each arrow carries a number called a weight, and learning is the process of adjusting these weights by looking at data. The name deep learning comes from the network being deep, with several hidden layers stacked.

The bottom of Figure 10 shows images of handwritten digits from 0 to 9. The MNIST dataset, a collection of such handwritten digits, consists of 28 × 28 pixel grayscale images, with 60,000 for training and 10,000 for testing [8]. A neural network can be trained to classify which digit an image shows by feeding it the pixel values of the image, so this is a common first example in deep learning.

> **[Deep Learning]** The weights of a neural network are learned by gradient descent, which adjusts them little by little in the direction that reduces the difference between the prediction and the correct answer, and how much to adjust each weight is computed by backpropagation, which passes the error backward from the output layer toward the input layer. Neural network architectures such as CNNs used for image classification and training techniques are covered in Deep Learning.

---

<br>

## Concept Applications

**True/False Check:**

| Statement | Judgment and Reason |
|:-----|:------------|
| In the von Neumann architecture, programs are stored in a separate device from data. | **F.** In the stored-program concept, instructions and data are stored in the same memory. |
| Decoding an instruction is done by the arithmetic logic unit. | **F.** Fetching, decoding, and controlling the arithmetic logic unit are done by the control unit, and the arithmetic logic unit executes the calculation it is told to do. |
| Cache memory is faster than main memory but more expensive for the same capacity. | **T.** That is why only a small cache is placed close to the CPU, holding copies of frequently used data from main memory. |
| A document kept only in RAM remains even after the power is turned off. | **F.** RAM is volatile, so its contents are lost when the power is turned off. Data that must remain is saved as a file in secondary storage. |
| Applications use the hardware through the API provided by the operating system. | **T.** Because applications do not handle the hardware directly, the same application works even on different hardware. |
| Compiled languages are generally more portable than interpreted languages. | **F.** Compiled machine code is tied to a specific CPU and operating system, so portability is generally low. Interpreted languages, which run wherever an interpreter exists, are more portable. |
| In Python, the value of `3 + 10 * 3` is 39. | **F.** Multiplication is computed first, so the value is 33. To get 39, write `(3 + 10) * 3`. |
| The value of `bin(13) + 1` is the binary number 1110. | **F.** `bin()` returns the string `'0b1101'`, which cannot be added to an integer, so a `TypeError` occurs. Use the integer 13 as is for calculation. |
| Even if the third line of a source file has an unclosed parenthesis, the first and second lines run. | **F.** A syntax error is found at the compilation stage before execution, so no line runs. |
| Encoding the string `"가나"` in UTF-8 gives 2 bytes. | **F.** A Hangul syllable takes 3 bytes per character in UTF-8, so the result is 6 bytes. The number of characters, `len("가나")`, is 2. |

---

<br>

## Summary

| Concept | Key Summary |
|:-----|:----------|
| von Neumann architecture | The structure described by von Neumann in 1945, consisting of the central processing unit, memory, input devices, and output devices, which most computers today follow. |
| Stored-program concept | Instructions are stored in memory together with data and executed one at a time, so changing only the program makes the computer do something else. |
| Central processing unit | Performs all computation and consists of the arithmetic logic unit, which performs arithmetic and logical operations, and the control unit, which controls it. |
| Instruction cycle | One instruction is processed in five steps, fetch, decode, control, execute, and store, and the process repeats with the next instruction. |
| Memory hierarchy | Cache memory, main memory (RAM), and secondary storage (SSD, hard disk) become slower, cheaper, and larger in that order. |
| Volatility | Cache and RAM lose their contents when the power is turned off, so data that must remain is saved as a file in secondary storage. |
| Bits and bytes | A bit is the smallest unit of information, holding the value 0 or 1; 8 bits make 1 byte, and n bits distinguish $2^n$ values. |
| Binary and hexadecimal | Each digit of a binary number carries a power of 2 as its weight, and four binary digits are grouped into one hexadecimal digit. |
| Character codes and encodings | Unicode assigns a number to each character, and UTF-8 stores that number as a sequence of one to four bytes. |
| Input/output devices and the bus | Input/output devices are the means of communicating with the outside world, and the bus is the information transfer circuit connecting the central processing unit, memory, and input/output devices. |
| Operating system | System software that lets applications run on hardware and provides hardware functions through an API. |
| Compiled approach | Translating to machine code before execution makes programs fast, but moving them to another CPU and operating system is hard, so portability is low. |
| Interpreted approach | The interpreter translates on every run, which is slow, but programs run anywhere an interpreter exists, so portability is high. |
| Execution of Python | The standard interpreter compiles source code into bytecode and then runs it on a virtual machine. |
| Syntax errors and run-time errors | A syntax error is found at the compilation stage, so no statement runs, while a run-time error occurs when execution reaches the statement. |
| Uses of Python | Python is used widely, from simple programs such as calculators to data analysis such as regression and deep learning with neural networks. |

---

<br>

## Self-Check Questions

1. **von Neumann architecture:** Name the four components of the von Neumann architecture, and explain why the same computer can do something else in this architecture simply by changing the program.

   <details>
   <summary>Answer</summary>

   The four components are the central processing unit (the arithmetic logic unit and the control unit), memory, input devices, and output devices. Under the stored-program concept, the program, a list of instructions, is stored in memory together with data, and the central processing unit takes the instructions out one at a time and executes them, so changing only the program in memory, without rewiring, changes what the computer does.

   </details>

2. **Instruction cycle:** List in order the five steps of processing one instruction, and state which unit performs each step.

   <details>
   <summary>Answer</summary>

   The order is fetch, decode, control (moving data to the arithmetic logic unit and directing the operation), execute, and store. Fetch, decode, and control are performed by the control unit, execute by the arithmetic logic unit, and in the store step the result is written to memory.

   </details>

3. **Arithmetic logic unit and control unit:** Which unit does each of the following: comparing which of two numbers is larger, and fetching the next instruction to execute from memory?

   <details>
   <summary>Answer</summary>

   Comparison is an operation that produces true or false as its result, so it is performed by the arithmetic logic unit. Fetching an instruction is the job of the control unit.

   </details>

4. **Memory hierarchy:** List cache memory, main memory, and secondary storage in order of access speed from fastest, and explain why memory is arranged in a hierarchy instead of using a single kind.

   <details>
   <summary>Answer</summary>

   The order is cache memory, main memory, and secondary storage. Fast memory is expensive for the same capacity and slow memory is cheap, so placing a small amount of fast, expensive memory close to the CPU and a large amount of slow, cheap memory farther away provides both a large capacity and fast access at low cost.

   </details>

5. **Volatility:** Using a property of memory, explain why the content being written in a word processor disappears if the computer is turned off without saving the document.

   <details>
   <summary>Answer</summary>

   The document being written exists only in main memory (RAM) as data of a running program. RAM is volatile, so its contents are lost when the power is turned off. To keep the content, it must be saved as a file, which records it in nonvolatile secondary storage.

   </details>

6. **Bus and operating system:** Compare what the bus and the operating system each connect.

   <details>
   <summary>Answer</summary>

   The bus is a physical information transfer circuit that lets hardware devices such as the central processing unit, memory, and input/output devices exchange data. The operating system is system software placed between applications and hardware, and through its API it lets applications use the hardware.

   </details>

7. **Compiling and interpreting:** An executable file of a program written in C often does not run as is on another operating system, while a Python source file usually does. Explain why.

   <details>
   <summary>Answer</summary>

   C is a compiled language, so its executable file consists of machine code for a specific CPU and operating system and must be recompiled for another environment. Python is an interpreted language, so the interpreter installed in each environment interprets the source code every time it runs, and the same source file runs as long as the interpreter supports that environment.

   </details>

8. **Order of calculation:** What values do a calculator that computes from the front and Python each produce for the expression `2 + 4 * 5`? How must the expression be changed in Python to get the same value as the calculator?

   <details>
   <summary>Answer</summary>

   The calculator that computes from the front produces 2 + 4 = 6 and 6 × 5 = 30. Python performs the multiplication first, 4 * 5 = 20, and then 2 + 20 = 22. To get 30 in Python, use parentheses, as in `(2 + 4) * 5`.

   </details>

9. **Binary conversion:** Convert the decimal number 45 to binary by repeatedly dividing by 2, and verify the result with the weight of each digit. Also write an expression that checks this result in Python.

   <details>
   <summary>Answer</summary>

   45 ÷ 2 = 22 remainder 1, 22 ÷ 2 = 11 remainder 0, 11 ÷ 2 = 5 remainder 1, 5 ÷ 2 = 2 remainder 1, 2 ÷ 2 = 1 remainder 0, and 1 ÷ 2 = 0 remainder 1. Reading the remainders from bottom to top gives 101101, and checking gives 32 + 8 + 4 + 1 = 45. In Python, `bin(45)` gives `'0b101101'` and `int("101101", 2)` gives 45.

   </details>

10. **Kinds of errors:** What does running the following file print? How does the result change if the third line is `print(total`, with the parenthesis left unclosed?

    ```python
    print("시작")
    total = 10
    print(totl)
    ```

    <details>
    <summary>Answer</summary>

    `시작` is printed, and then `NameError: name 'totl' is not defined` occurs on the third line (from Python 3.10 on, `Did you mean: 'total'?`, which suggests a similar name, is appended to the message). The file follows the grammar, so it is compiled, the first and second lines run, and the name cannot be found when execution reaches the third line. If the parenthesis on the third line were left unclosed, `SyntaxError: '(' was never closed` would occur at the compilation stage, so not even `시작` would be printed.

    </details>

---

<br>

## References

1. Python Software Foundation, "History and License," *Python 3 Documentation*, accessed Nov. 4, 2026. https://docs.python.org/3/license.html
2. J. von Neumann, "First Draft of a Report on the EDVAC," Moore School of Electrical Engineering, University of Pennsylvania, Philadelphia, PA, USA, Jun. 1945.
3. D. A. Patterson and J. L. Hennessy, *Computer Organization and Design: The Hardware/Software Interface*, 5th ed. Waltham, MA, USA: Morgan Kaufmann, 2014.
4. Python Software Foundation, "Glossary," *Python 3 Documentation*, accessed Nov. 4, 2026. https://docs.python.org/3/glossary.html
5. Python Software Foundation, "Modules," *The Python Tutorial*, accessed Nov. 4, 2026. https://docs.python.org/3/tutorial/modules.html
6. Python Software Foundation, "dis: Disassembler for Python bytecode," *The Python Standard Library*, accessed Nov. 19, 2026. https://docs.python.org/3/library/dis.html
7. Python Software Foundation, "What's New In Python 3.0," *Python 3 Documentation*, accessed Nov. 19, 2026. https://docs.python.org/3/whatsnew/3.0.html
8. Y. LeCun, L. Bottou, Y. Bengio, and P. Haffner, "Gradient-based learning applied to document recognition," *Proceedings of the IEEE*, vol. 86, no. 11, pp. 2278-2324, 1998.
