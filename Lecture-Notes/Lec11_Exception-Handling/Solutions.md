# Lecture 11 Solutions — Exception Handling

[Repository Guide](../../README.md) | [English](Solutions.md) | [한국어](Solutions.ko.md)

> **Last Updated:** 2026-11-19

---

<br>

## Table of Contents

- [Exercise 1: Finding the Cause from a Traceback](#exercise-1-finding-the-cause-from-a-traceback)
- [Exercise 2: Integer Input within a Range](#exercise-2-integer-input-within-a-range)
- [Exercise 3: The Order of Execution of the Four Clauses](#exercise-3-the-order-of-execution-of-the-four-clauses)
- [Exercise 4: A Four-Operation Calculator](#exercise-4-a-four-operation-calculator)
- [Exercise 5: The Total of Several Files](#exercise-5-the-total-of-several-files)
- [Exercise 6: A Hierarchy of Validation Exceptions](#exercise-6-a-hierarchy-of-validation-exceptions)
- [Exercise 7: Reporting as a Configuration Error](#exercise-7-reporting-as-a-configuration-error)
- [Exercise 8: A Context Manager That Rolls Back](#exercise-8-a-context-manager-that-rolls-back)

---

<br>

## Exercise 1: Finding the Cause from a Traceback

**Problem:** From the traceback of `grades.py`, find the kind and cause of the exception, and fix `summary()` so that the remaining results are printed even when a score cannot be interpreted. The full problem and sample run are in [Exercise 1](Exercises.md#exercise-1-finding-the-cause-from-a-traceback).

### Solution

**(1) The exception and its cause:** According to the last line, the exception is a `ValueError`; `int()` could not convert the string `'7O'` to an integer. Park's score was entered as `"7O"`, with the letter O instead of the digit 0. The `File` line just above points to line 11 of `summary()`, and the `~~~^^^^^^^` marker points to `int(score)` on that line ([Lecture 11, Section 1.3](Concepts_Lecture.md#13-reading-a-traceback)).

**(2) Why Kim and Lee were not printed:** `summary()` collects everyone's results in a list and returns it, and printing happens on lines 15-16 from the returned list. When the exception occurred at Park, `summary()` left without returning, so the lines already made for Kim and Lee never reached the printing stage either.

**(3) The fixed code:** Wrap only the part that interprets one person's score in `try`, and use a substitute string on `ValueError`. This is "recover with a substitute value" of Table 2 ([Lecture 11, Section 2.6](Concepts_Lecture.md#26-what-a-handler-can-do)).

```python
def letter(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    return "C"

def summary(records):
    lines = []
    for name, score in records.items():
        try:
            grade = letter(int(score))
        except ValueError:
            grade = "점수 오류(" + repr(score) + ")"
        lines.append(name + ": " + grade)
    return lines

data = {"Kim": "95", "Lee": "88", "Park": "7O"}
for line in summary(data):
    print(line)
```

**Output:**

```text
Kim: A
Lee: B
Park: 점수 오류('7O')
```

- **The position of the `try` statement:** It is inside the loop, so one person's failure does not affect the processing of the others. Had the whole loop been wrapped, the results would have been cut off in the same way.
- **The extent of the `try` clause:** Only the single line `letter(int(score))` is included. Including `lines.append()` would wrongly show other `ValueError`s that could arise on that line as score errors too.
- **`repr(score)`:** It shows the value with quotation marks, which makes spaces or look-alike characters mixed into the value easy to spot.

---

<br>

## Exercise 2: Integer Input within a Range

**Problem:** Write `read_int(prompt, low, high)`, which asks again if the input is not an integer or out of range. The full problem and sample run are in [Exercise 2](Exercises.md#exercise-2-integer-input-within-a-range).

### Solution

**Approach:** Turn the loop of [Lecture 11, Section 2.5](Concepts_Lecture.md#25-repeating-until-a-valid-input-is-received) into a function. Integer conversion tries `int()` and handles `ValueError` (EAFP), and the range is checked with the chained comparison `low <= value <= high` (LBYL). A valid value is returned with `return`, so no separate `break` is needed to end the loop.

**Code:**

```python
def read_int(prompt, low, high):
    while True:
        text = input(prompt)
        try:
            value = int(text)
        except ValueError:
            print("정수를 입력해야 한다:", repr(text))
            continue
        if not (low <= value <= high):
            print(low, "이상", high, "이하여야 한다")
            continue
        return value

month = read_int("월을 입력하시오 (1~12): ", 1, 12)
print("입력한 월:", month)
```

**Output:** The result of entering `삼월`, `13`, and `3` in turn.

```text
월을 입력하시오 (1~12): 삼월
정수를 입력해야 한다: '삼월'
월을 입력하시오 (1~12): 13
1 이상 12 이하여야 한다
월을 입력하시오 (1~12): 3
입력한 월: 3
```

- **`"삼월"`:** `int()` raises a `ValueError`, so the message is printed and the question is asked again with `continue`.
- **`"13"`:** It converts to an integer, but `1 <= 13 <= 12` is false, so the range message is printed.
- **`"3"`:** It passes both checks, and 3 is returned. Entering it with surrounding spaces, as `" 3 "`, gives the same result because `int()` ignores the whitespace.
- **The benefit of a function:** The same function can receive input in other ranges, as in `read_int("나이: ", 0, 150)`.

---

<br>

## Exercise 3: The Order of Execution of the Four Clauses

**Problem:** Write the output when 4, 0, and `"4"` are given to `check()`, which has `try`, two `except` clauses, `else`, and `finally`. The full problem is in [Exercise 3](Exercises.md#exercise-3-the-order-of-execution-of-the-four-clauses).

### Solution

**Output:**

```text
가 나 마 바
25
가 다 바
zero
가 라 바
바깥에서 처리
```

**Trace:**

| Call | Clauses Run | Output | Result |
|:-----|:-----|:-----|:-----|
| `check(4)` | All of `try` → `else` → `finally` | `가 나 마 바` | Returns 25 by `return r` in `else` |
| `check(0)` | The first part of `try` → `except ZeroDivisionError` → `finally` | `가 다 바` | Returns `"zero"` |
| `check("4")` | The first part of `try` → `except TypeError` → `finally` | `가 라 바` | Re-raises the `TypeError` with `raise` |

*Table 1. Clauses run in the three calls of check()*

- **`return` and `finally`:** `check(4)` and `check(0)` returned in the `else` and `except` clauses, but before the function ended, the `finally` clause printed `바` and a newline. The return values were printed afterward by the outer `print()`, so `25` and `zero` appear on the next lines ([Lecture 11, Section 3.2](Concepts_Lecture.md#32-the-finally-clause)).
- **`100 // "4"`:** An integer cannot be divided by a string, so a `TypeError` occurred. The handler printed `라` and raised the same exception again with `raise`, and after the `finally` clause ran, the exception left the function.
- **The outer `print()`:** `check("4")` could not return a value, so the `print()` of `print(check("4"))` was never called, and the outer `except TypeError` printed `바깥에서 처리`.

---

<br>

## Exercise 4: A Four-Operation Calculator

**Problem:** Write `calc(expr)`, which computes a string of the form `"number operator number"` and handles division by zero, unknown operators, and format errors. The full problem and sample run are in [Exercise 4](Exercises.md#exercise-4-a-four-operation-calculator).

### Solution

**Approach:** Obtain three pieces with `split()`, convert the two numbers with `float()`, and compute according to the operator. If the number of pieces is wrong or a number cannot be converted, Python raises a `ValueError`. To handle unknown operators with the same handler, raise one directly with `raise ValueError(...)` ([Lecture 11, Section 5.1](Concepts_Lecture.md#51-the-raise-statement)). Division by zero uses a different message, so it gets a separate handler.

**Code:**

```python
def calc(expr):
    try:
        a, op, b = expr.split()
        a = float(a)
        b = float(b)
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            return a / b
        else:
            raise ValueError("모르는 연산자 " + repr(op))
    except ZeroDivisionError:
        return "오류: 0으로 나눌 수 없다"
    except ValueError as e:
        return "오류: " + str(e)

for e in ["3 + 4", "10 / 4", "1 / 0", "2 ^ 3", "abc * 2", "1 +"]:
    print(e, "=>", calc(e))
```

**Output:**

```text
3 + 4 => 7.0
10 / 4 => 2.5
1 / 0 => 오류: 0으로 나눌 수 없다
2 ^ 3 => 오류: 모르는 연산자 '^'
abc * 2 => 오류: could not convert string to float: 'abc'
1 + => 오류: not enough values to unpack (expected 3, got 2)
```

- **The type of the result:** Both numbers were converted with `float()`, so even `3 + 4` gives the float `7.0`.
- **`raise` within the same function:** An exception raised with `raise ValueError(...)` is received by the `except ValueError` of the same `try` statement exactly like one raised by Python.
- **`1 / 0`:** Float division `1.0 / 0.0` also raises `ZeroDivisionError`.
- **The order of the handlers:** `ZeroDivisionError` and `ValueError` have no inheritance relationship, so swapping the two clauses gives the same results.

---

<br>

## Exercise 5: The Total of Several Files

**Problem:** Write `total_of_files(paths)`, which adds up all the numbers in several files while skipping missing files and lines that are not numbers. The full problem and sample run are in [Exercise 5](Exercises.md#exercise-5-the-total-of-several-files).

### Solution

**Approach:** There are two units of failure, so the `try` statements are nested in two layers. The outer `try` wraps opening and reading one file and skips only that file on `FileNotFoundError`, and the inner `try` wraps the conversion of one line and skips only that line on `ValueError`. This is "record and continue" of Table 2 ([Lecture 11, Section 2.6](Concepts_Lecture.md#26-what-a-handler-can-do)).

**Code:**

```python
from pathlib import Path

def total_of_files(paths):
    total = 0
    bad_lines = 0
    missing = []
    for p in paths:
        try:
            with open(p, encoding="utf-8") as f:
                for line in f:
                    if line.strip() == "":      # skip blank lines
                        continue
                    try:
                        total += float(line)
                    except ValueError:
                        bad_lines += 1
        except FileNotFoundError:
            missing.append(p)
    return total, bad_lines, missing

Path("a.txt").write_text("10\n20\n\n", encoding="utf-8")
Path("b.txt").write_text("1.5\n둘\n2.5\n", encoding="utf-8")
print(total_of_files(["a.txt", "nothing.txt", "b.txt"]))
```

**Output:**

```text
(34.0, 1, ['nothing.txt'])
```

- **The total:** $10 + 20 + 1.5 + 2.5 = 34.0$. `float()` ignores the newline at the end of the line.
- **Lines that are not numbers:** Only `둘`. Blank lines are skipped first and are not counted. Passing a blank line to `float()` as it is would raise a `ValueError` and count it as a line that is not a number.
- **The missing file:** At the moment `nothing.txt` was opened, the `FileNotFoundError` was handled by the outer `try`, and the loop moved on to `b.txt`.
- **Why two layers:** Merging the `try` of the line conversion into the single outer one would make one line's failure skip all the remaining lines of that file. The extent of a `try` is exactly the extent skipped when it fails.

---

<br>

## Exercise 6: A Hierarchy of Validation Exceptions

**Problem:** Define `EmptyFieldError` and `RangeError` with `ValidationError` as their superclass, and write `validate()`, which checks student information. The full problem and sample run are in [Exercise 6](Exercises.md#exercise-6-a-hierarchy-of-validation-exceptions).

### Solution

**Approach:** The common superclass `ValidationError` stores the field name as an attribute and builds a message of the form `"field: explanation"`. The subclasses only build the explanation and pass it to the superclass constructor ([Lecture 11, Section 5.3](Concepts_Lecture.md#53-user-defined-exceptions)). The handling side writes the specific `EmptyFieldError` first and the general `ValidationError` later ([Lecture 11, Section 4.2](Concepts_Lecture.md#42-the-order-of-except-clauses)).

**Code:**

```python
class ValidationError(Exception):
    def __init__(self, field, message):
        super().__init__(field + ": " + message)
        self.field = field

class EmptyFieldError(ValidationError):
    def __init__(self, field):
        super().__init__(field, "값이 비어 있다")

class RangeError(ValidationError):
    def __init__(self, field, value, low, high):
        super().__init__(field, "값 " + str(value) + ", 허용 범위 " + str(low) + "~" + str(high))

def validate(student):
    for field in ["name", "age"]:
        if student.get(field) in (None, ""):
            raise EmptyFieldError(field)
    if not (0 <= student["age"] <= 150):
        raise RangeError("age", student["age"], 0, 150)
    return True

tests = [{"name": "Kim", "age": 20}, {"name": "", "age": 20}, {"name": "Lee", "age": 200}]
for s in tests:
    try:
        validate(s)
        print(s, "-> 통과")
    except EmptyFieldError as e:
        print(s, "-> 빈 칸:", e.field)
    except ValidationError as e:
        print(s, "-> 검증 실패:", e)
```

**Output:**

```text
{'name': 'Kim', 'age': 20} -> 통과
{'name': '', 'age': 20} -> 빈 칸: name
{'name': 'Lee', 'age': 200} -> 검증 실패: age: 값 200, 허용 범위 0~150
```

- **The chain of constructors:** `EmptyFieldError("name")` goes through `ValidationError.__init__(self, "name", "값이 비어 있다")` to `Exception.__init__(self, "name: 값이 비어 있다")`. Every subclass therefore has the `field` attribute and a message of the same form.
- **`student.get(field)`:** It returns `None` if the key is missing, so the cases of a missing field and an empty string are checked together with `in (None, "")`.
- **Choice of handler:** The second student raises `EmptyFieldError`, so the first handler takes it, and the third student's `RangeError` is a subclass of `ValidationError`, so the second handler takes it. Even if subclasses for new validation rules are added, the second handler still receives them.

---

<br>

## Exercise 7: Reporting as a Configuration Error

**Problem:** Write `parse_config(text)`, which converts the `ValueError` and `KeyError` arising while interpreting a settings string into a `ConfigError` with the cause chained. The full problem and sample run are in [Exercise 7](Exercises.md#exercise-7-reporting-as-a-configuration-error).

### Solution

**Approach:** The caller need not know which built-in exception makes the interpretation of settings fail. Catching the low-level exceptions inside the function and converting them with `raise ConfigError(...) from e` lets the caller handle only `ConfigError` while still being able to inspect the original exception through `__cause__` ([Lecture 11, Section 5.4](Concepts_Lecture.md#54-exception-chaining)). Line numbers come from `enumerate()`, and lines are split with the string method `splitlines()`.

**Code:**

```python
class ConfigError(Exception):
    pass

def parse_config(text):
    settings = {}
    for no, line in enumerate(text.splitlines(), start=1):
        if line.strip() == "":
            continue
        try:
            key, value = line.split("=")
        except ValueError as e:
            raise ConfigError(str(no) + "번째 줄에 '='가 하나여야 한다: " + repr(line)) from e
        settings[key.strip()] = value.strip()
    try:
        port = int(settings["port"])
    except KeyError as e:
        raise ConfigError("port 설정이 없다") from e
    except ValueError as e:
        raise ConfigError("port는 정수여야 한다: " + repr(settings["port"])) from e
    return settings["host"], port

for text in ["host = example.com\nport = 8080", "host = a\nport = eighty", "host = a", "host a\nport = 1"]:
    try:
        print(parse_config(text))
    except ConfigError as e:
        print("설정 오류:", e, "| 원인:", type(e.__cause__).__name__)
```

**Output:**

```text
('example.com', 8080)
설정 오류: port는 정수여야 한다: 'eighty' | 원인: ValueError
설정 오류: port 설정이 없다 | 원인: KeyError
설정 오류: 1번째 줄에 '='가 하나여야 한다: 'host a' | 원인: ValueError
```

- **The failure of `split("=")`:** `"host a"` has no `=`, so there is one piece, and unpacking it into two variables raises a `ValueError`. A line with two `=` signs raises the same exception.
- **`strip()`:** Splitting `"host = example.com"` gives the pieces `"host "` and `" example.com"`, so surrounding whitespace is removed before storing.
- **Two handlers:** The `KeyError` (missing key) and the `ValueError` (not an integer) of `int(settings["port"])` were converted into different messages. The class name of the cause distinguishes the two cases.
- **Without handling:** If the caller had no handler, the traceback would show the original exception and the `ConfigError` joined by "The above exception was the direct cause of the following exception:".

---

<br>

## Exercise 8: A Context Manager That Rolls Back

**Problem:** Write `Transaction(data)`, which restores a list to its contents before the `with` block if the block ends with an exception, and apply it to a transfer function. The full problem and sample run are in [Exercise 8](Exercises.md#exercise-8-a-context-manager-that-rolls-back).

### Solution

**Approach:** `__enter__()` stores a copy (a snapshot) of the list and returns the original list. `__exit__()` replaces the contents of the original list with the snapshot only when it receives an exception class, and returns false to send the exception outward ([Lecture 11, Section 7.2](Concepts_Lecture.md#72-the-with-statement-and-context-managers)). The contents are replaced with the slice assignment `self.data[:] = ...` so that the same list object is kept.

**Code:**

```python
class Transaction:
    def __init__(self, data):
        self.data = data

    def __enter__(self):
        self.snapshot = list(self.data)     # copy taken at the start
        return self.data

    def __exit__(self, exc_type, exc_value, tb):
        if exc_type is not None:
            self.data[:] = self.snapshot     # roll back in place
            print("롤백:", exc_type.__name__)
        return False                         # let the exception propagate

balances = [100, 50]

def transfer(amount):
    with Transaction(balances) as b:
        b[0] -= amount
        if b[0] < 0:
            raise ValueError("잔액 부족")
        b[1] += amount

transfer(30)
print(balances)
try:
    transfer(500)
except ValueError as e:
    print("이체 실패:", e)
print(balances)
```

**Output:**

```text
[70, 80]
롤백: ValueError
이체 실패: 잔액 부족
[70, 80]
```

- **The successful transfer:** The transfer of 30 won ends without an exception and `__exit__()` does nothing, so `[70, 80]` remains.
- **The failed transfer:** The transfer of 500 won changed `b[0]` to $70 - 500 = -430$ and then raised a `ValueError`. `__exit__()` restored the list to `[70, 80]`, its state before the block, and let the exception out, so the balances are unchanged even after the outer handler reported the failure.
- **Why slice assignment:** Writing `self.data = self.snapshot` would only make the context manager's instance variable refer to a different list, leaving the list that the outer `balances` refers to in its changed state ([Lecture 7, Section 9.2](../Lec07_Lists-and-Dictionaries/Concepts_Lecture.md#92-aliasing)).
- **The limit of a shallow copy:** `list(self.data)` is a shallow copy, so if the elements are mutable objects such as lists, changes inside them cannot be rolled back. In that case, make the snapshot with `copy.deepcopy()`.
