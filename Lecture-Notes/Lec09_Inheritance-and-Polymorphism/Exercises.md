# Lecture 9 Exercises — Inheritance and Polymorphism

[Repository Guide](../../README.md) | [English](Exercises.md) | [한국어](Exercises.ko.md)

> **Last Updated:** 2026-11-19

Exercises 1 and 3 build class hierarchies with inheritance, overriding, and abstract base classes, and Exercises 2 and 4 trace the output of given code. Exercises 5-8 make objects work with other code through duck typing, composition, and the special methods for operators.

---

<br>

## Table of Contents

- [Exercise 1: Employees and Managers](#exercise-1-employees-and-managers)
- [Exercise 2: Tracing Dynamic Dispatch](#exercise-2-tracing-dynamic-dispatch)
- [Exercise 3: Abstract Shape Classes](#exercise-3-abstract-shape-classes)
- [Exercise 4: Cooperative super() and the MRO](#exercise-4-cooperative-super-and-the-mro)
- [Exercise 5: Output Destinations Built with Duck Typing](#exercise-5-output-destinations-built-with-duck-typing)
- [Exercise 6: Composing a Playlist](#exercise-6-composing-a-playlist)
- [Exercise 7: A Money Class That Works with sum()](#exercise-7-a-money-class-that-works-with-sum)
- [Exercise 8: A Fraction Class](#exercise-8-a-fraction-class)

---

<br>

## Exercise 1: Employees and Managers

**Problem:** Define a class `Employee` that represents an employee and a class `Manager`, a kind of employee.

- `Employee` has a name `name` and a monthly salary `salary` as instance variables, and has `pay()`, which returns the actual amount paid, and `__str__()`, which returns a string of the form `"name: amount원"`. An employee's pay equals the salary.
- `Manager` inherits from `Employee` and also has a bonus `bonus`. A manager's pay is the salary plus the bonus.
- The code that stores the name and salary, and `__str__()`, belong only in `Employee`.

Put an employee Kim with a salary of 3000000 won and a manager Lee with a salary of 4000000 won and a bonus of 1000000 won in one list, print each of them, and print the total pay.

**Sample Run:**

```text
Kim: 3000000원
Lee: 5000000원
총 급여: 8000000원
```

**[Solution](Solutions.md#exercise-1-employees-and-managers)**

---

<br>

## Exercise 2: Tracing Dynamic Dispatch

**Problem:** Write the output of the following program without running it. Then explain, for the third `print()`, which class's method each of `f`, `super().f()`, and `self.g()` runs.

```python
class A:
    def f(self):
        return "A.f > " + self.g()

    def g(self):
        return "A.g"

class B(A):
    def g(self):
        return "B.g"

class C(B):
    def f(self):
        return "C.f > " + super().f()

print(A().f())
print(B().f())
print(C().f())
```

**[Solution](Solutions.md#exercise-2-tracing-dynamic-dispatch)**

---

<br>

## Exercise 3: Abstract Shape Classes

**Problem:** Define an abstract base class `Shape` with the `abc` module.

- `Shape` has `area()`, which returns the area, and `perimeter()`, which returns the perimeter, as abstract methods.
- The `__str__()` of `Shape` shows the area and perimeter to two decimal places in the form `"ClassName: 넓이 0.00, 둘레 0.00"`. The class name is the name of the object's actual class.
- Define the subclasses rectangle `Rectangle(w, h)`, square `Square(side)`, and circle `Circle(r)`. A square is a rectangle whose width and height are equal, so it inherits from `Rectangle` and does not define the area and perimeter again.

Put `Rectangle(2, 5)`, `Square(3)`, and `Circle(1.5)` in a list, sort them from the smallest area, print them, and on the last line print the values of `isinstance(Square(3), Rectangle)` and `issubclass(Square, Shape)`.

**Sample Run:**

```text
Circle: 넓이 7.07, 둘레 9.42
Square: 넓이 9.00, 둘레 12.00
Rectangle: 넓이 10.00, 둘레 14.00
True True
```

**[Solution](Solutions.md#exercise-3-abstract-shape-classes)**

---

<br>

## Exercise 4: Cooperative super() and the MRO

**Problem:** In the following program, compute the MRO of `App` by hand with C3 linearization, and write the output of `App().setup()`. Then write how the MRO and the output change when the definition of `App` is changed to `class App2(Saver, Logger):`.

```python
class Base:
    def setup(self):
        print("Base.setup")

class Logger(Base):
    def setup(self):
        print("Logger.setup")
        super().setup()

class Saver(Base):
    def setup(self):
        print("Saver.setup")
        super().setup()

class App(Logger, Saver):
    def setup(self):
        print("App.setup")
        super().setup()

App().setup()
print([c.__name__ for c in App.__mro__])
```

**[Solution](Solutions.md#exercise-4-cooperative-super-and-the-mro)**

---

<br>

## Exercise 5: Output Destinations Built with Duck Typing

**Problem:** Write a function `save_report(lines, out)` that receives a list of strings `lines` and an output destination `out`, and writes each string followed by a newline character with `out.write()`. Then define the following two classes.

- `ListWriter`: `write(text)` appends the received string to the instance variable list `lines`.
- `CountingWriter`: `write(text)` accumulates the number of characters of the received string in the instance variable `chars`.

Save `report = ["1분기 매출 120", "2분기 매출 150"]` to a `ListWriter` object, a `CountingWriter` object, and the screen output object `sys.stdout` in turn, and then print the `lines` of the `ListWriter` object and the `chars` of the `CountingWriter` object. The three output destinations must have no inheritance relationship with one another.

**Sample Run:**

```text
1분기 매출 120
2분기 매출 150
['1분기 매출 120\n', '2분기 매출 150\n']
22
```

**[Solution](Solutions.md#exercise-5-output-destinations-built-with-duck-typing)**

---

<br>

## Exercise 6: Composing a Playlist

**Problem:** Define a song `Song(title, seconds)` and a playlist `Playlist(name)`. A playlist is not a kind of song but an object that has songs.

- `add(song)`: Adds a song to the end of the list.
- `total_seconds()`: Returns the sum of the lengths (in seconds) of all songs.
- `longest()`: Returns the longest song.
- The number of songs can be obtained with `len()`, and a playlist with no songs must be false in a condition.
- Printing it with `print()` gives the form `"name (n곡, m분 s초)"`.

Put the songs `Song A`, `Song B`, and `Song C`, of 215, 187, and 242 seconds, in a playlist named "출근길", and print the playlist, the title of the longest song, the number of songs, and the truth value of an empty playlist.

**Sample Run:**

```text
출근길 (3곡, 10분 44초)
Song C
3 False
```

**[Solution](Solutions.md#exercise-6-composing-a-playlist)**

---

<br>

## Exercise 7: A Money Class That Works with sum()

**Problem:** Define a class `Money(amount)` that represents an amount in won.

- `+` on two `Money` objects returns a new `Money` with the amounts added. Adding a value that is not `Money` must cause a `TypeError` according to Python's rules.
- A list of `Money` objects must be passable directly to the built-in function `sum()`, as in `sum(wallet)`, to obtain the total.
- `==` is true between `Money` objects with equal amounts, and comparing `Money` with an integer is false.
- The order of amounts must be comparable with `sorted()`, `min()`, and `max()`.
- `repr()` has the form `Money(5000)`.

**Sample Run:** For the wallet `[Money(5000), Money(1000), Money(10000)]`, print the following.

```text
Money(6000)
Money(16000)
[Money(1000), Money(5000), Money(10000)]
True False
Money(1000) Money(10000)
```

The first line is `Money(5000) + Money(1000)`, the second the total of the wallet, the third the sorted wallet, the fourth `Money(3000) == Money(3000)` and `Money(3000) == 3000`, and the fifth the minimum and maximum of the wallet.

**[Solution](Solutions.md#exercise-7-a-money-class-that-works-with-sum)**

---

<br>

## Exercise 8: A Fraction Class

**Problem:** Define a class `Fraction(num, den)` that represents a fraction whose numerator and denominator are integers.

- When an object is created, reduce the fraction to lowest terms and keep the negative sign in the numerator. Assume that the denominator is not 0.
- `+` and `*` return the result as a new `Fraction`.
- `==` is true between fractions with the same value. For example, `Fraction(2, 4) == Fraction(1, 2)` is true.
- `repr()` and `print()` use the form `numerator/denominator`.

Finally, compute $\frac{1}{2} + \frac{1}{3}$ with `Fraction` from the standard module `fractions` and compare it with the result of your own class.

**Sample Run:**

```text
5/6
1/2
True
-1/2 1/2
1/2
5/6
```

The lines are, in order, $\frac{1}{2} + \frac{1}{3}$, $\frac{2}{3} \times \frac{3}{4}$, `Fraction(2, 4) == Fraction(1, 2)`, `Fraction(1, -2)` and `Fraction(-3, -6)`, $\frac{1}{6} + \frac{1}{3}$, and $\frac{1}{2} + \frac{1}{3}$ computed with the standard module.

**[Solution](Solutions.md#exercise-8-a-fraction-class)**
