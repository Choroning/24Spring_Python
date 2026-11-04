# Lab 5 Explanation — Loops

[Repository Guide](../../README.md) | [English](Lab-Explanation.md) | [한국어](Lab-Explanation.ko.md)

> **Last Updated:** 2026-11-04

> **Learning Objectives:**
> 1. Iterate over a list and over the integer sequence made by `range()` with a `for` statement
> 2. Build a desired integer sequence with the start, stop, and step of `range()`
> 3. Accumulate values in a variable inside a loop to compute a sum
> 4. Write a `while` statement that repeats until its condition becomes false, and convert between `while` and `for` statements
> 5. Change the flow of a loop with `break` and `continue`

---

## Table of Contents

- [1. Lab Layout and How to Run](#1-lab-layout-and-how-to-run)
- [2. The for Statement and range()](#2-the-for-statement-and-range)
  - [2.1 A for Statement over a List](#21-a-for-statement-over-a-list)
  - [2.2 range() and Indices](#22-range-and-indices)
  - [2.3 Start, Stop, and Step](#23-start-stop-and-step)
  - [2.4 Counting Down](#24-counting-down)
  - [2.5 Comparing range() and a List](#25-comparing-range-and-a-list)
- [3. Accumulation and Repeated Drawing with Loops](#3-accumulation-and-repeated-drawing-with-loops)
  - [3.1 The Sum from 1 to n](#31-the-sum-from-1-to-n)
  - [3.2 The Sum of the Digits](#32-the-sum-of-the-digits)
  - [3.3 Repeating Circles with Turtle Graphics](#33-repeating-circles-with-turtle-graphics)
- [4. The while Statement](#4-the-while-statement)
  - [4.1 Password Check](#41-password-check)
  - [4.2 A Running Sum with a while Statement](#42-a-running-sum-with-a-while-statement)
  - [4.3 Converting a for Statement to a while Statement](#43-converting-a-for-statement-to-a-while-statement)
- [5. break and continue](#5-break-and-continue)
  - [5.1 break](#51-break)
  - [5.2 continue](#52-continue)
- [Summary](#summary)
- [Self-Check Questions](#self-check-questions)

---

<br>

## 1. Lab Layout and How to Run

This code was written while following [Lecture 5, Loops](../../Lecture-Notes/Lec05_Loops/Concepts_Lecture.md). Section 2 covers the `for` statement and `range()`, Section 3 covers programs that accumulate sums in a loop and turtle graphics, Section 4 covers the `while` statement, and Section 5 covers `break` and `continue`.

```text
Coursework/Lab05_Loops/
├── Lab-Explanation.ko.md          # This document (Korean)
├── Lab-Explanation.md             # This document (English)
├── Lab_ForList.py                 # 2.1 A for statement over a list
├── Lab_ForRangeIndex.py           # 2.2 range() and indices
├── Lab_RangeStep.py               # 2.3 Start, stop, and step
├── Lab_RangeCountdown.py          # 2.4 Counting down
├── Lab_RangeAndListIteration.py   # 2.5 Comparing range() and a list
├── Lab_SumToN.py                  # 3.1 The sum from 1 to n
├── Lab_DigitSum.py                # 3.2 The sum of the digits
├── Lab_TurtleCircles.py           # 3.3 Repeating circles with turtle graphics
├── Lab_PasswordCheck.py           # 4.1 Password check
├── Lab_WhileSumToN.py             # 4.2 A running sum with a while statement
├── Lab_ForToWhile.py              # 4.3 Converting a for statement to a while statement
├── Lab_Break.py                   # 5.1 break
└── Lab_Continue.py                # 5.2 continue
```

*Figure 1. Directory layout of Lab 5*

All programs use only the standard library and run as they are under Python 3. `Lab_TurtleCircles.py` opens a graphics window with the standard `turtle` module. Each file begins with a documentation string (docstring) that records the file name, a one-line description, the author, and the date written, and the code blocks in this document omit that part.

```bash
cd Coursework/Lab05_Loops
python3 Lab_ForList.py
```

---

<br>

## 2. The for Statement and range()

### 2.1 A for Statement over a List

**Code:** [Lab_ForList.py](Lab_ForList.py)

```python
for i in [1, 2, 3, 4, 5]:
    print("i =", i)
```

- **Form of the `for` statement:** An indented block follows the line `for variable in iterable:`. The loop takes the elements of the iterable one at a time, assigns each to the loop variable `i`, and runs the block once, repeating until no elements remain.
- **Number of iterations:** The list has five elements, so the block runs five times and `i` becomes 1, 2, 3, 4, and 5 in turn.
- **Output:** When `print()` receives several values separated by commas, it prints them with one space between them, which gives `i = 1`.

**Output:**

```text
i = 1
i = 2
i = 3
i = 4
i = 5
```

### 2.2 range() and Indices

**Code:** [Lab_ForRangeIndex.py](Lab_ForRangeIndex.py)

```python
a = [1, 2, 3, 4, 5]

for i in range(5):
    print("i =", i+1)
    print("i =", a[i])
```

- **`range(5)`:** Produces the integers from 0 up to but not including 5, that is, 0, 1, 2, 3, and 4. The stop value 5 is excluded, so there are exactly five of them.
- **Access by index:** List indices start at 0, so `a[0]` is 1 and `a[4]` is 5. While `i` runs through 0-4, `a[i]` refers to the list elements from first to last.
- **Comparing the two outputs:** `i+1` is the index plus 1, and `a[i]` is the element at that position. Because the list holds the integers 1 to 5, the two values are equal and each line is printed twice.

**Output:**

```text
i = 1
i = 1
i = 2
i = 2
i = 3
i = 3
i = 4
i = 4
i = 5
i = 5
```

### 2.3 Start, Stop, and Step

**Code:** [Lab_RangeStep.py](Lab_RangeStep.py)

```python
for i in range(4):
    print(i)
a="*"*5
print(a)
for j in range(0,4,1): #0 시작, 3까지, 1씩 증가
    print(j)
```

- **The three arguments of `range()`:** `range(start, stop, step)` produces integers from the start value, adding the step each time, up to just before the stop value. With a single argument, the start is 0 and the step is 1, so `range(4)` and `range(0, 4, 1)` produce the same sequence 0, 1, 2, 3. The comment says "start at 0, up to 3, increase by 1".
- **String repetition:** `"*" * 5` is `"*****"`, the string `"*"` joined five times. The symbol `*` means multiplication between numbers and repetition between a string and an integer.

**Output:**

```text
0
1
2
3
*****
0
1
2
3
```

### 2.4 Counting Down

**Code:** [Lab_RangeCountdown.py](Lab_RangeCountdown.py)

```python
for i in range(10, 1, -1):
    print(i)
```

- **Negative step:** With a step of -1, the sequence starts at 10 and decreases by 1, stopping at 2, just before the stop value 1 is reached. The stop value is excluded regardless of the direction.
- **Result:** Nine values, 10, 9, 8, 7, 6, 5, 4, 3, and 2, are printed one per line. To print down to 1, `range(10, 0, -1)` must be used.

**Output:**

```text
10
9
8
7
6
5
4
3
2
```

### 2.5 Comparing range() and a List

**Code:** [Lab_RangeAndListIteration.py](Lab_RangeAndListIteration.py)

```python
#for i in _____: => _____; range(s, stop, increase), list
#배웠던 내용 리뷰

for i in range(0,10,1):
    print(i)

for j in [0,1,2,3,4,5,6,7,8,9]:
    print(j)

a_list=[]
for i in range(0,10,1):
    a_list.append(i)
```

- **Comments:** The first comment is a review note ("review of what was learned") that the iterable after `for` may be `range(start, stop, step)` or a list.
- **Two forms of the same iteration:** The first `for` statement iterates over `range(0, 10, 1)`, and the second over a list that spells out 0-9. Both iterables give the same integers in the same order, so the outputs are also the same. When there are many elements or they follow a rule, `range()` is shorter and less error-prone.
- **Filling a list with `append()`:** After the empty list `a_list` is created, each iteration adds one element at the end with `append(i)`. When the loop ends, `a_list` is `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`. This part prints nothing, so it does not appear on the screen.

**Output:** The integers 0 to 9 are printed one per line, twice in a row (20 lines in all).

---

<br>

## 3. Accumulation and Repeated Drawing with Loops

### 3.1 The Sum from 1 to n

**Code:** [Lab_SumToN.py](Lab_SumToN.py)

```python
n = int(input("정수를 입력하시오: "))

plus = 0
for i in range(1, n+1):
    plus = plus + i  #입력한 값(n)까지의 합 구하기

print(n, "까지의 양의 정수를 모두 더하면", plus, "이다.")
```

- **Accumulator variable:** `plus`, which holds the sum, is initialized to 0 before the loop. Since 0 is the identity element of addition, `plus` after the first iteration is exactly the first term.
- **Loop range:** `range(1, n+1)` runs from 1 to `n`. Writing `n` as the stop value would leave `n` out, so 1 is added.
- **Accumulation:** `plus = plus + i` adds the current `i` to the sum so far and stores the result back in `plus`. For `n` equal to 4, `plus` changes through 0, 1, 3, 6, and 10.
- **Check:** The sum from 1 to $n$ is $n(n+1)/2$, so for $n = 10$ it is $10 \times 11 / 2 = 55$.

**Output:** With input 10. The prompt asks for an integer, and the result reads "The sum of all positive integers up to 10 is 55."

```text
정수를 입력하시오: 10
10 까지의 양의 정수를 모두 더하면 55 이다.
```

> **Note:** If 0 or a negative number is entered for `n`, `range(1, n+1)` is empty and the block never runs, so the sum is printed as 0.

### 3.2 The Sum of the Digits

**Code:** [Lab_DigitSum.py](Lab_DigitSum.py)

```python
num = int(input("네 자리 숫자를 입력하세요: "))

#S1 = num // 1000
#R = num - (1000*S1)
#S2 = R // 100
#R = R - (100*S2)
#S3 = R // 10
#R = R - (10 * S3)
#S4 = R
#nums = S1 + S2 + S3 + S4

nums = 0
for i in [3, 2, 1, 0]:
    S1 = num // (10 ** i)  # 10의 i제곱 자리의 숫자
    num -= S1 * (10 ** i)  # 그 자리의 값을 빼서 아래 자리만 남김
    nums += S1

print("각 자리 숫자의 합:", nums)
```

- **Problem:** Read a four-digit integer and compute the sum of its digits.
- **Extracting a digit:** `//` is integer division that keeps only the quotient. The quotient of a four-digit number divided by 1000 is its thousands digit, and subtracting that place value (digit × 1000) leaves only the lower three digits. The same is repeated for 100, 10, and 1. The comments in the loop say "the digit in the 10-to-the-i place" and "subtract that place value, leaving only the lower places".
- **Commented-out part:** The comments above spell this process out one line per place. The loop changes the divisor as `10 ** i` and runs the same two lines four times, so the code is shorter.
- **Compound assignment operators:** `num -= x` is the same as `num = num - x`, and `nums += S1` the same as `nums = nums + S1`.

For an input of 1234, the variables take the following values in each iteration.

| `i` | `10 ** i` | `S1 = num // 10**i` | `num` after subtraction | `nums` |
|:-----|:-----|:-----|:-----|:-----|
| 3 | 1000 | 1 | 234 | 1 |
| 2 | 100 | 2 | 34 | 3 |
| 1 | 10 | 3 | 4 | 6 |
| 0 | 1 | 4 | 0 | 10 |

*Table 1. Variable values in each iteration for an input of 1234*

**Output:** Two runs with inputs 1234 and 9075. The output reads "Sum of the digits", and $9 + 0 + 7 + 5 = 21$.

```text
네 자리 숫자를 입력하세요: 1234
각 자리 숫자의 합: 10
```

```text
네 자리 숫자를 입력하세요: 9075
각 자리 숫자의 합: 21
```

> **Caution:** This method assumes an input from 0 to 9999. For a five-digit number, the quotient in the first iteration is 10 or more, so a value that is not a single digit is added. To handle any number of digits, use a `while` statement that takes the ones digit with `num % 10` and removes it with `num //= 10` until `num` becomes 0.

### 3.3 Repeating Circles with Turtle Graphics

**Code:** [Lab_TurtleCircles.py](Lab_TurtleCircles.py)

```python
import turtle
t = turtle.Turtle()

for count in range(12):
    t.circle(100)
    t.left(360/12)
```

- **Turtle graphics:** The `turtle` module is a graphics tool that moves a turtle (cursor) on the screen and draws a line where it passes. `turtle.Turtle()` creates a turtle object and stores it in `t`.
- **What is repeated:** `t.circle(100)` draws a circle of radius 100 whose center lies to the turtle's left and returns to the starting point. `t.left(360/12)` turns the turtle 30 degrees to the left. `360/12` uses the `/` operator, so it is the real number 30.0.
- **Resulting picture:** Twelve circles share the starting point and are drawn in directions turned by 30 degrees each, so after one full turn (12 × 30 = 360 degrees) a flower-like pattern is complete. The loop variable `count` is not used in the block and only counts the iterations.

> **Note:** Run in IDLE, the graphics window stays open after drawing, but run with `python3` in a terminal, the window may close the moment the program ends. To keep the window open, put `turtle.done()` on the last line.

---

<br>

## 4. The while Statement

### 4.1 Password Check

**Code:** [Lab_PasswordCheck.py](Lab_PasswordCheck.py)

```python
password = ""
while password != "pythonisfun":
    password = input("암호를 입력하시오: ")
print("로그인 성공")
```

- **The `while` statement:** It repeats the block under `while condition:` as long as the condition is true. The condition is checked again before every run of the block, so it is used when the number of iterations is not known in advance.
- **Initial value:** Starting `password` as an empty string makes the first check `"" != "pythonisfun"` true, so the block runs at least once and reads input.
- **Termination condition:** The moment the input equals `pythonisfun`, the condition becomes false, the loop ends, and the `print()` outside the block runs. The comparison is case-sensitive, so `PythonIsFun` is a different string.

**Output:** Three wrong passwords followed by the correct one. The prompt asks for the password, and the last line means "Login successful".

```text
암호를 입력하시오: idontknow
암호를 입력하시오: 12345678
암호를 입력하시오: password
암호를 입력하시오: pythonisfun
로그인 성공
```

### 4.2 A Running Sum with a while Statement

**Code:** [Lab_WhileSumToN.py](Lab_WhileSumToN.py)

```python
n = int(input("정수를 입력하시오: "))
Sum = 0

#for i in range(n+1):
#    print(i)
#    Sum += i

i = 0
while (i <= n):
    print(i)
    Sum += i
    print(Sum)
    i += 1
```

- **Correspondence with the `for` statement:** The commented-out `for` statement adds 0 through `n`. Doing the same with a `while` statement requires writing the initialization of the loop variable (`i = 0`), the condition (`i <= n`), and the update (`i += 1`) explicitly.
- **Output:** Each iteration prints the `i` about to be added and then the running sum `Sum`, so the sum can be seen building up. The last `Sum` printed is the sum from 0 to `n`.
- **Variable name:** `Sum` begins with a capital letter, so it is a different name from the built-in function `sum()`. Assigning a value to lowercase `sum` would make the built-in `sum()` unusable in that program.

**Output:** With input 5. Each pair of lines is `i` and the running sum, and the last sum, 15, equals $5 \times 6 / 2$.

```text
정수를 입력하시오: 5
0
0
1
1
2
3
3
6
4
10
5
15
```

> **Caution:** If `i += 1` is left out of the block, `i` stays 0 and the condition `i <= n` stays true forever. A loop that never ends in this way is called an **infinite loop**, and a running program can be stopped with Ctrl+C.

### 4.3 Converting a for Statement to a while Statement

**Code:** [Lab_ForToWhile.py](Lab_ForToWhile.py)

```python
#sum = 0
#for i in range(1,11,1):  <- 1부터 11보다 작은 때까지 1씩 증가(1~10)
#   sum = sum + i

#while문으로 바꾸기

Sum = 0
i = 1
while (i < 11):
    Sum += i
    i+=1
print(Sum)
```

- **How to convert:** The start value 1 of `range(1, 11, 1)` moves to `i = 1` before the loop, the stop value 11 to the condition `i < 11`, and the step 1 to `i += 1` at the end of the block. This correspondence holds for every `range()` with a positive step. The comments say "from 1 while less than 11, increasing by 1 (1-10)" and "convert to a while loop".
- **Result:** The block runs while `i` is 1-10, so $1 + 2 + \cdots + 10 = 55$ is printed. When `i` becomes 11, the condition is false and the loop ends.

**Output:**

```text
55
```

---

<br>

## 5. break and continue

### 5.1 break

**Code:** [Lab_Break.py](Lab_Break.py)

```python
for i in range(10):
    if i == 5: break
    print(i)
print("End of Program")
```

- **`break`:** As soon as it runs, it ends the innermost enclosing loop and moves to the statement after the loop. The remaining iterations are not run.
- **Flow:** While `i` is 0-4, the condition is false, so `print(i)` runs. When `i` becomes 5, `break` runs and the loop ends, so 5-9 are not printed and `End of Program` is printed.
- **One-line `if` statement:** When a block has only one statement, it may follow the colon on the same line, as in `if i == 5: break`.

**Output:**

```text
0
1
2
3
4
End of Program
```

### 5.2 continue

**Code:** [Lab_Continue.py](Lab_Continue.py)

```python
for i in range(10):
    if i == 5: continue  # i가 5일 때 다음 문장을 실행하지 않고 넘어감
    print(i)
print("End of Program")
```

- **`continue`:** As soon as it runs, it skips the rest of the block and moves to the next iteration. The loop itself does not end. The comment says "when i is 5, skip the next statement".
- **Flow:** Only when `i` is 5 is `print(i)` skipped, so 0-9 without 5 are printed. In a `for` statement the loop variable moves to the next value even after `continue`, so no infinite loop arises.

**Output:**

```text
0
1
2
3
4
6
7
8
9
End of Program
```

> **Caution:** In a `while` statement, running `continue` before the statement that updates the loop variable checks the condition again with the variable unchanged, which can cause an infinite loop. In a `while` statement, the loop variable must be updated before `continue`.

---

<br>

## Summary

| Concept | Key Summary |
|:-----|:-----|
| `for` statement | Takes the elements of the iterable one at a time, assigns each to the loop variable, and runs the block, repeating until no elements remain. |
| `range(start, stop, step)` | Produces integers from the start value, changing by the step, up to just before the stop value, and with one argument the start is 0 and the step is 1. |
| Negative step | With a negative step the sequence counts from larger to smaller numbers, and the stop value is still excluded. |
| Accumulation | The accumulator variable is initialized to 0 before the loop, and values are added in the block with `+=`. |
| Splitting digits | `//` gives the digit of a place, and subtracting its place value or keeping the remainder with `%` moves on to the next place. |
| `while` statement | Repeats the block while the condition is true, and without an update of the loop variable it becomes an infinite loop. |
| Converting `for` to `while` | The start value becomes the initialization before the loop, the stop value the condition, and the step the update at the end of the block. |
| `break` and `continue` | `break` ends the loop, and `continue` skips the rest of the current iteration and moves to the next one. |

---

<br>

## Self-Check Questions

1. **Elements of range():** List all integers produced by `range(2, 11, 3)` and `range(5, 0, -2)`.

   <details>
   <summary>Answer</summary>

   `range(2, 11, 3)` gives 2, 5, and 8. The next value, 11, is the stop value and is excluded. `range(5, 0, -2)` gives 5, 3, and 1, and the next value, -1, passes the stop value 0 and is excluded.

   </details>

2. **Tracing a running sum:** How does the value of `plus` change in each iteration when 4 is entered into `Lab_SumToN.py`?

   <details>
   <summary>Answer</summary>

   When `i` is 1, 2, 3, and 4, `plus` becomes 1, 3, 6, and 10 in turn, and finally `4 까지의 양의 정수를 모두 더하면 10 이다.` is printed. This equals $4 \times 5 / 2 = 10$.

   </details>

3. **Sum of the digits:** Give `S1` in each iteration and the final output when 2024 is entered into `Lab_DigitSum.py`.

   <details>
   <summary>Answer</summary>

   `S1` is 2024 // 1000 = 2, 24 // 100 = 0, 24 // 10 = 2, and 4 // 1 = 4, and the sum is $2 + 0 + 2 + 4 = 8$, so `각 자리 숫자의 합: 8` is printed.

   </details>

4. **Converting to a while statement:** Write a `while` statement that does the same as the following `for` statement.

   ```python
   for k in range(10, 0, -2):
       print(k)
   ```

   <details>
   <summary>Answer</summary>

   Initialize `k = 10` and put `print(k)` and `k -= 2` under `while k > 0:`. Because the step is negative, the condition is `k > 0`, and 10, 8, 6, 4, and 2 are printed.

   </details>

5. **break and continue:** How does the output change if `break` in `Lab_Break.py` is replaced with `continue`?

   <details>
   <summary>Answer</summary>

   `continue` does not end the loop and skips only `print(i)` when `i` is 5, so 0, 1, 2, 3, 4, 6, 7, 8, 9 and `End of Program` are printed. This is the same as the output of `Lab_Continue.py`.

   </details>
