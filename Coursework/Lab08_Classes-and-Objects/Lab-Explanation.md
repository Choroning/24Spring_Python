# Lab 8 Explanation — Classes and Objects

[Repository Guide](../../README.md) | [English](Lab-Explanation.md) | [한국어](Lab-Explanation.ko.md)

> **Last Updated:** 2026-11-04

> **Learning Objectives:**
> 1. Define a class, create objects, and call their methods
> 2. Explain the roles of `self` and instance variables
> 3. Initialize instance variables when an object is created with the constructor `__init__()`
> 4. Handle instance variables with getters and setters, and explain how names beginning with `__` are used for information hiding
> 5. Write a program in which a method of one object changes the instance variables of another object

---

## Table of Contents

- [1. Lab Layout and How to Run](#1-lab-layout-and-how-to-run)
- [2. Classes and Objects](#2-classes-and-objects)
  - [2.1 A Counter Class without a Constructor](#21-a-counter-class-without-a-constructor)
  - [2.2 The Constructor `__init__()`](#22-the-constructor-__init__)
- [3. Getters, Setters, and Information Hiding](#3-getters-setters-and-information-hiding)
  - [3.1 get() and set()](#31-get-and-set)
  - [3.2 Instance Variables Beginning with `__`](#32-instance-variables-beginning-with-__)
- [4. Interaction between Objects](#4-interaction-between-objects)
  - [4.1 Attack and Heal](#41-attack-and-heal)
- [Summary](#summary)
- [Self-Check Questions](#self-check-questions)

---

<br>

## 1. Lab Layout and How to Run

This code was written while following [Lecture 8, Classes and Objects](../../Lecture-Notes/Lec08_Classes-and-Objects/Concepts_Lecture.md). Section 2 covers defining classes and constructors, Section 3 covers getters, setters, and information hiding, and Section 4 covers a program in which several objects change each other's state.

```text
Coursework/Lab08_Classes-and-Objects/
├── Lab-Explanation.ko.md       # This document (Korean)
├── Lab-Explanation.md          # This document (English)
├── Lab_Counter.py              # 2.1 A Counter class without a constructor
├── Lab_CounterConstructor.py   # 2.2 The constructor __init__()
├── Lab_CounterAccessors.py     # 3.1 get() and set()
├── Lab_CounterPrivate.py       # 3.2 Instance variables beginning with __
└── Lab_AttackAndHeal.py        # 4.1 Attack and heal
```

*Figure 1. Directory layout of Lab 8*

All programs use only the standard library and run as they are under Python 3. Each file begins with a documentation string (docstring) that records the file name, a one-line description, the author, and the date written, and the code blocks in this document omit that part.

```bash
cd Coursework/Lab08_Classes-and-Objects
python3 Lab_Counter.py
```

---

<br>

## 2. Classes and Objects

### 2.1 A Counter Class without a Constructor

**Code:** [Lab_Counter.py](Lab_Counter.py)

```python
class Counter:
    def reset(self):
        self.count = 0
    def increment(self):
        self.count += 1
    def get(self):
        return self.count

## main ##
a = Counter()
a.reset()
a.increment()
print("카운터 a의 값은", a.get())
```

- **Classes and objects:** A **class** is a blueprint for objects, and calling a class, as in `Counter()`, creates one **object** according to that blueprint. An object created this way is an **instance** of the class. `Counter` represents a mechanical counter for counting the visitors entering a stadium.
- **Methods and `self`:** A function defined inside a class is called a **method**. The first parameter of a method, `self`, is the object that called the method. Calling `a.reset()` makes Python put `a` into `self` and run it like `Counter.reset(a)`.
- **Instance variables:** Assigning to a variable prefixed with `self.`, as in `self.count = 0`, creates an **instance variable** belonging to that object. Each object has its own, so if another `b = Counter()` is created, `b.count` is separate from `a.count`.
- **Order of execution:** `reset()` creates `count` and sets it to 0, `increment()` adds 1, and `get()` returns the value.

**Output:** "The value of counter a is 1" is printed.

```text
카운터 a의 값은 1
```

> **Caution:** This class has no constructor, so `count` is created only when `reset()` is called. Calling `a.increment()` first without `reset()` tries to read `self.count`, which does not exist yet, so `AttributeError: 'Counter' object has no attribute 'count'` occurs. The constructor in Section 2.2 removes this problem.

### 2.2 The Constructor `__init__()`

**Code:** [Lab_CounterConstructor.py](Lab_CounterConstructor.py)

```python
class Counter:
    def __init__(self): #자동호출
        self.count = 0
    def increment(self):
        self.count += 1
    def reset(self):
        self.count = 0
    def get(self):
        print(self.count)

## main ##        #절차지향ver.
C = Counter()
C.get()               #print(C.count)
C.increment()    #C.count += 1
C.increment()    #C.count += 1
C.get()               #print(C.count)
C.reset()            #C.count = 0
C.get()
print(C.count)
#객체지향처럼 짜는 것이 더 나음
```

- **Constructor:** A method named `__init__` is called automatically when an object is created (the comment reads "called automatically"). The moment `C = Counter()` runs, `count` is initialized to 0, so `count` always exists from right after the object is created.
- **This `get()`:** Unlike Section 2.1, it prints the value instead of returning it. So calling just `C.get()` shows the value on the screen.
- **Method calls and direct access:** The comments on the right pair each method call with the statement that handles the instance variable directly, such as `C.count += 1` (the comment after `## main ##` labels this the "procedural version"). The last `print(C.count)` reads the instance variable directly without a method. The final comment means that the object-oriented way, handling variables through methods rather than directly from outside the object, is better.

**Output:** `get()` prints 0 right after creation, 2 after two increments, and 0 after `reset()`, and the last line prints the 0 read directly.

```text
0
2
0
0
```

---

<br>

## 3. Getters, Setters, and Information Hiding

### 3.1 get() and set()

**Code:** [Lab_CounterAccessors.py](Lab_CounterAccessors.py)

```python
class Counter:
    def __init__(self):
        self.count = 0
    def reset(self):
        self.count = 0
    def increment(self):
        self.count += 1
    def get(self):
        return self.count
    def set(self, a):
        self.count = a

## main ##
C = Counter() # 객체 생성

print(C.count)
C_count = C.get() # C_count는 main에서 선언된 별개의 변수이다
print(C_count)
C.count = 100
print(C.count)
C.set(10)
C_count = C.get()
print(C_count)
```

- **Getters and setters:** A method that returns the value of an instance variable, `get()`, is called a **getter**, and a method that changes it, `set()`, a **setter**. Making code outside the object go through methods instead of touching the variable directly gathers checks on the value in one place, for example rejecting negative numbers inside the setter.
- **A variable holding the return value:** `C_count = C.get()` copies the current value 0 into the main part's variable `C_count` (the comment reads "C_count is a separate variable declared in main"). `C_count` is separate from the object, so when the object's `count` changes later, `C_count` changes only if `get()` is called again.
- **Direct assignment:** An instance variable can also be assigned directly from outside the object, as in `C.count = 100`. This class does not hide `count`, so nothing prevents it, which Section 3.2 addresses.
- **Using the setter:** `C.set(10)` changes `count` to 10, and `get()` returns that value.

**Output:**

```text
0
0
100
10
```

### 3.2 Instance Variables Beginning with `__`

**Code:** [Lab_CounterPrivate.py](Lab_CounterPrivate.py)

```python
class Counter:
    def __init__(self):
        self.__count = 0
    def reset(self):
        self.__count = 0
    def increment(self):
        self.__count += 1
    def get(self):
        return self.__count
    def set(self, a):
        self.__count = a

## main ##
C = Counter() # 객체 생성

try:
    print(C.__count)
except AttributeError as e:
    print("AttributeError:", e)
C_count = C.get() # C_count는 main에서 선언된 별개의 변수이다
print(C_count)
C.__count = 100
print(C.__count) #main에서 class로 접근 vs. class에서 접근해서 main으로 값 전송
C.set(10)
C_count = C.get()
print(C_count)
```

- **Information hiding:** The principle of hiding an object's internal state so that it cannot be handled directly from outside and is handled only through methods. In Python, starting the name of an instance variable with `__` (two underscores) makes it inaccessible by that name from outside the class.
- **Name mangling:** Python stores `self.__count` written inside the class under the changed name `self._Counter__count`. So `C.__count` outside the class finds no such attribute and raises an `AttributeError`, whose message `try-except` prints. The method `get()` inside the class goes through the same renaming, so it reads the value 0 normally.
- **A `__count` assigned from outside:** `C.__count = 100` outside the class does not go through name mangling, so instead of changing the hidden variable it creates one more instance variable named `__count`. So the next `print(C.__count)` prints 100, but at this point `C.get()` is still 0. Printing `C.__dict__` shows the two variables separately, as `{'_Counter__count': 0, '__count': 100}`.
- **Access through methods:** `C.set(10)` and `C.get()` handle the hidden `_Counter__count`, so 10 is printed. The comment is a note comparing direct access from the main part with a class method passing the value to the main part.

**Output:**

```text
AttributeError: 'Counter' object has no attribute '__count'
0
100
10
```

> **Note:** Name mangling only guards against accidental access and is not complete protection; using the changed name, as in `C._Counter__count`, allows access from outside. Python also has the convention of treating a name that begins with a single underscore (`_count`) as internal and not using it outside the class.

---

<br>

## 4. Interaction between Objects

### 4.1 Attack and Heal

**Code:** [Lab_AttackAndHeal.py](Lab_AttackAndHeal.py)

```python
class person():
    def __init__(self):
        self.hp=100
        self.r=50
    def a(self, person): #공격
        person.hp-=10
    def heal(self, person): #힐 (인스턴스 변수 r과 이름이 겹치지 않게 함)
        self.hp+=person.r

## main ##
A=person()
B=person()
C=person()
A.a(B)
C.heal(B)
print("A:", A.hp, "B:", B.hp, "C:", C.hp)
```

- **State:** The constructor sets each object's hit points `hp` to 100 and its heal amount `r` to 50. The three objects `A`, `B`, and `C` come from the same class but have their own instance variables. The comments mark the methods as "attack" and "heal (named so as not to clash with the instance variable r)".
- **Attack:** In `A.a(B)`, `self` is `A` and the parameter `person` is `B`, so `B.hp` drops by 10 to 90. This shows that a method can change the instance variables of an object other than itself.
- **Heal:** `C.heal(B)` runs `self.hp += person.r`, so it adds `B`'s heal amount 50 to the hit points of the caller `C`, making `C.hp` 150. Healing `B` instead would require `person.hp += self.r`, so inside a method it is necessary to distinguish whether `self` or the parameter is being changed.
- **Names:** The class name `person` and the parameter name `person` are the same, so inside the methods `person` refers to the parameter (the object passed in). Class names conventionally begin with a capital letter, as in `Person`, which keeps the two apart.

**Output:**

```text
A: 100 B: 90 C: 150
```

> **Caution:** A method and an instance variable must not share a name. If the heal method were named `r`, the constructor's `self.r=50` would create an integer `r` on the object, and since an instance variable is found before a method of the class when a name is looked up on an object, `C.r(B)` would try to call the integer 50 and raise `TypeError: 'int' object is not callable`.

---

<br>

## Summary

| Concept | Key Summary |
|:-----|:-----|
| Classes and objects | A class is a blueprint for objects, and calling the class creates an object with its own instance variables. |
| `self` | The first parameter of a method, referring to the object that called the method. |
| Instance variables | Assigning to `self.name` creates a variable belonging to that object, and reading it before the assignment raises an `AttributeError`. |
| Constructor | `__init__()` is called automatically when an object is created and initializes its instance variables. |
| Getters and setters | Instance variables are handled with methods that return values, such as `get()`, and methods that change them, such as `set()`. |
| Information hiding | An instance variable beginning with `__` is renamed to `_ClassName__name` and cannot be accessed by its original name outside the class. |
| Name clashes | When a name is looked up on an object, instance variables are found before methods, so the two must have different names. |

---

<br>

## Self-Check Questions

1. **Instance variables per object:** Using the class of `Lab_Counter.py`, create `a = Counter()` and `b = Counter()`, call `reset()` on both, then call `a.increment()` twice and `b.increment()` once. What are `a.get()` and `b.get()`?

   <details>
   <summary>Answer</summary>

   `a.get()` is 2 and `b.get()` is 1. `count` is an instance variable that each object has separately, so method calls on one object do not affect the value of another.

   </details>

2. **The role of the constructor:** What happens if the line `a.reset()` is deleted from `Lab_Counter.py`? What happens if the same is done with the class of `Lab_CounterConstructor.py`?

   <details>
   <summary>Answer</summary>

   The class of `Lab_Counter.py` has no constructor, so `increment()` reads `self.count` before `count` has been created and an `AttributeError` occurs. The class of `Lab_CounterConstructor.py` initializes `count` to 0 in the constructor when the object is created, so `increment()` works normally without `reset()`.

   </details>

3. **Return value versus printing:** The `get()` of `Lab_CounterConstructor.py` prints the value and does not return it. With this class, what is stored in `x` when `x = C.get()` runs?

   <details>
   <summary>Answer</summary>

   `get()` has no `return` statement, so `None` is stored. To use the value in other computations, it must be returned with `return self.count` as in `Lab_CounterAccessors.py`.

   </details>

4. **Name mangling:** For the object `C` of `Lab_CounterPrivate.py`, what does `C.get()` return after `C._Counter__count = 5` runs?

   <details>
   <summary>Answer</summary>

   It returns 5. `self.__count` inside the class is stored as `self._Counter__count`, so assigning through the changed name changes the hidden variable. Name mangling only guards against accidental access and is not complete protection.

   </details>

5. **self and parameters:** Rewrite the body of the `heal` method of `Lab_AttackAndHeal.py` so that `C.heal(B)` increases `B`'s hit points by `C`'s heal amount, and write the output in that case.

   <details>
   <summary>Answer</summary>

   Write the body as `person.hp += self.r`. Then `B.hp` becomes 90 after the attack and 140 after adding 50, while `C.hp` stays 100, so `A: 100 B: 140 C: 100` is printed.

   </details>
