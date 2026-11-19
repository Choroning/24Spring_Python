# Lecture 4 — Conditional Statements

[Repository Guide](../../README.md) | [English](Concepts_Lecture.md) | [한국어](Concepts_Lecture.ko.md)

> **Last Updated:** 2026-11-19

> **Learning Objectives:**
> 1. Distinguish the three basic control structures of sequence, selection, and iteration, and represent them as flowcharts
> 2. Write conditions with relational and logical operators, and apply short-circuit evaluation, the values returned by `and` and `or`, chained comparisons, and the rules of string comparison
> 3. Execute different statements depending on a condition with the `if-else` statement and blocks formed by indentation
> 4. Check several conditions in turn with the `if-elif-else` statement and nested `if` statements, and rewrite one form as the other
> 5. Generate random numbers with `randrange()`, `randint()`, and `choice()` of the `random` module and use them with conditional statements
> 6. Design a program containing conditional statements by analyzing its input, output, and data and deciding the processing order

---

## Table of Contents

- [1. Basic Control Structures](#1-basic-control-structures)
- [2. Conditions](#2-conditions)
  - [2.1 The Boolean Type](#21-the-boolean-type)
  - [2.2 Relational Operators](#22-relational-operators)
  - [2.3 Logical Operators](#23-logical-operators)
  - [2.4 The Values Returned by and and or](#24-the-values-returned-by-and-and-or)
  - [2.5 Chained Comparisons and String Comparison](#25-chained-comparisons-and-string-comparison)
- [3. The if-else Statement](#3-the-if-else-statement)
  - [3.1 Basic Form](#31-basic-form)
  - [3.2 Example: Pass or Fail](#32-example-pass-or-fail)
  - [3.3 Example: Even or Odd](#33-example-even-or-odd)
  - [3.4 if Statements Without else](#34-if-statements-without-else)
  - [3.5 Evaluating Conditional Expressions](#35-evaluating-conditional-expressions)
- [4. Blocks and Indentation](#4-blocks-and-indentation)
- [5. The if-elif-else Statement](#5-the-if-elif-else-statement)
  - [5.1 Checking Conditions in Succession](#51-checking-conditions-in-succession)
  - [5.2 The Order of Conditions](#52-the-order-of-conditions)
  - [5.3 Conditions That Are Complete and Nonoverlapping](#53-conditions-that-are-complete-and-nonoverlapping)
- [6. Nested if Statements](#6-nested-if-statements)
  - [6.1 The Form of Nesting](#61-the-form-of-nesting)
  - [6.2 Nested if Statements and Logical Operators](#62-nested-if-statements-and-logical-operators)
  - [6.3 Negating Conditions and De Morgan's Laws](#63-negating-conditions-and-de-morgans-laws)
- [7. Random Numbers and Conditional Statements](#7-random-numbers-and-conditional-statements)
- [8. Designing Programs with Conditional Statements](#8-designing-programs-with-conditional-statements)
- [Concept Applications](#concept-applications)
- [Summary](#summary)
- [Self-Check Questions](#self-check-questions)
- [References](#references)

---

<br>

## 1. Basic Control Structures

The order in which the statements of a program are executed is called the **control flow**, and the way the control flow is determined is called a **control structure**. The control flow of a program is made of the following three basic control structures.

- **Sequence:** A structure in which commands are executed one by one in the order written. All programs of Lectures 2 and 3 are sequence structures.
- **Selection:** A structure that selects and executes one of two commands depending on a condition. Conditional statements (Sections 3-6) create selection structures.
- **Iteration:** A structure that executes the same commands repeatedly while a condition holds. Loops are covered in Lecture 5.

```mermaid
flowchart TB
    subgraph seq["Sequence"]
        direction TB
        s1["Command 1"] --> s2["Command 2"] --> s3["Command 3"]
    end
    subgraph sel["Selection"]
        direction TB
        c1{"Condition"} -- True --> a1["Command A"]
        c1 -- False --> b1["Command B"]
        a1 --> n1["Next command"]
        b1 --> n1
    end
    subgraph itr["Iteration"]
        direction TB
        c2{"Condition"} -- True --> r1["Command"]
        r1 --> c2
        c2 -- False --> n2["Next command"]
    end
```

*Figure 1. Flowcharts of the sequence, selection, and iteration structures*

Figure 1 represents each structure as a **flowchart**. In a flowchart, a rectangle is a command, a diamond is a condition judged true or false, and an arrow is the order of execution. The three structures can be compared to roads. A sequence is a straight road without forks, a selection is a road that splits in two, and an iteration is a looping road that goes around and passes the same place again.

![Figure 2. Sequence, selection, and iteration structures compared to roads](../../images/Lec04_p02.png)

*Figure 2. Sequence, selection, and iteration structures compared to roads*

> **Note:** In 1966, Böhm and Jacopini showed that every program that can be represented as a flowchart can be converted into a program with the same behavior by combining only the three structures of sequence, selection, and iteration (adding auxiliary variables if necessary) [1]. This result became the theoretical basis of structured programming, which writes programs with these three structures alone.

---

<br>

## 2. Conditions

In a selection structure, which command to execute is decided by whether a condition is true or false. An expression that evaluates to true or false is called a **condition**.

### 2.1 The Boolean Type

True and false are represented by the two values `True` and `False` of the **Boolean type** `bool`. The first letter must be uppercase, and they are not enclosed in quotes. `"True"` in quotes is a string, not a Boolean value.

```pycon
>>> 100 > 1
True
>>> 1 > 100
False
>>> type(True)
<class 'bool'>
```

Values that are not Boolean can also appear where a condition is expected. In that case, Python judges numeric zero (`0`, `0.0`), empty values such as the empty string `""` and the empty list `[]`, and `None` (Lecture 3), which means no value, as false, and other values as true [2]. Whether a value is judged true or false can be checked with `bool()`.

```pycon
>>> bool(0)
False
>>> bool(3)
True
>>> bool("")
False
>>> bool("abc")
True
>>> bool([])
False
>>> bool([1])
True
```

### 2.2 Relational Operators

A **relational operator** is an operator that compares two operands and returns `True` or `False` as the result of the comparison. It is also called a comparison operator.

| Operation | Meaning |
|:-----|:-----|
| `x == y` | Are x and y equal? |
| `x != y` | Are x and y different? |
| `x > y` | Is x greater than y? |
| `x < y` | Is x less than y? |
| `x >= y` | Is x greater than or equal to y? |
| `x <= y` | Is x less than or equal to y? |

*Table 1. Relational operators*

For example, `100 > 1` is true (`True`) because 100 is greater than 1, and `1 > 100` is false (`False`).

```pycon
>>> x = 3
>>> x == 3
True
>>> x != 3
False
>>> x >= 3
True
>>> "apple" == "apple"
True
>>> "apple" == "Apple"
False
>>> 3 == 3.0
True
```

- Strings can also be compared with `==`, and two strings are equal only if all their characters are the same. Uppercase and lowercase letters are different characters, so `"apple"` and `"Apple"` are different.
- The integer 3 and the floating-point number 3.0 are equal because their numerical values are the same, even though their data types differ.

> **Caution:** The operator that tests equality is `==`, not `=`. `=` is the assignment operator that stores a value in a variable, so using it in a condition is a syntax error. Python asks in the message whether `==` was intended.
> ```pycon
> >>> if x = 5:
>   File "<stdin>", line 1
>     if x = 5:
>        ^^^^^
> SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
> ```

When values of different data types are compared, the result depends on the operator. `==` returns `False` without an error even for values whose magnitudes cannot be compared, such as a number and a string, but `<`, which compares magnitude, raises a `TypeError`. Therefore, an input string must be converted with `int()` or `float()` before being compared with a number (Lecture 3).

```pycon
>>> 10 == "10"
False
>>> 10 < "10"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    10 < "10"
TypeError: '<' not supported between instances of 'int' and 'str'
```

In Python, relational operators can be chained like mathematical inequalities. `6 <= time < 9` means the same as `6 <= time and time < 9` [3].

```pycon
>>> time = 7
>>> 6 <= time < 9
True
>>> time >= 6 and time < 9
True
```

### 2.3 Logical Operators

To combine several conditions into one, use **logical operators**. For example, the rule "나이가 10살 이상이고, 그리고 키가 165cm 이상이면 놀이기구를 탈 수 있다" ("If you are 10 years old or older and also 165 cm tall or taller, you can ride the ride") contains two conditions. Condition 1 is that the age is 10 or more, and condition 2 is that the height is 165 cm or more. Both must hold, so the rule is `(age is 10 or more) and (height is 165 cm or more)`, which is `age >= 10 and height >= 165` as a Python condition.

| Operation | Meaning |
|:-----|:-----|
| `x and y` | AND operation. True if both x and y are true, false otherwise |
| `x or y` | OR operation. True if even one of x and y is true, false if both are false |
| `not x` | NOT operation. False if x is true, true if x is false |

*Table 2. Logical operators*

| `x` | `y` | `x and y` | `x or y` | `not x` |
|:-----|:-----|:-----|:-----|:-----|
| `True` | `True` | `True` | `True` | `False` |
| `True` | `False` | `False` | `True` | `False` |
| `False` | `True` | `False` | `True` | `True` |
| `False` | `False` | `False` | `False` | `True` |

*Table 3. Truth table of the logical operators*

```pycon
>>> age = 12
>>> height = 170
>>> age >= 10 and height >= 165
True
>>> age >= 10 and height >= 180
False
>>> age >= 15 or height >= 165
True
>>> not (age >= 10)
False
```

- Both `age >= 10` and `height >= 165` are true, so the result of `and` is true.
- `height >= 180` is false, so the result of `and` is false.
- `age >= 15` is false, but `height >= 165` is true, so the result of `or` is true.
- `age >= 10` is true, so the result of `not` is false.

**Precedence:** Relational operators are computed before logical operators, so `age >= 10 and height >= 165` needs no parentheses. Among the logical operators, `not`, `and`, and `or` are computed first in that order [3]. So in `True or False and False`, `and` is computed first, giving `True or False`, that is, `True`. If a different order is intended, group with parentheses.

```pycon
>>> True or False and False
True
>>> (True or False) and False
False
```

**Short-circuit evaluation:** If the left operand of `and` is false, the result is already false, so the right operand is not evaluated. Likewise, if the left operand of `or` is true, the right operand is not evaluated [3]. With this property, a case in which the right expression could cause an error can be filtered out in advance by the left condition. In the following example, `x != 0` is false, so `10 / x`, which divides by 0, is not computed. If the order is reversed, the division is computed first and an error occurs.

```pycon
>>> x = 0
>>> x != 0 and 10 / x > 1
False
>>> 10 / x > 1 and x != 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    10 / x > 1 and x != 0
    ~~~^~~
ZeroDivisionError: division by zero
```

> **[Discrete Mathematics]** `and`, `or`, and `not` correspond to conjunction, disjunction, and negation in propositional logic, and Table 3 is the truth table of these operations. By De Morgan's laws, `not (A and B)` always has the same value as `(not A) or (not B)`, and `not (A or B)` always has the same value as `(not A) and (not B)`; these laws allow a condition to be rewritten in another form with the same meaning.

### 2.4 The Values Returned by and and or

Table 3 gives the results when the operands are `True` or `False`. However, as seen in Section 2.1, any value can appear in the place of a condition, so the operands of `and` and `or` need not be Boolean values either. In that case, `and` and `or` return **one of the two operands as it is**, not a value converted to `True` or `False` [2]. Following the rules of short-circuit evaluation exactly determines which one is returned.

| Expression | When the Left `x` Is Judged True | When the Left `x` Is Judged False |
|:-----|:-----|:-----|
| `x and y` | Evaluates `y` and returns `y` | Returns `x` without evaluating `y` |
| `x or y` | Returns `x` without evaluating `y` | Evaluates `y` and returns `y` |
| `not x` | `False` | `True` |

*Table 4. What and, or, and not evaluate and return*

When the left side of `and` is false, the result is already determined to be false, so it returns the left value; when the left side is true, the result depends on the right side, so it returns the right value. `or` works the other way around. Only `not` always returns `True` or `False`.

```pycon
>>> 3 and 5
5
>>> 0 and 5
0
>>> "" or "손님"
'손님'
>>> "홍길동" or "손님"
'홍길동'
>>> None or 0
0
>>> not "abc"
False
```

- **Line 1:** 3 is true, so the result depends on the right side, 5, which is returned.
- **Line 3:** 0 is false, so 0 is returned without looking at the right side.
- **Lines 5 and 7:** `or` returns the right side `"손님"` when the left side is an empty string (false), and the left side when it is `"홍길동"` (true).
- **Line 9:** `None` is false, so the right side 0 is evaluated and returned. The result 0 is also false, but `or` simply returns that value as it is.
- **Line 11:** A nonempty string is true, so the result of `not` is `False`.

Because of this property, `or` is often used to choose a value to use instead when a value is empty. In the following program, if the user presses only the Enter key without typing anything, `input()` returns an empty string, so `"손님"` (guest) is used as the name.

```python
name = input("이름: ") or "손님"
print(name + "님, 환영합니다.")
```

```text
이름:
손님님, 환영합니다.
```

```text
이름: 철수
철수님, 환영합니다.
```

That short-circuit evaluation actually skips the right side becomes visible when `print()`, which prints characters on the screen, is used as an operand. `print()` prints its characters and then returns `None`, meaning no value, and `None` is judged false.

```pycon
>>> print("왼쪽") and print("오른쪽")
왼쪽
>>> print("왼쪽") or print("오른쪽")
왼쪽
오른쪽
```

In the first expression, the left side `print("왼쪽")` printed `왼쪽` (left) and returned `None`. `None` is false, so `and` did not evaluate the right side, and `오른쪽` (right) was not printed. In the second expression the left side is false, so `or` evaluated the right side as well and both lines were printed. Because the right operand is evaluated only when needed in this way, the method of Section 2.3 works: put an expression that may cause an error on the right, and a condition that prevents the error on the left.

Not knowing that `and` and `or` return their operands as they are makes the following mistake easy. `x == 1 or 2`, a literal translation of "if `x` is 1 or 2", is true even when `x` is 5.

```pycon
>>> x = 5
>>> x == 1 or 2
2
>>> bool(x == 1 or 2)
True
>>> x == 1 or x == 2
False
>>> x in (1, 2)
False
```

`==` has higher precedence than `or`, so `x == 1 or 2` is evaluated as `(x == 1) or 2`. `x == 1` is `False`, so `or` returns the right side 2, and 2, being a nonzero number, is judged true in an `if` statement. Therefore the block of `if x == 1 or 2:` runs whatever `x` is. Write each condition as a complete expression, as in `x == 1 or x == 2`, or use the `in` operator, which checks whether a value is one of several candidates, as in `x in (1, 2)`.

> **Caution:** A string is true whenever it is nonempty, regardless of its content. So `bool("False")`, `bool("0")`, and `bool(" ")` are all `True`. To judge true or false from a string the user entered, such as `"0"` or `"no"`, compare the content, as in `answer == "no"`.

### 2.5 Chained Comparisons and String Comparison

A chained comparison `a < b < c`, like `6 <= time < 9` in Section 2.2, is the same as `a < b and b < c`, except that the middle `b` is evaluated only once and `c` is not evaluated when `a < b` is false [2]. A chained comparison compares only neighboring values, so shapes not used in mathematics are also grammatical.

```pycon
>>> 1 < 3 > 2
True
>>> x = 5
>>> 1 <= x <= 10
True
>>> 0 < x < 3
False
```

`1 < 3 > 2` is `1 < 3 and 3 > 2`, so it is true, but it does not compare 1 with 2. Because this easily confuses readers, chaining is best used only to express a range with inequality signs in the same direction, as in `1 <= x <= 10`.

Strings can also be compared in size with `<` and `>`. String comparison follows **lexicographic order**, the same order as looking up words in a dictionary. The characters of the two strings are compared in turn from the first, and at the first position where the characters differ, the string whose character has the smaller Unicode number (Lecture 1, Section 4.2) is the smaller string; if one string equals the beginning of the other, the shorter one is the smaller string.

```pycon
>>> "apple" < "banana"
True
>>> "Apple" < "apple"
True
>>> "Z" < "a"
True
>>> "abc" < "abd"
True
>>> "ab" < "abc"
True
>>> "10" < "9"
True
>>> 10 < 9
False
>>> ord("1"), ord("9")
(49, 57)
```

- **Line 1:** The first character `a` (97) is smaller than `b` (98), so the result is true.
- **Lines 3 and 5:** The numbers of uppercase letters (A is 65, Z is 90) are smaller than those of lowercase letters (a is 97), so strings starting with an uppercase letter come first.
- **Line 7:** The two characters `ab` are equal, and at the third character `c` (99) is smaller than `d` (100).
- **Line 9:** `"ab"` equals the beginning of `"abc"` and is shorter, so it is smaller.
- **Lines 11-14:** The strings `"10"` and `"9"` are compared not by numeric size but by their first characters `1` (49) and `9` (57), so `"10"` is smaller. The result is the opposite of comparing the integers 10 and 9.

The last example is the mistake made when input values are compared without conversion. Comparing strings returned by `input()` gives a lexicographic result without any error, so the error of judging a score of 10 lower than a score of 9 is hard to notice. To compare as numbers, always convert with `int()` or `float()` before comparing. Also, a condition comparing floats with `==` can turn out false against expectation because of rounding error, so use `math.isclose()` (Lecture 3, Section 1.4), and do not use `is`, which asks whether two operands are the same object, to compare numbers or strings (Lecture 3, Section 1.3).

---

<br>

## 3. The if-else Statement

### 3.1 Basic Form

A statement that chooses which statements to execute according to the value of a condition is called a **conditional statement**, and Python's basic conditional statement is the `if-else` statement [4]. Its basic syntax is as follows.

```text
if condition:             # Write if, then put a colon (:) after the condition
    statement 1-1         # Indent, then write the statements to run when the condition is true
    statement 1-2         # Statements run under the same condition keep the same indentation
else:                     # The statements to run when the condition is not true follow
    statement 2-1         # Write the statements to run when the condition is not true
    statement 2-2         # Keep the same indentation
```

The following code is used to name each part and its role.

```python
if score >= 60:
    print("합격입니다.")
else:
    print("불합격입니다.")
```

- **`if`:** A keyword corresponding to "if". A keyword is a word that Python reserves for a special meaning and cannot be used as a variable name.
- **Condition:** An expression that evaluates to true or false, such as `score >= 60`. It may be enclosed in parentheses, as in `if (score >= 60):`, but they are not necessary.
- **Colon (`:`):** Means that the statement is not finished yet and the statements to execute follow, indented, from the next line. Omitting the colon is a syntax error.
- **Then clause:** The statements executed when the condition is true ("Pass."). They must be indented more than the `if` line.
- **`else` and the else clause:** `else` means "otherwise", and the else clause is the statements executed when the condition is not true ("Fail."). `else` starts in the same column as `if` and is followed by a colon.

Exactly one of the then clause and the else clause is executed, and whichever is executed, control then moves to the statement after the `if-else` statement.

```mermaid
flowchart TD
    start(["Start"]) --> cond{"score >= 60"}
    cond -- True --> then["Print pass message"]
    cond -- False --> els["Print fail message"]
    then --> next["Statement after if-else"]
    els --> next
```

*Figure 3. Flowchart of the pass-or-fail if-else statement*

### 3.2 Example: Pass or Fail

The program reads a score and prints pass if it is 60 or higher, and fail otherwise.

```python
score = int(input("성적을 입력하시오: "))
if score >= 60:
    print("합격입니다.")
else:
    print("불합격입니다.")
```

```text
성적을 입력하시오: 80
합격입니다.
```

```text
성적을 입력하시오: 50
불합격입니다.
```

- **Line 1:** Converts the string entered at the prompt ("Enter your score: ") to an integer with `int()` and stores it in `score` (Lecture 3).
- **Line 2:** Computes `score >= 60`. It is true if 80 is entered and false if 50 is entered.
- **Line 3:** Executed only when the condition is true.
- **Line 5:** Executed only when the condition is false. A score of 60 passes because `60 >= 60` is true.

> **Caution:** If a number with a decimal point such as `0.1` is entered into a program that reads with `int(input(...))`, a `ValueError` occurs before the conditional statement is reached (Lecture 3). If scores can be decimals, read them with `float(input(...))`. How to ask again without stopping when the input is not an integer is covered in Lecture 11, Section 2.5.
> ```pycon
> >>> num = int(input("정수를 입력하시오: "))
> 정수를 입력하시오: 0.1
> Traceback (most recent call last):
>   File "<stdin>", line 1, in <module>
>     num = int(input("정수를 입력하시오: "))
>           ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
> ValueError: invalid literal for int() with base 10: '0.1'
> ```

### 3.3 Example: Even or Odd

The program reads an integer and prints whether it is even or odd. An even number is an integer whose remainder when divided by 2 is 0, so the condition `num % 2 == 0` is made with the remainder operator `%` (Lecture 2).

```python
num = int(input("정수를 입력하시오: "))
if num % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")
```

```text
정수를 입력하시오: 10
짝수입니다.
```

```text
정수를 입력하시오: 7
홀수입니다.
```

If 10 is entered, `10 % 2` is 0, so `0 == 0` is true and the number is even ("짝수입니다."). If 7 is entered, `7 % 2` is 1, so it is odd ("홀수입니다."). When the divisor is positive, Python's `%` returns a remainder of 0 or more even when dividing a negative number (`-7 % 2` is 1), so negative inputs are also judged correctly.

### 3.4 if Statements Without else

When there is something to do only when the condition is true and nothing to do when it is false, the `else` clause is omitted. Then, if the condition is false, nothing is done and control moves to the next statement.

```python
score = int(input("성적을 입력하시오: "))
if score > 90:
    print("합격입니다.")
    print("장학금도 받을 수 있습니다.")
print("프로그램을 종료합니다.")
```

```text
성적을 입력하시오: 95
합격입니다.
장학금도 받을 수 있습니다.
프로그램을 종료합니다.
```

```text
성적을 입력하시오: 80
프로그램을 종료합니다.
```

If 95 is entered, the condition is true, so the two indented statements ("Pass." and "You can also receive a scholarship.") are executed; if 80 is entered, the two statements are skipped. The last line is not indented, so it does not belong to the `if` statement and is always executed regardless of the condition ("The program ends.").

> **Note:** When one of two values only needs to be chosen according to a condition, the conditional expression `A if condition else B` can be used. Its value is `A` if the condition is true and `B` if it is false [3]. With `num = 7`, running `result = "짝수" if num % 2 == 0 else "홀수"` makes `result` equal to `"홀수"` (odd).

### 3.5 Evaluating Conditional Expressions

The **conditional expression** `A if condition else B`, introduced in the note box of Section 3.4, is not a statement but an expression that produces a single value. Whereas an `if-else` statement chooses which **statements** to execute depending on a condition, a conditional expression chooses a **value** depending on a condition. So it can be used wherever a value may appear, such as the right side of an assignment statement, an argument of a function, or part of another expression. The order of evaluation is as follows.

1. The condition in the middle is evaluated first.
2. If the condition is true, only `A` is evaluated and its value becomes the value of the expression; if false, only `B` is evaluated and its value becomes the value of the expression. The side not chosen is not evaluated.

```pycon
>>> score = 75
>>> "합격" if score >= 60 else "불합격"
'합격'
>>> x = -3
>>> abs_x = x if x >= 0 else -x
>>> abs_x
3
>>> "A" if score >= 90 else "B" if score >= 80 else "C"
'C'
>>> y = 0
>>> "0으로 나눌 수 없음" if y == 0 else 10 / y
'0으로 나눌 수 없음'
>>> "합격" if score >= 60
  File "<stdin>", line 1
    "합격" if score >= 60
    ^^^^^^^^^^^^^^^^^^^
SyntaxError: expected 'else' after 'if' expression
```

- **Line 2:** 75 >= 60 is true, so the left side `"합격"` (pass) is the value of the expression.
- **Line 5:** `x` is negative, so the condition is false, the right side `-x` is evaluated, and `abs_x` is 3. This writes the four lines of an `if-else` statement for the absolute value in one line.
- **Line 8:** Placing another conditional expression on the `else` side of a conditional expression divides several cases, like an `if-elif-else` statement. 75 is neither 90 or more nor 80 or more, so the value is `"C"`. However, chaining this way is hard to read, so with three or more cases an `if-elif-else` statement is preferable.
- **Line 11:** `y == 0` is true, so only the string on the left is evaluated, and `10 / y` on the right is not evaluated, so no `ZeroDivisionError` occurs. As in short-circuit evaluation (Section 2.4), only the side needed is evaluated.
- **Line 13:** A conditional expression must always produce a value, so the `else` side cannot be omitted. To do something only when a condition is true, use an `if` statement without `else` (Section 3.4).

---

<br>

## 4. Blocks and Indentation

When several statements must be executed if a condition is true, they are grouped into a block. A **block** is a group of statements, a unit of statements that are executed together or skipped together. In the example of Section 3.4, `print("합격입니다.")` and `print("장학금도 받을 수 있습니다.")` form one block belonging to `if score > 90:`.

Languages such as C and Java mark blocks with braces `{ }`, but Python marks blocks with **indentation**, the spaces at the beginning of a line [5]. Indentation is not decoration for readability but part of the syntax, and it follows these rules.

- A line ending with a colon (`:`) must be followed by an indented block.
- All statements in the same block are indented by the same number of columns. Four spaces is the convention [6].
- A block ends when the indentation returns to the original column.
- If tabs and spaces are mixed for indentation in one file, Python may be unable to decide whether two lines have the same indentation and raise a `TabError` [5]. For this reason, spaces alone are recommended for indentation [6].

Wrong indentation raises an **`IndentationError`**. The following are a case in which a statement that should be indented is not, and a case in which statements of the same block are indented differently.

```pycon
>>> score = 95
>>> if score > 90:
... print("합격입니다.")
  File "<stdin>", line 2
    print("합격입니다.")
    ^^^^^
IndentationError: expected an indented block after 'if' statement on line 1
```

```pycon
>>> score = 95
>>> if score > 90:
...     print("합격입니다.")
...       print("장학금도 받을 수 있습니다.")
  File "<stdin>", line 3
    print("장학금도 받을 수 있습니다.")
IndentationError: unexpected indent
```

Indentation can also change the meaning without causing an error. In the following code, the second `print()` is not indented, so it is outside the `if` statement, and the scholarship message is printed even though the score is 80.

```python
score = 80
if score > 90:
    print("합격입니다.")
print("장학금도 받을 수 있습니다.")
```

```text
장학금도 받을 수 있습니다.
```

> **Note:** A block must contain at least one statement. When a block that does nothing is needed, such as a block not yet written, use `pass`, a statement that performs no action.

---

<br>

## 5. The if-elif-else Statement

### 5.1 Checking Conditions in Succession

To read an integer and print whether it is positive, zero, or negative, conditions must be checked in succession because there are three cases. First, `num > 0` is checked; if it is true, the number is positive. If it is false, `num == 0` is checked; if that is true, the number is 0, and if it is also false, the number is negative. Such successive checking is written with `elif`. `elif` is a keyword short for "else if" that attaches a new condition to be checked when all preceding conditions are false [4].

```mermaid
flowchart TD
    c1{"num > 0"} -- True --> p1["Print positive message"]
    c1 -- False --> c2{"num == 0"}
    c2 -- True --> p2["Print zero message"]
    c2 -- False --> p3["Print negative message"]
```

*Figure 4. Flowchart of the if-elif-else statement that classifies positive, zero, and negative numbers*

```python
num = int(input("정수를 입력하시오: "))

if num > 0:
    print("양수입니다.")
elif num == 0:
    print("0입니다.")
else:
    print("음수입니다.")
```

```text
정수를 입력하시오: 10
양수입니다.
```

```text
정수를 입력하시오: 0
0입니다.
```

```text
정수를 입력하시오: -5
음수입니다.
```

- `if`, `elif`, and `else` are checked in turn from the top, and only the one block of the first condition that is true is executed. The conditions after it are not checked.
- `elif` can be used as many times as needed, and the final `else` can be omitted. If `else` is omitted, no block is executed when all conditions are false.
- If 0 is entered, `num > 0` is false, so `num == 0` is checked; it is true, so `0입니다.` ("It is 0.") is printed.

### 5.2 The Order of Conditions

The `if-elif-else` statement executes only the first condition that is true, so the order in which conditions are written can change the result. The following code, which assigns a letter grade according to a score, checks the highest threshold first.

```python
score = int(input("점수를 입력하시오: "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")
```

```text
점수를 입력하시오: 85
B
```

For 85, `score >= 90` is false and `score >= 80` is true, so the grade is B. Reaching `elif score >= 80` means that the preceding condition `score >= 90` was false, so this block is in fact executed only for scores of 80 or more and less than 90. If the order of the conditions in the same code is changed to `score >= 70`, `score >= 80`, and `score >= 90`, even 95 becomes true at the first condition `score >= 70`, and C is printed.

```text
점수를 입력하시오: 95
C
```

> **Note:** **The `match` statement.** Since Python 3.10, the `match` statement, which compares one value with several patterns in turn, can also be used [4]. It does not exist in Python 3.7 [7]; when `case` clauses such as `case "start":`, `case "stop" | "quit":`, and `case _:` are placed under `match command:`, only the block of the first pattern that `command` matches is executed, `|` means one of several patterns, and `_` means the remaining case that matches any value. If `command = "quit"`, the block of the second `case` is executed. `match` suits deciding which of a fixed set of candidates a value is, while `if-elif-else` statements suit comparisons of ranges such as the one above.

### 5.3 Conditions That Are Complete and Nonoverlapping

When using an `if-elif-else` statement, check that every input falls into exactly one case. Tracing which block each input reaches when boundary values and out-of-range values are fed to the grading program of Section 5.2 gives the following.

| Score | First Condition That Is True | Output |
|:-----|:-----|:-----|
| 100, 90 | `score >= 90` | A |
| 89, 80 | `score >= 80` | B |
| 79, 70 | `score >= 70` | C |
| 69, 0 | None (`else`) | F |
| 105 | `score >= 90` | A |
| -5 | None (`else`) | F |

*Table 5. Trace of the grading program with boundary and out-of-range values*

Boundary values such as 90, 80, and 70 fall into the higher grade because `>=` was used; writing the criteria with `>` by mistake would make 90 points a B. Also, `else` receives every remaining case in which all the preceding conditions are false, so this program prints something for any integer, but it also gives A and F for impossible scores such as 105 and -5 points. Checking first, at the very top, whether the input lies in the valid range prevents this problem.

```python
score = int(input("점수를 입력하시오: "))
if score < 0 or score > 100:
    print("점수는 0부터 100까지입니다.")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")
```

The conditions are checked in order from the top, so reaching the second condition means the score is between 0 and 100 inclusive. In this way the conditions of an `if-elif-else` statement are read on the premise that the preceding conditions are false, so a range need not be written on both sides, as in `80 <= score < 90`. Conversely, using `if` several times instead of `elif` checks each condition separately, so 95 points satisfies `score >= 90`, `score >= 80`, and `score >= 70`, and A, B, and C are all printed. When conditions may overlap, they must be joined with `elif`; to use `if` several times, write the ranges so that they do not overlap, as in `80 <= score < 90`.

---

<br>

## 6. Nested if Statements

### 6.1 The Form of Nesting

An `if` statement can also be placed inside the block of another `if` statement. This is called a **nested if statement**. The classification of positive, zero, and negative numbers in Section 5.1 can also be written with nested `if` statements. First check whether the number is 0 or more, and in that case check again whether it is 0.

```mermaid
flowchart TD
    c1{"num >= 0"} -- True --> c2{"num == 0"}
    c1 -- False --> p3["Print negative message"]
    c2 -- True --> p1["Print zero message"]
    c2 -- False --> p2["Print positive message"]
```

*Figure 5. Flowchart of the nested if statements that classify positive, zero, and negative numbers*

```python
num = int(input("정수를 입력하시오: "))
if num >= 0:
    if num == 0:
        print("0입니다.")
    else:
        print("양수입니다.")
else:
    print("음수입니다.")
```

```text
정수를 입력하시오: 10
양수입니다.
```

```text
정수를 입력하시오: -3
음수입니다.
```

- **Line 2:** The outer `if` statement checks `num >= 0`.
- **Lines 3-6:** The block executed when the outer condition is true; it contains the inner `if-else` statement. The inner `if` statement is indented one more level.
- **Lines 7-8:** The outer `else` is in the same column as the outer `if`, so it pairs with the outer `if`. Which `if` an `else` pairs with is determined by indentation.

If 10 is entered, `num >= 0` is true and `num == 0` is false, so `양수입니다.` ("It is positive.") is printed; if -3 is entered, `num >= 0` is false, so `음수입니다.` ("It is negative.") is printed. Compared with the `if-elif-else` statement of Section 5.1, which makes the same classification, deeper nesting adds indentation and makes the code harder to read, so when the cases can be listed at the same level, `elif` is easier to read.

### 6.2 Nested if Statements and Logical Operators

Conditions combined with `and` can be rewritten as nested `if` statements. The following two programs judge the ride rule of Section 2.3 and give the same result for every input.

```python
age = int(input("나이를 입력하시오: "))
height = int(input("키를 입력하시오: "))
if age >= 10:
    if height >= 165:
        print("놀이기구를 탈 수 있습니다.")
    else:
        print("놀이기구를 탈 수 없습니다.")
else:
    print("놀이기구를 탈 수 없습니다.")
```

```python
age = int(input("나이를 입력하시오: "))
height = int(input("키를 입력하시오: "))
if age >= 10 and height >= 165:
    print("놀이기구를 탈 수 있습니다.")
else:
    print("놀이기구를 탈 수 없습니다.")
```

```text
나이를 입력하시오: 12
키를 입력하시오: 170
놀이기구를 탈 수 있습니다.
```

```text
나이를 입력하시오: 12
키를 입력하시오: 150
놀이기구를 탈 수 없습니다.
```

```text
나이를 입력하시오: 8
키를 입력하시오: 170
놀이기구를 탈 수 없습니다.
```

The nested `if` statements check the inner condition only when the outer condition is true, so they judge in the same order as the short-circuit evaluation of `and` (Section 2.3). If either condition is false, the ride is not allowed, so the same output statement appears twice in the nested form and only once in the `and` form. When a different message must be printed for each condition, the nested form is suitable; when there are only two results, the `and` form is more concise.

### 6.3 Negating Conditions and De Morgan's Laws

To check the case of not being allowed to ride first in the program of Section 6.2, the condition for being allowed to ride, `age >= 10 and height >= 165`, must be negated. Putting `not` before the whole condition, as in `not (age >= 10 and height >= 165)`, is always correct, but rewriting the inside of the parentheses directly requires De Morgan's laws (Section 2.3). The negation of two conditions joined by `and` negates each condition and changes `and` to `or`.

```math
\text{not}\,(A \;\text{and}\; B) = (\text{not}\, A) \;\text{or}\; (\text{not}\, B)
```

The negation of `age >= 10` is `age < 10` and the negation of `height >= 165` is `height < 165`, so the condition for not being allowed to ride is `age < 10 or height < 165`. Note that in negation `>=` becomes `<` and `>` becomes `<=`, so the boundary value moves to the other side. A common mistake is to negate each condition but leave `and` as it is. The following program compares three expressions for four cases, including boundary values.

```python
for age, height in [(9, 170), (10, 164), (10, 165), (12, 180)]:
    can_ride = age >= 10 and height >= 165
    cannot1 = not (age >= 10 and height >= 165)
    cannot2 = age < 10 or height < 165
    wrong = age < 10 and height < 165
    print(age, height, can_ride, cannot1, cannot2, wrong)
```

```text
9 170 False True True False
10 164 False True True False
10 165 True False False False
12 180 True False False False
```

The `for` statement on the first line puts the four pairs inside the brackets into `age` and `height` in turn and runs the body four times (Lecture 5). In the results, `cannot1` and `cannot2` are the opposite of `can_ride` in all four cases, so they are the same condition. In contrast, `wrong`, which keeps `and`, gives `False` in the first two cases, where only the age or only the height falls short, judging people who cannot ride as able to ride. This expression is true only when both the age and the height fall short.

After rewriting a condition, comparing its results with those of the original condition on boundary values in this way finds such mistakes. In the same way, the negation of conditions joined by `or` is `not (A or B) = (not A) and (not B)`, and "it is not the case that the age is under 10 or the height is under 165 cm" is the same as "the age is 10 or more and the height is 165 cm or more".

---

<br>

## 7. Random Numbers and Conditional Statements

Programs that must give a different result on each run, such as games, need numbers decided at random, that is, **random numbers**. Python provides the standard module `random` for generating random numbers; it is loaded with `import random` and used in the form `random.function_name()` [8].

| Function | Result | Example |
|:-----|:-----|:-----|
| `random.randrange(n)` | One integer from 0 up to but not including n | `random.randrange(2)` is 0 or 1 |
| `random.randrange(a, b)` | One integer from a up to but not including b (b excluded) | `random.randrange(1, 6)` is one of 1-5 |
| `random.randint(a, b)` | One integer from a to b inclusive (both a and b included) | `random.randint(1, 10)` is one of 1-10 |
| `random.choice(list)` | One of the elements of the list | `random.choice([True, False])` is `True` or `False` |

*Table 6. Main functions of the random module*

```pycon
>>> import random
>>> random.randrange(2)
0
>>> random.randrange(2)
1
>>> random.randint(1, 10)
1
>>> random.randint(1, 10)
2
>>> random.choice([True, False])
True
>>> random.choice(['가위', '바위', '보'])
'가위'
```

The results differ on every run, and the values above are an example of one run. Note that `randrange()` and `randint()` differ in whether the end value is included. Like string slicing (Lecture 3), `randrange()` excludes the end value, while `randint()` includes it.

Using a random number in a condition makes a program in which a different block is executed on each run. For example, generating 0 or 1 with `coin = random.randrange(2)` and then separating heads and tails with `if coin == 0:` makes a coin toss. Programs that use random numbers with conditional statements in this way appear in [Exercises](Exercises.md) 3, 4, and 7.

> **Note:** The numbers that the `random` module produces are pseudo-random numbers computed by a fixed algorithm (the Mersenne Twister). Setting the same starting value with `random.seed()` produces the same sequence of numbers every time, which is useful when testing a program. On the other hand, they are not suitable for security purposes, where numbers must be unpredictable [8].

---

<br>

## 8. Designing Programs with Conditional Statements

When writing a program containing conditional statements, organizing the problem in the following order, rather than writing code at once, reduces mistakes.

| Step | What to Organize | Example of the Automatic Coffee Ordering Machine |
|:-----|:-----|:-----|
| 1. Problem analysis | The input, the output, and the data the program must remember | The input is the number of cups of each coffee and the amount paid; the output is the price per cup of each coffee, the total, and the change |
| 2. Deciding the processing order | The processing steps from input to output and the places where a decision is needed | Print the menu, read the number of cups, compute the total, read the amount, and decide whether the amount is insufficient |
| 3. Deciding the variables | The names and meanings of the variables that hold the data | `noA` (number of americanos), `money` (amount paid), and so on |
| 4. Programming | Translate the decided order into code and run it with various inputs | Accumulate the total with the compound assignment operator `+=` and decide whether the amount is insufficient with an `if-else` statement |

*Table 7. The four steps of program design*

Drawing a flowchart (Section 1) in step 2 reveals the places where decisions are needed, that is, where conditional statements go, as diamonds. In step 4, inputs for which the condition is true, inputs for which it is false, and inputs at the boundary, such as `money == total`, must all be tried. A problem that applies this whole process is [Exercise 8](Exercises.md#exercise-8-automatic-coffee-ordering-machine).

---

<br>

## Concept Applications

**True/False Check:**

| Statement | Judgment and Reason |
|:-----|:-----|
| `if x = 10:` is a correct conditional statement that tests whether `x` is 10. | **F.** `=` is the assignment operator, so this is a syntax error. To test equality, use `==`. |
| `x and y` is true if even one of `x` and `y` is true. | **F.** `and` is true only when both are true. The operator that is true if even one is true is `or`. |
| In an `if-elif-else` statement, if several conditions are true, all the true blocks are executed. | **F.** The conditions are checked from the top, and only the block of the first true condition is executed. |
| In Python, indentation is part of the syntax. | **T.** Python marks blocks with indentation, so changing the indentation causes an error or changes the meaning of the program. |
| `random.randint(1, 10)` can return 10. | **T.** `randint(a, b)` chooses an integer from a range that includes both a and b. |
| `random.randrange(1, 10)` can return 10. | **F.** `randrange(a, b)` excludes b, so it returns one of 1-9. |
| An `if` statement must always have an `else` clause. | **F.** The `else` clause can be omitted; if it is omitted, nothing is done when the condition is false. |
| The value of `0 and 5` is `False`. | **F.** `and` returns the left operand as it is when the left side is false, so the value is 0. 0 is judged false in a condition. |
| With `x = 5`, the block of `if x == 1 or 2:` is not executed. | **F.** The value of `(x == 1) or 2` is 2, and 2 is true, so the block runs. It must be written `x == 1 or x == 2`. |
| The value of `"10" < "9"` is `True`. | **T.** Strings are compared lexicographically from the first character, and the number of `1`, 49, is smaller than that of `9`, 57. |
| `not (a > 0 and b > 0)` is the same as `a <= 0 and b <= 0`. | **F.** By De Morgan's laws, it is the same as `a <= 0 or b <= 0`. |

---

<br>

## Summary

| Concept | Key Summary |
|:-----|:-----|
| Basic control structures | There are three structures, sequence, selection, and iteration, and conditional statements create selection structures. |
| Boolean type | Has the two values `True` and `False`; in conditions, 0, the empty string, and the empty list are judged false. |
| Relational operators | `==`, `!=`, `>`, `<`, `>=`, and `<=` compare two values and return `True` or `False`. |
| Logical operators | `and` is true when all are true, `or` is true when at least one is true, `not` flips true and false, and they are computed in the order `not`, `and`, `or`. |
| Short-circuit evaluation and its result | `and` and `or` skip the right side once the result is determined, and return one of the operands as it is rather than `True` or `False`. |
| Chained comparisons | `a < b < c` is the same as `a < b and b < c`, with the middle value evaluated only once. |
| String comparison | Follows lexicographic order, comparing Unicode numbers from the first character, so `"10" < "9"` is true; convert first to compare as numbers. |
| `if-else` statement | A colon follows the condition; the then clause is executed if it is true, and the else clause if it is not. |
| Blocks and indentation | Statements indented by the same number of columns form one block, and wrong indentation raises an `IndentationError`. |
| `if-elif-else` statement | Conditions are checked from the top and only the block of the first true one is executed, so the order of conditions matters. |
| Conditional expression | `A if condition else B` is an expression that evaluates only the side chosen by the condition to produce a value, and its `else` cannot be omitted. |
| Complete and nonoverlapping conditions | Trace with boundary and out-of-range values to check that every input falls into exactly one block, and filter invalid input at the very top. |
| Nested `if` statements | An `if` statement is placed inside another; the `if` that an `else` pairs with is determined by indentation, and they can be rewritten with conditions combined by `and`. |
| Negating conditions | `not (A and B)` is `(not A) or (not B)`, so when negating each condition, also swap `and` and `or`, and check the results with boundary values. |
| `random` module | `randrange()` excludes the end value, `randint()` includes it, and `choice()` picks one element of a list. |
| Program design | Proceeds in the order of problem analysis, deciding the processing order, deciding the variables, and programming, and tests inputs at the boundary as well. |

---

<br>

## Self-Check Questions

1. **Values of conditions:** If `x = 7`, write the values of `x > 5 and x < 10`, `x % 2 == 0 or x > 10`, and `not (x == 7)`.

   <details>
   <summary>Answer</summary>

   They are `True`, `False`, and `False`, in that order. The first is true because both `7 > 5` and `7 < 10` are true. The second is false because `7 % 2` is 1, making `x % 2 == 0` false, and `x > 10` is also false. The third is false because `x == 7` is true and `not` is applied to it.

   </details>

2. **if versus elif:** If `score = 95`, write the output of each of the following two pieces of code and explain why they differ.

   ```python
   # (a)
   if score >= 90:
       print("A")
   if score >= 80:
       print("B")

   # (b)
   if score >= 90:
       print("A")
   elif score >= 80:
       print("B")
   ```

   <details>
   <summary>Answer</summary>

   (a) prints `A` and `B` on two lines, and (b) prints only `A`. The two `if` statements of (a) are independent, so both conditions are checked, and 95 satisfies both. (b) is a single `if-elif` statement, so only the block of `score >= 90`, the first true condition, is executed and the condition of `elif` is not checked.

   </details>

3. **Rewriting nested if statements:** Rewrite the nested `if` statements of Section 6.1 as an `if-elif-else` statement with the same results.

   <details>
   <summary>Answer</summary>

   It is the same as the code in Section 5.1. Positive is printed at `if num > 0:`, zero at `elif num == 0:`, and negative at `else:`. Combining the outer condition `num >= 0` and the inner condition `num == 0` of the nested form, a positive number is the case where `num >= 0` is true and `num == 0` is false, that is, the case `num > 0`.

   </details>

4. **Indentation:** What is printed when the following code is run with `score = 80`? How should it be fixed so that the second `print()` runs only when `score` is greater than 90?

   ```python
   if score > 90:
       print("합격입니다.")
   print("장학금도 받을 수 있습니다.")
   ```

   <details>
   <summary>Answer</summary>

   Only `장학금도 받을 수 있습니다.` is printed. The second `print()` is not indented, so it is a statement outside the `if` statement and is executed regardless of the condition. Indenting it by the same number of columns as the first `print()` puts it in the same block, so it runs only when the condition is true.

   </details>

5. **Range of random numbers:** You want to generate the face of a die (1-6). Which is suitable, `random.randint(1, 6)` or `random.randrange(1, 6)`?

   <details>
   <summary>Answer</summary>

   `random.randint(1, 6)`. `randint(a, b)` includes both a and b, so it returns one of 1-6. `randrange(1, 6)` excludes the end value 6, so 6 never appears. To produce the same range with `randrange()`, write `random.randrange(1, 7)`.

   </details>

6. **Values of and and or:** Give the values of `0 or "기본값"`, `"a" and "b"`, `[] or [] and [1]`, and `not 0`.

   <details>
   <summary>Answer</summary>

   `0 or "기본값"` is the right side `'기본값'` because the left side 0 is false. `"a" and "b"` is the right side `'b'` because the left side is true. In `[] or [] and [1]`, `and` is evaluated first, giving `[] or ([] and [1])`; `[] and [1]` is `[]` because the left side `[]` is false, and then `[] or []` is the right side `[]`. `not 0` is `True`.

   </details>

7. **String comparison:** What does the following program print when `100` and `25` are entered? Fix it so that it compares the sizes of the numbers as intended.

   ```python
   a = input("첫 번째 수: ")
   b = input("두 번째 수: ")
   if a > b:
       print("첫 번째 수가 크다")
   else:
       print("두 번째 수가 크거나 같다")
   ```

   <details>
   <summary>Answer</summary>

   It prints `두 번째 수가 크거나 같다` (the second number is greater or equal). `a` and `b` are the strings `"100"` and `"25"`, and the first character `1` (49) is smaller than `2` (50), so `a > b` is false. Converting to integers, as in `a = int(input("첫 번째 수: "))` and `b = int(input("두 번째 수: "))`, makes 100 > 25 true, so `첫 번째 수가 크다` (the first number is greater) is printed.

   </details>

8. **Negating a condition:** Write the negation of the condition `score >= 60 and attend >= 10`, "pass if the score is 60 or more and attendance is 10 or more", without `not`, and find the values of both conditions when `score = 60` and `attend = 9`.

   <details>
   <summary>Answer</summary>

   By De Morgan's laws, it is `score < 60 or attend < 10`. With `score = 60` and `attend = 9`, the original condition is `True and False`, which is `False`, and the negated condition is `False or True`, which is `True`. The two values are opposite, so the negation is correct.

   </details>

---

<br>

## References

1. C. Böhm and G. Jacopini, "Flow diagrams, Turing machines and languages with only two formation rules," *Communications of the ACM*, vol. 9, no. 5, pp. 366-371, 1966.
2. Python Software Foundation, "Built-in Types," *The Python Standard Library*. https://docs.python.org/3/library/stdtypes.html
3. Python Software Foundation, "Expressions," *The Python Language Reference*. https://docs.python.org/3/reference/expressions.html
4. Python Software Foundation, "Compound Statements," *The Python Language Reference*. https://docs.python.org/3/reference/compound_stmts.html
5. Python Software Foundation, "Lexical Analysis," *The Python Language Reference*. https://docs.python.org/3/reference/lexical_analysis.html
6. G. van Rossum, B. Warsaw, and A. Coghlan, "PEP 8: Style Guide for Python Code," 2001. https://peps.python.org/pep-0008/
7. Python Software Foundation, "What's New In Python 3.10," *Python 3 Documentation*, accessed Nov. 19, 2026. https://docs.python.org/3/whatsnew/3.10.html
8. Python Software Foundation, "random: Generate Pseudo-Random Numbers," *The Python Standard Library*. https://docs.python.org/3/library/random.html
