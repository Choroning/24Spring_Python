# Lecture 8 Exercises — Classes and Objects

[Repository Guide](../../README.md) | [English](Exercises.md) | [한국어](Exercises.ko.md)

> **Last Updated:** 2026-11-04

Exercises 1-5 are lab problems that represent real-world things as classes and create and use objects, and Exercise 6 is a challenge problem that solves the same problem with a class and with lists and compares the two.

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

**Problem:** Represent a circle as a class `Circle`. A circle has its radius as a private instance variable and receives the radius in the constructor (1.0 if omitted). Define the setter `setRadius()` and the getter `getRadius()` for the radius, `calcArea()`, which returns the area of the circle, and `calcCircum()`, which returns its circumference. Create a circle of radius 10 and print its radius, area, and circumference. Use `math.pi` for pi.

**Sample Run:**

```text
원의 반지름= 10
원의 넓이= 314.1592653589793
원의 둘레= 62.83185307179586
```

**[Solution](Solutions.md#exercise-1-circle-class)**

---

<br>

## Exercise 2: Bank Account Class

**Problem:** Money can be deposited into and withdrawn from a bank account. Model a bank account as a class `BankAccount`. The account has only its current balance as a private instance variable, and has only a constructor that initializes the balance to 0, a deposit method `deposit()`, and a withdrawal method `withdraw()`. Both methods receive an amount, change the balance, print what was done, and return the new balance. Create an account, deposit 100 won, and withdraw 10 won.

**Sample Run:**

```text
통장에 100원이 입금되었음
통장에서 10원이 출금되었음
```

**[Solution](Solutions.md#exercise-2-bank-account-class)**

---

<br>

## Exercise 3: Cat Class

**Problem:** Define a cat as a class `Cat`. A cat has a name and an age as private attributes, and receives the two values in the constructor. Define a setter and a getter for each attribute, create Missy, aged 3, and Lucky, aged 5, as objects, and print their names and ages.

**Sample Run:**

```text
Missy 3
Lucky 5
```

**[Solution](Solutions.md#exercise-3-cat-class)**

---

<br>

## Exercise 4: Box Class

**Problem:** Write a `Box` class that represents a box. The `Box` class has private instance variables for the width, length, and height, and receives the three values in the constructor (0 each if omitted). Define setters for the three values, `getVolume()`, which returns the volume, and `__str__()`, which makes `print()` show a string of the form `(width, length, height)`. Create a box whose width, length, and height are all 100, print it, and print its volume.

**Sample Run:**

```text
(100, 100, 100)
상자의 부피는 1000000
```

**[Solution](Solutions.md#exercise-4-box-class)**

---

<br>

## Exercise 5: Car Class

**Problem:** Define a class `Car` that represents a car. A car object can be thought of as having attributes such as color, current speed, and current gear, and actions such as shifting gears, accelerating, and decelerating. Of these, implement only the following attributes and actions.

- **Attributes:** Keep the speed `speed` (default 0), the gear `gear` (default 1), and the color `color` (default `"white"`) as private instance variables.
- **Actions:** Provide the setters `setSpeed()`, `setGear()`, and `setColor()` for the attributes, and `__str__()`, which returns a string of the form `(speed, gear, color)`.

Create a car with the default values, change the gear to 3 and the speed to 100, and print the car.

**Sample Run:**

```text
(100, 3, white)
```

**[Solution](Solutions.md#exercise-5-car-class)**

---

<br>

## Exercise 6: Counters with Identification Numbers

**Problem:** Define a class with two instance variables, `count` and `id`.

- Create five objects, putting the values of the predefined list `id_set = [3, 6, 10, 5, 2]` in turn into the `id` of each object created.
- The `count` of each object starts at 0 and is increased by 1 as many times as the value of that object's `id`.
- Print the `id` and `count` of the objects whose `id` is even.

Then solve the same problem again using only lists, without a class.

**Sample Run:** The two programs produce the same output.

```text
id = 6, count = 6
id = 10, count = 10
id = 2, count = 2
```

**[Solution](Solutions.md#exercise-6-counters-with-identification-numbers)**
