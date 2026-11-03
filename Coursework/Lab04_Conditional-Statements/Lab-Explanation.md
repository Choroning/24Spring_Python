# Lab 4 Explanation — Conditional Statements

[Repository Guide](../../README.md) | [English](Lab-Explanation.md) | [한국어](Lab-Explanation.ko.md)

> **Last Updated:** 2026-11-04

> **Learning Objectives:**
> 1. Use an `if-else` statement to run one of two blocks depending on whether a condition is true or false
> 2. Combine several conditions into one condition with the logical operators `and` and `or`
> 3. Rewrite a condition combined with logical operators as nested `if` statements with the same behavior
> 4. Distinguish three or more cases with an `if-elif-else` statement
> 5. Use a random number produced by the `random` module as the operand of a condition

---

## Table of Contents

- [1. Lab Layout and How to Run](#1-lab-layout-and-how-to-run)
- [2. The if-else Statement](#2-the-if-else-statement)
  - [2.1 Pass or Fail](#21-pass-or-fail)
  - [2.2 Several Statements in a Block](#22-several-statements-in-a-block)
- [3. Combining Conditions](#3-combining-conditions)
  - [3.1 Two Conditions Joined by and](#31-two-conditions-joined-by-and)
  - [3.2 Threshold Variables and Nested if Statements](#32-threshold-variables-and-nested-if-statements)
  - [3.3 Subject Cutoff Check](#33-subject-cutoff-check)
- [4. Random Numbers and Conditional Statements](#4-random-numbers-and-conditional-statements)
  - [4.1 Coin Toss Game](#41-coin-toss-game)
  - [4.2 Number Guessing](#42-number-guessing)
- [Summary](#summary)
- [Self-Check Questions](#self-check-questions)

---

<br>

## 1. Lab Layout and How to Run

This code was written while following [Lecture 4, Conditional Statements](../../Lecture-Notes/Lec04_Conditional-Statements/Concepts_Lecture.md). Section 2 covers the basic form of the `if-else` statement, Section 3 covers combining conditions with `and` and `or` and nested `if` statements, and Section 4 covers conditional statements that compare against a random number from the `random` module.

```text
Coursework/Lab04_Conditional-Statements/
├── Lab-Explanation.ko.md     # This document (Korean)
├── Lab-Explanation.md        # This document (English)
├── Lab_PassFail.py           # 2.1 Pass or fail
├── Lab_Scholarship.py        # 2.2 Several statements in a block
├── Lab_AgeHeightCheck.py     # 3.1 Two conditions joined by and
├── Lab_NestedCondition.py    # 3.2 Threshold variables and nested if
├── Lab_SubjectCutoff.py      # 3.3 Subject cutoff check
├── Lab_CoinToss.py           # 4.1 Coin toss game
└── Lab_NumberGuess.py        # 4.2 Number guessing
```

*Figure 1. Directory layout of Lab 4*

All programs use only the standard library and run as they are under Python 3. Each file begins with a documentation string (docstring) that records the file name, a one-line description, the author, and the date written, and the code blocks in this document omit that part.

```bash
cd Coursework/Lab04_Conditional-Statements
python3 Lab_PassFail.py
```

---

<br>

## 2. The if-else Statement

### 2.1 Pass or Fail

**Code:** [Lab_PassFail.py](Lab_PassFail.py)

```python
score = float(input("점수를 입력하세요: "))

if score >= 60 :
    print("합격입니다.")

# if (score >= 60) :
# 괄호 삽입 가능

else :
    print("불합격입니다.")
```

- **Input:** `input()` always returns what the user typed as a string. Comparing scores by size requires numbers, so `float()` converts the input to a real number, which is stored in `score`. A score with a decimal point such as `75.5` is also accepted.
- **Condition:** `score >= 60` is a condition whose value is `True` or `False` as the result of the comparison operator `>=`. If it is true, the block under `if` runs, and if it is false, the block under `else` runs.
- **Block:** The statements indented to the same depth from the line after the colon (`:`) form one block. Python separates blocks by indentation instead of braces.
- **Position of the comment:** The blank lines and comments between the `if` block and `else` do not affect execution, so `else` still pairs with the preceding `if`. The comment (Korean: "parentheses can be inserted") records that the condition may be wrapped in parentheses as `(score >= 60)`.

**Output:** Two runs with inputs 75 and 45. An input of 60 is judged a pass because the operator is `>=`.

```text
점수를 입력하세요: 75
합격입니다.
```

```text
점수를 입력하세요: 45
불합격입니다.
```

> **Caution:** Entering a string that cannot be converted to a number, such as `abc`, makes `float()` raise a `ValueError` and stops the program. Exception handling for input errors is outside the scope of this lab.

### 2.2 Several Statements in a Block

**Code:** [Lab_Scholarship.py](Lab_Scholarship.py)

```python
score = float(input("점수를 입력하세요."))

if score > 90 :
    print("합격입니다.")
    print("장학금도 받을 수 있습니다.")

else :
    print("에휴")
```

- **A block of several statements:** The `if` block holds two `print()` calls with the same indentation, so both run in order when the condition is true. A statement with different indentation does not belong to the block.
- **Boundary value:** Because the condition is `score > 90`, a score of 90 is false and goes to the `else` block. To make 90 points eligible for the scholarship, `>=` must be used.
- **Prompt:** The prompt string ends with a period and no space, so the entered value appears right after the period.

**Output:** Two runs with inputs 95 and 80. The outputs mean "You passed.", "You can also receive a scholarship.", and a sigh.

```text
점수를 입력하세요.95
합격입니다.
장학금도 받을 수 있습니다.
```

```text
점수를 입력하세요.80
에휴
```

---

<br>

## 3. Combining Conditions

### 3.1 Two Conditions Joined by and

**Code:** [Lab_AgeHeightCheck.py](Lab_AgeHeightCheck.py)

```python
a = int(input("a: "))
h = float(input("h: "))

if a  >= 10 and h >= 165 :
    print("ok")

else :
    print("no")

# 10과 165를 변수에 담아서 if문에서 대치 가능
# if문 속에 다시 if문이 종속될 수 있음
#   ㄴ if( if( ~ ) else( ~ ) ) else ( ~ ) 구조
```

- **Input:** The age `a` is converted to an integer with `int()`, and the height `h` to a real number with `float()`.
- **The `and` operator:** `a >= 10 and h >= 165` is true only when both comparisons are true. Comparison operators are evaluated before logical operators, so without parentheses it means the same as `(a >= 10) and (h >= 165)`.
- **Short-circuit evaluation:** If the left operand of `and` is false, the result is already false, so the right comparison is not evaluated.
- **Comments:** The comments at the end note that the thresholds 10 and 165 can be stored in variables and that an `if` statement can be placed inside another `if` statement, and the program in Section 3.2 implements both.

**Output:** With age 12 and height 170 both conditions are true, and with age 9 the first condition is false.

```text
a: 12
h: 170
ok
```

```text
a: 9
h: 170
no
```

### 3.2 Threshold Variables and Nested if Statements

**Code:** [Lab_NestedCondition.py](Lab_NestedCondition.py)

```python
a=int(input("a:"))
a_th=10
h=float(input("h"))
h_th=165

if ((a>=a_th) and (h>=h_th)) :
    print("ok")
else :
    print("no")

if (a>=a_th) :
    if (h>=h_th) :
        print("ok")
    else :
        print("no")
else :
    print("no")
```

- **Threshold variables:** Keeping the thresholds in `a_th` and `h_th` means that only one assignment has to change when a threshold changes. The `th` in the names stands for threshold.
- **First `if`:** The same `and` condition as in Section 3.1, with each comparison wrapped in parentheses to make the order of evaluation visible.
- **Second `if` (nested `if` statement):** The outer `if` checks the age, and the inner `if` checks the height. The inner `if` runs only when the outer condition is true, so `ok` is printed only when both conditions are true. If the outer condition is false, the outer `else` prints `no`, and if the outer condition is true but the inner one is false, the inner `else` prints `no`.
- **Relation between the two structures:** The two `if` statements give the same result for every input, so each run prints the same word twice. The single `and` line is concise, and the nested structure makes it easy to handle each failed condition differently.

**Output:** Two runs, with age 12 and height 170, and with age 12 and height 150. The second prompt `h` has no colon or space, so the input follows it directly.

```text
a:12
h170
ok
ok
```

```text
a:12
h150
no
no
```

### 3.3 Subject Cutoff Check

**Code:** [Lab_SubjectCutoff.py](Lab_SubjectCutoff.py)

```python
kor = int(input("국어 점수: "))
eng = int(input("영어 점수: "))
his = int(input("한국사 점수: "))
se1 = int(input("선택과목1 점수: "))
se2 = int(input("선택과목2 점수: "))
ave = (kor + eng + his + se1 + se2) / 5

if (kor < 40 or eng < 40 or his < 40 or se1 < 40 or se2 < 40):  #조건 뒤집어서 and 사용도 가능
   print("과락")
else:
   print("과락 아님")
print("평균 점수: %f" %ave)

#아니면 int(input(~)) 하나마다 if문으로 판별할수도 있음

#if (kor < 40):
#    print("과락")
#else:
#    if (eng < 40):
#        print("과락")
#    else:
#        if (his < 40):
#            print("과락")
#        else:
#            if (se1 < 40):
#                print("과락")
#            else:
#                if (se2 < 40):
#                    print("과락")
#                else:
#                    print("과락 아님")
#print("평균 점수: %f" %ave)
```

- **Problem:** Read the scores of five subjects (Korean, English, Korean history, and two electives), judge a cutoff failure (과락) if any subject is below 40 and no cutoff failure (과락 아님) otherwise, and print the average of the five subjects.
- **The `or` operator:** The whole condition is true if any of the five comparisons joined by `or` is true. Evaluation proceeds from the left, and once a true comparison is met the rest are not evaluated.
- **Rewriting with `and`:** As the comment notes, the condition may be inverted so that no cutoff failure is judged when `kor >= 40 and eng >= 40 and his >= 40 and se1 >= 40 and se2 >= 40` is true. By De Morgan's law, `not (A or B)` equals `(not A) and (not B)`, and the negation of `x < 40` is `x >= 40`.
- **Average:** `/` returns a real number even when both operands are integers, so `ave` is a real number. The format specifier `%f` prints six digits after the decimal point.
- **Commented-out nested structure:** The comments below show the same check written as one nested `if` statement per subject. The result is the same, but the indentation deepens as subjects are added, so the single `or` line is easier to read.

**Output:** The first run has every subject at 40 or above, and the second run has English at 35.

```text
국어 점수: 50
영어 점수: 60
한국사 점수: 70
선택과목1 점수: 58
선택과목2 점수: 63
과락 아님
평균 점수: 60.200000
```

```text
국어 점수: 50
영어 점수: 35
한국사 점수: 70
선택과목1 점수: 58
선택과목2 점수: 63
과락
평균 점수: 55.200000
```

The average in the first run is $(50 + 60 + 70 + 58 + 63) / 5 = 301 / 5 = 60.2$, and in the second run $(50 + 35 + 70 + 58 + 63) / 5 = 276 / 5 = 55.2$.

---

<br>

## 4. Random Numbers and Conditional Statements

### 4.1 Coin Toss Game

**Code:** [Lab_CoinToss.py](Lab_CoinToss.py)

```python
import random

print("동전 던지기 게임을 시작합니다.")
coin = random.randrange(2)

answer = int(input("나온 숫자는 0과 1 중 무엇일까요?"))

if answer == coin :
             print("맞았습니다.")
else :
    print("틀렸습니다.")

print("게임이 종료되었습니다.")
```

- **The `random` module:** `import random` loads the standard module that holds the random number functions. `random.randrange(2)` returns an integer from 0 up to but not including 2, that is, 0 or 1 with equal probability. The values 0 and 1 stand for the two sides of a coin.
- **Comparison:** The input is converted to an integer with `int()` and then compared with `coin` using `==`. The string `"1"` and the integer `1` are not equal, so without the conversion every guess would be judged wrong.
- **Depth of indentation:** The `print()` in the `if` block is indented by 13 spaces and the `print()` in the `else` block by 4 spaces. Only the statements within one block need the same indentation, so different depths in the two blocks are not a syntax error. For readability, however, one level of indentation is usually unified to 4 spaces.
- **The last `print()`:** It is not indented, so it lies outside the `if-else` statement and runs regardless of the result.

**Output:** Examples with input 1. The first result appears if `coin` was 1, and the second if it was 0. The program announces the start, asks which number came up, prints "Correct." or "Wrong.", and announces the end.

```text
동전 던지기 게임을 시작합니다.
나온 숫자는 0과 1 중 무엇일까요?1
맞았습니다.
게임이 종료되었습니다.
```

```text
동전 던지기 게임을 시작합니다.
나온 숫자는 0과 1 중 무엇일까요?1
틀렸습니다.
게임이 종료되었습니다.
```

### 4.2 Number Guessing

**Code:** [Lab_NumberGuess.py](Lab_NumberGuess.py)

```python
import random
val = random.randint(1,10)
guess = int(input("정수를 입력하시오(0~10): "))

if guess > val:  #조건식 괄호의 삽입여부는 상관없음
    print("입력한 값보다 작습니다.")
elif guess < val:
    print("입력한 값보다 큽니다.")
else:
    print("정답입니다.")
#print("답은" + str(val) + "입니다.")
#print("답은 %s입니다." %val)
print("답은 %d입니다." %val)
```

- **`random.randint(a, b)`:** Returns an integer from `a` to `b` inclusive. Unlike `randrange()`, it includes the end value `b`, so `val` is one of 1-10. The prompt says 0-10, but 0 can never be the answer.
- **`if-elif-else`:** The conditions are checked from the top, and only the first block whose condition is true runs. If the input is greater than the answer, the program prints a message meaning "the answer is smaller than your input", and if it is smaller, a message meaning "larger". If both conditions are false, then `guess == val`, so `else` judges it correct.
- **Printing the answer:** The last line reveals the answer regardless of the result. The two commented-out lines build the same sentence with string concatenation (`+` and `str()`) and with the format specifier `%s`, and `%d` is the format specifier that inserts an integer in decimal.

**Output:** An example with input 5 when `val` was 7. The output means "The answer is larger than your input." and "The answer is 7."

```text
정수를 입력하시오(0~10): 5
입력한 값보다 큽니다.
답은 7입니다.
```

> **Note:** This program compares only once and ends. To ask again until the answer is guessed, the input and comparison must be wrapped in the `while` statement of Lecture 5.

---

<br>

## Summary

| Concept | Key Summary |
|:-----|:-----|
| `if-else` statement | Runs the `if` block if the condition is true and the `else` block if it is false, and a block is the statements indented to the same depth from the line after the colon. |
| Converting input | `input()` returns a string, so it is converted with `int()` or `float()` before numeric comparison. |
| Boundary values | `>` and `>=` differ in whether the boundary value itself is included, so the threshold itself should be tried as an input. |
| `and` and `or` | `and` is true when all conditions are true and `or` when any one is true, and the remaining conditions are not evaluated once the result is determined. |
| Nested `if` statements | A condition joined by `and` can be split into an outer `if` and an inner `if`, which makes it easy to handle each failed condition differently. |
| `if-elif-else` statement | Checks the conditions from the top, runs only the first block whose condition is true, and runs the `else` block if all are false. |
| Random numbers | `random.randrange(n)` returns an integer from 0 to n-1, and `random.randint(a, b)` an integer from a to b. |

---

<br>

## Self-Check Questions

1. **Boundary value:** What does `Lab_Scholarship.py` print for an input of 90? What must change to make 90 points eligible for the scholarship as well?

   <details>
   <summary>Answer</summary>

   With the condition `score > 90`, 90 is false, so the `else` block runs and prints `에휴`. Changing the condition to `score >= 90` makes 90 points print `합격입니다.` and `장학금도 받을 수 있습니다.` as well.

   </details>

2. **Rewriting nested if statements:** Rewrite the following conditional statement as a single `if-else` statement that uses `and`.

   ```python
   if x > 0:
       if y > 0:
           print("1사분면")
       else:
           print("아님")
   else:
       print("아님")
   ```

   <details>
   <summary>Answer</summary>

   Put `print("1사분면")` under `if x > 0 and y > 0:` and `print("아님")` under `else:`. `1사분면` (first quadrant) is printed only when both the outer and inner conditions are true and `아님` (not) in every other case, which is the same as joining the two conditions with `and`.

   </details>

3. **De Morgan's law:** Rewrite the condition of `Lab_SubjectCutoff.py` with `and` so that it judges "no cutoff failure".

   <details>
   <summary>Answer</summary>

   It is `kor >= 40 and eng >= 40 and his >= 40 and se1 >= 40 and se2 >= 40`. If this expression is true the program prints `과락 아님`, and otherwise `과락`. Each comparison is negated and `or` is replaced with `and`.

   </details>

4. **Range of random numbers:** List all values that `random.randrange(2)` and `random.randint(1, 10)` can return.

   <details>
   <summary>Answer</summary>

   `random.randrange(2)` does not include the end value 2, so it returns 0 and 1. `random.randint(1, 10)` includes the end value, so it returns 1, 2, 3, 4, 5, 6, 7, 8, 9, and 10.

   </details>

5. **Order of elif:** In `Lab_NumberGuess.py`, which block runs when `val` is 3 and the input is 4? Does the result change if `elif` is replaced with `if`?

   <details>
   <summary>Answer</summary>

   `4 > 3` is true, so the first block runs and prints `입력한 값보다 작습니다.`, and the remaining conditions are not checked. If `elif` is replaced with `if`, there are two separate statements, `if` and `if-else`, so the condition of the second `if`, `4 < 3`, is false and its `else` block also prints `정답입니다.`.

   </details>
