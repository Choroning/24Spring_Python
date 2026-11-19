# Lecture 10 Exercises — File Input and Output

[Repository Guide](../../README.md) | [English](Exercises.md) | [한국어](Exercises.ko.md)

> **Last Updated:** 2026-11-19

Exercise 1 computes byte counts under different encodings, and Exercises 2-5 read and write text files. Exercise 6 identifies the kind of a file in binary mode, and Exercises 7 and 8 work with CSV and JSON files. Unless stated otherwise, every text file is written and read in UTF-8.

---

<br>

## Table of Contents

- [Exercise 1: Byte Counts by Encoding](#exercise-1-byte-counts-by-encoding)
- [Exercise 2: Counting Lines, Words, and Characters](#exercise-2-counting-lines-words-and-characters)
- [Exercise 3: Summarizing a Score File](#exercise-3-summarizing-a-score-file)
- [Exercise 4: A Numbered Log](#exercise-4-a-numbered-log)
- [Exercise 5: The First Difference between Two Files](#exercise-5-the-first-difference-between-two-files)
- [Exercise 6: Identifying the Kind of a File](#exercise-6-identifying-the-kind-of-a-file)
- [Exercise 7: Transforming a CSV Grade Sheet](#exercise-7-transforming-a-csv-grade-sheet)
- [Exercise 8: A JSON Settings File](#exercise-8-a-json-settings-file)

---

<br>

## Exercise 1: Byte Counts by Encoding

**Problem:** Write a function `byte_report(text)` that receives a string `text` and prints, on one line, the number of characters, the number of bytes when encoded in UTF-8, and the number of bytes when encoded in cp949. Call it for the strings `"Python"`, `"파이썬"`, `"Py파이썬3"`, and `"가나다 ABC"`, and on the last line print the hexadecimal notation of the UTF-8 bytes of `"한"` and its code point. Then compute the UTF-8 bytes of `"한"` (U+D55C) by hand from the bit layout and compare them with the output.

**Sample Run:**

```text
Python: 문자 6, UTF-8 6바이트, cp949 6바이트
파이썬: 문자 3, UTF-8 9바이트, cp949 6바이트
Py파이썬3: 문자 6, UTF-8 12바이트, cp949 9바이트
가나다 ABC: 문자 7, UTF-8 13바이트, cp949 10바이트
ed 95 9c 0xd55c
```

**[Solution](Solutions.md#exercise-1-byte-counts-by-encoding)**

---

<br>

## Exercise 2: Counting Lines, Words, and Characters

**Problem:** Write a function `count_file(path)` that receives the path of a text file and returns the number of lines, words, and characters as a tuple. A word is a chunk separated by whitespace, and the character count includes newline characters. The function must not load the whole file into memory at once.

Save the following four lines (the third line is blank) to `notes.txt`, and then call the function.

```text
파일은 바이트의 나열이다
텍스트 파일은 인코딩을 따른다

with 문은 파일을 닫는다
```

**Sample Run:**

```text
(4, 11, 48)
```

**[Solution](Solutions.md#exercise-2-counting-lines-words-and-characters)**

---

<br>

## Exercise 3: Summarizing a Score File

**Problem:** Read `scores.txt`, in which each line holds `name score`, and write the number of people, the average, and the person with the highest score to `result.txt`. Skip blank lines and lines starting with `#` (comments). Write the result file with the `file` parameter of `print()`, and write the average to two decimal places. The program first creates `scores.txt` with the following contents.

```text
# 이름 점수
Kim 85
Lee 92

Park 78
# 결시자 제외
Choi 90
```

**Sample Run:** The result of printing the contents of `result.txt`.

```text
인원: 4
평균: 86.25
최고: Lee 92
```

**[Solution](Solutions.md#exercise-3-summarizing-a-score-file)**

---

<br>

## Exercise 4: A Numbered Log

**Problem:** Write a function `log(message, path="app.log")` that appends one line of the form `[001] message` to the end of a log file. The number is the count of lines already in the file plus 1, written with three digits. If the file does not exist yet, numbering starts at 001. Check whether the file exists with `pathlib`.

Call `log()` three times and then print the contents of the log file.

**Sample Run:** The result of the first run when no log file exists.

```text
[001] 프로그램 시작
[002] 파일 3개 처리
[003] 프로그램 종료
```

Running the same program once more appends `[004]` through `[006]` after the existing lines.

**[Solution](Solutions.md#exercise-4-a-numbered-log)**

---

<br>

## Exercise 5: The First Difference between Two Files

**Problem:** Write a function `first_difference(path1, path2)` that compares two text files line by line from the beginning and returns, as a tuple, the number (from 1) of the first line that differs and that line from each file (without the final newline). If the two files are the same to the end, return `None`. If one file ends first, treat its line as the empty string. Open both files at once and read them with `readline()`.

Save `사과`, `배`, `포도` to `v1.txt`, `사과`, `배`, `귤`, `포도` to `v2.txt`, and `사과`, `배` to `v3.txt`, one per line, and then compare `v1.txt` with `v2.txt`, `v1.txt` with `v1.txt`, and `v1.txt` with `v3.txt`.

**Sample Run:**

```text
(3, '포도', '귤')
None
(3, '포도', '')
```

**[Solution](Solutions.md#exercise-5-the-first-difference-between-two-files)**

---

<br>

## Exercise 6: Identifying the Kind of a File

**Problem:** Write a function `detect(path)` that reads the bytes of a file in binary mode and identifies its kind. Apply the following rules in order from the top.

1. If it starts with the PNG signature `89 50 4E 47 0D 0A 1A 0A`, it is `"PNG 그림"`.
2. If it starts with the UTF-8 BOM `EF BB BF`, it is `"UTF-8 텍스트 (BOM)"`.
3. If every byte is ASCII (0-127), it is `"ASCII 텍스트"`.
4. If it has no 0 byte and decodes as UTF-8 without errors, it is `"UTF-8 텍스트"`.
5. Otherwise it is `"알 수 없는 이진 파일"`.

Create the following six files and identify each. `a.png` is the PNG signature followed by eight 0 bytes, `b.txt` is `머리말` written with `"utf-8-sig"`, `c.txt` is `hello`, `d.txt` is `안녕하세요` written in UTF-8, `e.txt` is `안녕하세요` written in cp949, and `f.bin` is the bytes 0, 255, 3, and 128. Each text file ends with one newline.

**Sample Run:**

```text
a.png PNG 그림
b.txt UTF-8 텍스트 (BOM)
c.txt ASCII 텍스트
d.txt UTF-8 텍스트
e.txt 알 수 없는 이진 파일
f.bin 알 수 없는 이진 파일
```

**[Solution](Solutions.md#exercise-6-identifying-the-kind-of-a-file)**

---

<br>

## Exercise 7: Transforming a CSV Grade Sheet

**Problem:** Read `grades.csv`, whose columns are `name`, `korean`, `english`, and `math`, add to each student a total `total` and an average `average` to one decimal place, sort by total from the highest, and write the result to `report.csv`. Use `csv.DictReader` and `csv.DictWriter` for reading and writing. The program first creates `grades.csv` with the following contents using `csv.writer`.

```text
name,korean,english,math
Kim,85,90,78
Lee,92,88,95
Park,70,65,80
```

**Sample Run:** The result of printing the contents of `report.csv`.

```text
name,korean,english,math,total,average
Lee,92,88,95,275,91.7
Kim,85,90,78,253,84.3
Park,70,65,80,215,71.7
```

**[Solution](Solutions.md#exercise-7-transforming-a-csv-grade-sheet)**

---

<br>

## Exercise 8: A JSON Settings File

**Problem:** Write two functions that save and load a program's settings as a JSON file.

- `load_settings(path)`: Starting from the default settings `DEFAULTS = {"user": "guest", "volume": 5, "recent": []}`, returns a dictionary in which the defaults are overwritten by the contents of the settings file if it exists. If the file does not exist, it returns a copy of the default settings. `DEFAULTS` itself must not change however many times the settings are loaded.
- `save_settings(path, settings)`: Saves the settings as JSON indented for readability. Hangul is not escaped.

Load the settings and print them, increase `volume` by 1, append `"보고서" + volume + ".txt"` to the `recent` list, save, and then print the saved settings and `DEFAULTS`.

**Sample Run:** The results of the first run, when no settings file exists, and of the second run.

```text
불러온 설정: {'user': 'guest', 'volume': 5, 'recent': []}
저장한 설정: {'user': 'guest', 'volume': 6, 'recent': ['보고서6.txt']}
기본값: {'user': 'guest', 'volume': 5, 'recent': []}
```

```text
불러온 설정: {'user': 'guest', 'volume': 6, 'recent': ['보고서6.txt']}
저장한 설정: {'user': 'guest', 'volume': 7, 'recent': ['보고서6.txt', '보고서7.txt']}
기본값: {'user': 'guest', 'volume': 5, 'recent': []}
```

**[Solution](Solutions.md#exercise-8-a-json-settings-file)**
