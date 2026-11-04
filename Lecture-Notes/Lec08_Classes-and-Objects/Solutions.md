# Lecture 8 Solutions — Classes and Objects

[Repository Guide](../../README.md) | [English](Solutions.md) | [한국어](Solutions.ko.md)

> **Last Updated:** 2026-11-04

---

<br>

## Table of Contents

- [Exercise 1: Circle Class](#exercise-1-circle-class)
- [Exercise 2: Bank Account Class](#exercise-2-bank-account-class)
- [Exercise 3: Cat Class](#exercise-3-cat-class)
- [Exercise 4: Box Class](#exercise-4-box-class)
- [Exercise 5: Car Class](#exercise-5-car-class)
- [Exercise 6: Counters with Identification Numbers](#exercise-6-counters-with-identification-numbers)

---

<br>

## Exercise 1: Circle Class

**Problem:** Write a `Circle` class that has the radius as a private instance variable, a setter and a getter for the radius, and methods that compute the area and the circumference, and print the information of a circle of radius 10. The full problem and sample run are in [Exercise 1](Exercises.md#exercise-1-circle-class).

### Solution

**Approach:** The state of a circle is its radius alone, so the only instance variable is `self.__radius` ([Lecture 8, Section 7.1](Concepts_Lecture.md#71-private-instance-variables)). The area and circumference can be computed from the radius, so they are not stored in instance variables but implemented as methods that compute and return them on each call.

- **Area:** The area of a circle of radius $r$ is $\pi r^2$.
- **Circumference:** The circumference of a circle of radius $r$ is $2 \pi r$.
- **Pi:** The constant `math.pi` (about 3.141592653589793) of the `math` module is used.

**Code:**

```python
import math

class Circle:
    def __init__(self, radius=1.0):
        self.__radius = radius

    def setRadius(self, r):
        self.__radius = r

    def getRadius(self):
        return self.__radius

    def calcArea(self):
        area = math.pi * self.__radius * self.__radius
        return area

    def calcCircum(self):
        circumference = 2.0 * math.pi * self.__radius
        return circumference

c1 = Circle(10)
print("원의 반지름=", c1.getRadius())
print("원의 넓이=", c1.calcArea())
print("원의 둘레=", c1.calcCircum())
```

**Output:**

```text
원의 반지름= 10
원의 넓이= 314.1592653589793
원의 둘레= 62.83185307179586
```

- **Constructor:** `Circle(10)` passes 10 to `radius` and initializes `self.__radius` to 10. `radius=1.0` is a default value, so `Circle()` creates a circle of radius 1.0.
- **Area:** $\pi \times 10 \times 10 = 100\pi \approx 314.1592653589793$. (The three printed labels mean radius, area, and circumference.)
- **Circumference:** $2 \times \pi \times 10 = 20\pi \approx 62.83185307179586$.
- **Private variable:** Outside the class the radius cannot be read as `c1.__radius`, so the getter `getRadius()` is used.

An example that uses the default value and the setter follows. To print fewer digits, use the `%.2f` format.

```python
c2 = Circle()
print(c2.getRadius(), c2.calcArea())
c2.setRadius(2.5)
print(c2.getRadius(), c2.calcArea(), c2.calcCircum())
print('%.2f' % c2.calcArea())
```

```text
1.0 3.141592653589793
2.5 19.634954084936208 15.707963267948966
19.63
```

When the setter changes the radius to 2.5, the area and circumference are computed from the new radius. Had the area and circumference been stored in instance variables in advance, they would have to be updated every time the radius changed; computing them in methods leaves the radius as the only state, so nothing can get out of step.

---

<br>

## Exercise 2: Bank Account Class

**Problem:** Write a `BankAccount` class that has only the balance as a private instance variable, with a constructor and the methods `deposit()` and `withdraw()`, and deposit 100 won and withdraw 10 won. The full problem and sample run are in [Exercise 2](Exercises.md#exercise-2-bank-account-class).

### Solution

**Approach:** The balance of a new account is 0, so the constructor takes no parameters and only does `self.__balance = 0`. A deposit adds the amount to the balance, and a withdrawal subtracts it. Keeping the balance private ensures that, outside the account, the balance can be changed only through the two methods ([Lecture 8, Section 7.3](Concepts_Lecture.md#73-getters-and-setters)).

**Code:**

```python
class BankAccount:
    def __init__(self):
        self.__balance = 0             # every new account starts with 0

    def withdraw(self, amount):
        self.__balance -= amount
        print("통장에서 %d원이 출금되었음" % amount)
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount
        print("통장에 %d원이 입금되었음" % amount)
        return self.__balance

a = BankAccount()
a.deposit(100)
a.withdraw(10)
```

**Output:**

```text
통장에 100원이 입금되었음
통장에서 10원이 출금되었음
```

- **`a.deposit(100)`:** The balance goes from 0 to 100, a message with the amount 100 in place of `%d` is printed ("100 won has been deposited into the account"), and 100 is returned.
- **`a.withdraw(10)`:** The balance goes from 100 to 90, and 90 is returned. (The message means "10 won has been withdrawn from the account.")
- **Return values:** Both methods return the new balance, but the code above does not use the return values, so they do not appear on the screen. Writing `print("잔액:", a.deposit(100))` prints the balance as well.

> **Caution:** This `withdraw()` withdraws even an amount larger than the balance, making the balance negative. To behave like a real account, it must check the balance before withdrawing. Because the balance is private, putting this check in the single place `withdraw()` applies it to every withdrawal.

```python
class BankAccount:
    def __init__(self):
        self.__balance = 0

    def withdraw(self, amount):
        if amount > self.__balance:    # refuse to go below zero
            print("잔액이 부족합니다.")
            return self.__balance
        self.__balance -= amount
        print("통장에서 %d원이 출금되었음" % amount)
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount
        print("통장에 %d원이 입금되었음" % amount)
        return self.__balance

a = BankAccount()
print("잔액:", a.deposit(100))
print("잔액:", a.withdraw(10))
print("잔액:", a.withdraw(500))
```

```text
통장에 100원이 입금되었음
잔액: 100
통장에서 10원이 출금되었음
잔액: 90
잔액이 부족합니다.
잔액: 90
```

Since 500 exceeds the balance of 90, `a.withdraw(500)` leaves the balance unchanged, prints only a message ("Insufficient balance."), and returns 90. In `print("잔액:", a.deposit(100))`, the argument `a.deposit(100)` runs first and prints the deposit message, and then its return value 100 is printed together with `"잔액:"` ("Balance:").

---

<br>

## Exercise 3: Cat Class

**Problem:** Write a `Cat` class that has a name and an age as private attributes with a setter and a getter for each, and print the names and ages of Missy (3 years old) and Lucky (5 years old). The full problem and sample run are in [Exercise 3](Exercises.md#exercise-3-cat-class).

### Solution

**Approach:** Each cat has a different name and age, so the constructor receives the two values and stores them in private instance variables. The two cats are different objects created from the same class ([Lecture 8, Section 3.3](Concepts_Lecture.md#33-creating-many-objects-from-one-class)).

**Code:**

```python
class Cat:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setAge(self, age):
        self.__age = age

    def getAge(self):
        return self.__age

missy = Cat('Missy', 3)
lucky = Cat('Lucky', 5)

print(missy.getName(), missy.getAge())
print(lucky.getName(), lucky.getAge())
```

**Output:**

```text
Missy 3
Lucky 5
```

- **Creating objects:** `Cat('Missy', 3)` and `Cat('Lucky', 5)` create two objects, each with its own name and age. The two objects share the methods but have separate instance variables.
- **Output:** Two return values of the getters are passed to `print()`, so the name and age are printed separated by a space.

Changing an attribute of one object with a setter does not affect the other object.

```python
missy.setAge(4)
print(missy.getName(), missy.getAge())
print(lucky.getName(), lucky.getAge())
```

```text
Missy 4
Lucky 5
```

---

<br>

## Exercise 4: Box Class

**Problem:** Write and use a `Box` class that has the width, length, and height as private instance variables, with setters for the three values, `getVolume()`, which returns the volume, and `__str__()`, which returns `(width, length, height)`. The full problem and sample run are in [Exercise 4](Exercises.md#exercise-4-box-class).

### Solution

**Approach:** The volume of a rectangular box is width × length × height. To make `print()` show the desired form for an object, the special method `__str__()` returns that string ([Lecture 8, Section 6.3](Concepts_Lecture.md#63-the-string-representation-method)).

**Code:**

```python
class Box:
    def __init__(self, width=0, length=0, height=0):
        self.__width = width
        self.__length = length
        self.__height = height

    def setWidth(self, width):
        self.__width = width

    def setLength(self, length):
        self.__length = length

    def setHeight(self, height):
        self.__height = height

    def getVolume(self):
        return self.__width * self.__length * self.__height

    def __str__(self):
        return '(%d, %d, %d)' % (self.__width, self.__length, self.__height)

box = Box(100, 100, 100)
print(box)
print('상자의 부피는', box.getVolume())
```

**Output:**

```text
(100, 100, 100)
상자의 부피는 1000000
```

- **`print(box)`:** `print()` calls `box.__str__()`, and the string `'(100, 100, 100)'` that the method builds with `%` formatting is printed.
- **Volume:** $100 \times 100 \times 100 = 1000000$. (The label means "The volume of the box is".)
- **Default values:** All parameters of the constructor have the default value 0, so a box can also be created with `Box()` and sized later with the setters.

```python
b = Box()
print(b, b.getVolume())
b.setWidth(2)
b.setLength(3)
b.setHeight(4)
print(b, b.getVolume())
```

```text
(0, 0, 0) 0
(2, 3, 4) 24
```

> **Note:** `%d` is a format for integers, so if a real number is given, as in `Box(2.5, 1, 1)`, `__str__()` returns `(2, 1, 1)` with the fractional part dropped. To handle real-valued sizes, use the `%g` format, which prints real numbers compactly, as in `'(%g, %g, %g)'`.

---

<br>

## Exercise 5: Car Class

**Problem:** Write a `Car` class that has the speed, gear, and color as private instance variables (defaults 0, 1, `"white"`), with setters for the three attributes and `__str__()`, and print a car whose gear has been changed to 3 and speed to 100. The full problem and sample run are in [Exercise 5](Exercises.md#exercise-5-car-class).

### Solution

**Approach:** Create the car with a constructor that has default values, change its state with the setters, and turn the state into a string with `__str__()`. The color is a string, so it is inserted with the `%s` format.

**Code:**

```python
class Car:
    def __init__(self, speed=0, gear=1, color="white"):
        self.__speed = speed
        self.__gear = gear
        self.__color = color

    def setSpeed(self, speed):
        self.__speed = speed

    def setGear(self, gear):
        self.__gear = gear

    def setColor(self, color):
        self.__color = color

    def __str__(self):
        return '(%d, %d, %s)' % (self.__speed, self.__gear, self.__color)

myCar = Car()
myCar.setGear(3)
myCar.setSpeed(100)
print(myCar)
```

**Output:**

```text
(100, 3, white)
```

- **`Car()`:** With no arguments, a car with speed 0, gear 1, and color `"white"` is created.
- **Setters:** `setGear(3)` and `setSpeed(100)` change the gear and speed, and the color remains the default.
- **`__str__()`:** The speed, gear, and color go in turn into the three places of `'(%d, %d, %s)'`, giving `'(100, 3, white)'`.

Only some of the constructor's default values can be changed as well. The keyword argument `color="red"` changes only the color and uses the defaults for the rest ([Lecture 6, Section 6.2](../Lec06_Functions/Concepts_Lecture.md#62-keyword-arguments)).

```python
print(Car(), Car(color="red"), Car(30, 2, "black"))
```

```text
(0, 1, white) (0, 1, red) (30, 2, black)
```

---

<br>

## Exercise 6: Counters with Identification Numbers

**Problem:** With a class that has `count` and `id` as instance variables, create an object for each value of `id_set = [3, 6, 10, 5, 2]`, increase each object's `count` `id` times, and print the values of the objects whose `id` is even. Solve the same problem again with lists only. The full problem and sample run are in [Exercise 6](Exercises.md#exercise-6-counters-with-identification-numbers).

### Solution

**Approach:** Make a class that adds an identification number `id` to the `Counter` class of [Lecture 8, Section 4](Concepts_Lecture.md#4-the-counter-class). The constructor receives and stores `id` and initializes `count` to 0, and `increment()` increases `count` by 1.

- **Creating objects:** Traverse `id_set`, create one object per value, and put the objects in the list `objects`.
- **Increasing:** For each object, the loop over `range(obj.id)` calls `increment()` `obj.id` times, so when the loop ends `count` equals `id`.
- **Selective output:** If `obj.id % 2 == 0`, the `id` is even.

**Code (Using a Class):**

```python
class IdCounter:
    def __init__(self, id_value):
        self.id = id_value            # identifier taken from id_set
        self.count = 0                # every object starts counting from 0

    def increment(self):
        self.count += 1

id_set = [3, 6, 10, 5, 2]
objects = []

for v in id_set:
    obj = IdCounter(v)
    for _ in range(obj.id):           # increase count id times
        obj.increment()
    objects.append(obj)

for obj in objects:
    if obj.id % 2 == 0:               # only objects with an even id
        print("id = %d, count = %d" % (obj.id, obj.count))
```

**Output:**

```text
id = 6, count = 6
id = 10, count = 10
id = 2, count = 2
```

- **List of objects:** `objects` is a list whose elements are five `IdCounter` objects, and the second loop traverses this list and reads the instance variables of each object.
- **Parameter name:** The constructor's parameter is named `id_value` rather than `id`. `id` is the name of the built-in function `id()`, so using it as a parameter would hide the built-in function inside the function. The instance variable `self.id` is an attribute of the object, so it does not clash with the built-in function.

**Code (Using Lists Only):**

```python
id_set = [3, 6, 10, 5, 2]
counts = [0] * len(id_set)            # counts[k] belongs to id_set[k]

for k in range(len(id_set)):
    for _ in range(id_set[k]):        # increase count id times
        counts[k] += 1

for k in range(len(id_set)):
    if id_set[k] % 2 == 0:
        print("id = %d, count = %d" % (id_set[k], counts[k]))
```

**Output:**

```text
id = 6, count = 6
id = 10, count = 10
id = 2, count = 2
```

The list solution uses parallel lists that pair `id_set` and `counts` by the same index `k` ([Lecture 8, Section 1.1](Concepts_Lecture.md#11-the-problem)). With only two kinds of data, as in this problem, the list solution is also short, but sorting or removing objects or adding attributes would require changing both lists together every time. In the class solution, `id` and `count` are inside one object, so no such synchronization is needed, and the operation that increases `count` is also defined inside the class together with the data, as the method `increment()`.
