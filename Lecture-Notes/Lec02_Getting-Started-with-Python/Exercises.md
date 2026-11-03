# Lecture 2 Exercises — Getting Started with Python

[Repository Guide](../../README.md) | [English](Exercises.md) | [한국어](Exercises.ko.md)

> **Last Updated:** 2026-11-04

Exercises 1-5 are lab problems that each check a concept of [Lecture 2](Concepts_Lecture.md), and Exercises 6-8 are challenge problems in which the problem is analyzed and the variables are chosen before the program is written. In the sample runs, the value right after a prompt message is the value the user typed on the keyboard.

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

**Problem:** Write a program that prints the following. Do not type the 72 on the third line directly; let Python calculate `9*8` and print it.

**Sample Run:**

```text
안녕하세요? 여러분
저는 파이썬을 무척 좋아합니다.
9*8은 72 입니다.
안녕히 계세요.
```

**[Solution](Solutions.md#exercise-1-practicing-the-print-function)**

---

<br>

## Exercise 2: Robot Reporter

**Problem:** Write a program that asks the user for the stadium, the winning team, the losing team, the best player, and the score, stores the answers in variables, and writes a baseball game article by attaching sentences to these strings. Leave one empty line before the article, and print separator lines made of `=` above and below the article.

**Sample Run:**

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

**[Solution](Solutions.md#exercise-2-robot-reporter)**

---

<br>

## Exercise 3: Coffee Shop Sales

**Problem:** You are about to open a coffee shop. With the coffee menu below, write a program that reads the number of cups sold for each menu item and calculates how much revenue can be made.

| Menu | Price |
|:-----|:-----|
| Americano | 2,000 won |
| Cafe latte | 3,000 won |
| Cappuccino | 3,500 won |

*Table 1. The coffee menu and prices*

**Sample Run:**

```text
아메리카노 판매 개수: 10
카페라떼 판매 개수: 20
카푸치노 판매 개수: 30
총 매출은 185000 입니다.
```

**[Solution](Solutions.md#exercise-3-coffee-shop-sales)**

---

<br>

## Exercise 4: Vending Machine

**Problem:** Write a program that simulates a vending machine.

- The vending machine reads the money inserted and the price of the item from the user.
- Assume that prices are multiples of 100 won.
- The program calculates and prints the change.
- Assume that the machine has only 500-won and 100-won coins. The change is given first with as many 500-won coins as possible, and the rest with 100-won coins.

**Sample Run:**

```text
투입한 돈: 5000
물건값: 2600
거스름돈: 2400
500원 동전의 개수: 4
100원 동전의 개수: 4
```

**[Solution](Solutions.md#exercise-4-vending-machine)**

---

<br>

## Exercise 5: Computing an Average

**Problem:** The following program was written to read three numbers and compute their average. However, entering 10, 20, and 30 prints an average of 40.0 instead of 20.0. Where is the mistake? Explain the cause and correct it.

```python
x = int(input("첫 번째 수를 입력하시오: "))
y = int(input("두 번째 수를 입력하시오: "))
z = int(input("세 번째 수를 입력하시오: "))
avg = x + y + z / 3
print("평균 =", avg)
```

**Sample Run (Wrong Result):**

```text
첫 번째 수를 입력하시오: 10
두 번째 수를 입력하시오: 20
세 번째 수를 입력하시오: 30
평균 = 40.0
```

**[Solution](Solutions.md#exercise-5-computing-an-average)**

---

<br>

## Exercise 6: Greeting and the Sum of Two Integers

**Problem:** Write a program like the following that asks for the user's name, then reads two integers, adds them, and prints the result.

**Sample Run:**

```text
이름을 입력하시오: 홍길동
홍길동 씨, 안녕하세요?
파이썬에 오신 것을 환영합니다.
첫 번째 정수를 입력하시오: 300
두 번째 정수를 입력하시오: 400
300 과 400 의 합은 700 입니다.
```

**[Solution](Solutions.md#exercise-6-greeting-and-the-sum-of-two-integers)**

---

<br>

## Exercise 7: Four Arithmetic Operations on Two Integers

**Problem:** Write a program that reads two integers, performs the four arithmetic operations (addition, subtraction, multiplication, and division) on them, and prints the results.

**Sample Run:**

```text
첫 번째 정수를 입력하시오: 4
두 번째 정수를 입력하시오: 2
4 + 2 = 6
4 - 2 = 2
4 * 2 = 8
4 / 2 = 2.0
```

**[Solution](Solutions.md#exercise-7-four-arithmetic-operations-on-two-integers)**

---

<br>

## Exercise 8: Sum of Digits

**Problem:** Write a program that reads an integer from the user and calculates the sum of its digits. For example, the sum of the digits of 1234 is 1 + 2 + 3 + 4 = 10. Assume that the input is an integer of at most four digits that is 0 or greater.

**Hint:** Use the operator `//`.

**Sample Run:** These are the results of running the program twice and entering 1234 and 3456, respectively.

```text
네 자리 이하의 정수를 입력하시오: 1234
자릿수의 합=10
```

```text
네 자리 이하의 정수를 입력하시오: 3456
자릿수의 합=18
```

**[Solution](Solutions.md#exercise-8-sum-of-digits)**
