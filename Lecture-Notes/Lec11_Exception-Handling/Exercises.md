# Lecture 11 Exercises — Exception Handling

[Repository Guide](../../README.md) | [English](Exercises.md) | [한국어](Exercises.ko.md)

> **Last Updated:** 2026-11-19

Exercises 1 and 3 read tracebacks and orders of execution, and Exercises 2, 4, and 5 handle failures of input, computation, and files with `try` statements. Exercises 6-8 build user-defined exceptions, exception chaining, and context managers.

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

**Problem:** Running the following `grades.py` produces the traceback below.

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
        lines.append(name + ": " + letter(int(score)))
    return lines

data = {"Kim": "95", "Lee": "88", "Park": "7O"}
for line in summary(data):
    print(line)
```

```text
Traceback (most recent call last):
  File "grades.py", line 15, in <module>
    for line in summary(data):
                ~~~~~~~^^^^^^
  File "grades.py", line 11, in summary
    lines.append(name + ": " + letter(int(score)))
                                      ~~~^^^^^^^
ValueError: invalid literal for int() with base 10: '7O'
```

(1) Write the kind of exception and the data that caused it. (2) Explain why the results for Kim and Lee were not printed. (3) Fix `summary()` so that a person whose score cannot be interpreted is shown as `점수 오류('7O')` and the results for the other people are printed as usual.

**Sample Run:** The output of the fixed program.

```text
Kim: A
Lee: B
Park: 점수 오류('7O')
```

**[Solution](Solutions.md#exercise-1-finding-the-cause-from-a-traceback)**

---

<br>

## Exercise 2: Integer Input within a Range

**Problem:** Write a function `read_int(prompt, low, high)` that shows the message `prompt` and receives an integer; if the input is not an integer it prints `정수를 입력해야 한다: 'input'`, and if it is not at least `low` and at most `high` it prints `low 이상 high 이하여야 한다`, and then asks again. When a valid value is entered, it returns that integer. Use this function to receive a month from 1 to 12 and print it.

**Sample Run:** The result of entering `삼월`, `13`, and `3` in turn.

```text
월을 입력하시오 (1~12): 삼월
정수를 입력해야 한다: '삼월'
월을 입력하시오 (1~12): 13
1 이상 12 이하여야 한다
월을 입력하시오 (1~12): 3
입력한 월: 3
```

**[Solution](Solutions.md#exercise-2-integer-input-within-a-range)**

---

<br>

## Exercise 3: The Order of Execution of the Four Clauses

**Problem:** Write the output of the following program without running it. `print(..., end=" ")` prints one space without ending the line.

```python
def check(x):
    try:
        print("가", end=" ")
        r = 100 // x
        print("나", end=" ")
    except ZeroDivisionError:
        print("다", end=" ")
        return "zero"
    except TypeError:
        print("라", end=" ")
        raise
    else:
        print("마", end=" ")
        return r
    finally:
        print("바")

print(check(4))
print(check(0))
try:
    print(check("4"))
except TypeError:
    print("바깥에서 처리")
```

**[Solution](Solutions.md#exercise-3-the-order-of-execution-of-the-four-clauses)**

---

<br>

## Exercise 4: A Four-Operation Calculator

**Problem:** Write a function `calc(expr)` that receives a string of a number, an operator, and a number separated by spaces, such as `"3 + 4"`, and returns the result of the computation (a float). In the following cases, handle the exception and return a string starting with `"오류: "`.

- Dividing by 0 returns `"오류: 0으로 나눌 수 없다"`.
- If the operator is not `+`, `-`, `*`, or `/`, raise `ValueError("모르는 연산자 'operator'")` inside the function, receive that exception in a handler of the same function, and return it with its message attached.
- If a number cannot be converted or there are not exactly three pieces, return the message of the `ValueError` raised by Python attached.

**Sample Run:**

```text
3 + 4 => 7.0
10 / 4 => 2.5
1 / 0 => 오류: 0으로 나눌 수 없다
2 ^ 3 => 오류: 모르는 연산자 '^'
abc * 2 => 오류: could not convert string to float: 'abc'
1 + => 오류: not enough values to unpack (expected 3, got 2)
```

**[Solution](Solutions.md#exercise-4-a-four-operation-calculator)**

---

<br>

## Exercise 5: The Total of Several Files

**Problem:** Write a function `total_of_files(paths)` that receives a list of file paths and adds up the numbers written on each line of each file. The function returns `(total, number of lines that are not numbers, list of missing files)`.

- Skip missing files and collect their paths in the list.
- Ignore blank lines.
- Skip lines that cannot be converted to numbers and count them.
- A failure of one file or one line must not stop the rest of the processing.

Save `10`, `20`, and a blank line to `a.txt`, and `1.5`, `둘`, and `2.5` to `b.txt`, one per line, and then call the function for `["a.txt", "nothing.txt", "b.txt"]`.

**Sample Run:**

```text
(34.0, 1, ['nothing.txt'])
```

**[Solution](Solutions.md#exercise-5-the-total-of-several-files)**

---

<br>

## Exercise 6: A Hierarchy of Validation Exceptions

**Problem:** Define a function `validate(student)` that checks a dictionary of student information, and the following exception classes.

- `ValidationError`: The superclass of every validation error. It has the name of the problematic field `field` as an attribute, and its message has the form `"field: explanation"`.
- `EmptyFieldError`: The error when `name` or `age` is missing or an empty string, with the explanation `값이 비어 있다`.
- `RangeError`: The error when `age` is not at least 0 and at most 150, with an explanation of the form `값 200, 허용 범위 0~150`.

`validate()` returns `True` if there is no problem. Check the three students `{"name": "Kim", "age": 20}`, `{"name": "", "age": 20}`, and `{"name": "Lee", "age": 200}`, printing only the field name for an empty-field error and the whole message for other validation errors.

**Sample Run:**

```text
{'name': 'Kim', 'age': 20} -> 통과
{'name': '', 'age': 20} -> 빈 칸: name
{'name': 'Lee', 'age': 200} -> 검증 실패: age: 값 200, 허용 범위 0~150
```

**[Solution](Solutions.md#exercise-6-a-hierarchy-of-validation-exceptions)**

---

<br>

## Exercise 7: Reporting as a Configuration Error

**Problem:** Write a function `parse_config(text)` that interprets a settings string made of lines of the form `key = value` and returns `(host, port)`. Convert every low-level exception arising inside the function into a user-defined exception `ConfigError`, chaining the original exception as its cause.

- Ignore blank lines.
- A line that does not have exactly one `=` becomes a `ConfigError` saying `"N번째 줄에 '='가 하나여야 한다: 'line'"`.
- A missing `port` becomes a `ConfigError` saying `"port 설정이 없다"`, and a non-integer one a `ConfigError` saying `"port는 정수여야 한다: 'value'"`.

The caller handles only `ConfigError`, printing the message together with the class name of the cause. Interpret the following four strings in turn.

```text
"host = example.com\nport = 8080"
"host = a\nport = eighty"
"host = a"
"host a\nport = 1"
```

**Sample Run:**

```text
('example.com', 8080)
설정 오류: port는 정수여야 한다: 'eighty' | 원인: ValueError
설정 오류: port 설정이 없다 | 원인: KeyError
설정 오류: 1번째 줄에 '='가 하나여야 한다: 'host a' | 원인: ValueError
```

**[Solution](Solutions.md#exercise-7-reporting-as-a-configuration-error)**

---

<br>

## Exercise 8: A Context Manager That Rolls Back

**Problem:** Write a context manager `Transaction(data)` that receives a list and lets it be changed inside a `with` block, but restores the list to its contents before the block if the block ends with an exception.

- The `b` of `with Transaction(list) as b:` is the original list itself.
- If the block ends with an exception, restore the list, print `롤백: ExceptionClassName`, and pass the exception outward unchanged.
- When restoring, do not create a new list; change the contents of the original list object.

Using this context manager, write `transfer(amount)`, which moves money from the first account to the second in the balances of two accounts `balances = [100, 50]`. If the balance of the first account becomes negative, raise `ValueError("잔액 부족")`. Print the balances after transferring 30 won and after a failed transfer of 500 won.

**Sample Run:**

```text
[70, 80]
롤백: ValueError
이체 실패: 잔액 부족
[70, 80]
```

**[Solution](Solutions.md#exercise-8-a-context-manager-that-rolls-back)**
