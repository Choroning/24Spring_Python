# Lecture 3 Solutions — Data Types

[Repository Guide](../../README.md) | [English](Solutions.md) | [한국어](Solutions.ko.md)

> **Last Updated:** 2026-11-04

---

<br>

## Table of Contents

- [Exercise 1: Greeting the Turtle](#exercise-1-greeting-the-turtle)
- [Exercise 2: A Friendly Conversation Program](#exercise-2-a-friendly-conversation-program)
- [Exercise 3: Making a List of Friends](#exercise-3-making-a-list-of-friends)
- [Exercise 4: Average of Four Numbers](#exercise-4-average-of-four-numbers)

---

<br>

## Exercise 1: Greeting the Turtle

**Problem:** Read a name through a turtle graphics dialog, write a greeting containing the name, and draw a square whose sides are 100 long. The full problem and sample run are in [Exercise 1](Exercises.md#exercise-1-greeting-the-turtle).

### Solution

**Approach:** Input is handled with `turtle.textinput()` and output with the turtle's `write()` ([Lecture 3, Section 7](Concepts_Lecture.md#7-string-input-and-output-in-turtle-graphics)). The greeting is made by concatenating the input name between two fixed strings with `+` ([Lecture 3, Section 4.1](Concepts_Lecture.md#41-concatenation)). The square is drawn by repeating four times the action of turning left by 90 degrees and moving forward by 100.

- **Input:** `textinput()` returns the input name as a string, so it can be used in the concatenation directly without conversion.
- **Greeting:** `"안녕하세요? " + s + "씨, 터틀 인사드립니다."` is the concatenation of three strings. `+` does not insert spaces, so the space after the question mark is put directly into the first string.
- **Square:** The turtle starts at the origin (0, 0) facing right (east). `t.left(90)` turns the turtle 90 degrees to the left in place, and `t.forward(100)` moves it 100 in the direction it faces while drawing a line.
- **Keeping the window:** `turtle.done()` on the last line keeps the drawing window from closing immediately even when the program is run from a command window ([Lecture 3, Section 7.2](Concepts_Lecture.md#72-string-output)).

**Code:**

```python
import turtle
t = turtle.Turtle()
t.shape("turtle")
s = turtle.textinput("", "이름을 입력하시오: ")
t.write("안녕하세요? " + s + "씨, 터틀 인사드립니다.")
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
turtle.done()
```

**Output:** If `홍길동` is entered in the dialog, `안녕하세요? 홍길동씨, 터틀 인사드립니다.` is written at the origin, and the turtle moves in the following order, draws a square to the upper left of the origin, and returns to the origin. The greeting is written to the right from the origin, the position at the moment `write()` was called, so it starts at the lower right corner of the square, as in Figure 1.

| Commands | Direction Faced | Change of Position |
|:-----|:-----|:-----|
| `t.left(90)`, `t.forward(100)` | Up | (0, 0) → (0, 100) |
| `t.left(90)`, `t.forward(100)` | Left | (0, 100) → (-100, 100) |
| `t.left(90)`, `t.forward(100)` | Down | (-100, 100) → (-100, 0) |
| `t.left(90)`, `t.forward(100)` | Right | (-100, 0) → (0, 0) |

*Table 1. Direction and position of the turtle while drawing the square*

> **Note:** In turtle graphics coordinates, the center of the window is the origin (0, 0), x increases to the right, and y increases upward. This is the same as the coordinate plane of mathematics.

---

<br>

## Exercise 2: A Friendly Conversation Program

**Problem:** Read a name and an age, and print a greeting, the length of the name, and the age next year. The full problem and sample run are in [Exercise 2](Exercises.md#exercise-2-a-friendly-conversation-program).

### Solution

**Approach:** The name is used as a string as is, while the age is used in a computation (age + 1), so it is converted to an integer ([Lecture 3, Section 3.1](Concepts_Lecture.md#31-converting-strings-to-numbers)). The length of the name is obtained with `len()` ([Lecture 3, Section 5.3](Concepts_Lecture.md#53-string-length-and-immutability)).

**Code:**

```python
print('안녕하세요?')
name = input('이름이 어떻게 되시나요? ')

print('만나서 반갑습니다. ' + name + "씨")
print('이름의 길이는 다음과 같군요:', end=' ')
print(len(name))

age = int(input("나이가 어떻게 되나요? "))
print("내년이면", str(age+1), "이 되시는군요.")
```

- **Lines 1-2:** Print a greeting ("Hello?"), read the name ("What is your name?"), and store it in `name`. Double and single quotes are mixed, but strings created in the two ways are the same.
- **Line 4:** Concatenates three strings and prints `만나서 반갑습니다. 홍길동씨` ("Nice to meet you, Hong Gildong").
- **Line 5:** `print()` normally outputs a newline character after its output, but with `end=' '` it outputs one space instead of the newline. So the output of the next `print()` continues on the same line ("The length of your name is:").
- **Line 6:** `len(name)` is the number of characters in the name. `홍길동` consists of three Hangul characters, so it is 3. `len()` counts characters, not bytes.
- **Line 8:** The inner `input()` runs first and returns the string `"21"` ("How old are you?"), and the outer `int()` converts it to the integer 21 and stores it in `age`.
- **Line 9:** `age+1` is 22, and `str()` makes it the string `"22"`. `print()` inserts spaces between the three comma-separated values, so `내년이면 22 이 되시는군요.` ("Next year you will be 22.") is printed.

**Output:**

```text
안녕하세요?
이름이 어떻게 되시나요? 홍길동
만나서 반갑습니다. 홍길동씨
이름의 길이는 다음과 같군요: 3
나이가 어떻게 되나요? 21
내년이면 22 이 되시는군요.
```

> **Note:** The `str()` on line 9 is unnecessary, because `print()` converts the values it receives with commas to strings itself ([Lecture 3, Section 3.2](Concepts_Lecture.md#32-converting-numbers-to-strings)). To print a natural sentence without the space between `22` and `이`, use a format specifier ([Lecture 3, Section 4.3](Concepts_Lecture.md#43-string-formatting)). `age + 1` must be enclosed in parentheses so that the addition is computed before the `%` operation.
> ```python
> age = int(input("나이가 어떻게 되나요? "))
> print("내년이면 %d살이 되시는군요." % (age + 1))
> ```
> ```text
> 나이가 어떻게 되나요? 21
> 내년이면 22살이 되시는군요.
> ```

---

<br>

## Exercise 3: Making a List of Friends

**Problem:** Read the names of five friends, store them in a list, and print it. The full problem and sample run are in [Exercise 3](Exercises.md#exercise-3-making-a-list-of-friends).

### Solution

**Approach:** Create an empty list, and each time a name is read, add it to the end of the list with `append()` ([Lecture 3, Section 8.2](Concepts_Lecture.md#82-adding-elements)). After reading five times, print the whole list.

- **Empty list:** `friend_list = [ ]` creates a list with no elements. The space between the brackets has no meaning.
- **Input and adding:** `friend = input(...)` and `friend_list.append(friend)` are repeated five times. A new name is stored in `friend` each time, but the previous names are already in the list, so they are not lost.
- **Output:** Printing a list with `print()` prints it in list notation, including the brackets and quotes. The elements are in the order in which they were added.

**Code:**

```python
friend_list = [ ]

friend = input("친구의 이름을 입력하시오: ")
friend_list.append(friend)

friend = input("친구의 이름을 입력하시오: ")
friend_list.append(friend)

friend = input("친구의 이름을 입력하시오: ")
friend_list.append(friend)

friend = input("친구의 이름을 입력하시오: ")
friend_list.append(friend)

friend = input("친구의 이름을 입력하시오: ")
friend_list.append(friend)

print(friend_list)
```

**Output:**

```text
친구의 이름을 입력하시오: 홍길동
친구의 이름을 입력하시오: 강감찬
친구의 이름을 입력하시오: 이순신
친구의 이름을 입력하시오: 권율
친구의 이름을 입력하시오: 정약용
['홍길동', '강감찬', '이순신', '권율', '정약용']
```

> **Note:** Instead of writing the same two lines five times, a loop lets the code be written once with only the count specified. `for i in range(5):` runs the two indented lines five times; loops are covered in Lecture 5. The output is the same as above.
> ```python
> friend_list = []
> for i in range(5):
>     friend = input("친구의 이름을 입력하시오: ")
>     friend_list.append(friend)
> print(friend_list)
> ```

---

<br>

## Exercise 4: Average of Four Numbers

**Problem:** Read four numbers, store them in a list, and print their average. The full problem and sample run are in [Exercise 4](Exercises.md#exercise-4-average-of-four-numbers).

### Solution

**Approach:** As in Exercise 3, add values one at a time to an empty list, but since the average must be computed, convert each input to an integer with `int()` before adding it. The average is the sum of the elements divided by the number of elements.

- **Sum:** The built-in function `sum()` returns the total of all numbers in a list. `sum([10, 20, 30, 40])` is 100.
- **Division:** `/` always returns a floating-point number even when the division is exact (Lecture 2), so 100 / 4 is `25.0`.
- **Output:** `print("평균:", ...)` inserts one space between the two values and prints `평균: 25.0` ("Average: 25.0").

**Code:**

```python
nlist = []

n = int(input("숫자입력:"))
nlist.append(n)
n = int(input("숫자입력:"))
nlist.append(n)
n = int(input("숫자입력:"))
nlist.append(n)
n = int(input("숫자입력:"))
nlist.append(n)

print("평균:", sum(nlist) / 4)
```

**Output:**

```text
숫자입력:10
숫자입력:20
숫자입력:30
숫자입력:40
평균: 25.0
```

An average that is not an integer is also computed exactly. Entering 1, 2, 3, and 5 gives a sum of 11, so 11 / 4 = 2.75 is printed as follows.

```text
숫자입력:1
숫자입력:2
숫자입력:3
숫자입력:5
평균: 2.75
```

> **Caution:** If the strings are put into the list as is without `int()`, `sum()` cannot add strings and a `TypeError` occurs. Also, writing `sum(nlist) / len(nlist)` instead of writing the divisor 4 directly means the code need not be changed when the number of inputs changes.
