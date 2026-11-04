# Lecture 6 Solutions — Functions

[Repository Guide](../../README.md) | [English](Solutions.md) | [한국어](Solutions.ko.md)

> **Last Updated:** 2026-11-04

---

<br>

## Table of Contents

- [Exercise 1: A Function That Draws a Square](#exercise-1-a-function-that-draws-a-square)
- [Exercise 2: A Function That Draws an n-Sided Polygon](#exercise-2-a-function-that-draws-an-n-sided-polygon)
- [Exercise 3: Circle Area and Circumference with a Global Constant](#exercise-3-circle-area-and-circumference-with-a-global-constant)
- [Exercise 4: Arithmetic Functions and Keyword Arguments](#exercise-4-arithmetic-functions-and-keyword-arguments)
- [Exercise 5: The Largest of Three Integers](#exercise-5-the-largest-of-three-integers)
- [Exercise 6: A Calculator Module](#exercise-6-a-calculator-module)

---

<br>

## Exercise 1: A Function That Draws a Square

**Problem:** Call the square-drawing function `square(length)` three times to draw 3 squares starting at (-200, 0), (0, 0), and (200, 0). The full problem and sample run are in [Exercise 1](Exercises.md#exercise-1-a-function-that-draws-a-square).

### Solution

**Approach:** Drawing a square is already contained in the function `square()`, so what remains is to move the turtle to each starting position and call the function ([Lecture 6, Section 2.2](Concepts_Lecture.md#22-function-calls-and-the-flow-of-execution)).

- **Function `square(length)`:** Repeats 4 times moving forward by `length` and turning 90 degrees to the left. Four turns add up to 360 degrees, so after drawing the square the turtle is at the starting point facing the original direction.
- **Moving without drawing a line:** With the pen lifted by `t.up()`, move to the coordinates (x, y) with `t.goto(x, y)`, and put the pen down again with `t.down()`. Moving while the pen is up leaves no line.
- **Three calls:** Call the same function three times with the argument 100. The function is defined only once.

**Code:**

```python
import turtle
t = turtle.Turtle()
t.shape("turtle")

def square(length):            # length is the side length
    for i in range(4):
        t.forward(length)
        t.left(90)

t.up()                         # lift the pen
t.goto(-200, 0)                # move to (-200, 0)
t.down()                       # put the pen down
square(100)                    # call square()

t.up()
t.goto(0, 0)
t.down()
square(100)

t.up()
t.goto(200, 0)
t.down()
square(100)
```

**Output:** No text is printed, and 3 squares like Figure 1 of Exercise 1 are drawn in the turtle graphics window. The turtle initially faces right (east), so each square is drawn counterclockwise, drawing one side to the right from the starting point and then turning left. The first square therefore occupies the region with x from -200 to -100 and y from 0 to 100, and the starting point becomes the lower-left corner of each square. After drawing the last square, the turtle stops at (200, 0) facing right.

In the code above, the four lines that lift the pen, move, put the pen down, and draw are repeated three times. Grouping these four lines into a function as well and calling it in a loop makes the program shorter.

```python
import turtle
t = turtle.Turtle()
t.shape("turtle")

def square(length):            # length is the side length
    for i in range(4):
        t.forward(length)
        t.left(90)

def square_at(x, y, length):   # draw a square whose start corner is (x, y)
    t.up()
    t.goto(x, y)
    t.down()
    square(length)

for x in [-200, 0, 200]:
    square_at(x, 0, 100)
```

This program performs the same actions (lifting the pen, moving, putting the pen down, and 4 moves and turns) three times in the same order as the first program, so it draws the same picture. Just as the function `square_at()` calls another function `square()`, a function can use other functions as parts to do a larger job. To increase the squares to four, it suffices to add one more starting x coordinate to the list.

---

<br>

## Exercise 2: A Function That Draws an n-Sided Polygon

**Problem:** Write a function `n_polygon(n, length)` that draws a regular $n$-sided polygon, and repeat a 20-degree turn followed by drawing a regular hexagon 10 times. The full problem and sample run are in [Exercise 2](Exercises.md#exercise-2-a-function-that-draws-an-n-sided-polygon).

### Solution

**Approach:** To draw a regular $n$-sided polygon, repeat $n$ times drawing one side and turning outward by a fixed angle. The exterior angles of a convex polygon add up to 360 degrees, so one exterior angle of a regular $n$-sided polygon, that is, the angle the turtle must turn at each vertex, is $360 / n$ degrees. For a regular hexagon it is $360 / 6 = 60$ degrees.

- **Function `n_polygon(n, length)`:** Repeats `n` times moving forward by `length` and turning `360//n` degrees to the left. After `n` turns the turtle has turned 360 degrees in total and returns to the starting point facing the original direction.
- **Repeated calls:** Repeat 10 times turning 20 degrees to the left and drawing a regular hexagon. The turns while drawing a hexagon add up to 360 degrees and do not change the direction, so the next hexagon starts in a direction turned exactly 20 degrees from the previous one.

**Code:**

```python
import turtle
t = turtle.Turtle()

# define a function that draws an n-sided polygon
def n_polygon(n, length):
    for i in range(n):
        t.forward(length)
        t.left(360//n)         # integer division uses //

for i in range(10):
    t.left(20)
    n_polygon(6, 100)
```

**Output:** No text is printed, and a picture like Figure 2 of Exercise 2 is drawn. All hexagons share the starting point as one vertex, and the directions of their first sides run from 20 degrees to $20 + 9 \times 20 = 200$ degrees at 20-degree intervals. At the starting point each hexagon occupies the range of its interior angle, 120 degrees, counterclockwise from the direction of its first side, so the whole picture covers 300 degrees, from 20 to 320 degrees, and only the 60 degrees to the right of the starting point remain empty. The function `n_polygon()` is called 10 times in total, and the turtle moves 60 times and turns 70 times (60 times inside the hexagons and 10 times in the loop).

> **Caution:** The integer division `360//n` is exact only when $n$ divides 360. For example, for $n = 7$, $360 / 7 \approx 51.43$, but `360//7` is 51, so even after 7 turns the turtle has turned only $7 \times 51 = 357$ degrees. Drawing a heptagon with side 100 this way leaves the turtle about 6.08 units away from the starting point, and the shape does not close. To draw an exact polygon for any $n$, use the floating-point division `360/n`.

---

<br>

## Exercise 3: Circle Area and Circumference with a Global Constant

**Problem:** Declare pi as a global constant, write functions that compute the area and circumference of a circle, and print both values for an input radius. The full problem and sample run are in [Exercise 3](Exercises.md#exercise-3-circle-area-and-circumference-with-a-global-constant).

### Solution

**Approach:** The area of a circle is $\pi r^2$ and the circumference is $2 \pi r$. Both formulas use pi, so define pi once as the global constant `PI` and have two functions, one for each formula, read this constant ([Lecture 6, Section 5.5](Concepts_Lecture.md#55-global-constants)).

- **Global constant:** The capitalized name `PI` marks it as a constant. The functions only read it, so no `global` statement is needed.
- **Computing functions:** `circleArea(radius)` returns `PI*radius*radius`, and `circleCircumference(radius)` returns `2*PI*radius`.
- **The `main()` function:** The part responsible for input and output is also grouped into a function `main()`, which is called once at the very end of the program.

**Code:**

```python
PI = 3.14159265358979          # global constant

def main():
    radius = float(input('원의 반지름을 입력하시오: '))
    print('원의 면적:', circleArea(radius))
    print('원의 둘레:', circleCircumference(radius))

def circleArea(radius):
    return PI*radius*radius

def circleCircumference(radius):
    return 2*PI*radius

main()
```

**Output:** The first run uses the input of the sample run, and the second run enters the real number 2.5 as the radius.

```text
원의 반지름을 입력하시오: 10
원의 면적: 314.159265358979
원의 둘레: 62.8318530717958
```

```text
원의 반지름을 입력하시오: 2.5
원의 면적: 19.634954084936187
원의 둘레: 15.70796326794895
```

For a radius of 10, the area is $3.14159265358979 \times 10 \times 10 = 314.159265358979$ and the circumference is $2 \times 3.14159265358979 \times 10 = 62.8318530717958$. The area for the radius 2.5 has many digits because the exact product $3.14159265358979 \times 6.25 = 19.6349540849361875$ has more digits. Floating-point numbers are stored in binary, so the floating-point number closest to this product is stored, and `print()` prints `19.634954084936187`, the shortest decimal that represents that floating-point number.

- **Order of function definitions:** The body of `main()` calls `circleArea()` and `circleCircumference()`, which are defined further down, but no error occurs. The body is executed when `main()` is called, and the last line, which calls `main()`, comes after all three functions have been defined ([Lecture 6, Section 2.3](Concepts_Lecture.md#23-the-error-of-calling-before-defining)).
- **Local variables:** `radius` is a local variable of `main()`, and the parameter `radius` of each computing function is a local variable of that function. They have the same name but are different variables, and the value is passed as an argument in the call.

> **Note:** The standard module `math` defines the constant `math.pi` (value 3.141592653589793), so in real programs it is accurate and convenient to use `math.pi` after `import math`. Also, by the PEP 8 convention, a function name such as `circle_area` in lowercase with underscores is more Pythonic than a camelCase name such as `circleArea`.

---

<br>

## Exercise 4: Arithmetic Functions and Keyword Arguments

**Problem:** Write the arithmetic functions `add()`, `sub()`, `mul()`, and `div()`, and compute `10+20*30` by calling them with keyword arguments. The full problem and sample run are in [Exercise 4](Exercises.md#exercise-4-arithmetic-functions-and-keyword-arguments).

### Solution

**Approach:** Each function receives the parameters `a` and `b` and returns the result of the operation with `return`. Because they return results, a call of one function can be placed as an argument of another.

- **Order of operations:** In `10+20*30`, multiplication is computed before addition, so it is `10 + (20*30)`. Therefore the multiplication function goes inside and the addition function outside.
- **Keyword arguments:** Call with the parameter names specified, as in `mul(a=20, b=30)` ([Lecture 6, Section 6.2](Concepts_Lecture.md#62-keyword-arguments)).
- **Order of execution:** Arguments are evaluated before the function is called, so in `add(a=10, b=mul(a=20, b=30))` the inner `mul(a=20, b=30)` runs first and returns 600, and then `add(a=10, b=600)` returns 610.

**Code:**

```python
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

result = add(a=10, b=mul(a=20, b=30))   # 10 + (20 * 30)
print(result)
print(sub(b=4, a=10), div(a=7, b=2))
```

**Output:**

```text
610
6 3.5
```

The first line, 610, is the answer to the problem. The second line shows the results of calling the other two functions with keyword arguments. `sub(b=4, a=10)` writes the keyword arguments in a different order, but they correspond by name, so it is $10 - 4 = 6$, and `div(a=7, b=2)` is 3.5 because `/` is floating-point division. Subtraction and division are not commutative, so stating with keyword arguments which value is `a` and which is `b` reduces mistakes.

---

<br>

## Exercise 5: The Largest of Three Integers

**Problem:** Using the function `get_max()` that finds the larger of two numbers, write a function that returns the largest of three integers. The full problem is in [Exercise 5](Exercises.md#exercise-5-the-largest-of-three-integers).

### Solution

**Approach:** The maximum of three numbers $x, y, z$ equals the result of first finding the larger of $x$ and $y$ and then the larger of that result and $z$. That is, $\max(x, y, z) = \max(\max(x, y), z)$. So it suffices to call `get_max()` twice, passing the return value of the first call directly as an argument of the second.

**Code:**

```python
def get_max(x, y):
    if x > y:
        return x
    else:
        return y

def get_max3(x, y, z):
    return get_max(get_max(x, y), z)

print(get_max3(10, 30, 20))
print(get_max3(30, 20, 10))
print(get_max3(10, 20, 30))
print(get_max3(-5, -9, -7))
print(get_max3(7, 7, 3))
```

**Output:**

```text
30
30
30
-5
7
```

The five calls cover, in order, the maximum in the second, first, and third positions, all negative numbers, and equal values. For example, in `get_max3(10, 30, 20)`, `get_max(10, 30)` returns 30, and `get_max(30, 20)` returns 30 again. Reusing an existing function as a part avoids writing a new `if` statement that compares three numbers.

> **Note:** Python has the built-in function `max()`, which returns the largest value, 30, when given several arguments as in `max(10, 30, 20)`. This problem is an exercise in combining functions, so it does not use `max()`.

---

<br>

## Exercise 6: A Calculator Module

**Problem:** Make the arithmetic functions into a module `cals`, and use this module to compute `30+10/5*10` from left to right. The full problem is in [Exercise 6](Exercises.md#exercise-6-a-calculator-module).

### Solution

**Approach:** The module name is `cals`, so the file name is `cals.py`. Define the computing functions in this file, and put the program `main.py`, which performs the computation, in the same folder so that it imports the module with `import cals` ([Lecture 6, Section 8.2](Concepts_Lecture.md#82-writing-and-using-a-module)).

```text
cals_demo/
├── cals.py     module: defines add(), sub(), mul(), div()
└── main.py     program: imports the module with import cals and computes
```

*Figure 1. Folder layout of the calculator module and the program*

- **Computing without precedence:** Computing from left to right gives $30 + 10 = 40$, $40 / 5 = 8.0$, and $8.0 \times 10 = 80.0$. The result of one step becomes the first argument of the next step.
- **Calling functions of a module:** With `import cals`, functions are called with the module name attached, as in `cals.add()`.

**Code:** `cals.py` is as follows.

```python
# cals.py: calculator module
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b
```

`main.py` is as follows.

```python
import cals

# 30+10/5*10 evaluated from left to right, without operator precedence
step1 = cals.add(30, 10)      # 30 + 10
step2 = cals.div(step1, 5)    # (30 + 10) / 5
step3 = cals.mul(step2, 10)   # ((30 + 10) / 5) * 10
print(step3)

print(cals.mul(cals.div(cals.add(30, 10), 5), 10))
print(30+10/5*10)             # with Python's operator precedence
```

**Output:** The result of running `python main.py` in the `cals_demo` folder.

```text
80.0
80.0
50.0
```

The first line is the value computed step by step while storing intermediate results in variables, and the second line is the same computation written as one expression with nested function calls. Nested calls are executed starting from the innermost `cals.add(30, 10)`. The third line, for comparison, applies Python's operator precedence as it is: division and multiplication are computed first, giving $30 + (10 / 5) \times 10 = 30 + 20.0 = 50.0$. `div()` uses the floating-point division `/`, so the results are real numbers.

When `import cals` is executed, Python looks for `cals.py` in `cals_demo/`, the folder of `main.py` and the first entry of the module search path, executes the file once to create the four functions, and binds the module object to the name `cals` ([Lecture 6, Section 8.3](Concepts_Lecture.md#83-how-the-import-statement-finds-a-module)). In this process, a `__pycache__` folder holding the compiled file is created inside `cals_demo/`. If `cals.py` is moved to another folder, `ModuleNotFoundError: No module named 'cals'` occurs.

> **Note:** If a module name is long or used often, `import cals as c` gives it an alias so that it can be used as `c.add(30, 10)`. With `from cals import *`, the functions can be used without the module name, as in `add(30, 10)`, but care is needed because a function of the same name in the current program is overwritten.
