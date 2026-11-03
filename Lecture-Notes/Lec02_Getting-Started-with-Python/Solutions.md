# Lecture 2 Solutions — Getting Started with Python

[Repository Guide](../../README.md) | [English](Solutions.md) | [한국어](Solutions.ko.md)

> **Last Updated:** 2026-11-04

---

<br>

## Table of Contents

- [Exercise 1: Practicing the `print()` Function](#exercise-1-practicing-the-print-function)
- [Exercise 2: Robot Reporter](#exercise-2-robot-reporter)
- [Exercise 3: Coffee Shop Sales](#exercise-3-coffee-shop-sales)
- [Exercise 4: Vending Machine](#exercise-4-vending-machine)
- [Exercise 5: Computing an Average](#exercise-5-computing-an-average)
- [Exercise 6: Greeting and the Sum of Two Integers](#exercise-6-greeting-and-the-sum-of-two-integers)
- [Exercise 7: Four Arithmetic Operations on Two Integers](#exercise-7-four-arithmetic-operations-on-two-integers)
- [Exercise 8: Sum of Digits](#exercise-8-sum-of-digits)

---

<br>

## Exercise 1: Practicing the `print()` Function

**Problem:** Print four lines of greetings, letting Python calculate `9*8` for the 72 on the third line. The full problem and sample run are in [Exercise 1](Exercises.md#exercise-1-practicing-the-print-function).

### Solution

**Approach:** Call `print()` once for each line to be printed. `print()` moves to a new line after printing the values it receives, so calling it four times prints four lines ([Lecture 2, Section 4.2](Concepts_Lecture.md#42-the-print-function)).

- **Lines 1, 2, and 4:** The string inside the double quotation marks is printed as is, one line each. The `?` and `.` inside the strings are also part of the characters.
- **Line 3:** `print("9*8은", 9*8, "입니다.")` has three arguments. The first argument `"9*8은"` is a string inside quotation marks, so it is not calculated, and the second argument `9*8` is an expression outside quotation marks, so it is calculated to 72. `print()` puts one space between each pair of the three values and prints `9*8은 72 입니다.`.

**Code:**

```python
print("안녕하세요? 여러분")
print("저는 파이썬을 무척 좋아합니다.")
print("9*8은", 9*8, "입니다.")
print("안녕히 계세요.")
```

**Output:**

```text
안녕하세요? 여러분
저는 파이썬을 무척 좋아합니다.
9*8은 72 입니다.
안녕히 계세요.
```

> **Note:** Writing the third line as `print("9*8은 72 입니다.")` gives the same result, but then 72 is merely text that a person calculated and typed in. When the expression is passed as an argument, changing `9*8` to `7*8` automatically changes the printed value to 56 as well.

---

<br>

## Exercise 2: Robot Reporter

**Problem:** Read the stadium, the winning team, the losing team, the best player, and the score, store them in variables, and print a baseball game article that includes them. The full problem and sample run are in [Exercise 2](Exercises.md#exercise-2-robot-reporter).

### Solution

**Approach:** The input consists of five strings, so the results of `input()` are stored as they are in five variables (`stadium`, `winner`, `loser`, `vip`, and `score`) ([Lecture 2, Section 9.2](Concepts_Lecture.md#92-string-input)). The score `8:7` is not used in any calculation, so it is not converted with `int()` and is kept as a string. The output is made by passing variables and fixed strings, mixed and separated by commas, to `print()`.

- **Lines 1 and 8:** Comments starting with `#`. They explain what the input part and the output part do and do not affect the result.
- **Lines 2-6:** Print each question and store the user's answer in a variable. A space at the end of each question keeps the typed text from sticking to the question mark.
- **Line 9:** `print("")` prints an empty string and moves to a new line, producing one empty line. Writing `print()` with no argument does the same.
- **Lines 10 and 15:** Print a string of `=` characters to make separator lines above and below the article.
- **Lines 11-14:** For example, line 11 joins the three values `"오늘"` (today), the value of `stadium` `"서울"`, and `"에서 야구 경기가 열렸습니다."` (a baseball game was held in) with spaces and prints `오늘 서울 에서 야구 경기가 열렸습니다.`.

**Code:**

```python
# Store the user's answers in variables.
stadium = input("경기장은 어디입니까? ")
winner = input("이긴 팀은 어디입니까? ")
loser = input("진 팀은 어디입니까? ")
vip = input("우수 선수는 누구입니까? ")
score = input("스코어는 몇 대 몇입니까? ")

# Combine the variables with fixed text to write the article.
print("")
print("===========================================")
print("오늘", stadium, "에서 야구 경기가 열렸습니다.")
print(winner, "과", loser, "은 치열한 공방전을 펼쳤습니다.")
print(vip, "이 맹활약을 하였습니다.")
print("결국", winner, "가", loser, "를", score, "로 이겼습니다.")
print("===========================================")
```

**Output:**

```text
경기장은 어디입니까? 서울
이긴 팀은 어디입니까? 삼성
진 팀은 어디입니까? LG
우수 선수는 누구입니까? 홍길동
스코어는 몇 대 몇입니까? 8:7

===========================================
오늘 서울 에서 야구 경기가 열렸습니다.
삼성 과 LG 은 치열한 공방전을 펼쳤습니다.
홍길동 이 맹활약을 하였습니다.
결국 삼성 가 LG 를 8:7 로 이겼습니다.
===========================================
```

> **Note:** The article sentences have two awkward points. First, `print()` puts a space between values, so a space appears between a name and the Korean particle after it, as in `서울 에서`. Second, the particles are fixed in the code and do not change to fit the preceding word. A Korean particle takes a different form depending on whether the last syllable of the preceding word ends in a consonant (`과` and `와`, `은` and `는`, `이` and `가`, `을` and `를`), so `삼성 가` should be `삼성이` and `LG 은` should be `LG는` to read naturally. Joining strings without spaces is covered in Lecture 3, and choosing a different particle depending on a condition in Lecture 4.

---

<br>

## Exercise 3: Coffee Shop Sales

**Problem:** With an Americano at 2,000 won, a cafe latte at 3,000 won, and a cappuccino at 3,500 won, read the number sold for each menu item and print the total sales. The full problem and sample run are in [Exercise 3](Exercises.md#exercise-3-coffee-shop-sales).

### Solution

**Approach:** The total sales are the sum, over all menu items, of (number sold × price). The prices do not change, so they are stored in variables at the beginning of the program, and the numbers sold are read as integers with `int(input())` ([Lecture 2, Section 9.1](Concepts_Lecture.md#91-integer-input-input-and-int)).

- **Lines 1-3:** Store the price of each menu item in a variable. If a price changes, only these three lines need to be edited.
- **Lines 5-7:** Read the numbers sold and convert them to integers. Without `int()`, the numbers sold would be strings, so `*` would mean string repetition instead of multiplication and `+` would mean string concatenation, and a long string of more than ten thousand characters such as `1010101010...` would be printed without any error.
- **Lines 9-11:** Add the sales of each menu item to `sales` one after another. On the right sides of lines 10 and 11, multiplication is calculated before addition, so no parentheses are needed.
- **Line 12:** Prints the total sales.

**Code:**

```python
americano_price = 2000
cafelatte_price = 3000
cappuccino_price = 3500

americanos = int(input("아메리카노 판매 개수: "))
cafelattes = int(input("카페라떼 판매 개수: "))
cappuccinos = int(input("카푸치노 판매 개수: "))

sales = americanos * americano_price
sales = sales + cafelattes * cafelatte_price
sales = sales + cappuccinos * cappuccino_price
print("총 매출은", sales, "입니다.")
```

When 10, 20, and 30 are entered, the value of `sales` changes as follows.

| Line | Calculation | Value of `sales` |
|:-----|:-----|:-----|
| 9 | 10 × 2000 = 20000 | 20000 |
| 10 | 20000 + 20 × 3000 = 20000 + 60000 | 80000 |
| 11 | 80000 + 30 × 3500 = 80000 + 105000 | 185000 |

*Table 1. Changes in `sales` when 10, 20, and 30 are entered*

**Output:**

```text
아메리카노 판매 개수: 10
카페라떼 판매 개수: 20
카푸치노 판매 개수: 30
총 매출은 185000 입니다.
```

> **Note:** Lines 10 and 11 can also be written with compound assignment operators, as in `sales += cafelattes * cafelatte_price` and `sales += cappuccinos * cappuccino_price` ([Lecture 2, Section 11.2](Concepts_Lecture.md#112-compound-assignment-operators)). Calculating in one statement, as in `sales = americanos * americano_price + cafelattes * cafelatte_price + cappuccinos * cappuccino_price`, also gives the same result.

---

<br>

## Exercise 4: Vending Machine

**Problem:** Read the money inserted and the price of the item, and print the change and the numbers of 500-won and 100-won coins given as change. The full problem and sample run are in [Exercise 4](Exercises.md#exercise-4-vending-machine).

### Solution

**Approach:** The change is the money inserted minus the price. The number of 500-won coins is the quotient of the change divided by 500, and the amount left after giving 500-won coins is the remainder of that division. The quotient of the remaining amount divided by 100 is the number of 100-won coins ([Lecture 2, Section 10](Concepts_Lecture.md#10-uses-of-the-remainder-operator)). Inserting 5000 won and buying an item that costs 2600 won gives the following.

1. Change: 5000 - 2600 = 2400
2. 500-won coins: 2400 // 500 = 4 (2000 won)
3. Remaining amount: 2400 % 500 = 400
4. 100-won coins: 400 // 100 = 4 (400 won)

As a check, 4 × 500 + 4 × 100 = 2400.

**Code:**

```python
money = int(input("투입한 돈: "))
price = int(input("물건값: "))

change = money - price
print("거스름돈:", change)
coin500s = change // 500    # the quotient by 500 is the number of 500-won coins
change = change % 500       # compute the remainder after dividing by 500
coin100s = change // 100    # the quotient by 100 is the number of 100-won coins

print("500원 동전의 개수:", coin500s)
print("100원 동전의 개수:", coin100s)
```

- **Lines 4-5:** Calculate the change, store it in `change`, and print it.
- **Line 6:** Stores 2400 // 500 = 4 in `coin500s`.
- **Line 7:** Stores 2400 % 500 = 400 back in `change`. Assigning a new value to the same variable discards the previous value 2400, so line 5, which prints the whole change, must come before this line.
- **Line 8:** Stores 400 // 100 = 4 in `coin100s`.

**Output:**

```text
투입한 돈: 5000
물건값: 2600
거스름돈: 2400
500원 동전의 개수: 4
100원 동전의 개수: 4
```

> **Caution:** This program is correct only when the assumptions of the problem hold. If the price is not a multiple of 100 won, for example 2650 won, the program gives only 2300 won of the 2350 won change, as four 500-won coins and three 100-won coins, and does not return the 50 won. If the money inserted is less than the price, for example 1000 won for an item of 2600 won, the change is printed as -1600 and the coin counts become the meaningless values -4 and 4. Filtering out such input requires a conditional statement (Lecture 4).

---

<br>

## Exercise 5: Computing an Average

**Problem:** Find and correct the cause of a program that computes the average of three numbers with `avg = x + y + z / 3` and prints 40.0 for 10, 20, and 30. The full problem and code are in [Exercise 5](Exercises.md#exercise-5-computing-an-average).

### Solution

**Answer:** `avg = x + y + z / 3` on line 4 is wrong. Change it to `avg = (x + y + z) / 3`.

**Explanation:** Division `/` has higher precedence than addition `+` ([Lecture 2, Section 13.1](Concepts_Lecture.md#131-precedence-and-parentheses)), so the original expression divides only `z` by 3 instead of dividing the sum of the three numbers by 3.

- **Wrong expression:** `x + y + z / 3` is calculated as `x + y + (z / 3)`. 10 + 20 + (30 / 3) = 10 + 20 + 10.0 = 40.0.
- **Corrected expression:** `(x + y + z) / 3` performs the addition in the parentheses first, giving (10 + 20 + 30) / 3 = 60 / 3 = 20.0.

**Code:**

```python
x = int(input("첫 번째 수를 입력하시오: "))
y = int(input("두 번째 수를 입력하시오: "))
z = int(input("세 번째 수를 입력하시오: "))
avg = (x + y + z) / 3
print("평균 =", avg)
```

**Output:**

```text
첫 번째 수를 입력하시오: 10
두 번째 수를 입력하시오: 20
세 번째 수를 입력하시오: 30
평균 = 20.0
```

The average is printed as `20.0` rather than the integer 20 because `/` produces a floating-point result even when the division is exact. A mistake like this one, in which the program runs without a syntax error but produces a result different from what was intended, is called a **logic error**. Python gives no error message, so it must be found by comparing the result of running the program with a value calculated by hand.

---

<br>

## Exercise 6: Greeting and the Sum of Two Integers

**Problem:** Read the user's name and greet the user, then read two integers and print their sum. The full problem and sample run are in [Exercise 6](Exercises.md#exercise-6-greeting-and-the-sum-of-two-integers).

### Solution

**Problem Analysis:** Before writing the program, organize the input, the output, and the data needed.

- **Input:** The user's name and two integers
- **Output:** The name entered (in a greeting), and the integers entered and their sum
- **Data:** A variable representing the name, variables representing each number, and a variable representing the sum of the numbers

**Choosing Variables:** Choose one variable for each piece of data found in the analysis.

| Variable | Meaning | Data Type |
|:-----|:-----|:-----|
| `name` | The name entered | String |
| `n1` | The first number entered | Integer |
| `n2` | The second number entered | Integer |
| `Sum` | The sum of the numbers entered | Integer |

*Table 2. Variables used in Exercise 6*

**Programming:** Read input with the function `input()`, convert the integers with `int()`, and then calculate the sum of the two integers ([Lecture 2, Section 9](Concepts_Lecture.md#9-user-input)).

**Code:**

```python
name = input("이름을 입력하시오: ")
print(name, "씨, 안녕하세요?")
print("파이썬에 오신 것을 환영합니다.")
n1 = int(input("첫 번째 정수를 입력하시오: "))
n2 = int(input("두 번째 정수를 입력하시오: "))
Sum = n1 + n2
print(n1, "과", n2, "의 합은", Sum, "입니다.")
```

- **Lines 1-3:** Store the name as a string in `name` and print two lines of greeting that include the name.
- **Lines 4-5:** Read two integers, convert them with `int()`, and store them in `n1` and `n2`.
- **Lines 6-7:** Store the sum in `Sum` and print the two numbers and their sum as a sentence.

**Output:**

```text
이름을 입력하시오: 홍길동
홍길동 씨, 안녕하세요?
파이썬에 오신 것을 환영합니다.
첫 번째 정수를 입력하시오: 300
두 번째 정수를 입력하시오: 400
300 과 400 의 합은 700 입니다.
```

**Another Approach: Formatted String Literals.** The sentence on line 7 can also be built with a **formatted string literal (f-string)**. Putting `f` before the opening quotation mark of a string inserts the value of each variable at the `{variable}` positions inside the string.

```python
message = f"{n1} 과 {n2} 의 합은 {Sum} 입니다."
print(message)
```

```text
300 과 400 의 합은 700 입니다.
```

In a formatted string literal, spaces appear exactly as written in the string, so writing `f"{n1}과 {n2}의 합은 {Sum}입니다."` attaches the numbers and the text directly and prints `300과 400의 합은 700입니다.`. This cannot be done with `print()` and comma-separated values. String formatting is covered in Lecture 3.

> **Note:** Naming the variable that stores the sum `Sum` does not hide the name of the built-in function `sum()`, because Python distinguishes uppercase from lowercase ([Lecture 2, Section 9.1](Concepts_Lecture.md#91-integer-input-input-and-int)). However, PEP 8 recommends names starting with an uppercase letter for classes (Lecture 8) ([Lecture 2, Section 7.3](Concepts_Lecture.md#73-rules-for-variable-names)), so another lowercase name such as `total` follows the convention better for a variable.

---

<br>

## Exercise 7: Four Arithmetic Operations on Two Integers

**Problem:** Read two integers and print the results of addition, subtraction, multiplication, and division in the form `4 + 2 = 6`. The full problem and sample run are in [Exercise 7](Exercises.md#exercise-7-four-arithmetic-operations-on-two-integers).

### Solution

**Problem Analysis:**

- **Input:** Two integers
- **Output:** The sum, difference, product, and quotient of the integers entered
- **Data:** Variables representing each number and variables representing the result of each operation

**Choosing Variables:** `n1` is the first number entered and `n2` the second, and `S` is the sum of the two numbers, `M` the difference, `Mul` the product, and `Div` the result of the division.

**Programming:** Read input with the function `input()`, convert it to the integer type with `int()`, store the results of the four operations on the two integers in variables, and then print them ([Lecture 2, Section 8.2](Concepts_Lecture.md#82-arithmetic-operators)).

**Code:**

```python
n1 = int(input("첫 번째 정수를 입력하시오: "))
n2 = int(input("두 번째 정수를 입력하시오: "))
S = n1 + n2
M = n1 - n2
Mul = n1 * n2
Div = n1 / n2

print(n1, "+", n2, "=", S)
print(n1, "-", n2, "=", M)
print(n1, "*", n2, "=", Mul)
print(n1, "/", n2, "=", Div)
```

- **Lines 3-6:** Entering 4 and 2 makes `S` 6, `M` 2, `Mul` 8, and `Div` 2.0. `/` produces a floating-point result even when the division is exact, so only `Div` is printed as `2.0`.
- **Lines 8-11:** For example, line 8 joins the five values `n1`, `"+"`, `n2`, `"="`, and `S` with spaces and prints `4 + 2 = 6`. The operator symbols are inside quotation marks, so they are printed as characters, not calculated.

**Output:**

```text
첫 번째 정수를 입력하시오: 4
두 번째 정수를 입력하시오: 2
4 + 2 = 6
4 - 2 = 2
4 * 2 = 8
4 / 2 = 2.0
```

> **Caution:** Entering 0 as the second integer raises the error `ZeroDivisionError: division by zero` at `n1 / n2` on line 6, and the program stops. All the print statements come after line 6, so even the result of the addition is not printed. Checking in advance so as not to divide by 0 requires a conditional statement (Lecture 4). To print the quotient and remainder as well, add `print(n1, "//", n2, "=", n1 // n2)` and `print(n1, "%", n2, "=", n1 % n2)`.

---

<br>

## Exercise 8: Sum of Digits

**Problem:** Read an integer of at most four digits that is 0 or greater and print the sum of its digits (for example, 1 + 2 + 3 + 4 = 10 for 1234). The full problem and sample runs are in [Exercise 8](Exercises.md#exercise-8-sum-of-digits).

### Solution

**Problem Analysis:**

- **Input:** An integer of at most four digits
- **Output:** The sum of the digits of the integer entered
- **Data:** A variable representing the number, variables representing each digit, and a variable representing the sum of the digits

**Idea:** Treat the number entered as a four-digit number, and find the quotient by 1000 to get the thousands digit. Subtracting the thousands part and taking the quotient of what remains by 100 gives the hundreds digit; in the same way, the quotient by 10 gives the tens digit, and the number left at the end is the ones digit.

**Choosing Variables:** `n` is the number entered, `R` is the value remaining after the higher digits are removed, `S1`, `S2`, `S3`, and `S4` are the thousands, hundreds, tens, and ones digits, and `Sum` is the sum of the digits.

**Code:**

```python
n = int(input("네 자리 이하의 정수를 입력하시오: "))
S1 = n // 1000
R = n - (1000 * S1)
S2 = R // 100
R = R - (100 * S2)
S3 = R // 10
R = R - (10 * S3)
S4 = R
Sum = S1 + S2 + S3 + S4
print("자릿수의 합=%s" % Sum)
```

When 1234 is entered, the values of the variables change as follows.

| Line | Statement | Calculation | Result |
|:-----|:-----|:-----|:-----|
| 2 | `S1 = n // 1000` | 1234 // 1000 | `S1` = 1 |
| 3 | `R = n - (1000 * S1)` | 1234 - 1000 | `R` = 234 |
| 4 | `S2 = R // 100` | 234 // 100 | `S2` = 2 |
| 5 | `R = R - (100 * S2)` | 234 - 200 | `R` = 34 |
| 6 | `S3 = R // 10` | 34 // 10 | `S3` = 3 |
| 7 | `R = R - (10 * S3)` | 34 - 30 | `R` = 4 |
| 8 | `S4 = R` | | `S4` = 4 |
| 9 | `Sum = S1 + S2 + S3 + S4` | 1 + 2 + 3 + 4 | `Sum` = 10 |

*Table 3. Changes in the variable values when 1234 is entered*

In `"자릿수의 합=%s" % Sum` on line 10, `%` is not the remainder operator. When the left side is a string, `%` becomes the string formatting operator, which makes a new string with the value on the right inserted at the `%s` position in the string. So `자릿수의 합=10` (sum of digits=10) is printed. String formatting is covered in Lecture 3.

**Output:**

```text
네 자리 이하의 정수를 입력하시오: 1234
자릿수의 합=10
```

```text
네 자리 이하의 정수를 입력하시오: 3456
자릿수의 합=18
```

For 3456, 3 + 4 + 5 + 6 = 18. Entering a number shorter than four digits, such as 405, makes `S1` 0 and gives 0 + 4 + 0 + 5 = 9, so any number of at most four digits is calculated correctly.

**Another Approach: Using the Remainder Operator.** `n - (1000 * S1)` on line 3 equals `n % 1000`, the remainder of `n` divided by 1000. Therefore each digit can be taken out directly with the remainder operator.

```python
n = int(input("네 자리 이하의 정수를 입력하시오: "))
Q1 = n // 1000
Q2 = (n % 1000) // 100
Q3 = (n % 100) // 10
Q4 = n % 10
print("자릿수의 합=%s" % (Q1 + Q2 + Q3 + Q4))
```

```text
네 자리 이하의 정수를 입력하시오: 1234
자릿수의 합=10
```

`n % 1000` is 234, which is 1234 with the thousands digit removed, `n % 100` is 34, and `n % 10` is 4, the ones digit. Their quotients by 100, 10, and 1 are the hundreds, tens, and ones digits. On the last line, `Q1 + Q2 + Q3 + Q4` is enclosed in parentheses because `%` is calculated before `+`.

> **Caution:** Both solutions rely on the assumption that the input is an integer of at most four digits that is 0 or greater. Entering 12345 makes `S1` 12 and prints 12 + 3 + 4 + 5 = 24, but the correct answer is 1 + 2 + 3 + 4 + 5 = 15. Entering -1234 makes `S1` -2, because `//` rounds down toward the smaller integer, and prints 17. With a loop (Lecture 5), the sum can be found regardless of the number of digits by repeating, until `n` becomes 0, the steps of taking out the ones digit with `n % 10` and removing it with `n //= 10`.
