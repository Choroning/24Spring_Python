# Lecture 7 Solutions — Lists and Dictionaries

[Repository Guide](../../README.md) | [English](Solutions.md) | [한국어](Solutions.ko.md)

> **Last Updated:** 2026-11-04

---

<br>

## Table of Contents

- [Exercise 1: Pythagorean Triangles](#exercise-1-pythagorean-triangles)
- [Exercise 2: Guests at Both Parties](#exercise-2-guests-at-both-parties)
- [Exercise 3: Convenience Store Inventory](#exercise-3-convenience-store-inventory)
- [Exercise 4: English-Korean Dictionary](#exercise-4-english-korean-dictionary)
- [Exercise 5: Average of Five Numbers](#exercise-5-average-of-five-numbers)
- [Exercise 6: Probabilities of Dice Faces](#exercise-6-probabilities-of-dice-faces)

---

<br>

## Exercise 1: Pythagorean Triangles

**Problem:** Using a list comprehension, find and print all combinations $(a, b, c)$ of integers from 1 to 30 inclusive that satisfy $a \le b \le c$ and $a^2 + b^2 = c^2$. The full problem and sample run are in [Exercise 1](Exercises.md#exercise-1-pythagorean-triangles).

### Solution

**Approach:** The problem is solved by **exhaustive search**: every possible combination is generated in turn, and only those that satisfy the condition are kept. The three side lengths must vary simultaneously, so a list comprehension with three `for` clauses is used ([Lecture 7, Section 5.2](Concepts_Lecture.md#52-list-comprehensions-with-a-condition)).

- **Range:** The integers from 1 to 30 inclusive are `range(1, 31)`. The stop value of `range` is not included, so 31 must be given to include 30.
- **Removing duplicates:** Starting `y` at `x` and `z` at `y` generates only combinations with $a \le b \le c$. Then the same triangle is not counted twice, as (3, 4, 5) and (4, 3, 5) would be.
- **Condition:** Only the combinations for which `x**2 + y**2 == z**2` is true are put into the new list as tuples `(x, y, z)`.

**Code:**

```python
new_list = [(x, y, z) for x in range(1, 31)
                      for y in range(x, 31)
                      for z in range(y, 31)
                      if x**2 + y**2 == z**2]
print(new_list)
```

**Output:**

```text
[(3, 4, 5), (5, 12, 13), (6, 8, 10), (7, 24, 25), (8, 15, 17), (9, 12, 15), (10, 24, 26), (12, 16, 20), (15, 20, 25), (18, 24, 30), (20, 21, 29)]
```

A list comprehension may span several lines inside its brackets, so writing one `for` clause per line makes it easier to read. The same behavior written with nested loops is as follows; the leftmost `for` clause corresponds to the outermost loop.

```python
new_list = []
for x in range(1, 31):
    for y in range(x, 31):
        for z in range(y, 31):
            if x**2 + y**2 == z**2:
                new_list.append((x, y, z))
print(new_list)
```

```text
[(3, 4, 5), (5, 12, 13), (6, 8, 10), (7, 24, 25), (8, 15, 17), (9, 12, 15), (10, 24, 26), (12, 16, 20), (15, 20, 25), (18, 24, 30), (20, 21, 29)]
```

- **Tracing the first combination:** When `x` is 3 and `y` is 4, `z` varies from 4 to 30, and when `z` is 5, $3^2 + 4^2 = 9 + 16 = 25 = 5^2$, so `(3, 4, 5)` is added.
- **Order of the result:** Combinations with a smaller `x` of the outer loop are added first, so the result is in ascending order of the first component.
- **Integer multiples:** (6, 8, 10), (9, 12, 15), (12, 16, 20), (15, 20, 25), and (18, 24, 30) are 2-6 times (3, 4, 5), and (10, 24, 26) is twice (5, 12, 13). Integer multiples also satisfy the theorem, so they are printed as well.
- **Number of checks:** The number of combinations with $1 \le x \le y \le z \le 30$ is $\binom{32}{3} = 4960$. This is fewer checks than the $30^3 = 27000$ needed if all three variables ran through 1-30.

> **Caution:** Writing the stop value as `range(1, 30)` checks side lengths only up to 29, so (18, 24, 30) is missed and only 10 combinations are printed. A range that includes its end value, such as "up to 30 inclusive," must be written `range(1, 31)`. Getting the end of a range wrong by one in this way is called an off-by-one error.

---

<br>

## Exercise 2: Guests at Both Parties

**Problem:** For the sets `partyA = {"Park", "Kim", "Lee"}` and `partyB = {"Park", "Choi"}`, print the people who attended both parties, and print in alphabetical order the people who attended at least one party and those who attended only party A. The full problem and sample run are in [Exercise 2](Exercises.md#exercise-2-guests-at-both-parties).

### Solution

**Approach:** Set operations solve this directly ([Lecture 7, Section 10.4](Concepts_Lecture.md#104-subsets-and-set-operations)). The people who attended both parties are the intersection, those who attended at least one are the union, and those who attended only party A are the difference $A - B$.

- **Part 1:** `partyA.intersection(partyB)` builds a new set of the elements that are in both sets. It is the same as `partyA & partyB`.
- **Part 2:** The union and the difference are computed with `|` and `-`, and then sorted lists made with `sorted()` are printed.

**Code (Part 1):**

```python
partyA = set(["Park", "Kim", "Lee"])
partyB = set(["Park", "Choi"])

print("2개의 파티에 모두 참석한 사람은 다음과 같습니다.")
print(partyA.intersection(partyB))
```

**Output:**

```text
2개의 파티에 모두 참석한 사람은 다음과 같습니다.
{'Park'}
```

**Code (Part 2):**

```python
partyA = {"Park", "Kim", "Lee"}
partyB = {"Park", "Choi"}

either = partyA | partyB          # union
only_a = partyA - partyB          # difference

print("한 파티 이상 참석:", sorted(either))
print("A 파티에만 참석:", sorted(only_a))
```

**Output:**

```text
한 파티 이상 참석: ['Choi', 'Kim', 'Lee', 'Park']
A 파티에만 참석: ['Kim', 'Lee']
```

- **`set([...])` and `{...}`:** Part 1 creates the sets by giving lists to `set()`, and Part 2 creates them directly with braces. The sets created in the two ways are the same.
- **Union:** `Park` is in both parties but appears only once in a set, so the union has 4 elements.
- **Difference:** `partyA - partyB` is `partyA` without `Park`, which is also in `partyB`, so it is `{'Kim', 'Lee'}`. `partyB - partyA` is `{'Choi'}`, a different result.

> **Note:** `sorted()` is used in Part 2 because the output order of a set of strings may differ from run to run ([Lecture 7, Section 10.2](Concepts_Lecture.md#102-membership-tests-and-iteration)). For example, `print(partyA | partyB)` prints `{'Choi', 'Kim', 'Lee', 'Park'}` in one run and `{'Lee', 'Kim', 'Park', 'Choi'}` in another. The result of Part 1 has only one element, so order is not an issue.

---

<br>

## Exercise 3: Convenience Store Inventory

**Problem:** From the dictionary `items`, which stores the stock of each item, print the stock of the item whose name is entered. The program must not stop with an error even when an item that is not sold is entered. The full problem and sample run are in [Exercise 3](Exercises.md#exercise-3-convenience-store-inventory).

### Solution

**Approach:** A value is looked up by its key in a dictionary whose keys are item names and whose values are stock counts ([Lecture 7, Section 11.2](Concepts_Lecture.md#112-looking-up-values)). First look at the basic program that looks up the key directly, and then modify it to handle missing keys.

**Code (Basic):**

```python
items = {"커피음료": 7, "펜": 3, "종이컵": 2, "우유": 1, "콜라": 4, "책": 5}

item = input("물건의 이름을 입력하시오: ")
print(items[item])
```

**Output:**

```text
물건의 이름을 입력하시오: 콜라
4
```

- **`input()`:** Returns the entered string `"콜라"` (cola), and this string is used as the key as it is.
- **`items[item]`:** Returns the value 4 associated with the key `"콜라"`.

If `라면` (ramen), which is not in the dictionary, is entered into this program, `KeyError: '라면'` is printed on the last line and the program stops. Checking first with `in` whether the key exists prevents this error.

**Code (Handling Missing Items):**

```python
items = {"커피음료": 7, "펜": 3, "종이컵": 2, "우유": 1, "콜라": 4, "책": 5}

item = input("물건의 이름을 입력하시오: ")
if item in items:                 # check the key before indexing
    print(items[item])
else:
    print("%s은(는) 판매하지 않는 물건입니다." % item)
```

**Output:**

```text
물건의 이름을 입력하시오: 콜라
4
```

```text
물건의 이름을 입력하시오: 라면
라면은(는) 판매하지 않는 물건입니다.
```

- **`item in items`:** `in` on a dictionary tests the keys, so it is `True` for the name of an item that is sold.
- **`%s` formatting:** The `%` operator puts the entered name in place of `%s` in the string ([Lecture 3, Section 4.3](../Lec03_Data-Types/Concepts_Lecture.md#43-string-formatting)). The Korean particle depends on whether the preceding syllable has a final consonant, so it is written as `은(는)`.

> **Note:** Instead of `if`-`else`, giving `get()` a default of 0, as in `print(items.get(item, 0))`, prints a stock of 0 for an item that is not sold. Choose one of the two approaches depending on whether an item with zero stock must be distinguished from an item that is not sold.

---

<br>

## Exercise 4: English-Korean Dictionary

**Problem:** Build an English-Korean dictionary by adding `'one'`, `'two'`, `'three'` and their meanings to an empty dictionary, and print the meaning of an entered word. The full problem and sample run are in [Exercise 4](Exercises.md#exercise-4-english-korean-dictionary).

### Solution

**Approach:** Create an empty dictionary with `dict()` and add items one at a time with `dictionary[key] = value` ([Lecture 7, Section 11.1](Concepts_Lecture.md#111-keys-and-values)). Look up the meaning using the entered word as the key.

**Code:**

```python
english_dict = dict()             # empty dictionary

english_dict['one'] = '하나'
english_dict['two'] = '둘'
english_dict['three'] = '셋'

word = input("단어를 입력하시오: ")
print(english_dict[word])
```

**Output:**

```text
단어를 입력하시오: one
하나
```

```text
단어를 입력하시오: two
둘
```

- **`dict()`:** Creates an empty dictionary, the same as `{}`.
- **Adding items:** `english_dict['one'] = '하나'` adds a new item because the key `'one'` does not exist. After the three lines run, the dictionary is `{'one': '하나', 'two': '둘', 'three': '셋'}`.
- **Lookup:** The meaning is found using the entered string as the key. Entering a word that is not present raises `KeyError`, as in the basic program of Exercise 3.

This program looks up only one word per run. To look up several words in succession and also handle words that are not in the dictionary, use a loop and `get()`. The following program ends when Enter is pressed without typing anything.

**Code (Repeated Lookup):**

```python
english_dict = {'one': '하나', 'two': '둘', 'three': '셋'}

while True:
    word = input("단어를 입력하시오: ")
    if word == "":                # an empty line ends the program
        break
    print(english_dict.get(word, "사전에 없는 단어입니다."))
```

**Output:**

```text
단어를 입력하시오: one
하나
단어를 입력하시오: two
둘
단어를 입력하시오: four
사전에 없는 단어입니다.
단어를 입력하시오:
```

- **`while True` and `break`:** The infinite loop runs until an empty string is entered, at which point `break` ends the loop ([Lecture 5, Section 6.4](../Lec05_Loops/Concepts_Lecture.md#64-infinite-loops), [Section 9.1](../Lec05_Loops/Concepts_Lecture.md#91-the-break-statement)).
- **`get(word, "사전에 없는 단어입니다.")`:** Returns the meaning if the key exists and otherwise a message ("The word is not in the dictionary."), so the program moves on to the next input without an error.

---

<br>

## Exercise 5: Average of Five Numbers

**Problem:** Read five integers, store them in a list, and print their average. The full problem and sample run are in [Exercise 5](Exercises.md#exercise-5-average-of-five-numbers).

### Solution

**Approach:** Create an empty list, read an integer five times in a loop, and add each with `append()` ([Lecture 7, Section 3.2](Concepts_Lecture.md#32-adding-elements)). The average is the sum divided by the count, so it is computed with `sum()` and `len()` ([Lecture 7, Section 4.2](Concepts_Lecture.md#42-length-minimum-and-maximum)).

**Code:**

```python
numbers = []                      # the five integers are stored here

for i in range(5):
    n = int(input("정수를 입력하시오: "))
    numbers.append(n)

average = sum(numbers) / len(numbers)
print("평균=", average)
```

**Output:**

```text
정수를 입력하시오: 1
정수를 입력하시오: 2
정수를 입력하시오: 3
정수를 입력하시오: 4
정수를 입력하시오: 5
평균= 3.0
```

- **Input and storage:** The string returned by `input()` is converted to an integer with `int()` and appended to the end of the list. When the loop ends, `numbers` is `[1, 2, 3, 4, 5]`.
- **Average:** `sum(numbers)` is 15 and `len(numbers)` is 5. In Python 3, `/` produces the result of true division even when the division is exact, so the average is printed as `3.0` (Lecture 2).
- **Why `len()` is used:** Computing the count as `len(numbers)` instead of writing 5 directly means the line that computes the average need not change even if the number of inputs changes.

Accumulating the sum directly without `sum()` looks as follows. The elements of the list are assigned to the loop variable `n` in turn.

```python
numbers = []

for i in range(5):
    numbers.append(int(input("정수를 입력하시오: ")))

total = 0
for n in numbers:                 # add the elements one by one
    total += n

print("평균=", total / 5)
```

```text
정수를 입력하시오: 1
정수를 입력하시오: 2
정수를 입력하시오: 3
정수를 입력하시오: 4
정수를 입력하시오: 5
평균= 3.0
```

---

<br>

## Exercise 6: Probabilities of Dice Faces

**Problem:** Roll a die 1000 times with the `random` module, count how many times each face comes up, and print that count divided by 1000 as the probability of each face. The full problem and sample run are in [Exercise 6](Exercises.md#exercise-6-probabilities-of-dice-faces).

### Solution

**Approach:** Create a list `counts` with six slots for the number of times faces 1-6 come up, and on each roll increase the slot for the face that came up by 1. The count of face $k$ is stored at index $k-1$.

- **Rolling the die:** `random.randint(1, 6)` returns one integer from 1 to 6 inclusive with equal probability (Lecture 4).
- **Counting:** `counts = [0] * 6` is a list of six zeros. If the face is `face`, `counts[face - 1] += 1` increases that slot.
- **Probability:** After the loop ends, the value of each slot is divided by 1000 and printed.

**Code:**

```python
import random

counts = [0] * 6                  # counts[0] for face 1, ..., counts[5] for face 6

for i in range(1000):
    face = random.randint(1, 6)   # 1 <= face <= 6
    counts[face - 1] += 1

for face in range(1, 7):
    print("주사위가", face, "인 확률은", counts[face - 1] / 1000)
```

**Output:** The values differ on every run; the following is the result of one run. The sum of the six counts 162, 180, 181, 170, 144, 163 is 1000.

```text
주사위가 1 인 확률은 0.162
주사위가 2 인 확률은 0.18
주사위가 3 인 확률은 0.181
주사위가 4 인 확률은 0.17
주사위가 5 인 확률은 0.144
주사위가 6 인 확률은 0.163
```

- **Mapping between indices and faces:** List indices start at 0 and die faces start at 1, so `face - 1` aligns them. When printing as well, `range(1, 7)` runs through faces 1-6 and reads `counts[face - 1]`. Mixing face numbers and indices easily leads to reading the slot of a different face, so the mapping rule is written down in a comment.
- **Why a list is used:** Storing the counts in six separate variables would require six `if` statements to increase a different variable for each face, whereas with a list a single line `counts[face - 1] += 1` suffices. The code stays the same even if there were 100 faces.

> **[Probability and Statistics]** The true probability of each face is $1/6 \approx 0.1667$, and the printed value is the **relative frequency**, the proportion of the 1000 trials in which that face came up. By the law of large numbers, the relative frequency approaches the true probability as the number of trials $n$ grows. The standard error of the relative frequency is $\sqrt{p(1-p)/n} = \sqrt{(1/6)(5/6)/1000} \approx 0.0118$, so with 1000 rolls it is natural for each value to deviate from 0.1667 by up to about 0.024, twice the standard error. In the result above, 0.144, which deviates the most (by about 0.023), is also within this range.

> **Note:** If, instead of counts, a variable holding the proportion of each face is kept and `0.001` is added to it each time that face comes up, values with an error in the last digits, such as `0.16700000000000012`, may be printed. 0.001 cannot be represented exactly in binary and is stored as an approximation, and repeated additions accumulate that error. Counting with integers and dividing only once at the end avoids this problem. Also, fixing the seed with `random.seed(2024)` right after `import random` gives the same result on every run.
