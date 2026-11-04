# Lecture 5 Solutions — Loops

[Repository Guide](../../README.md) | [English](Solutions.md) | [한국어](Solutions.ko.md)

> **Last Updated:** 2026-11-04

---

<br>

## Table of Contents

- [Exercise 1: Random Movement of the Turtle](#exercise-1-random-movement-of-the-turtle)
- [Exercise 2: Computing a Factorial](#exercise-2-computing-a-factorial)
- [Exercise 3: Printing One Multiplication Table](#exercise-3-printing-one-multiplication-table)
- [Exercise 4: Printing the Entire Multiplication Table](#exercise-4-printing-the-entire-multiplication-table)
- [Exercise 5: Rewriting a for Statement as a while Statement](#exercise-5-rewriting-a-for-statement-as-a-while-statement)
- [Exercise 6: Rewriting a while Statement as a for Statement](#exercise-6-rewriting-a-while-statement-as-a-for-statement)

---

<br>

## Exercise 1: Random Movement of the Turtle

**Problem:** Make the turtle repeat, 30 times, a move of random length followed by a turn of random angle. The full problem and sample run are in [Exercise 1](Exercises.md#exercise-1-random-movement-of-the-turtle).

### Solution

**Approach:** The same action is repeated a fixed number of times, 30, so the `for` statement with `range(30)` is used ([Lecture 5, Section 3.1](Concepts_Lecture.md#31-rangestop)). The algorithm performed on each iteration is as follows.

- Generate a random number in [1, 100] and store it in the variable `length`.
- Move the turtle by `length`.
- Generate a random number in [-180, 180] and store it in the variable `angle`.
- Turn the turtle by `angle`.

Random numbers are generated with `random.randint(a, b)` of the `random` module (Lecture 4). This function returns one integer from `a` to `b` inclusive with equal probability, and the end values `a` and `b` can also occur. Giving `t.right(angle)` a negative angle turns the turtle left by its absolute value, so angles in [-180, 180] cover every change of direction to the left and to the right.

**Code:**

```python
import turtle
import random
t = turtle.Turtle()
t.shape("turtle")

for i in range(30):
    length = random.randint(1, 100)   # random length in [1, 100]
    t.forward(length)
    angle = random.randint(-180, 180) # random angle in [-180, 180]
    t.right(angle)
```

**Output:** The program prints no text and draws a path in the turtle graphics window. The turtle moves forward 30 times and turns 30 times in total, and because of the random numbers a different path is drawn on every run. An example of one run is Figure 1 of Exercise 1.

- **`import random`:** Imports the standard module that generates random numbers.
- **`t.shape("turtle")`:** Changes the default arrow-shaped cursor to a turtle shape.
- **Loop body:** The four statements correspond directly to the four steps of the algorithm. The loop variable `i` is not used in the body and only counts the iterations.

> **Note:** To get the same path on every run, fix the starting value of the random number generator before the loop, as in `random.seed(1)`. The same seed produces the same sequence of random numbers, which is useful for testing programs with randomness or for reproducing results.

---

<br>

## Exercise 2: Computing a Factorial

**Problem:** Read an integer $n$ and compute and print $n! = 1 \times 2 \times \cdots \times n$ with the `for` statement. The full problem and sample run are in [Exercise 2](Exercises.md#exercise-2-computing-a-factorial).

### Solution

**Approach:** This is a problem of accumulating a product ([Lecture 5, Section 5.2](Concepts_Lecture.md#52-accumulating-a-product-and-the-factorial)). Initialize the accumulator `fact` to 1, the identity element of multiplication, and repeat from 1 to $n$ with `range(1, n+1)`, multiplying each value into `fact`.

- **Input:** Convert the string returned by `input()` to an integer with `int()` (Lecture 2).
- **Repetition:** The stop is not included in the range, so to multiply up to $n$ the stop is given as `n+1`.
- **Output:** Pass the result to `print()`.

**Code:**

```python
n = int(input("정수를 입력하시오: "))

fact = 1
for i in range(1, n+1):
    fact = fact * i
print(n, "!은", fact, "이다.")
```

**Output:**

```text
정수를 입력하시오: 10
10 !은 3628800 이다.
```

When the input is 5, `fact` changes as follows.

| `i` | 1 | 2 | 3 | 4 | 5 |
|:-----|:---:|:---:|:---:|:---:|:---:|
| `fact` after the body | 1 | 2 | 6 | 24 | 120 |

*Table 1. Changes of the accumulator fact while computing 5!*

The spaces between `10` and `!은` and between `3628800` and `이다.` in the output appear because `print()` puts one space between values separated by commas ([Lecture 5, Section 2.2](Concepts_Lecture.md#22-using-the-loop-variable)). To print without these spaces as in the sample run, build a single string with string formatting (Lecture 3) and print it. The following code also handles the case where a negative number is entered.

```python
n = int(input("정수를 입력하시오: "))

if n < 0:
    print("음수의 팩토리얼은 정의되지 않는다.")
else:
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    print("%d!은 %d이다." % (n, fact))
```

```text
정수를 입력하시오: 10
10!은 3628800이다.
```

```text
정수를 입력하시오: 0
0!은 1이다.
```

```text
정수를 입력하시오: 30
30!은 265252859812191058636308480000000이다.
```

```text
정수를 입력하시오: -3
음수의 팩토리얼은 정의되지 않는다.
```

- **When 0 is entered:** `range(1, 1)` is an empty range, so the body is never executed and `fact` keeps its initial value 1. This value agrees with the definition $0! = 1$.
- **When a negative number is entered:** In the first program, `range(1, n+1)` becomes an empty range and the wrong result `-3 !은 1 이다.` (-3! is 1.) is printed. The factorial is defined only for non-negative integers, so the revised program first filters out negative numbers with an `if` statement (Lecture 4) and prints `음수의 팩토리얼은 정의되지 않는다.` (The factorial of a negative number is undefined.).

> **Note:** Python integers have no size limit, so even large values such as 30! are computed exactly. In contrast, the largest value a signed 64-bit integer type in C can represent is $2^{63} - 1 = 9223372036854775807$, so it can store up to $20! = 2432902008176640000$ but overflows from $21! = 51090942171709440000$.

---

<br>

## Exercise 3: Printing One Multiplication Table

**Problem:** Read the desired table (dan) and print `dan*1` to `dan*9` of that table. The full problem and sample run are in [Exercise 3](Exercises.md#exercise-3-printing-one-multiplication-table).

### Solution

**Approach:** Repeat 9 times while changing the multiplier `i` from 1 to 9. Here a counter-controlled `while` statement is used ([Lecture 5, Section 6.3](Concepts_Lecture.md#63-counter-controlled-repetition)).

- **Initialization:** Set the multiplier `i` to 1.
- **Condition:** Repeat while `i <= 9`.
- **Update:** Add 1 with `i = i + 1` at the end of the body.
- **Output:** `"%s*%s=%s" % (dan, i, dan*i)` uses string formatting with the `%` operator (Lecture 3) to insert three values into the `%s` slots of the string in order. `%s` converts a value to a string before inserting it, so it also works for integers, and no spaces appear between the values.

**Code:**

```python
dan = int(input("원하는 단은: "))
i = 1

while i <= 9:
    print("%s*%s=%s" % (dan, i, dan*i))
    i = i + 1
```

**Output:**

```text
원하는 단은: 9
9*1=9
9*2=18
9*3=27
9*4=36
9*5=45
9*6=54
9*7=63
9*8=72
9*9=81
```

When `i` becomes 10 in the 9th iteration, the condition `i <= 9` becomes false and the repetition ends. Since the number of iterations is fixed at 9, using `for i in range(1, 10):` instead of the `while` statement gives the same result without the initialization and update statements ([Lecture 5, Section 7.1](Concepts_Lecture.md#71-how-to-convert)).

---

<br>

## Exercise 4: Printing the Entire Multiplication Table

**Problem:** Modify the program of Exercise 3 to print the tables from 1 to 9, one table per line. The full problem and sample run are in [Exercise 4](Exercises.md#exercise-4-printing-the-entire-multiplication-table).

### Solution

**Approach:** Put the whole loop of Exercise 3 inside an outer loop that changes the table `dan` from 1 to 9. A structure in which a loop is placed inside a loop in this way is a nested loop ([Lecture 5, Section 8](Concepts_Lecture.md#8-nested-loops)).

- **Outer loop:** Changes `dan` from 1 to 9. No input is read.
- **Inner loop:** As in Exercise 3, changes `i` from 1 to 9 and prints the products. To print one table on one line, `end=" "` adds a space instead of a line break.
- **Line break:** After the inner loop ends, `print()` without arguments moves to a new line.
- **Resetting the counter:** `i` must count from 1 again for each table, so `i = 1` is placed inside the body of the outer loop, immediately before the inner loop.

**Code:**

```python
dan = 1
while dan <= 9:                  # outer loop: tables 1 to 9
    i = 1                        # reset the multiplier for each table
    while i <= 9:                # inner loop: multipliers 1 to 9
        print("%s*%s=%s" % (dan, i, dan*i), end=" ")
        i = i + 1
    print()                      # line break after each table
    dan = dan + 1
```

**Output:**

```text
1*1=1 1*2=2 1*3=3 1*4=4 1*5=5 1*6=6 1*7=7 1*8=8 1*9=9
2*1=2 2*2=4 2*3=6 2*4=8 2*5=10 2*6=12 2*7=14 2*8=16 2*9=18
3*1=3 3*2=6 3*3=9 3*4=12 3*5=15 3*6=18 3*7=21 3*8=24 3*9=27
4*1=4 4*2=8 4*3=12 4*4=16 4*5=20 4*6=24 4*7=28 4*8=32 4*9=36
5*1=5 5*2=10 5*3=15 5*4=20 5*5=25 5*6=30 5*7=35 5*8=40 5*9=45
6*1=6 6*2=12 6*3=18 6*4=24 6*5=30 6*6=36 6*7=42 6*8=48 6*9=54
7*1=7 7*2=14 7*3=21 7*4=28 7*5=35 7*6=42 7*7=49 7*8=56 7*9=63
8*1=8 8*2=16 8*3=24 8*4=32 8*5=40 8*6=48 8*7=56 8*8=64 8*9=72
9*1=9 9*2=18 9*3=27 9*4=36 9*5=45 9*6=54 9*7=63 9*8=72 9*9=81
```

Each line ends with one space added by `end=" "`. The outer loop runs 9 times and the inner loop 9 times, so $9 \times 9 = 81$ products are printed in total. The numbers of iterations of both loops are fixed, so the program is shorter with `for` statements.

```python
for dan in range(1, 10):
    for i in range(1, 10):
        print("%s*%s=%s" % (dan, i, dan*i), end=" ")
    print()
```

The output of this program is the same as that of the `while` program above.

> **Caution:** If `i = 1` is placed only once before the outer `while` statement, `i` remains 10 after the table of 1 is printed, and from the table of 2 on, the inner condition `i <= 9` is false from the start. Then only the table of 1 is printed on the first line and the remaining 8 lines are empty. The counter of an inner loop must be initialized each time the outer loop starts a new iteration.

---

<br>

## Exercise 5: Rewriting a for Statement as a while Statement

**Problem:** Rewrite the `for` statement that loops over `range(1001)` as a `while` statement. The full problem is in [Exercise 5](Exercises.md#exercise-5-rewriting-a-for-statement-as-a-while-statement).

### Solution

**Approach:** `range(1001)` is a range with start 0, stop 1001, and step 1. Following the correspondence in [Lecture 5, Section 7.1](Concepts_Lecture.md#71-how-to-convert), build the three parts.

- **Initialization:** The first element is the start 0, so set `i = 0` before the loop.
- **Condition:** Repeat while the element is less than the stop 1001, so `while i < 1001:`.
- **Update:** The step is 1, so put `i = i + 1` at the end of the body.

The body `sum = sum + 1` adds 1, not `i`, so this program counts how many times the body is executed. `range(1001)` has the 1001 elements 0 to 1000, so `sum` becomes 1001.

**Code:** `print(sum, i)` is placed at the end of both programs so that their results can be compared.

```python
sum=0
for i in range(1001):
    sum=sum+1
print(sum, i)
```

```python
sum = 0
i = 0                    # initialization: first value of range(1001)
while i < 1001:          # condition: i has not reached the stop value
    sum = sum + 1
    i = i + 1            # update: step of range(1001)
print(sum, i)
```

**Output:** The first is the output of the `for` statement and the second that of the `while` statement.

```text
1001 1000
```

```text
1001 1001
```

`sum` is 1001 in both programs. `i` after the loop differs, because the `for` statement leaves the last element, 1000, while the `while` statement leaves 1001, the value that made the condition false.

> **Note:** If the body were `sum = sum + i`, the program would compute the sum from 0 to 1000, and the result would be $\frac{1000 \times 1001}{2} = 500500$. The conversion method is the same regardless of the body.

---

<br>

## Exercise 6: Rewriting a while Statement as a for Statement

**Problem:** Rewrite as a `for` statement the `while` statement that adds 1, 2, 3, ... until the sum reaches 10000 or more. The full problem is in [Exercise 6](Exercises.md#exercise-6-rewriting-a-while-statement-as-a-for-statement).

### Solution

**Approach:** First analyze what the original program does. `i` grows by 1 from 1, and `i` is added to `sum` in turn. The condition `sum < 10000` is checked before each addition, so the repetition ends the moment the sum first reaches 10000 or more. The sum from 1 to $k$ is $k(k+1)/2$, which is $140 \times 141 / 2 = 9870$ for $k = 140$ and $141 \times 142 / 2 = 10011$ for $k = 141$. Therefore, after 141 is added, `sum` is 10011, `i` is 142, and the repetition ends.

This repetition has no predetermined count and ends by a condition, so it is a problem suited to the `while` statement ([Lecture 5, Section 7.2](Concepts_Lecture.md#72-choosing-a-loop)). Converting it into a `for` statement requires the following two things.

- **A sufficiently large range:** The `for` statement must fix the range in advance, so give a generous `range(1, 10001)` that exceeds the number of iterations actually needed. Each addition increases the sum by at least 1, so within this range the sum is certain to reach 10000.
- **Ending with `break`:** Leave the loop with `break` the moment the original condition becomes false, that is, the moment `sum >= 10000` holds ([Lecture 5, Section 9.1](Concepts_Lecture.md#91-the-break-statement)).

The original program checks the condition before the body, so to keep the same order the `break` check is placed at the very beginning of the body.

**Code:** `print(sum, i)` is placed at the end of both programs so that their results can be compared.

```python
i=1
sum=0
while sum<10000:
   sum=sum+i
   i+=1
print(sum, i)
```

```python
sum = 0
for i in range(1, 10001):
    if sum >= 10000:     # the while condition, tested before each addition
        break
    sum = sum + i
print(sum, i)
```

**Output:** Both programs print the following.

```text
10011 142
```

The `for` statement performs the addition while `i` is 1 to 141, and when `i` is 142 the check at the beginning finds `sum` at 10011 and leaves with `break`. That is why `sum` and `i` are the same as in the original program. Checking the condition at the beginning of the body also preserves the property of the `while` statement that nothing is added if the initial value of `sum` is already 10000 or more.

The following form, with the check after the addition, is also common.

```python
sum = 0
for i in range(1, 10001):
    sum = sum + i
    if sum >= 10000:     # tested after each addition
        break
print(sum, i)
```

```text
10011 141
```

`sum` is the same, but `i` is 141. This form leaves right after adding 141, so `i` does not grow by one more. This form also adds at least once regardless of the initial value of `sum`. If `i` is not used after the loop, both forms are correct conversions.
