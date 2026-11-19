# Lecture 12 Exercises — Recursion

[Repository Guide](../../README.md) | [English](Exercises.md) | [한국어](Exercises.ko.md)

> **Last Updated:** 2026-11-19

Exercises 1, 3, and 4 write functions that reduce numbers and lists recursively, and Exercise 2 traces the order and number of recursive calls. Exercises 5 and 6 are recursions that count combinations and subsets, Exercise 7 is a recursion that follows a folder structure, and Exercise 8 converts a recursion into iteration.

---

<br>

## Table of Contents

- [Exercise 1: The Digit Sum and the Number of Digits](#exercise-1-the-digit-sum-and-the-number-of-digits)
- [Exercise 2: Tracing a Recursion That Calls Twice](#exercise-2-tracing-a-recursion-that-calls-twice)
- [Exercise 3: Binary Strings](#exercise-3-binary-strings)
- [Exercise 4: Flattening Nested Lists](#exercise-4-flattening-nested-lists)
- [Exercise 5: The Number of Combinations](#exercise-5-the-number-of-combinations)
- [Exercise 6: All Subsets](#exercise-6-all-subsets)
- [Exercise 7: The Total Size of a Folder](#exercise-7-the-total-size-of-a-folder)
- [Exercise 8: Binary Search Converted to Iteration](#exercise-8-binary-search-converted-to-iteration)

---

<br>

## Exercise 1: The Digit Sum and the Number of Digits

**Problem:** Write recursively `digit_sum(n)`, which returns the sum of all the digits of a nonnegative integer `n`, and `num_digits(n)`, which returns the number of digits of `n`. Do not convert to strings; use only `//` and `%`. For 7, 1234, 9875, and 1000000, print the number, its digit sum, and its number of digits.

**Sample Run:**

```text
7 7 1
1234 10 4
9875 29 4
1000000 1 7
```

**[Solution](Solutions.md#exercise-1-the-digit-sum-and-the-number-of-digits)**

---

<br>

## Exercise 2: Tracing a Recursion That Calls Twice

**Problem:** Write the output of the following program without running it. Then draw the call tree to find how many times in total the function `m` is called.

```python
calls = 0

def m(n):
    global calls
    calls += 1
    if n <= 0:
        return
    m(n - 1)
    print(n, end=" ")
    m(n - 2)

m(3)
print()
print(calls)
```

**[Solution](Solutions.md#exercise-2-tracing-a-recursion-that-calls-twice)**

---

<br>

## Exercise 3: Binary Strings

**Problem:** Write recursively `to_binary(n)`, which returns the string representing a nonnegative integer in binary. Do not use the built-in function `bin()`. For 0, 1, 6, 13, 255, and 1024, print the number, the result, and whether the result equals `bin(n)` without its first two characters `0b`.

**Sample Run:**

```text
0 0 True
1 1 True
6 110 True
13 1101 True
255 11111111 True
1024 10000000000 True
```

**[Solution](Solutions.md#exercise-3-binary-strings)**

---

<br>

## Exercise 4: Flattening Nested Lists

**Problem:** Write `flatten(items)`, which receives a nested list whose elements can themselves be lists and returns a one-dimensional list holding only the non-list elements in their original order. There is no limit on the depth of nesting. Call it for the following three lists.

```text
[1, [2, [3, [4]], 5], [], [[6]]]
[]
[[["a"]], "b"]
```

**Sample Run:**

```text
[1, 2, 3, 4, 5, 6]
[]
['a', 'b']
```

**[Solution](Solutions.md#exercise-4-flattening-nested-lists)**

---

<br>

## Exercise 5: The Number of Combinations

**Problem:** The number of combinations $\binom{n}{k}$ of choosing $k$ out of $n$ satisfies the following relations.

```math
\binom{n}{0} = \binom{n}{n} = 1, \qquad \binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k} \quad (0 < k < n)
```

Write a recursive function `comb(n, k)` that transcribes these relations directly, count its calls with a global variable, and print the values and numbers of calls of `comb(5, 2)` and `comb(20, 10)`. Then compute `comb_memo(20, 10)` with a `comb_memo(n, k)` decorated with `functools.lru_cache`, printing the value and the number of new computations (`cache_info().misses`), and finally print the value of the standard function `math.comb(20, 10)`.

**Sample Run:**

```text
10 19
184756 369511
184756 120
184756
```

**[Solution](Solutions.md#exercise-5-the-number-of-combinations)**

---

<br>

## Exercise 6: All Subsets

**Problem:** Write recursively `subsets(items)`, which receives a list and returns, as a list of lists, all subsets (including the empty set) that can be made from its elements. The elements of each subset follow the original order. Print the number and the list of subsets of `["a", "b", "c"]`, and print the number of subsets made from the 10 integers 0 through 9.

**Sample Run:**

```text
8
[[], ['c'], ['b'], ['b', 'c'], ['a'], ['a', 'c'], ['a', 'b'], ['a', 'b', 'c']]
1024
```

**[Solution](Solutions.md#exercise-6-all-subsets)**

---

<br>

## Exercise 7: The Total Size of a Folder

**Problem:** Write recursively `total_size(path)`, which receives a `pathlib.Path` and returns its size (in bytes) if it is a file, or the sum of the sizes of all files inside it if it is a folder. While computing, the function prints folders and files with indentation. Print `/` after a folder name and the size after a file name, and process the entries of a folder in order of name.

First create the following structure, and then call the function for `tree_demo`. Write `hello` and a newline to `a.txt`, `한글` and a newline to `b.txt` in UTF-8, and 100 `x` characters to `c.txt`.

```text
tree_demo/
├── a.txt
└── docs/
    ├── b.txt
    └── old/
        └── c.txt
```

**Sample Run:**

```text
tree_demo/
  a.txt 6
  docs/
    b.txt 7
    old/
      c.txt 100
합계: 113
```

**[Solution](Solutions.md#exercise-7-the-total-size-of-a-folder)**

---

<br>

## Exercise 8: Binary Search Converted to Iteration

**Problem:** Write `search_loop(a, target)`, which converts the recursive binary search `search_rec(a, target, lo, hi)` into a `while` statement. `search_loop()` returns `(index found, number of comparisons)`, with index -1 if the value is absent. In a list of the one million even numbers from 0 to 1999998, search for 1234568 and 1234567 and print the results, and print the result of searching for 1234568 in the same list with `search_rec()`. Finally, search for every integer from -3 to 39 in `[0, 3, 6, ..., 27]` with both functions and print whether all the results agree.

**Sample Run:**

```text
(617284, 17)
(-1, 20)
617284
True
```

**[Solution](Solutions.md#exercise-8-binary-search-converted-to-iteration)**
