# Lab 6 Explanation — Functions

[Repository Guide](../../README.md) | [English](Lab-Explanation.md) | [한국어](Lab-Explanation.ko.md)

> **Last Updated:** 2026-11-04

> **Learning Objectives:**
> 1. Define and call functions, and store their return values in variables or print them
> 2. Explain the behavior of a function without `return` and of a function that returns several values
> 3. Distinguish local and global variables and judge when a `global` declaration is needed
> 4. Use default arguments, keyword arguments, and anonymous functions (`lambda`)
> 5. Import a self-made module and call the functions in it

---

## Table of Contents

- [1. Lab Layout and How to Run](#1-lab-layout-and-how-to-run)
- [2. Defining Functions and Return Values](#2-defining-functions-and-return-values)
  - [2.1 A Function That Computes a Quadratic](#21-a-function-that-computes-a-quadratic)
  - [2.2 A Function That Does Not Return](#22-a-function-that-does-not-return)
  - [2.3 Returning Several Values](#23-returning-several-values)
  - [2.4 Type Hints and Returning a Tuple](#24-type-hints-and-returning-a-tuple)
  - [2.5 A Function That Calls a Function](#25-a-function-that-calls-a-function)
  - [2.6 The main() Function](#26-the-main-function)
- [3. Local and Global Variables](#3-local-and-global-variables)
  - [3.1 Passing a Result Back by Return Value](#31-passing-a-result-back-by-return-value)
  - [3.2 The global Declaration](#32-the-global-declaration)
  - [3.3 A Global Constant](#33-a-global-constant)
  - [3.4 Updating Several Global Variables](#34-updating-several-global-variables)
- [4. Ways of Passing Arguments and Anonymous Functions](#4-ways-of-passing-arguments-and-anonymous-functions)
  - [4.1 Default Arguments](#41-default-arguments)
  - [4.2 Keyword Arguments](#42-keyword-arguments)
  - [4.3 Anonymous Functions with lambda](#43-anonymous-functions-with-lambda)
- [5. Modules](#5-modules)
  - [5.1 Importing a Module](#51-importing-a-module)
  - [5.2 An Alias with import as](#52-an-alias-with-import-as)
- [Summary](#summary)
- [Self-Check Questions](#self-check-questions)

---

<br>

## 1. Lab Layout and How to Run

This code was written while following [Lecture 6, Functions](../../Lecture-Notes/Lec06_Functions/Concepts_Lecture.md). Section 2 covers defining and calling functions and return values, Section 3 covers local and global variables, Section 4 covers default arguments, keyword arguments, and `lambda`, and Section 5 covers modules.

```text
Coursework/Lab06_Functions/
├── Lab-Explanation.ko.md          # This document (Korean)
├── Lab-Explanation.md             # This document (English)
├── Lab_QuadraticFunction.py       # 2.1 A function that computes a quadratic
├── Lab_FunctionWithoutReturn.py   # 2.2 A function that does not return
├── Lab_MultipleReturnValues.py    # 2.3 Returning several values
├── Lab_AddWithAnnotations.py      # 2.4 Type hints and returning a tuple
├── Lab_AbsoluteValue.py           # 2.5 A function that calls a function
├── Lab_MainFunction.py            # 2.6 The main() function
├── Lab_CircleAreaReturn.py        # 3.1 Passing a result back by return value
├── Lab_CircleAreaGlobal.py        # 3.2 The global declaration
├── Lab_GlobalConstant.py          # 3.3 A global constant
├── Lab_SumAndAverageGlobal.py     # 3.4 Updating several global variables
├── Lab_DefaultArgument.py         # 4.1 Default arguments
├── Lab_KeywordArguments.py        # 4.2 Keyword arguments
├── Lab_Lambda.py                  # 4.3 Anonymous functions with lambda
├── Lab_ModuleImport.py            # 5.1 Importing a module
├── Lab_AddMinusModule.py          # Module used in 5.1
├── Lab_ModuleAlias.py             # 5.2 An alias with import as
└── Lab_ArithmeticModule.py        # Module used in 5.2
```

*Figure 1. Directory layout of Lab 6*

All programs use only the standard library and run as they are under Python 3. `Lab_AddMinusModule.py` and `Lab_ArithmeticModule.py` are not programs to run on their own but modules used by `Lab_ModuleImport.py` and `Lab_ModuleAlias.py`, so the four files must stay in the same folder. Each file begins with a documentation string (docstring) that records the file name, a one-line description, the author, and the date written, and the code blocks in this document omit that part.

```bash
cd Coursework/Lab06_Functions
python3 Lab_ModuleImport.py
```

---

<br>

## 2. Defining Functions and Return Values

### 2.1 A Function That Computes a Quadratic

**Code:** [Lab_QuadraticFunction.py](Lab_QuadraticFunction.py)

```python
#f(x)=a*x**2+b*x+c를 함수로 정의하기

def f(x):
    y=1*x**2+2*x+3
    return y #리턴 안하면 그냥 사라짐

##main##
x=10
y=1*x**2+2*x+3 #함수 속의 y와 메인문의 y는 다름(지역변수이므로)
f(x) #정의한 함수 이름을 적어주면 그냥 메인문에서 호출한 것이 됨
z=f(x)

#x를 따로 10이라고 정의하지 않고 그냥 f(10)으로 해도 됨

print(y)
print(1*x**2+2*x+3)
print(f(x))
print(z)
```

- **Function definition:** The block indented under `def name(parameter):` is the body of the function. A definition alone does not run anything, and the body runs each time the function is called. `f` computes the quadratic $f(x) = x^2 + 2x + 3$ (the first comment reads "define f(x)=ax²+bx+c as a function").
- **`return`:** It hands the computed `y` back to the caller. The comment means that the variables inside a function disappear when it ends, so a result must be returned to be used outside.
- **Local variable:** The `y` inside the function and the `y` in the main part are different variables that only share a name. A variable assigned inside a function is a **local variable** of that function and does not affect anything outside it, as the comment ("the y in the function differs from the y in main, being local") notes.
- **Calls and return values:** The line with only `f(x)` calls the function but stores the return value nowhere, so the result is discarded. `z=f(x)` stores the return value 123 in `z`. As the comment notes, the value may also be written directly as the argument, as in `f(10)`.
- **Result:** $10^2 + 2 \times 10 + 3 = 123$, so all four lines are 123.

**Output:**

```text
123
123
123
123
```

### 2.2 A Function That Does Not Return

**Code:** [Lab_FunctionWithoutReturn.py](Lab_FunctionWithoutReturn.py)

```python
def f(x):
    y=1*x**2+2*x+3
    print(y)
    #return y

##main##
x=10

f(x) #그냥 이렇게 쓰면 print됨(리턴 여부와 관계 없음)
```

- **Printing inside the function:** This `f` prints its result inside the function instead of returning it. So calling just `f(x)` makes 123 appear on the screen, as the comment says.
- **Return value `None`:** A function without a `return` statement also hands back a value when it ends, and that value is `None`, meaning no value. For example, writing `z = f(x)` prints 123 and then stores `None` in `z`.
- **Printing versus returning:** Printing only shows a value on the screen and the program cannot reuse it, while a return value can be stored in a variable or used in another computation.

**Output:**

```text
123
```

### 2.3 Returning Several Values

**Code:** [Lab_MultipleReturnValues.py](Lab_MultipleReturnValues.py)

```python
def f(x):
    y=1*x**2+2*x+3
    return y,x #C언어는 리턴값 2개 이상이 불가능

## main ##
y, x = f(10)
print(y, x)
```

- **Returning a tuple:** `return y,x` returns one **tuple** `(y, x)` that bundles the two values. A C function returns only one value (as the comment notes), but Python can hand back several values at once by bundling them in a tuple.
- **Unpacking:** `y, x = f(10)` splits the elements of the returned tuple `(123, 10)` and assigns them to `y` and `x` in order. The number of variables on the left must equal the number of tuple elements, and a `ValueError` occurs otherwise.

**Output:**

```text
123 10
```

### 2.4 Type Hints and Returning a Tuple

**Code:** [Lab_AddWithAnnotations.py](Lab_AddWithAnnotations.py)

```python
'''x=int(input("x:"))
y=int(input("y:"))
z=x+y
print(z)'''

def add(x : int,y : int) -> (int, int) :

# def add(x,y): 도 가능
# def add(x : int,y : int) -> int : 도 가능

    #x=int(input("x:"))
    #y=int(input("y:"))
    z=x+y
    #print(z)
    return z,x

## main ##
x=int(input("x:"))
y=int(input("y:"))
z,x=add(x,y)
# z=add(x,y)로 받으면 z에 튜플 (합, x)가 저장된다(합만 받으려면 return z로 쓴다)
print(z)
print(x)
```

- **Multi-line string:** The `'''...'''` at the top is a string assigned to nothing, so it does not affect execution. It is used like a comment that keeps the code from before it was turned into a function.
- **Type hints:** `x : int` indicates that the parameter `x` is expected to be an integer, and `-> (int, int)` describes the form of the return value. Such **type hints** are information for readers and tools only, and Python does not check types at run time. As the comments note, writing `def add(x,y):` without hints behaves the same.
- **Returning and unpacking:** `add` returns the sum `z` and the first argument `x` as a tuple, and the main part receives the two values separately with `z,x=add(x,y)`. `x` is assigned its original value again, so it does not change. The comment explains that receiving the result as `z=add(x,y)` stores the tuple (sum, x) in `z`, and that `return z` is needed to receive only the sum.

**Output:** With inputs 3 and 4. The prompts `x:` and `y:` have no space after them, so the inputs follow them directly.

```text
x:3
y:4
7
3
```

### 2.5 A Function That Calls a Function

**Code:** [Lab_AbsoluteValue.py](Lab_AbsoluteValue.py)

```python
'''x = int(input("x:"))

if (x < 0):
    x = -x

print(x)'''


def abs(x): # 절댓값 함수
    if (x < 0):
        x = -x
    return x

def abs2(): # 값을 입력받아 abs(x)를 돌려서 출력하는 함수
    x = int(input("x:"))
    print(abs(x))

## main ##
abs2()
```

- **Absolute value function:** `abs(x)` changes the sign of `x` if it is negative and returns it unchanged otherwise. Assigning a new value to the parameter `x` changes only the local variable inside the function, not the caller's variable.
- **Calling a function inside a function:** `abs2()` takes no parameters, reads input, calls `abs(x)`, and prints the result. It is a structure in which one function divides the work by calling another.
- **Order of calls:** `abs2` calls `abs` only when `abs2()` runs, and by then both functions are defined. The definitions therefore only need to come before the time of the call.

**Output:** With input -7.

```text
x:-7
7
```

> **Caution:** `abs` is the name of a Python built-in function. Defining a function with the same name hides the built-in `abs()` within that program. This program does the same thing, so the result is the same, but a name that does not clash with a built-in (e.g., `my_abs`) is safer.

### 2.6 The main() Function

**Code:** [Lab_MainFunction.py](Lab_MainFunction.py)

```python
## main ##
'''
a=int(input('a:'))
b=a**2
print(b)
'''
def s(x): #함수를 꼭 활용하기 전 작성
    y=x**2
    return y

## main ##
def main():
    a=int(input('a:'))
    b=s(a)
    print(b)
    print(s(a))

main()
```

- **Where functions are defined:** As the comment says ("write a function before using it"), a function must be defined before it is called. The function name exists only after its `def` has run.
- **The `main()` function:** It is a convention to wrap the executable part of a program in a function called `main()` and call it once at the end of the file. The variables `a` and `b` of the executable part become local variables of `main()` and do not mix with global names. Leaving out the call to `main()` only defines the functions, so nothing is printed.
- **Two outputs:** The program prints the return value stored in `b` and the return value of calling `s(a)` again, so the same number appears twice.

**Output:** With input 6.

```text
a:6
36
36
```

---

<br>

## 3. Local and Global Variables

### 3.1 Passing a Result Back by Return Value

**Code:** [Lab_CircleAreaReturn.py](Lab_CircleAreaReturn.py)

```python
def calculate_area(radius):
    area=3.14*radius**2
    return area

area=0
r=float(input("원의 반지름: "))
area=calculate_area(r)
print(area)
```

- **Two `area` variables:** The `area` inside the function is a local variable, and the `area` in the main part is a **global variable** created outside the function. They share a name but are different variables.
- **Passing the result back:** The function hands back the value of its local variable with `return`, and the main part assigns that value to the global variable `area`. The function does not change an outside variable directly, so the flow is easy to trace.
- **Computation:** The area of a circle is $\pi r^2$, with $\pi$ approximated by 3.14 here. For radius 5 it is $3.14 \times 25 = 78.5$.

**Output:** With radius 5. The prompt asks for the radius of the circle.

```text
원의 반지름: 5
78.5
```

### 3.2 The global Declaration

**Code:** [Lab_CircleAreaGlobal.py](Lab_CircleAreaGlobal.py)

```python
def calculate_area(radius):
    global area
    area = 3.14*radius**2
    return

area=0
r=float(input("원의 반지름: "))
calculate_area(r)
print(area)
```

- **The `global` declaration:** Assigning to a variable inside a function creates a local variable by default. Writing `global area` first makes `area` inside the function refer to the global variable `area`, so the assignment changes the value of the global variable.
- **No return value:** A bare `return` ends the function and hands back `None`. The result is passed through the global variable rather than a return value, so the main part prints `area` after the call.
- **Comparison with Section 3.1:** The result is the same, but when several functions change global variables it becomes hard to trace which function changed a value and when, so passing results back by return value as in Section 3.1 is generally recommended.

**Output:** With radius 5.

```text
원의 반지름: 5
78.5
```

### 3.3 A Global Constant

**Code:** [Lab_GlobalConstant.py](Lab_GlobalConstant.py)

```python
PI=3.14159265358979 #전역상수

def area_c(r):
    return PI*r**2

def main():
    r=float(input("r:"))
    print(area_c(r))

main()
```

- **Global constant:** A value that never changes throughout a program is conventionally defined once outside the functions with an uppercase name (the comment reads "global constant"). Python has no constant syntax that prevents a value from being changed, so an uppercase name is an agreement among programmers not to change the value.
- **Reading needs no `global`:** `area_c` only reads `PI`, so it can use the value of the global variable without a `global` declaration. A name that is not assigned inside a function is looked up outside it (globally).
- **Precision:** The value has 14 decimal places instead of 3.14, so the result is more precise than the 78.5 of Section 3.1.

**Output:** With radius 5.

```text
r:5
78.53981633974475
```

### 3.4 Updating Several Global Variables

**Code:** [Lab_SumAndAverageGlobal.py](Lab_SumAndAverageGlobal.py)

```python
def sumandavg(a, b):
    global sum, avg
    sum=a+b
    avg=(a+b)/2

sum=0 #주석처리해도 작동
avg=0 #주석처리해도 작동
a=50
b=60

sumandavg(a, b)
print("합=", sum)
print("평균=", avg)
```

- **Declaring several names `global`:** Several names can be declared at once, separated by commas, as in `global sum, avg`. The function stores the sum and the average in the two global variables.
- **Why initialization is not required:** As the comments say ("works even if commented out"), the program still works without `sum=0` and `avg=0`. Assigning inside the function to a name declared `global` creates the global variable at that moment, and the `print()` calls run after the function call.
- **Computation:** $50 + 60 = 110$ and $110 / 2 = 55.0$. `/` always returns a real number, so the average is printed as `55.0`.

**Output:** The labels mean "sum" and "average".

```text
합= 110
평균= 55.0
```

> **Caution:** `sum` is the name of a built-in function. This program assigns an integer to the global variable `sum`, so calling the built-in afterwards, as in `sum([1, 2, 3])`, raises a `TypeError`. Variable names should not clash with built-in functions (e.g., use `total`).

---

<br>

## 4. Ways of Passing Arguments and Anonymous Functions

### 4.1 Default Arguments

**Code:** [Lab_DefaultArgument.py](Lab_DefaultArgument.py)

```python
def greet(name, msg="별일없죠?"):
    print("안녕 ", name+', '+msg)

greet("영희")

#msg=" ~ "를 통해 디폴트 인수로 설정
#따로 매개변수에 대한 인자를 주지 않아도
#기본값을 출력함
```

- **Default argument:** Writing `=value` after a parameter lets a call omit that argument, in which case the value is used. This is called a **default argument**. In `greet("영희")`, `msg` is omitted, so `"별일없죠?"` is used, as the comments explain.
- **Order of parameters:** Parameters with default values must come after parameters without them. `def greet(msg="...", name):` is a syntax error.
- **Spaces in the output:** The space at the end of `"안녕 "` and the space that `print()` inserts between values combine, so two spaces are printed after `안녕`.

**Output:** The default value is used for `msg`. The output means "Hi Younghee, how have you been?"

```text
안녕  영희, 별일없죠?
```

Passing a second argument, as in `greet("철수", "반가워요")`, prints `반가워요` instead of the default value.

### 4.2 Keyword Arguments

**Code:** [Lab_KeywordArguments.py](Lab_KeywordArguments.py)

```python
def calc(x, y, z):
    print(x)
    print(y)
    print(z)

#입력창에 calc(y=20, x=10, z=30)
#calc(20, 10, 30)과 결과 비교

#키워드 인수는 인수의 이름을
#명시적으로 지정해서 전달하는 방법

## main ##
calc(y=20, x=10, z=30)
calc(20, 10, 30)
```

- **Positional arguments:** Writing only values, as in `calc(20, 10, 30)`, assigns them to `x`, `y`, and `z` in order. These are called **positional arguments**.
- **Keyword arguments:** Writing `parameter=value`, as in `calc(y=20, x=10, z=30)`, assigns each value to the parameter of the same name regardless of order. These are called **keyword arguments**, and they make it clear where each value goes when there are many arguments.
- **Comparison:** The first call gives `x=10, y=20, z=30` and the second `x=20, y=10, z=30`, so the printed order differs. The comments suggest calling the function directly in the IDLE shell window and comparing the two results.

**Output:** The first three lines come from the first call and the last three from the second.

```text
10
20
30
20
10
30
```

> **Note:** When positional and keyword arguments are mixed, the positional arguments must come first. `calc(10, z=30, y=20)` is valid, but `calc(x=10, 20, 30)` is a syntax error.

### 4.3 Anonymous Functions with lambda

**Code:** [Lab_Lambda.py](Lab_Lambda.py)

```python
sum = lambda x, y: x+y;

print("정수의 합: ", sum(10,20))
print("정수의 합: ", sum(20,20))

#def sum_(x,y):
#    return x+y
#위 함수의 무명함수 버전
```

- **`lambda`:** `lambda parameters: expression` creates a nameless function that returns the value of one expression, that is, an **anonymous function**. It does in one line what `def sum_(x,y): return x+y` in the comment does.
- **Assigning to a variable:** Assigning the created function object to the variable `sum` allows it to be called like an ordinary function, as in `sum(10,20)`.
- **Semicolon:** The `;` at the end of the line separates statements written on one line, and it is unnecessary here where there is only one statement.

**Output:** The label means "sum of the integers".

```text
정수의 합:  30
정수의 합:  40
```

> **Caution:** As in Section 3.4, the variable name `sum` hides the built-in function `sum()`. Also, a `lambda` can hold only one expression, so a function that needs several statements is defined with `def`.

---

<br>

## 5. Modules

### 5.1 Importing a Module

**Code:** [Lab_ModuleImport.py](Lab_ModuleImport.py), [Lab_AddMinusModule.py](Lab_AddMinusModule.py)

```python
import Lab_AddMinusModule

a=10
b=20
Lab_AddMinusModule.add(a,b)
Lab_AddMinusModule.minus(a,b)

#모듈명이 Lab_AddMinusModule로 너무 길 때는
#import Lab_AddMinusModule as t로 작성하면
#t.add(a,b)처럼 사용할 수 있음

#또는 from Lab_AddMinusModule import *로
#작성하면 모듈명 빼고 그냥
#add(a,b) 사용 가능하지만 이름이 겹칠 수 있으므로 가능하면 쓰지 않음
```

```python
##module##

def add(a,b):
    print(a+b)

def minus(a,b):
    print(a-b)
```

- **Module:** A single `.py` file holding functions and variables is a **module**. The second file, `Lab_AddMinusModule.py`, is a module with two functions that print the sum and the difference of two numbers.
- **`import`:** `import Lab_AddMinusModule` finds `Lab_AddMinusModule.py` in the same folder (or on the path where Python looks for modules), runs it, and makes its names usable in the form `module_name.function_name`. The module name is the file name without `.py`, and since it must be an identifier, a name containing a hyphen cannot be imported.
- **Two other ways:** The comments describe attaching a short alias with `import ... as t` (Section 5.2) and using names without the module name through `from ... import *`. The latter brings every name of the module into the current file, so when a name already exists one of them is hidden and errors become hard to find, which is why the comment advises avoiding it.

**Output:** $10 + 20 = 30$ and $10 - 20 = -10$.

```text
30
-10
```

> **Note:** On the first import, Python saves the compiled module in a `__pycache__` folder next to it to speed up later runs. This folder is recreated when the program runs, so it is not kept in the repository.

### 5.2 An Alias with import as

**Code:** [Lab_ModuleAlias.py](Lab_ModuleAlias.py), [Lab_ArithmeticModule.py](Lab_ArithmeticModule.py)

```python
import Lab_ArithmeticModule as t8

a=10
b=20
c=30

print(t8.add(a, t8.mul(b,c)))
```

```python
##module##

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b
```

- **Alias:** `import module as alias` lets the module be called by the short name `t8`. `t8.add` is the same function as `Lab_ArithmeticModule.add`.
- **Module functions that return:** The module functions of Section 5.1 only print their results, but the functions of this module return them, so they can be combined by passing one as an argument to another.
- **Order of evaluation:** The inner call `t8.mul(b,c)` is evaluated first, giving $20 \times 30 = 600$, and that value becomes an argument of `t8.add(a, 600)`, so $10 + 600 = 610$ is printed.

**Output:**

```text
610
```

---

<br>

## Summary

| Concept | Key Summary |
|:-----|:-----|
| Defining and calling functions | A body defined with `def` runs each time the function is called, and a function must be defined before it is called. |
| Return values | `return` hands a value back to the caller, and a function without `return` or with a bare `return` hands back `None`. |
| Returning several values | `return a, b` returns one tuple, and `x, y = f()` receives its elements separately. |
| Type hints | `x: int` and `-> int` only describe expected types and are not checked at run time. |
| Local and global variables | A name assigned inside a function is local, changing a global variable requires a `global` declaration, and reading it does not. |
| Default and keyword arguments | A parameter with a default value can be omitted, and passing `name=value` assigns regardless of order. |
| `lambda` | Creates in one line an anonymous function that returns the value of one expression. |
| Modules | A single `.py` file is a module, and `import`, `import as`, and `from ... import` bring in its names. |

---

<br>

## Self-Check Questions

1. **A function without a return value:** What is printed if the last line of `Lab_FunctionWithoutReturn.py` is replaced with the two lines `z = f(x)` and `print(z)`?

   <details>
   <summary>Answer</summary>

   Running `f(x)` makes the `print(y)` inside the function print `123`, and since `f` has no `return`, `None` is stored in `z` and `None` is printed. The output is the two lines `123` and `None`.

   </details>

2. **Unpacking:** What happens when `a, b = g()` runs, given `def g(): return 1, 2, 3`?

   <details>
   <summary>Answer</summary>

   `g()` returns the tuple `(1, 2, 3)` with three elements, but there are two variables on the left, so a `ValueError` (too many values to unpack) occurs. The number of variables must match, as in `a, b, c = g()`.

   </details>

3. **When global is needed:** Which of the following two functions raises an error when run without a `global count` declaration, and why?

   ```python
   count = 0
   def show():
       print(count)
   def add_one():
       count = count + 1
   ```

   <details>
   <summary>Answer</summary>

   `add_one`. Because `count` is assigned inside the function, `count` is a local variable throughout that function, and when the `count` on the right is read it has no value yet, so an `UnboundLocalError` occurs. `show` only reads it, so it prints the global value 0.

   </details>

4. **Keyword arguments:** Write the output of `calc(z=1, x=2, y=3)`.

   <details>
   <summary>Answer</summary>

   By name, `x=2, y=3, z=1`, so 2, 3, and 1 are printed one per line in the order `x`, `y`, `z`.

   </details>

5. **Combining module functions:** What is printed when `print(t8.sub(t8.div(c, a), b))` runs in `Lab_ModuleAlias.py`?

   <details>
   <summary>Answer</summary>

   `t8.div(30, 10)` uses the `/` operator, so it is the real number 3.0, and `t8.sub(3.0, 20)` is -17.0. Therefore `-17.0` is printed.

   </details>
