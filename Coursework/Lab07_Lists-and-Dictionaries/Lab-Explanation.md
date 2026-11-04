# Lab 7 Explanation — Lists and Dictionaries

[Repository Guide](../../README.md) | [English](Lab-Explanation.md) | [한국어](Lab-Explanation.ko.md)

> **Last Updated:** 2026-11-04

> **Learning Objectives:**
> 1. Read and change list elements by index, and use `append()`, `insert()`, `remove()`, `del`, `pop()`, and `index()`
> 2. Explain with references why a list passed to a function and changed inside it is also changed for the caller
> 3. Sort and build lists with bubble sort and list comprehensions
> 4. Create and fill 2D lists and distinguish assignment from copying
> 5. Look up, change, add, and delete dictionary values by key and use the main dictionary methods
> 6. Judge when a `global` declaration is needed for global variables and global lists inside a function

---

## Table of Contents

- [1. Lab Layout and How to Run](#1-lab-layout-and-how-to-run)
- [2. Creating Lists and Basic Operations](#2-creating-lists-and-basic-operations)
  - [2.1 The Type of a List](#21-the-type-of-a-list)
  - [2.2 Changing, Adding, Deleting, and Searching Elements](#22-changing-adding-deleting-and-searching-elements)
  - [2.3 Three Ways to Find an Index](#23-three-ways-to-find-an-index)
  - [2.4 The Index of the Smallest Value](#24-the-index-of-the-smallest-value)
- [3. Functions and Lists](#3-functions-and-lists)
  - [3.1 A List Changed Inside a Function](#31-a-list-changed-inside-a-function)
  - [3.2 Two Ways to Change an Element](#32-two-ways-to-change-an-element)
  - [3.3 An Average Computed with Functions](#33-an-average-computed-with-functions)
- [4. Sorting and List Comprehensions](#4-sorting-and-list-comprehensions)
  - [4.1 Bubble Sort](#41-bubble-sort)
  - [4.2 List Comprehensions](#42-list-comprehensions)
- [5. Global Variables and Global Lists](#5-global-variables-and-global-lists)
  - [5.1 Assigning to a Global Variable without global](#51-assigning-to-a-global-variable-without-global)
  - [5.2 A Local Variable Hiding a Global Variable](#52-a-local-variable-hiding-a-global-variable)
  - [5.3 Changing a Global List](#53-changing-a-global-list)
- [6. 2D Lists and Copying Lists](#6-2d-lists-and-copying-lists)
  - [6.1 A List Whose Elements Are Lists](#61-a-list-whose-elements-are-lists)
  - [6.2 Repeating and Concatenating Lists](#62-repeating-and-concatenating-lists)
  - [6.3 Filling a 2D List](#63-filling-a-2d-list)
  - [6.4 Assignment and Copying](#64-assignment-and-copying)
- [7. Dictionaries](#7-dictionaries)
  - [7.1 A Phone Book](#71-a-phone-book)
  - [7.2 Looking Up an Item Count](#72-looking-up-an-item-count)
  - [7.3 Looking Up, Changing, Adding, and Deleting Values](#73-looking-up-changing-adding-and-deleting-values)
  - [7.4 Dictionary Methods](#74-dictionary-methods)
- [8. Dice-Throwing Simulation](#8-dice-throwing-simulation)
  - [8.1 Counting with Six Variables](#81-counting-with-six-variables)
  - [8.2 Counting with a List](#82-counting-with-a-list)
- [Summary](#summary)
- [Self-Check Questions](#self-check-questions)

---

<br>

## 1. Lab Layout and How to Run

This code was written while following [Lecture 7, Lists and Dictionaries](../../Lecture-Notes/Lec07_Lists-and-Dictionaries/Concepts_Lecture.md). The global variables of Section 5 extend the local and global variables of [Lecture 6, Functions](../../Lecture-Notes/Lec06_Functions/Concepts_Lecture.md) to lists. Sections 2-4 and 6 cover lists, Section 7 covers dictionaries, and Section 8 covers a simulation that uses both types.

```text
Coursework/Lab07_Lists-and-Dictionaries/
├── Lab-Explanation.ko.md              # This document (Korean)
├── Lab-Explanation.md                 # This document (English)
├── Lab_ListType.py                    # 2.1 The type of a list
├── Lab_ListOperations.py              # 2.2 Changing, adding, deleting, and searching elements
├── Lab_IndexSearch.py                 # 2.3 Three ways to find an index
├── Lab_MinIndex.py                    # 2.4 The index of the smallest value
├── Lab_ListArgument.py                # 3.1 A list changed inside a function
├── Lab_ModifyListInFunction.py        # 3.2 Two ways to change an element
├── Lab_AverageWithFunctions.py        # 3.3 An average computed with functions
├── Lab_BubbleSort.py                  # 4.1 Bubble sort
├── Lab_ListComprehension.py           # 4.2 List comprehensions
├── Lab_GlobalVariableAssignment.py    # 5.1 Assigning to a global variable without global
├── Lab_LocalShadowing.py              # 5.2 A local variable hiding a global variable
├── Lab_GlobalList.py                  # 5.3 Changing a global list
├── Lab_ListOfLists.py                 # 6.1 A list whose elements are lists
├── Lab_ListRepetition.py              # 6.2 Repeating and concatenating lists
├── Lab_TwoDimensionalList.py          # 6.3 Filling a 2D list
├── Lab_ListCopy.py                    # 6.4 Assignment and copying
├── Lab_PhoneBook.py                   # 7.1 A phone book
├── Lab_ItemLookup.py                  # 7.2 Looking up an item count
├── Lab_DictionaryBasics.py            # 7.3 Looking up, changing, adding, and deleting values
├── Lab_DictionaryMethods.py           # 7.4 Dictionary methods
├── Lab_DiceCounters.py                # 8.1 Counting with six variables
└── Lab_DiceList.py                    # 8.2 Counting with a list
```

*Figure 1. Directory layout of Lab 7*

All programs use only the standard library and run as they are under Python 3. The programs that use random numbers (Sections 4.1 and 8) give different results on each run, and this document shows one example run. Each file begins with a documentation string (docstring) that records the file name, a one-line description, the author, and the date written, and the code blocks in this document omit that part.

```bash
cd Coursework/Lab07_Lists-and-Dictionaries
python3 Lab_ListOperations.py
```

---

<br>

## 2. Creating Lists and Basic Operations

### 2.1 The Type of a List

**Code:** [Lab_ListType.py](Lab_ListType.py)

```python
#<class 'list'>라고 출력되는 것들
a=[]
print(type(a))

b=list()
print(type(b))

c=[1,2,'4']
print(type(c))

d=[1,2,3,c] #c가 존재하므로 오류 발생 X
print(type(d)) #리스트 안에 리스트가 존재할 수 있음
```

- **Ways to create a list:** Empty brackets `[]` and `list()` both create an empty list. `type()` returns the type of a value, so all four lines print `<class 'list'>`.
- **Elements of several types:** As in `c`, one list can hold the integers `1` and `2` together with the string `'4'`.
- **Nested list:** The last element of `d` is the list `c`. A list can have other lists as elements, and the comments note that no error occurs because `c` is already defined. `d[3][2]` is `'4'`, the third element of `c`.

**Output:**

```text
<class 'list'>
<class 'list'>
<class 'list'>
<class 'list'>
```

### 2.2 Changing, Adding, Deleting, and Searching Elements

**Code:** [Lab_ListOperations.py](Lab_ListOperations.py)

```python
#리스트 항목 변경법
print("리스트 항목 변경법")
heroes=["아이언맨","토르"]
print(heroes)

#변경
print("\n변경")
heroes[1]="닥터 스트레인지"
print(heroes)

#추가
print("\n추가")
heroes.append("스파이더맨")
heroes.insert(2, "배트맨") #위치(인덱스) 지정
print(heroes)

#삭제
print("\n삭제")
heroes.remove("닥터 스트레인지")
del heroes[0] #위치(인덱스) 지정
print(heroes)

#pop은 리스트에서 마지막 항목을 삭제함
print("\npop 활용")
heroes9=["아이언맨","토르","헐크","스칼렛 위치"]
last_hero=heroes9.pop()
print(last_hero)

#조건문 활용 예
print("\n조건문 활용 예")
if "슈퍼맨" in heroes:
    heroes.remove("슈퍼맨")

#탐색
heroes8=["아이언맨","토르","헐크","스칼렛 위치"]
print(heroes8.index("헐크"))

#index를 직접 구현
for i in range (len(heroes8)):
    if "헐크" in heroes8[i]:
        print("인덱스: ", i)

#입력받은 데이터의 인덱스 출력
heroes7=["아이언맨","토르","헐크","스칼렛 위치"]
ans=input("찾고자 하는 데이터: ")
for i in range(len(heroes7)):
    if ans == heroes7[i]:
        print(i)
```

- **Changing:** `heroes[1] = value` replaces the element at index 1 with a new value. A list is a **mutable** type whose elements can be changed after it is created. The list holds superhero names (Iron Man, Thor, Doctor Strange, and so on).
- **Adding:** `append(x)` attaches `x` at the end, and `insert(2, x)` puts `x` at index 2 and shifts the elements from that position one place back.
- **Deleting:** `remove(x)` deletes the first element whose value is `x`, and `del heroes[0]` deletes the element at index 0. The choice depends on whether to delete by value or by position.
- **`pop()`:** It takes the last element out of the list and returns it. So `"스칼렛 위치"` (Scarlet Witch) is stored in `last_hero`, and `heroes9` shrinks to three elements.
- **`in` and a conditional:** `remove()` raises a `ValueError` when asked to delete a value that is not there, so `if "슈퍼맨" in heroes:` checks first. `"슈퍼맨"` (Superman) is not in the list, so nothing happens.
- **Searching:** `index("헐크")` returns 2, the index where `"헐크"` (Hulk) first appears. The loop that follows implements the same thing directly. The `"헐크" in heroes8[i]` in this loop is `in` between two strings, so it checks containment rather than equality. It is also true for an element `"헐크버스터"` (Hulkbuster), so to find exactly equal elements, compare with `==` as in the last loop.

**Output:** With `토르` entered at the last prompt. The headings of the steps are, in order, "how to change list items", "change", "add", "delete", "using pop", and "example with a conditional", and the prompt asks for the data to find.

```text
리스트 항목 변경법
['아이언맨', '토르']

변경
['아이언맨', '닥터 스트레인지']

추가
['아이언맨', '닥터 스트레인지', '배트맨', '스파이더맨']

삭제
['배트맨', '스파이더맨']

pop 활용
스칼렛 위치

조건문 활용 예
2
인덱스:  2
찾고자 하는 데이터: 토르
1
```

In the adding step, `append()` gives `['아이언맨', '닥터 스트레인지', '스파이더맨']`, and then `insert(2, ...)` puts `'배트맨'` (Batman) at index 2, shifting `'스파이더맨'` (Spider-Man) to index 3. In the deleting step, `remove()` deletes `'닥터 스트레인지'` and `del` deletes `'아이언맨'` at index 0.

### 2.3 Three Ways to Find an Index

**Code:** [Lab_IndexSearch.py](Lab_IndexSearch.py)

```python
def index_(list_, g):
    f_index=0
    for i in range(len(h)):
        if g==h[i]:
            f_index=i
    return f_index

h=["아","토","헐","스","헐"]
g=input("i:")
for i in range(len(h)):
    if g==h[i]:
        print(i)

print(index_(h,g))
print(h.index(g))

#수식에 따라 "헐"이 두개일때 모두 출력하거나
#마지막 값만 출력하게 됨
```

- **Printing all with a loop:** The loop in the main part prints the index each time it meets an element equal to `g`, so if a value appears several times, all positions are printed.
- **The self-made function `index_`:** It overwrites `f_index` each time it meets an equal element, so it returns the last matching index. If no element matches, it returns the initial value 0, which cannot be told apart from a match at index 0.
- **`list.index()`:** It returns the first matching index. As the comments say, when a value appears twice, the result depends on the method.

**Output:** With `헐` entered. `"헐"` is at indices 2 and 4, so the loop prints 2 and 4, `index_` prints 4, and `index()` prints 2.

```text
i:헐
2
4
4
2
```

> **Note:** The function `index_` takes the parameter `list_` but uses the global variable `h` in its body. This program passes `h` as the argument, so the result is the same, but passing another list would still search `h`. Replacing every `h` in the body with `list_` makes it a function that searches the list it is given. Also, entering a value not in `h` makes `h.index(g)` on the last line raise a `ValueError`.

### 2.4 The Index of the Smallest Value

**Code:** [Lab_MinIndex.py](Lab_MinIndex.py)

```python
list_=[1, 3, 67, 8, 3, 5, -1, 3, -9, 10]
temp=list_[0]

#가장 작은 값의 인덱스 구하기
min=0
for i in range (len(list_)):
    if list_[i] < temp:
        min=i
        temp=list_[i]

print("min index: ", min)
```

- **Method:** The first element is taken as the smallest value so far, `temp`, with its index 0 in `min`, and every element is examined in turn, updating both variables whenever an element smaller than `temp` is met.
- **Trace:** `temp` starts at 1, becomes -1 on meeting -1 at index 6, and becomes -9 on meeting -9 at index 8. So the final `min` is 8.
- **Equal minimum values:** The comparison is `<`, so when the minimum value appears several times, the first index remains.

**Output:**

```text
min index:  8
```

> **Caution:** The variable name `min` hides the built-in function `min()`. With the built-in, `list_.index(min(list_))` gives the same result, so a name such as `min_index` is safer.

---

<br>

## 3. Functions and Lists

### 3.1 A List Changed Inside a Function

**Code:** [Lab_ListArgument.py](Lab_ListArgument.py)

```python
# 리턴받지 않고 하는 함수
def f_c(list_):
    list_[0]=100

def f_c2(list_): # 이렇게 작성하지 않음.
    list_a[0]=1

##main##
list_a=[1,2,3,4,5]
f_c(list_a)
print(list_a)
f_c2(list_a)
print(list_a)
```

- **Passing references:** A Python variable holds not the value itself but a **reference** to an object. Calling `f_c(list_a)` makes the parameter `list_` refer to the same list object as `list_a`, so `list_[0]=100` changes that object, and the changed value is visible through the caller's `list_a`. So the result is passed back without a return (the first comment reads "a function that works without returning").
- **The problem with `f_c2`:** It ignores the parameter `list_` and changes the global variable `list_a` directly. In this call it is the same list, so the result is the same, but `list_a` would change even if another list were passed, so, as the comment says, this style is not used.

**Output:**

```text
[100, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
```

### 3.2 Two Ways to Change an Element

**Code:** [Lab_ModifyListInFunction.py](Lab_ModifyListInFunction.py)

```python
def func2(list):
    list[0] = 99

values = [0,1,1,2,3,5,8]
print(values)
func2(values)
print(values)

# 또는

def func1(list):
    return 99

value = [0,1,1,2,3,5,8]
print(value)
value[0] = func1(value)
print(value)
```

- **Changing inside the function:** `func2`, like `f_c` in Section 3.1, changes the list it receives directly.
- **Changing through a return value:** `func1` only returns the new value 99, and the caller assigns it with `value[0] = func1(value)`. The function does not change its argument, so its behavior is easy to understand.
- **Result:** Both ways make the first element 99. The list is the beginning of the Fibonacci sequence.

**Output:**

```text
[0, 1, 1, 2, 3, 5, 8]
[99, 1, 1, 2, 3, 5, 8]
[0, 1, 1, 2, 3, 5, 8]
[99, 1, 1, 2, 3, 5, 8]
```

> **Caution:** The parameter name `list` hides the built-in function `list()`. A list can then no longer be created with `list()` inside the function, so another name such as `nums` should be used.

### 3.3 An Average Computed with Functions

**Code:** [Lab_AverageWithFunctions.py](Lab_AverageWithFunctions.py)

```python
'''num = []
for i in range(5):
    num.append(int(input(":")))

sum_=0
for j in num: #num 리스트의 원소 중 하나가 들어감
    sum_ += j

avg = sum_ / 5
print(avg)
'''
#위 코드를 함수를 이용하여 작성

num=[]
def insert_():
    for i in range(5):
        num.append(int(input(":")))

def avg_():
    sum_ = 0
    for j in num:
        sum_ += j
    avg=sum_/5
    print(avg)

def main():
    insert_()
    avg_()

main()
```

- **Problem:** Split code that reads five integers and prints their average (kept as a string) into two functions, one for input and one for computation, as the comment ("rewrite the code above with functions") says.
- **Global list:** `insert_` and `avg_` share the global list `num`. `insert_` only changes the list object with `append()` and assigns no new value to `num`, so no `global` declaration is needed (Section 5.3).
- **Iterating over elements:** `for j in num:` takes the elements one at a time into `j` without indices. As the comment says, `j` receives the elements of `num` in turn.

**Output:** With inputs 10, 20, 30, 40, and 50. $150 / 5 = 30.0$.

```text
:10
:20
:30
:40
:50
30.0
```

---

<br>

## 4. Sorting and List Comprehensions

### 4.1 Bubble Sort

**Code:** [Lab_BubbleSort.py](Lab_BubbleSort.py)

```python
import random
datalist=[]

for i in range (0, 5, 1):
    datalist.append(random.randint(1, 100))

print(datalist)

for j in range(len(datalist)-1): # 비효율적인 방법
    for i in range(len(datalist)-1):
        if datalist[i] > datalist[i+1]:
            temp=datalist[i]
            datalist[i]=datalist[i+1]
            datalist[i+1]=temp
    print(datalist)

print(datalist)
```

- **Data:** Five random numbers from 1-100 are put in a list.
- **Bubble sort:** Comparing adjacent elements from the front and swapping them when the first is larger, all the way to the end of the list, is called one **pass**. After a pass, the largest value of the still unsorted part has moved to the end. The name comes from large values rising to the back like bubbles.
- **Swapping:** The first element is held in `temp` for a moment while the two elements are swapped. In Python this can also be written in one line as `datalist[i], datalist[i+1] = datalist[i+1], datalist[i]`.
- **Number of passes:** With $n$ elements, $n-1$ passes are enough. After the $k$-th pass the $k$ largest values are in place at the end, so after $n-1$ passes the one remaining value is also in place at the front. The outer loop runs these $n-1$ passes with `range(len(datalist)-1)` and prints the list after each pass.
- **Source of inefficiency:** As the comment ("an inefficient method") says, this implementation makes $n-1$ comparisons in every pass, $(n-1)^2$ in all. After the $k$-th pass the last $k$ elements need no comparison, so shrinking the inner loop to `range(len(datalist)-1-j)` reduces the comparisons to $n(n-1)/2$, and if a pass makes no swap at all, the list is already sorted and the loop can end.

**Output:** One example run. The first line is before sorting, the middle four lines are after each pass, and the last line is the sorted result.

```text
[78, 37, 88, 72, 61]
[37, 78, 72, 61, 88]
[37, 72, 61, 78, 88]
[37, 61, 72, 78, 88]
[37, 61, 72, 78, 88]
[37, 61, 72, 78, 88]
```

> **Caution:** Running the outer loop only $n-2$ times leaves some inputs unsorted. For example, `[5, 4, 3, 2, 1]` becomes `[4, 3, 2, 1, 5]`, `[3, 2, 1, 4, 5]`, and `[2, 1, 3, 4, 5]` after successive passes, so after three passes the first two elements are still swapped. When the smallest value is at the end, it moves forward only one place per pass, so $n-1$ passes are needed.

### 4.2 List Comprehensions

**Code:** [Lab_ListComprehension.py](Lab_ListComprehension.py)

```python
# 예시1
s=[]
for x in range(10):
    s.append(x**2)
print(s)

ss=[x**2 for x in range(10)] # 함축
print(ss)


# 예시2
sss=[]
for x in range(10):
    if x%2==0:
        sss.append(x**2)
print(sss)

ssss=[x**2 for x in range(10) if x%2==0] # 함축
print(ssss)
```

- **List comprehension:** `[expression for variable in iterable]` computes the expression for each element of the iterable and builds a new list from those values. It is the same as writing in one line the three lines that create an empty list and `append()` in a `for` statement. The comments label the examples ("example 1", "example 2") and the comprehensions ("comprehension").
- **Adding a condition:** `[expression for variable in iterable if condition]` computes the expression only for elements for which the condition is true. Example 2 collects only the squares of the even numbers (`x%2==0`) in 0-9.

**Output:** The two ways in each example build the same list.

```text
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 4, 16, 36, 64]
[0, 4, 16, 36, 64]
```

---

<br>

## 5. Global Variables and Global Lists

### 5.1 Assigning to a Global Variable without global

**Code:** [Lab_GlobalVariableAssignment.py](Lab_GlobalVariableAssignment.py)

```python
global_var = 10

def modify_global():
    #global global_var
    print("Before modification:", global_var)
    global_var = 20
    print("After modification:", global_var)

def access_global():
    print("Accessing global variable:", global_var)

# 함수 실행
access_global()
try:
    modify_global()
except UnboundLocalError as e:
    print("UnboundLocalError:", e)
access_global()
```

- **A function that only reads:** `access_global` only reads `global_var`, so it prints the global value 10.
- **A function that assigns:** `modify_global` contains the assignment `global_var = 20`. Before running a function, Python looks at its whole body and makes every name assigned inside it a local variable of that function. So the `global_var` read by the first `print()` is also a local variable that has no value yet, and an **`UnboundLocalError`** occurs. This is so even though the assignment comes after the read.
- **Handling the error:** The `global` declaration is commented out to show the error, and `try-except` catches the error, prints its message, and moves on to the next statement. The last `access_global()` shows that the global variable is still 10. The comment before the calls reads "run the functions".
- **How to fix it:** Restoring the commented-out `global global_var` makes `global_var` inside the function refer to the global variable, so `Before modification: 10` and `After modification: 20` are printed, and the last line prints 20.

**Output:** The error message is the wording of Python 3.11 and later, and earlier versions print `local variable 'global_var' referenced before assignment`.

```text
Accessing global variable: 10
UnboundLocalError: cannot access local variable 'global_var' where it is not associated with a value
Accessing global variable: 10
```

### 5.2 A Local Variable Hiding a Global Variable

**Code:** [Lab_LocalShadowing.py](Lab_LocalShadowing.py)

```python
global_var = 10

def modify_global():
    #global global_var
    print("Before modification:",global_var)
    global_var = 20
    print("After modification:",global_var)

def access_global():
    global_var = 200
    print("Accessing global variable:",global_var)

# 함수 실행
access_global()
try:
    modify_global()
except UnboundLocalError as e:
    print("UnboundLocalError:", e)
access_global()
```

- **Difference from Section 5.1:** `access_global` assigns `global_var = 200` inside itself, so this `global_var` is a local variable of `access_global`. The local variable hides the global variable of the same name, so 200 is printed inside the function while the global variable stays 10.
- **Result:** `access_global` assigns 200 to a new local variable on every call, so it prints 200 both times, and `modify_global` raises an `UnboundLocalError` for the same reason as in Section 5.1. The message says "Accessing global variable", but what is actually printed is the value of the local variable.

**Output:**

```text
Accessing global variable: 200
UnboundLocalError: cannot access local variable 'global_var' where it is not associated with a value
Accessing global variable: 200
```

### 5.3 Changing a Global List

**Code:** [Lab_GlobalList.py](Lab_GlobalList.py)

```python
global_list = [1, 2, 3, 4]

def modify_global_list():
    global global_list
    print("Before modification:", global_list)
    global_list.append(5)
    global_list.extend([6, 7])
    print("After modification:", global_list)

def access_global_list():
    print("Accessing global variable:", global_list)

# 함수 실행
access_global_list()
modify_global_list()
access_global_list()
```

- **List methods:** `append(5)` attaches one element at the end, and `extend([6, 7])` attaches the elements of another list. Writing `append([6, 7])` would put the list `[6, 7]` itself in as one element.
- **Why the `global` declaration can be omitted:** `append()` and `extend()` only change the list object that `global_list` refers to and assign no new value to the name `global_list`. Without an assignment, the name is looked up as a global variable, so deleting the line `global global_list` gives the same result. In contrast, assigning to the name, as in `global_list = global_list + [5]`, requires a `global` declaration.
- **Result:** The list changed inside the function appears as `[1, 2, 3, 4, 5, 6, 7]` outside the function as well.

**Output:**

```text
Accessing global variable: [1, 2, 3, 4]
Before modification: [1, 2, 3, 4]
After modification: [1, 2, 3, 4, 5, 6, 7]
Accessing global variable: [1, 2, 3, 4, 5, 6, 7]
```

---

<br>

## 6. 2D Lists and Copying Lists

### 6.1 A List Whose Elements Are Lists

**Code:** [Lab_ListOfLists.py](Lab_ListOfLists.py)

```python
s=[]
s.append([1,2,3,4])
s.append([1,2,3,4])
s.append([5,6,7]) #열의 개수가 달라지면?
print(s)
print(len(s))
print(len(s[0])) #열의 개수
```

- **2D list:** A list whose elements are lists can be used like a table of rows and columns. `s[i]` is the `i`-th row, and `s[i][j]` is the `j`-th element of that row.
- **Length:** `len(s)` is the number of rows, 3, and `len(s[0])` is the number of elements in the first row, 4 (the comment reads "number of columns").
- **Rows of different lengths:** As the comment asks ("what if the number of columns differs?"), the third row has three elements. Python lists allow rows of different lengths, so no error occurs, but then `len(s[0])` is only the length of the first row, not the number of columns of every row, and `s[2][3]` raises an `IndexError`.

**Output:**

```text
[[1, 2, 3, 4], [1, 2, 3, 4], [5, 6, 7]]
3
4
```

### 6.2 Repeating and Concatenating Lists

**Code:** [Lab_ListRepetition.py](Lab_ListRepetition.py)

```python
a=[1]
b=a*5
print(b)

c=a+b
print(c)
```

- **Repetition (`*`):** `list * n` creates a new list that joins the elements of the list `n` times. `[1] * 5` is `[1, 1, 1, 1, 1]`.
- **Concatenation (`+`):** It creates a new list that joins two lists. `[1] + [1, 1, 1, 1, 1]` has six elements. Neither operation changes the original lists `a` and `b`.

**Output:**

```text
[1, 1, 1, 1, 1]
[1, 1, 1, 1, 1, 1]
```

### 6.3 Filling a 2D List

**Code:** [Lab_TwoDimensionalList.py](Lab_TwoDimensionalList.py)

```python
rows = 3
cols = 5

s = []
for row in range(rows):
    s += [[0]*cols]
#for i in range(r):
#    s.append([0]*5) 도 가능

print("s =", s)

for i in range(rows):
    for j in range(cols):
        data=int(input("추가할 값을 입력하세요:"))
        s[i][j] = data
#자동으로 0~14로 채우려면
#s[i][j]=n
#n+=1 을 for i, for j 안에 채우면 됨

print("s =", s)
```

- **Making rows:** In each iteration, `[0]*cols` creates a new list of five zeros, and `s += [that list]` attaches it as one row. As the comment says, `s.append([0]*5)` also works.
- **Nested loops:** The outer loop fixes the row `i` and the inner loop the column `j` in turn, so 15 values are read in the order `s[0][0]`, `s[0][1]`, ..., `s[2][4]`. This order is called **row-major order**.
- **Filling automatically:** The comments note that instead of reading input, starting from `n = 0` and putting `s[i][j] = n` and `n += 1` in the inner loop fills in 0-14 in order. `s[i][j] = i * cols + j` gives the same values.

**Output:** With 0 to 14 entered in order. Of the 15 input lines, only the first two and the last are shown, and the middle is omitted. The prompt asks for the value to add.

```text
s = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
추가할 값을 입력하세요:0
추가할 값을 입력하세요:1
(12 lines omitted)
추가할 값을 입력하세요:14
s = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]]
```

> **Caution:** The rows must not be made with `s = [[0]*cols]*rows`. The outer `*` copies a reference to the same row list `rows` times, so all three rows are one object, and `s[0][0] = 7` changes the first element of all three rows to 7. A new list must be made for each row, with a loop as in this program or with `[[0]*cols for _ in range(rows)]`.

### 6.4 Assignment and Copying

**Code:** [Lab_ListCopy.py](Lab_ListCopy.py)

```python
a=[1,2,3,4]
b=a
a[3]=1000
print(a)
print(b)

#리스트를 이렇게 복사하고 바꾸면
# a=[1,2,3,1000]
# b=[1,2,3,4]
#로 출력될 것이라고 예상할 수도 있지만
# a와 b가 같은 리스트 객체를 가리키므로 b도 [1,2,3,1000]으로 출력된다

b[3]=4
print(a)
print(b)

#따라서 복사할 때
c=list(b)
b[3]=10
print(b)
print(c)
#이렇게 복사해야 바뀐 값까지 복사되지 않음
```

- **Assignment is not copying:** `b=a` does not copy the list but makes `b` refer to the same list object as `a`. The two names become **aliases** of one object, so changing `a[3]` is visible through `b`, and restoring it with `b[3]=4` restores `a` as well. The comments explain that one might expect `b` to stay `[1,2,3,4]`, but since `a` and `b` refer to the same list object, `b` is also printed as `[1,2,3,1000]`.
- **Copying with `list()`:** `c=list(b)` creates a new list object from the elements of `b`. Changing `b[3]` to 10 afterwards leaves `c` as `[1, 2, 3, 4]`. `b[:]` and `b.copy()` make the same kind of copy.
- **How to check:** `a is b` is `True` when the two names refer to the same object. In this program, `a is b` is `True` and `c is b` is `False`.

**Output:**

```text
[1, 2, 3, 1000]
[1, 2, 3, 1000]
[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 3, 10]
[1, 2, 3, 4]
```

> **Note:** `list()`, `[:]`, and `copy()` make a **shallow copy**. Only the outer list is new, and the elements refer to the same objects, so copying a 2D list this way shares the row lists. To copy the rows as well, use `deepcopy()` from the `copy` module.

---

<br>

## 7. Dictionaries

### 7.1 A Phone Book

**Code:** [Lab_PhoneBook.py](Lab_PhoneBook.py)

```python
pb = {}
pb["홍길동"] = "010-1234-5678"
print("1: ", pb)

pb2 = {"홍길동": "010-1234-5678"}
pb2["강감찬"] = "010-1234-5679"
print("2: ", pb2)

print("3: ", pb2["강감찬"])

print("4: 이 부분은 결과창에 한 줄씩 입력하면 나옴")
pb2.keys()
pb2.values()

print("5: ")
dict = {'Name': '홍길동', 'Age': 7, 'Class': '초급'}
print(dict['Name'])
print(dict['Age'])
```

- **Dictionary:** A type that holds `key: value` pairs in braces. Whereas a list finds elements by integer indices starting from 0, a dictionary finds values by names (keys). With names as keys and phone numbers as values, it becomes a phone book.
- **Adding and looking up:** `pb["홍길동"] = value` adds a new key-value pair if the key is absent and changes the value if it is present. `pb2["강감찬"]` returns the value for the key.
- **Part 4:** `pb2.keys()` and `pb2.values()` are only expressions that return values and print nothing. The printed message means "this part appears when typed line by line in the result window": in the IDLE shell window, the value of an expression typed on a line is shown automatically, but in a script it must be wrapped in `print()` to be seen.
- **Values of several types:** The dictionary in part 5 holds string and integer values together (`'초급'` means "beginner").

**Output:**

```text
1:  {'홍길동': '010-1234-5678'}
2:  {'홍길동': '010-1234-5678', '강감찬': '010-1234-5679'}
3:  010-1234-5679
4: 이 부분은 결과창에 한 줄씩 입력하면 나옴
5: 
홍길동
7
```

> **Caution:** The variable name `dict` hides the built-in type `dict`, so a dictionary can no longer be created with `dict()` afterwards. Use another name such as `student`.

### 7.2 Looking Up an Item Count

**Code:** [Lab_ItemLookup.py](Lab_ItemLookup.py)

```python
items = {"커피음료": 7, "펜": 3, "종이컵": 2, "우유": 1, "콜라": 4, "책": 5}

item = input("물건의 이름을 입력하시오: ")
print(items[item])
```

- **The input as a key:** The entered string is used as a key to find the count of that item (coffee drinks, pens, paper cups, milk, cola, books). The advantage of a dictionary is that one key finds its value directly, regardless of the number of keys.

**Output:** With `펜` (pen) entered. The prompt asks for the name of the item.

```text
물건의 이름을 입력하시오: 펜
3
```

> **Caution:** Entering a key that does not exist (e.g., `연필`, pencil) makes `items[item]` raise a `KeyError`. `items.get(item)` returns `None` when the key is absent and `items.get(item, 0)` returns 0, so the case can be handled without an error. Checking first with `if item in items:` also works.

### 7.3 Looking Up, Changing, Adding, and Deleting Values

**Code:** [Lab_DictionaryBasics.py](Lab_DictionaryBasics.py)

```python
person = {
    "name": "John",
    "age": 30,
    "city": "New York",
}

print(person["name"])
print(person["age"])

# 값 변경
person["age"] = 31
print(person["age"])

# 새로운 키-값 쌍 추가
person["job"] = "Developer"
print(person)

#키-값 쌍 삭제
del person["city"]
print(person)

# 키를 인덱스처럼 사용할 수 있는 것이
# 리스트와의 큰 차이
```

- **Writing over several lines:** When there are many key-value pairs, they are written one per line, and a comma after the last pair is allowed.
- **Changing and adding:** Assigning to the existing key `"age"` changes its value, and assigning to the absent key `"job"` adds a new pair (the comments read "change a value" and "add a new key-value pair"). The same syntax acts in two ways depending on whether the key exists.
- **Deleting:** `del person["city"]` deletes the key `"city"` together with its value.
- **Order:** Since Python 3.7, dictionaries keep the order in which keys were inserted, so the newly added `"job"` is printed last. As the last comment says, finding values by key instead of the integer indices of a list is the big difference from lists.

**Output:**

```text
John
30
31
{'name': 'John', 'age': 31, 'city': 'New York', 'job': 'Developer'}
{'name': 'John', 'age': 31, 'job': 'Developer'}
```

### 7.4 Dictionary Methods

**Code:** [Lab_DictionaryMethods.py](Lab_DictionaryMethods.py)

```python
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

keys = person.keys()
print(keys)

values = person.values()
print(values)

items = person.items()
print(items)

name = person.get("name")
# person["name"] 도 가능!
print(name)

person.update({"age": 31, "job": "Developer"})
print(person)
```

- **`keys()`, `values()`, `items()`:** They return view objects that show the keys, the values, and the `(key, value)` tuples, respectively. A view follows changes to the dictionary and can be turned into a list with `list(person.keys())`. They are used in loops to take keys and values together, as in `for k, v in person.items():`.
- **`get()`:** `person.get("name")` returns the same value as `person["name"]` (as the comment notes), but when the key is absent it returns `None` (or a default given as the second argument) instead of raising an error.
- **`update()`:** It changes or adds values from the pairs of the dictionary given as its argument. `"age"` changes to 31, and `"job"` is newly added.

**Output:**

```text
dict_keys(['name', 'age', 'city'])
dict_values(['John', 30, 'New York'])
dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])
John
{'name': 'John', 'age': 31, 'city': 'New York', 'job': 'Developer'}
```

---

<br>

## 8. Dice-Throwing Simulation

### 8.1 Counting with Six Variables

**Code:** [Lab_DiceCounters.py](Lab_DiceCounters.py)

```python
#주사위 1000번 던져서 각 숫자가 나올 확률 (1)
import random

pro1 = 0
pro2 = 0
pro3 = 0
pro4 = 0
pro5 = 0
pro6 = 0

for i in range(0, 1000, 1):
    a = random.randint(1,6)

    if (a == 1):
        pro1 += 1
    if (a == 2):
        pro2 += 1
    if (a == 3):
        pro3 += 1
    if (a == 4):
        pro4 += 1
    if (a == 5):
        pro5 += 1
    if (a == 6):
        pro6 += 1

print("주사위가 1인 확률은 ", pro1 / 1000)
print("주사위가 2인 확률은 ", pro2 / 1000)
print("주사위가 3인 확률은 ", pro3 / 1000)
print("주사위가 4인 확률은 ", pro4 / 1000)
print("주사위가 5인 확률은 ", pro5 / 1000)
print("주사위가 6인 확률은 ", pro6 / 1000)
```

- **Simulation:** The program throws a die 1000 times with `random.randint(1,6)` and adds 1 to the variable holding the count of the face that came up (the first comment reads "probability of each number when a die is thrown 1000 times").
- **Relative frequency:** The count divided by the total number of trials, 1000, is the **relative frequency**. The printed message calls this value a probability ("the probability that the die shows 1 is"), but strictly it is an estimate of the probability.
- **Limits of the structure:** One variable and one `if` statement per face means that the code grows as the number of faces grows. In one throw `a` has only one value, so only one of the six `if` conditions is true, and writing them with `if-elif` skips the remaining comparisons once the true condition is found.

**Output:** One example run.

```text
주사위가 1인 확률은  0.181
주사위가 2인 확률은  0.168
주사위가 3인 확률은  0.182
주사위가 4인 확률은  0.157
주사위가 5인 확률은  0.159
주사위가 6인 확률은  0.153
```

> **[Probability and Statistics]** For a fair die, the probability of each face is $1/6 \approx 0.167$. The tendency of the relative frequency to approach the probability as the same trial is repeated independently is called the law of large numbers. With about 1000 throws the values scatter around 0.15-0.18 as above, and with more throws the six values gather close to 0.167.

### 8.2 Counting with a List

**Code:** [Lab_DiceList.py](Lab_DiceList.py)

```python
#주사위 1000번 던져서 각 숫자가 나올 확률 (2)
import random

pro_=[0]*6

for i in range(1000):
    num=random.randint(1, 6)
    pro_[num-1] += 1

for i in range(6):
    print("주사위가", i+1, "인 확률은", pro_[i] / 1000)
```

- **A list as counters:** Indices 0-5 of the six-element list `pro_` correspond to faces 1-6. When face `num` comes up, 1 is added to `pro_[num-1]`, so counting takes one line without `if` statements.
- **Output:** The index `i` runs through 0-5, so the face number is printed as `i+1` and the relative frequency is computed as `pro_[i] / 1000`. It does the same as Section 8.1, but a different number of faces only requires changing the size of the list.

**Output:** One example run. Unlike the output of Section 8.1, the number is passed to `print()` separately, so a space follows it.

```text
주사위가 1 인 확률은 0.154
주사위가 2 인 확률은 0.165
주사위가 3 인 확률은 0.177
주사위가 4 인 확률은 0.166
주사위가 5 인 확률은 0.163
주사위가 6 인 확률은 0.175
```

---

<br>

## Summary

| Concept | Key Summary |
|:-----|:-----|
| Changing lists | A list is a mutable type, and its elements are changed, added, and deleted with index assignment, `append()`, `insert()`, `remove()`, `del`, and `pop()`. |
| Searching | `in` tells whether a value is contained and `index()` returns the first matching index, and using `index()` or `remove()` on an absent value raises a `ValueError`. |
| Passing references | A list passed to a function is the same object, so changing its elements inside the function is reflected for the caller. |
| Bubble sort | $n-1$ passes that compare and swap adjacent elements sort the list, and each pass moves the largest value to the back. |
| List comprehension | `[expression for variable in iterable if condition]` creates a new list of the expression's values for the elements that satisfy the condition. |
| `global` and lists | Assigning to a name inside a function makes it local, but merely changing the object, as with `append()`, needs no `global` declaration. |
| 2D lists | A new list must be created for each row, and `[[0]*c]*r` creates aliases that share one row. |
| Assignment and copying | `b = a` creates an alias of the same object, and `list(a)`, `a[:]`, and `a.copy()` create shallow copies. |
| Dictionaries | Values are found by key, assigning to an existing key changes it and to an absent key adds it, and reading an absent key with `[]` raises a `KeyError`. |
| Dictionary methods | `keys()`, `values()`, and `items()` give views, `get()` gives a default when the key is absent, and `update()` changes and adds several pairs. |

---

<br>

## Self-Check Questions

1. **Tracing list operations:** Write `x` after running `x.insert(1, 9)`, `x.remove(3)`, and `x.append(x.pop(0))` in turn on `x = [1, 2, 3]`.

   <details>
   <summary>Answer</summary>

   It becomes `[1, 9, 2, 3]` after `insert(1, 9)` and `[1, 9, 2]` after `remove(3)`. `x.pop(0)` takes out the 1 at index 0, leaving `[9, 2]`, and `append()` attaches that 1 at the end, so the result is `[9, 2, 1]`.

   </details>

2. **Functions and lists:** Write the output of the following code and explain why.

   ```python
   def f(a):
       a.append(4)
       a = [0]
   x = [1, 2, 3]
   f(x)
   print(x)
   ```

   <details>
   <summary>Answer</summary>

   `[1, 2, 3, 4]`. `a.append(4)` changes the same list object as `x`, so the change is reflected for the caller. The following `a = [0]` only makes the local variable `a` refer to a new list and does not change the object that `x` refers to.

   </details>

3. **Passes of bubble sort:** When bubble sort is applied to `[3, 1, 4, 2]`, write the list after the first pass and the number of passes needed to sort it.

   <details>
   <summary>Answer</summary>

   In the first pass, 3 and 1 are swapped to give `[1, 3, 4, 2]`, 3 and 4 stay, and 4 and 2 are swapped to give `[1, 3, 2, 4]`. In the second pass, 3 and 2 are swapped to give `[1, 2, 3, 4]`, so this input is sorted in two passes. With four elements, three passes are enough for any input.

   </details>

4. **Aliases in a 2D list:** What does `s` become after `s = [[0] * 3] * 2` followed by `s[1][2] = 5`?

   <details>
   <summary>Answer</summary>

   `[[0, 0, 5], [0, 0, 5]]`. The outer `* 2` holds two references to the same row list, so changing one row changes both.

   </details>

5. **Dictionaries:** For `d = {"a": 1}`, write the results of `d.get("b", 0)` and `d["b"]`. What does `d` become after `d["b"] = 2`?

   <details>
   <summary>Answer</summary>

   `d.get("b", 0)` returns the default 0 because the key `"b"` is absent, and `d["b"]` raises a `KeyError`. `d["b"] = 2` assigns to an absent key, so a new pair is added and `d` becomes `{"a": 1, "b": 2}`.

   </details>

6. **UnboundLocalError:** How does the output change if only the line `global_var = 20` in `modify_global` of `Lab_GlobalVariableAssignment.py` is deleted?

   <details>
   <summary>Answer</summary>

   With no assignment left inside the function, `global_var` is looked up as the global variable and no error occurs. The output is the four lines `Accessing global variable: 10`, `Before modification: 10`, `After modification: 10`, and `Accessing global variable: 10`.

   </details>
