# Lecture 9 Solutions — Inheritance and Polymorphism

[Repository Guide](../../README.md) | [English](Solutions.md) | [한국어](Solutions.ko.md)

> **Last Updated:** 2026-11-19

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

**Problem:** Define `Employee`, which has a name and a salary, and a subclass `Manager`, which also has a bonus and whose pay is the salary plus the bonus, and print the pay of two people and the total. The full problem and sample run are in [Exercise 1](Exercises.md#exercise-1-employees-and-managers).

### Solution

**Approach:** A manager is a kind of employee (is-a), so inheritance fits ([Lecture 9, Section 1.2](Concepts_Lecture.md#12-superclasses-and-subclasses)). In its constructor, `Manager` hands the storing of the name and salary to `Employee` with `super().__init__()` and adds only the bonus. The pay overrides `pay()` but obtains the salary through `super().pay()` and adds the bonus, so `Manager` needs no change even if the way the salary is computed changes ([Lecture 9, Section 2.2](Concepts_Lecture.md#22-calling-superclass-methods-with-super)).

**Code:**

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def pay(self):
        return self.salary

    def __str__(self):
        return self.name + ": " + str(self.pay()) + "원"

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)      # reuse Employee's initialization
        self.bonus = bonus

    def pay(self):
        return super().pay() + self.bonus   # extend, not replace

staff = [Employee("Kim", 3000000), Manager("Lee", 4000000, 1000000)]
total = 0
for e in staff:
    print(e)
    total += e.pay()
print("총 급여: " + str(total) + "원")
```

**Output:**

```text
Kim: 3000000원
Lee: 5000000원
총 급여: 8000000원
```

- **Sharing `__str__()`:** `__str__()` exists only in `Employee`, but the `self.pay()` inside it calls the `pay()` of the object's actual class by dynamic dispatch. That is why Lee's line shows 5000000 won, including the bonus.
- **The loop:** `print(e)` and `e.pay()` do not distinguish employees from managers. Adding a new kind, such as a contract worker, leaves this loop unchanged.
- **The total:** $3000000 + (4000000 + 1000000) = 8000000$.

---

<br>

## Exercise 2: Tracing Dynamic Dispatch

**Problem:** For the three classes `A`, `B`, and `C`, write the output of `A().f()`, `B().f()`, and `C().f()`, and explain which class each method of the third call belongs to. The full problem is in [Exercise 2](Exercises.md#exercise-2-tracing-dynamic-dispatch).

### Solution

**Output:**

```text
A.f > A.g
A.f > B.g
C.f > A.f > B.g
```

**Trace:** In all three calls, `self.g()` looks up `g` starting from the actual class of `self` ([Lecture 9, Section 2.4](Concepts_Lecture.md#24-tracing-dynamic-dispatch)).

| Call | Where `f` Is Found | Where `self.g()` Is Found | Result |
|:-----|:-----|:-----|:-----|
| `A().f()` | `A` | `A` | `A.f > A.g` |
| `B().f()` | Not in `B`, so `A` | `B` | `A.f > B.g` |
| `C().f()` | `C` | Not in `C`, so `B` | `C.f > A.f > B.g` |

*Table 1. The classes in which the methods of the three calls are found*

- **`f` in `C().f()`:** `C` overrides `f`, so `C.f()` runs and produces `"C.f > "`.
- **`super().f()`:** The MRO of `C` is `C, B, A, object`, so `f` is looked up starting from `B`, the class after `C`. `B` has no `f`, so `A.f()` runs, and `self` is still the object of `C`.
- **`self.g()` inside `A.f()`:** `self` is an object of `C`, so the lookup starts at `C`; `C` has no `g`, so `B.g()` runs. The fact that the code of `A.f()` calls `B.g()` rather than `A.g()` of the same class is the result of dynamic dispatch.

---

<br>

## Exercise 3: Abstract Shape Classes

**Problem:** Define `Shape` with `area()` and `perimeter()` as abstract methods, and the subclasses `Rectangle`, `Square` (inheriting from `Rectangle`), and `Circle`, and print them in order of area. The full problem and sample run are in [Exercise 3](Exercises.md#exercise-3-abstract-shape-classes).

### Solution

**Approach:** Inherit from `ABC` and put `@abstractmethod` on the two methods ([Lecture 9, Section 5.2](Concepts_Lecture.md#52-the-abc-module)). The output format is common to all shapes, so it is placed once in the `__str__()` of `Shape`, and the class name is obtained with `type(self).__name__`. A square is a rectangle with equal width and height, so calling `super().__init__(side, side)` in its constructor is enough to inherit both the area and the perimeter.

- **Rectangle:** The area is $wh$ and the perimeter is $2(w + h)$.
- **Circle:** The area is $\pi r^2$ and the perimeter is $2 \pi r$.

**Code:**

```python
import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def __str__(self):
        return "%s: 넓이 %.2f, 둘레 %.2f" % (type(self).__name__, self.area(), self.perimeter())

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)        # a square is a rectangle with w == h

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r ** 2

    def perimeter(self):
        return 2 * math.pi * self.r

shapes = [Rectangle(2, 5), Square(3), Circle(1.5)]
shapes.sort(key=lambda s: s.area())
for s in shapes:
    print(s)
print(isinstance(Square(3), Rectangle), issubclass(Square, Shape))
```

**Output:**

```text
Circle: 넓이 7.07, 둘레 9.42
Square: 넓이 9.00, 둘레 12.00
Rectangle: 넓이 10.00, 둘레 14.00
True True
```

- **Areas:** The circle has $\pi \times 1.5^2 = 2.25\pi \approx 7.07$, the square $3 \times 3 = 9$, and the rectangle $2 \times 5 = 10$, so the sorted order is circle, square, rectangle.
- **Perimeters:** The circle has $2 \pi \times 1.5 = 3\pi \approx 9.42$, the square $2(3 + 3) = 12$, and the rectangle $2(2 + 5) = 14$.
- **Sorting:** A lambda function that returns the area is given as the `key` of `sort()` ([Lecture 7, Section 4.3](../Lec07_Lists-and-Dictionaries/Concepts_Lecture.md#43-sorting)). Even without `__lt__()` in `Shape`, sorting works because the `key` returns numbers.
- **The class name of `Square`:** `Square` inherits `__str__()` from `Shape` and the area and perimeter from `Rectangle`, but `type(self).__name__` returns the actual class name `"Square"`.
- **Relationship checks:** A square is a rectangle and a rectangle is a shape, so both checks are true.

> **Note:** Making the square a subclass of the rectangle is natural only when objects do not change after creation. If the rectangle had a `set_width()` that changes only the width, a square inheriting that method could end up with different width and height and stop being a square. When a superclass operation can break a condition of the subclass in this way, the inheritance relationship should be reconsidered according to the criteria of [Lecture 9, Section 6.3](Concepts_Lecture.md#63-criteria-for-choosing-inheritance-or-composition).

---

<br>

## Exercise 4: Cooperative super() and the MRO

**Problem:** When `Logger` and `Saver` both inherit from `Base` and `App(Logger, Saver)` inherits from both, find the MRO of `App` and the output of `App().setup()`, and compare them with `App2(Saver, Logger)`, in which the order of the superclasses is swapped. The full problem is in [Exercise 4](Exercises.md#exercise-4-cooperative-super-and-the-mro).

### Solution

**Computing the MRO:** `L[Base] = [Base, object]`, `L[Logger] = [Logger, Base, object]`, and `L[Saver] = [Saver, Base, object]` ([Lecture 9, Section 4.2](Concepts_Lecture.md#42-diamond-inheritance-and-the-mro)).

| Step | Lists Remaining in merge | Class Chosen |
|:-----|:-----|:-----|
| 1 | `[Logger, Base, object]`, `[Saver, Base, object]`, `[Logger, Saver]` | `Logger` |
| 2 | `[Base, object]`, `[Saver, Base, object]`, `[Saver]` | `Base` is in a tail, so it is skipped; `Saver` |
| 3 | `[Base, object]`, `[Base, object]` | `Base` |
| 4 | `[object]`, `[object]` | `object` |

*Table 2. The merge process that computes the MRO of App*

The MRO of `App` is therefore `App, Logger, Saver, Base, object`.

**Checking code:**

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

class App2(Saver, Logger):
    def setup(self):
        print("App2.setup")
        super().setup()

App2().setup()
print([c.__name__ for c in App2.__mro__])
```

**Output:**

```text
App.setup
Logger.setup
Saver.setup
Base.setup
['App', 'Logger', 'Saver', 'Base', 'object']
App2.setup
Saver.setup
Logger.setup
Base.setup
['App2', 'Saver', 'Logger', 'Base', 'object']
```

- **`super()` inside `Logger`:** For an object of `App`, it refers to `Saver`, the class after `Logger` in the MRO. The superclass of `Logger` is `Base`, but the call does not skip `Saver` to go to `Base` ([Lecture 9, Section 4.3](Concepts_Lecture.md#43-cooperative-super-calls)).
- **`Base.setup` once:** All four classes call the next class with `super()`, so `Base`, the top of the diamond, runs exactly once.
- **When the order is swapped:** In `App2(Saver, Logger)`, local precedence places `Saver` before `Logger`, so the same classes run in the order `Saver`, `Logger`, `Base`. The order in which the superclasses are written changes the order of execution.

---

<br>

## Exercise 5: Output Destinations Built with Duck Typing

**Problem:** Write a function `save_report(lines, out)` that calls only `out.write()`, and two classes with `write()`, `ListWriter` and `CountingWriter`, and save the same report to three output destinations. The full problem and sample run are in [Exercise 5](Exercises.md#exercise-5-output-destinations-built-with-duck-typing).

### Solution

**Approach:** All that `save_report()` requires of an output destination is one `write()` method that accepts a string. By duck typing, any object with this method can be an output destination, so no common superclass is introduced ([Lecture 9, Section 3.2](Concepts_Lecture.md#32-duck-typing)). The screen output object `sys.stdout` is also an object with `write()`, so it can be passed as is.

**Code:**

```python
import sys

def save_report(lines, out):
    for line in lines:
        out.write(line + "\n")      # only requires a write() method

class ListWriter:
    def __init__(self):
        self.lines = []

    def write(self, text):
        self.lines.append(text)

class CountingWriter:
    def __init__(self):
        self.chars = 0

    def write(self, text):
        self.chars += len(text)

report = ["1분기 매출 120", "2분기 매출 150"]
w1 = ListWriter()
w2 = CountingWriter()
save_report(report, w1)
save_report(report, w2)
save_report(report, sys.stdout)
print(w1.lines)
print(w2.chars)
```

**Output:**

```text
1분기 매출 120
2분기 매출 150
['1분기 매출 120\n', '2분기 매출 150\n']
22
```

- **`sys.stdout`:** The first two lines were written to the screen by `save_report(report, sys.stdout)`. `print()` also calls `sys.stdout.write()` internally.
- **Character count:** `"1분기 매출 120\n"` has 11 characters, namely 4 Hangul syllables, 4 digits, 2 spaces, and 1 newline, and the second line also has 11, so the total is 22. `len()` counts characters, not bytes.
- **Extension:** The file objects of Lecture 10 also have `write()`, so passing a file opened with `open()` saves the report to a file with the same function.

---

<br>

## Exercise 6: Composing a Playlist

**Problem:** Define `Song` and `Playlist`, which has songs, and make `add()`, `total_seconds()`, `longest()`, `len()`, the truth value, and the string representation work. The full problem and sample run are in [Exercise 6](Exercises.md#exercise-6-composing-a-playlist).

### Solution

**Approach:** A playlist has songs (has-a), so it is built by composition ([Lecture 9, Section 6.1](Concepts_Lecture.md#61-the-is-a-and-has-a-relationships)). The songs are kept in a list held as an instance variable, and the number of songs is reported through `__len__()`. Even without a separate `__bool__()`, the object is false when `__len__()` returns 0 ([Lecture 9, Section 7.3](Concepts_Lecture.md#73-string-representations-and-length)). To split the total time into minutes and seconds, the built-in function `divmod()`, which returns the quotient and remainder together, is used.

**Code:**

```python
class Song:
    def __init__(self, title, seconds):
        self.title = title
        self.seconds = seconds

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []                 # a Playlist has Songs

    def add(self, song):
        self.songs.append(song)

    def total_seconds(self):
        total = 0
        for s in self.songs:
            total += s.seconds
        return total

    def longest(self):
        return max(self.songs, key=lambda s: s.seconds)

    def __len__(self):
        return len(self.songs)

    def __str__(self):
        m, s = divmod(self.total_seconds(), 60)
        return "%s (%d곡, %d분 %d초)" % (self.name, len(self), m, s)

p = Playlist("출근길")
p.add(Song("Song A", 215))
p.add(Song("Song B", 187))
p.add(Song("Song C", 242))
print(p)
print(p.longest().title)
print(len(p), bool(Playlist("빈 목록")))
```

**Output:**

```text
출근길 (3곡, 10분 44초)
Song C
3 False
```

- **Total time:** $215 + 187 + 242 = 644$ seconds, and `divmod(644, 60)` is `(10, 44)`, so the total is 10 minutes 44 seconds.
- **The longest song:** A lambda function returning the song length is given as the `key` of `max()`, so `Song C`, of 242 seconds, is returned. No size comparison between songs (`__lt__()`) needs to be defined.
- **Truth value:** An empty playlist has `__len__()` equal to 0, so `bool()` is `False`.

---

<br>

## Exercise 7: A Money Class That Works with sum()

**Problem:** Define a `Money` class for which addition, `sum()`, equality comparison, ordering comparison, and the representation string work. The full problem and sample run are in [Exercise 7](Exercises.md#exercise-7-a-money-class-that-works-with-sum).

### Solution

**Approach:** The built-in function `sum(list)` adds the elements in turn to the start value 0. In the first addition, `0 + Money(5000)`, the integer's `__add__()` does not know `Money`, so it returns `NotImplemented`, and Python calls the right operand's `Money.__radd__(Money(5000), 0)` ([Lecture 9, Section 7.4](Concepts_Lecture.md#74-notimplemented-and-reflected-operations)). Therefore `sum()` works if `__radd__()` returns the object itself when it receives 0. For unsupported operands, the methods return `NotImplemented` so that Python raises the appropriate `TypeError`.

**Code:**

```python
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        if isinstance(other, Money):
            return Money(self.amount + other.amount)
        return NotImplemented

    def __radd__(self, other):
        if other == 0:                  # sum() starts from 0
            return self
        return NotImplemented

    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return self.amount == other.amount

    def __lt__(self, other):
        return self.amount < other.amount

    def __repr__(self):
        return "Money(" + str(self.amount) + ")"

wallet = [Money(5000), Money(1000), Money(10000)]
print(Money(5000) + Money(1000))
print(sum(wallet))
print(sorted(wallet))
print(Money(3000) == Money(3000), Money(3000) == 3000)
print(min(wallet), max(wallet))
```

**Output:**

```text
Money(6000)
Money(16000)
[Money(1000), Money(5000), Money(10000)]
True False
Money(1000) Money(10000)
```

- **The steps of `sum(wallet)`:** `0 + Money(5000)` becomes `Money(5000)` through `__radd__()`, and then `Money(5000) + Money(1000)` and `Money(6000) + Money(10000)` are computed by `__add__()`, giving `Money(16000)`.
- **`Money(3000) == 3000`:** `Money.__eq__()` returns `NotImplemented`, and the integer's `__eq__()` does not know how to compare with `Money` either, so Python decides by whether the two are the same object (`is`) and produces `False` ([Lecture 9, Section 7.2](Concepts_Lecture.md#72-defining-comparison-operators)).
- **Sorting, minimum, and maximum:** `sorted()`, `min()`, and `max()` use only `<`, so `__lt__()` suffices.
- **Hashing:** Because `__eq__()` is defined, `Money` objects cannot be put in a set. If amounts must serve as set elements or dictionary keys, define `__hash__()` as `hash(self.amount)` and do not change the amount.

Computing `Money(1000) + 500` gives `TypeError: unsupported operand type(s) for +: 'Money' and 'int'`, because both `__add__()` and the integer's `__radd__()` return `NotImplemented`. The only integer that `__radd__()` accepts is 0, the start value of `sum()`, so only `0 + Money(1000)` is computed as an exception, and `500 + Money(1000)` gives `TypeError: unsupported operand type(s) for +: 'int' and 'Money'`.

---

<br>

## Exercise 8: A Fraction Class

**Problem:** Define a `Fraction` class that stores fractions in lowest terms and for which `+`, `*`, `==`, and the representation string work, and compare its results with the standard module `fractions`. The full problem and sample run are in [Exercise 8](Exercises.md#exercise-8-a-fraction-class).

### Solution

**Approach:** The sum and product of the fractions $\frac{a}{b}$ and $\frac{c}{d}$ are as follows.

```math
\frac{a}{b} + \frac{c}{d} = \frac{ad + cb}{bd}, \qquad \frac{a}{b} \times \frac{c}{d} = \frac{ac}{bd}
```

Passing the result to the constructor reduces it to lowest terms, so the operation methods compute only the numerator and denominator by the formulas. To reduce to lowest terms, divide the numerator and denominator by their greatest common divisor. The greatest common divisor is obtained with `math.gcd()`, which returns a value of 0 or more regardless of the signs of its arguments. If the denominator is negative, the signs of the numerator and denominator are first flipped together so that the sign sits in the numerator. Since every fraction is reduced by the same rule, `==` only needs to compare numerators with numerators and denominators with denominators.

**Code:**

```python
import math

class Fraction:
    def __init__(self, num, den):
        if den < 0:                     # keep the sign in the numerator
            num, den = -num, -den
        g = math.gcd(num, den)
        self.num = num // g
        self.den = den // g

    def __add__(self, other):
        return Fraction(self.num * other.den + other.num * self.den,
                        self.den * other.den)

    def __mul__(self, other):
        return Fraction(self.num * other.num, self.den * other.den)

    def __eq__(self, other):
        return self.num == other.num and self.den == other.den

    def __repr__(self):
        return str(self.num) + "/" + str(self.den)

print(Fraction(1, 2) + Fraction(1, 3))
print(Fraction(2, 3) * Fraction(3, 4))
print(Fraction(2, 4) == Fraction(1, 2))
print(Fraction(1, -2), Fraction(-3, -6))
print(Fraction(1, 6) + Fraction(1, 3))

import fractions
print(fractions.Fraction(1, 2) + fractions.Fraction(1, 3))
```

**Output:**

```text
5/6
1/2
True
-1/2 1/2
1/2
5/6
```

- **Addition:** $\frac{1}{2} + \frac{1}{3} = \frac{1 \times 3 + 1 \times 2}{2 \times 3} = \frac{5}{6}$, and since the greatest common divisor is 1, it stays as is.
- **Multiplication:** $\frac{2}{3} \times \frac{3}{4} = \frac{6}{12}$, which becomes $\frac{1}{2}$ after dividing by the greatest common divisor 6.
- **Equality:** `Fraction(2, 4)` is divided by the greatest common divisor 2 in the constructor and stored as 1/2, so it equals `Fraction(1, 2)`.
- **Sign:** `Fraction(1, -2)` has a negative denominator, so the signs are flipped and it is stored as $\frac{-1}{2}$, and `Fraction(-3, -6)` is stored as $\frac{1}{2}$ via $\frac{3}{6}$.
- **Reducing the result:** $\frac{1}{6} + \frac{1}{3} = \frac{1 \times 3 + 1 \times 6}{18} = \frac{9}{18}$, which becomes $\frac{1}{2}$ after dividing by the greatest common divisor 9.
- **The standard module:** `fractions.Fraction` gives the same result, `5/6`. Besides the operations of this solution, the fractions of the standard module support subtraction, division, ordering comparison, hashing, and mixed operations with integers, so use the standard module for real computations.
