# Lecture 10 Solutions — File Input and Output

[Repository Guide](../../README.md) | [English](Solutions.md) | [한국어](Solutions.ko.md)

> **Last Updated:** 2026-11-19

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

**Problem:** Write `byte_report()`, which prints the number of characters of a string and its byte counts in UTF-8 and cp949, and compute the UTF-8 bytes of `"한"` by hand. The full problem and sample run are in [Exercise 1](Exercises.md#exercise-1-byte-counts-by-encoding).

### Solution

**Approach:** `len()` counts characters for a `str` and bytes for a `bytes` ([Lecture 10, Section 1.3](Concepts_Lecture.md#13-character-encodings-and-utf-8)). Encode the string with each of the two encodings using `encode()` and measure the lengths.

**Code:**

```python
def byte_report(text):
    u = text.encode("utf-8")
    c = text.encode("cp949")
    print("%s: 문자 %d, UTF-8 %d바이트, cp949 %d바이트" % (text, len(text), len(u), len(c)))

for t in ["Python", "파이썬", "Py파이썬3", "가나다 ABC"]:
    byte_report(t)
print("한".encode("utf-8").hex(" "), hex(ord("한")))
```

**Output:**

```text
Python: 문자 6, UTF-8 6바이트, cp949 6바이트
파이썬: 문자 3, UTF-8 9바이트, cp949 6바이트
Py파이썬3: 문자 6, UTF-8 12바이트, cp949 9바이트
가나다 ABC: 문자 7, UTF-8 13바이트, cp949 10바이트
ed 95 9c 0xd55c
```

- **The rule for byte counts:** ASCII characters (English letters, digits, spaces) take 1 byte in both encodings, and a Hangul syllable takes 3 bytes in UTF-8 and 2 bytes in cp949. `"가나다 ABC"` has 3 Hangul syllables and 4 ASCII characters, so it is $3 \times 3 + 4 = 13$ bytes in UTF-8 and $3 \times 2 + 4 = 10$ bytes in cp949.
- **`ord()`:** Returns the code point of a character as an integer. Converted with `hex()`, it is `0xd55c`.

**Computing by hand:** U+D55C is in the range U+0800-U+FFFF, so the 3-byte template `1110xxxx 10xxxxxx 10xxxxxx` applies. Writing `0xD55C` as a 16-bit binary number gives `1101 0101 0101 1100`, and splitting it from the front into 4, 6, and 6 bits gives `1101`, `010101`, and `011100`. Filling the template gives `11101101`, `10010101`, and `10011100`, which is `ED 95 9C` in hexadecimal, the same as the output.

---

<br>

## Exercise 2: Counting Lines, Words, and Characters

**Problem:** Write `count_file(path)`, which counts lines, words, and characters without loading the whole file into memory. The full problem and sample run are in [Exercise 2](Exercises.md#exercise-2-counting-lines-words-and-characters).

### Solution

**Approach:** Iterating over a file object with a `for` statement keeps only one line in memory at a time ([Lecture 10, Section 3.3](Concepts_Lecture.md#33-iterating-over-a-file-object)). For each line, add 1 to the line count, `len(line.split())` to the word count, and `len(line)` to the character count. `split()` without arguments treats newlines as whitespace too, so a blank line has 0 words.

**Code:**

```python
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("파일은 바이트의 나열이다\n")
    f.write("텍스트 파일은 인코딩을 따른다\n")
    f.write("\n")
    f.write("with 문은 파일을 닫는다\n")

def count_file(path):
    lines = 0
    words = 0
    chars = 0
    with open(path, encoding="utf-8") as f:
        for line in f:
            lines += 1
            words += len(line.split())
            chars += len(line)
    return lines, words, chars

print(count_file("notes.txt"))
```

**Output:**

```text
(4, 11, 48)
```

| Line | Words | Characters (Including the Newline) |
|:-----|-----:|-----:|
| `파일은 바이트의 나열이다` | 3 | 14 |
| `텍스트 파일은 인코딩을 따른다` | 4 | 17 |
| Blank line | 0 | 1 |
| `with 문은 파일을 닫는다` | 4 | 16 |
| Total | 11 | 48 |

*Table 1. Words and characters per line of notes.txt*

- **Character counts:** The first line has 14 characters: 11 Hangul syllables, 2 spaces, and 1 newline. The blank line also has one newline character, so it counts as 1.
- **The difference from byte counts:** `len(line)` counts characters. To know the size of the file in bytes, use the length of the `bytes` read in binary mode, or `Path(path).stat().st_size`.

---

<br>

## Exercise 3: Summarizing a Score File

**Problem:** Read `scores.txt` while skipping blank and comment lines, and write the number of people, the average, and the person with the highest score to `result.txt` with `print(file=)`. The full problem and sample run are in [Exercise 3](Exercises.md#exercise-3-summarizing-a-score-file).

### Solution

**Approach:** After removing whitespace at both ends of each line with `strip()`, skip the line with `continue` if it is the empty string or `startswith("#")`. Split each remaining line into a name and a score with `split()` and put them into two lists. The person with the highest score is found through the index of the maximum.

**Code:**

```python
with open("scores.txt", "w", encoding="utf-8") as f:
    f.write("# 이름 점수\n")
    f.write("Kim 85\n")
    f.write("Lee 92\n")
    f.write("\n")
    f.write("Park 78\n")
    f.write("# 결시자 제외\n")
    f.write("Choi 90\n")

names = []
scores = []
with open("scores.txt", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line == "" or line.startswith("#"):    # skip blanks and comments
            continue
        name, score = line.split()
        names.append(name)
        scores.append(int(score))

best = scores.index(max(scores))
with open("result.txt", "w", encoding="utf-8") as out:
    print("인원:", len(scores), file=out)
    print("평균: %.2f" % (sum(scores) / len(scores)), file=out)
    print("최고:", names[best], scores[best], file=out)

with open("result.txt", encoding="utf-8") as f:
    print(f.read(), end="")
```

**Output:**

```text
인원: 4
평균: 86.25
최고: Lee 92
```

- **Skipped lines:** Two comment lines and one blank line were skipped, leaving 4 lines. If `# 이름 점수` were not skipped, `split()` would produce three pieces and a `ValueError` would occur.
- **The average:** $(85 + 92 + 78 + 90) / 4 = 86.25$.
- **The highest score:** `max(scores)` is 92 and `scores.index(92)` is 1, so it is `names[1]`, Lee ([Lecture 7, Section 4.1](../Lec07_Lists-and-Dictionaries/Concepts_Lecture.md#41-searching-for-elements)).
- **`print(file=out)`:** Numbers need not be converted to strings by hand, and the newline is added automatically ([Lecture 10, Section 4.2](Concepts_Lecture.md#42-writing-to-files-with-print)).

---

<br>

## Exercise 4: A Numbered Log

**Problem:** Write `log()`, which appends one line at a time to the end of a log file with a three-digit number equal to the existing line count plus 1. The full problem and sample run are in [Exercise 4](Exercises.md#exercise-4-a-numbered-log).

### Solution

**Approach:** First check whether the file exists with `Path(path).exists()`, and if it does, open it in read mode and count its lines. Opening a missing file with `"r"` causes a `FileNotFoundError`, so this check is necessary. Then open it in `"a"` mode and append to the end ([Lecture 10, Section 2.2](Concepts_Lecture.md#22-file-modes)). The three-digit number is made with the format specifier `%03d` (a 3-digit integer with empty places filled with 0).

**Code:**

```python
from pathlib import Path

def log(message, path="app.log"):
    p = Path(path)
    count = 0
    if p.exists():
        with open(p, encoding="utf-8") as f:
            for line in f:
                count += 1
    with open(p, "a", encoding="utf-8") as f:
        print("[%03d] %s" % (count + 1, message), file=f)

log("프로그램 시작")
log("파일 3개 처리")
log("프로그램 종료")
print(Path("app.log").read_text(encoding="utf-8"), end="")
```

**Output:** The result of the first run when no log file exists.

```text
[001] 프로그램 시작
[002] 파일 3개 처리
[003] 프로그램 종료
```

- **The second run:** The file already has three lines, so numbering continues from `[004]`, and the file contents printed at the end have six lines. Had the file been opened with `"w"`, the records would have been erased at every run.
- **`open()` and `Path`:** `open()` accepts a `Path` object as the path as well as a string.
- **A limitation:** Every log call reads the whole file to count its lines, so it slows down as the log grows very long. Storing the number in a separate file, or using the time instead of a number, is the usual approach in real log files.

---

<br>

## Exercise 5: The First Difference between Two Files

**Problem:** Write `first_difference()`, which compares two text files line by line and returns the number and contents of the first line that differs. The full problem and sample run are in [Exercise 5](Exercises.md#exercise-5-the-first-difference-between-two-files).

### Solution

**Approach:** Open both files together in one `with` statement ([Lecture 10, Section 4.3](Concepts_Lecture.md#43-opening-two-files-together)). At each iteration, read one line from each file with `readline()`. At the end of a file `readline()` returns `''`, so the line of the file that ends first automatically becomes the empty string ([Lecture 10, Section 3.2](Concepts_Lecture.md#32-readline-and-readlines)). If both lines are `''`, the two files ended together, so they are the same.

**Code:**

```python
def first_difference(path1, path2):
    with open(path1, encoding="utf-8") as f1, open(path2, encoding="utf-8") as f2:
        no = 0
        while True:
            a = f1.readline()
            b = f2.readline()
            no += 1
            if a == "" and b == "":
                return None                 # identical to the end
            if a != b:
                return no, a.rstrip("\n"), b.rstrip("\n")

with open("v1.txt", "w", encoding="utf-8") as f:
    f.write("사과\n배\n포도\n")
with open("v2.txt", "w", encoding="utf-8") as f:
    f.write("사과\n배\n귤\n포도\n")
with open("v3.txt", "w", encoding="utf-8") as f:
    f.write("사과\n배\n")

print(first_difference("v1.txt", "v2.txt"))
print(first_difference("v1.txt", "v1.txt"))
print(first_difference("v1.txt", "v3.txt"))
```

**Output:**

```text
(3, '포도', '귤')
None
(3, '포도', '')
```

- **The first comparison:** Lines 1 and 2 are equal, and at line 3 `포도` and `귤` differ.
- **The same file:** Comparing a file with itself, opened twice, makes both lines `''` at the fourth iteration, so `None` is returned. Opening the same file twice in read mode causes no problem, and the two file objects each have their own file position.
- **Files of different lengths:** `v3.txt` ends after line 2, so `b`, read at line 3, is `''` and is judged different from `포도`.
- **`return` and `with`:** Even when the function ends with `return` inside the `with` block, both files are closed.

---

<br>

## Exercise 6: Identifying the Kind of a File

**Problem:** Write `detect()`, which uses the bytes read in binary mode to identify PNG, UTF-8 with a BOM, ASCII, UTF-8, and other binary files. The full problem and sample run are in [Exercise 6](Exercises.md#exercise-6-identifying-the-kind-of-a-file).

### Solution

**Approach:** Opening in text mode can cause decoding errors, so every file is opened with `"rb"` and read as `bytes` ([Lecture 10, Section 5.1](Concepts_Lecture.md#51-reading-and-writing-bytes)). Check the signature and the BOM with the `startswith()` of `bytes`, and check whether every byte is 0-127 with `isascii()`. Whether the data decodes as UTF-8 is judged by whether the replacement character U+FFFD appears in the result of decoding with `errors="replace"`.

**Code:**

```python
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
UTF8_BOM = b"\xef\xbb\xbf"

def detect(path):
    with open(path, "rb") as f:
        data = f.read()
    if data.startswith(PNG_SIGNATURE):
        return "PNG 그림"
    if data.startswith(UTF8_BOM):
        return "UTF-8 텍스트 (BOM)"
    if data.isascii():
        return "ASCII 텍스트"
    if b"\x00" not in data:
        text = data.decode("utf-8", errors="replace")
        if "�" not in text:            # no replacement character
            return "UTF-8 텍스트"
    return "알 수 없는 이진 파일"

with open("a.png", "wb") as f:
    f.write(PNG_SIGNATURE + bytes(8))
with open("b.txt", "w", encoding="utf-8-sig") as f:
    f.write("머리말\n")
with open("c.txt", "w", encoding="utf-8") as f:
    f.write("hello\n")
with open("d.txt", "w", encoding="utf-8") as f:
    f.write("안녕하세요\n")
with open("e.txt", "w", encoding="cp949") as f:
    f.write("안녕하세요\n")
with open("f.bin", "wb") as f:
    f.write(bytes([0, 255, 3, 128]))

for name in ["a.png", "b.txt", "c.txt", "d.txt", "e.txt", "f.bin"]:
    print(name, detect(name))
```

**Output:**

```text
a.png PNG 그림
b.txt UTF-8 텍스트 (BOM)
c.txt ASCII 텍스트
d.txt UTF-8 텍스트
e.txt 알 수 없는 이진 파일
f.bin 알 수 없는 이진 파일
```

- **`bytes(8)`:** Given a single integer, `bytes()` creates a `bytes` of that length filled with 0.
- **The order of the rules:** A file of ASCII only also decodes as UTF-8, so rule 3 must be checked before rule 4 for `c.txt` to be identified as `ASCII 텍스트`.
- **The cp949 file:** The bytes of `e.txt` do not follow the rules of UTF-8, so replacement characters appear and it is identified as a binary file. This result reflects the point in [Lecture 10, Section 1.4](Concepts_Lecture.md#14-when-encodings-do-not-match) that bytes alone cannot reliably distinguish cp949 text from binary data.
- **A limitation:** `data = f.read()` reads the whole file. If only the signature is checked, `f.read(8)` suffices, and whether a file is text can be estimated by reading only the first few kilobytes.

---

<br>

## Exercise 7: Transforming a CSV Grade Sheet

**Problem:** Read `grades.csv`, add total and average columns, sort by total, and write the result to `report.csv`. The full problem and sample run are in [Exercise 7](Exercises.md#exercise-7-transforming-a-csv-grade-sheet).

### Solution

**Approach:** The rows given by `csv.DictReader` are dictionaries, so new keys can be added as in `row["total"] = ...`. The values read are strings, so the scores are converted with `int()` before adding ([Lecture 10, Section 7.3](Concepts_Lecture.md#73-dictwriter-and-dictreader)). For sorting, the total is given as the `key` and `reverse=True` makes it descending. When writing, `DictWriter` is given `fieldnames` that include the added columns. Both files are opened with `newline=""`.

**Code:**

```python
import csv

with open("grades.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(["name", "korean", "english", "math"])
    w.writerow(["Kim", 85, 90, 78])
    w.writerow(["Lee", 92, 88, 95])
    w.writerow(["Park", 70, 65, 80])

rows = []
with open("grades.csv", encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        total = int(row["korean"]) + int(row["english"]) + int(row["math"])
        row["total"] = total
        row["average"] = "%.1f" % (total / 3)
        rows.append(row)

rows.sort(key=lambda r: r["total"], reverse=True)
fields = ["name", "korean", "english", "math", "total", "average"]
with open("report.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    w.writerows(rows)

with open("report.csv", encoding="utf-8", newline="") as f:
    print(f.read(), end="")
```

**Output:**

```text
name,korean,english,math,total,average
Lee,92,88,95,275,91.7
Kim,85,90,78,253,84.3
Park,70,65,80,215,71.7
```

- **Totals and averages:** Lee has $92 + 88 + 95 = 275$ and $275 / 3 = 91.66...$, which gives 91.7. Kim has 253 and 84.3, and Park 215 and 71.7.
- **The sort key:** `row["total"]` was stored as an integer, so the rows are sorted by numeric size. Had it been stored as a string, the comparison would be lexicographic, and, for example, `"95"` would be judged larger than `"215"`.
- **Line endings:** Each line of `report.csv` actually ends with `\r\n` (the default of the `csv` module). The file was read with `newline=""` and printed, so the `\r` is printed along with it as an invisible character.

---

<br>

## Exercise 8: A JSON Settings File

**Problem:** Write `load_settings()`, which starts from the default settings and overwrites them with the contents of a JSON settings file, and `save_settings()`, which saves the settings. The full problem and sample run are in [Exercise 8](Exercises.md#exercise-8-a-json-settings-file).

### Solution

**Approach:** The settings file may not exist, so check with `Path.exists()` before opening it. A dictionary's `update()` overwrites the values of matching keys with the items of another dictionary and adds missing keys ([Lecture 7, Section 11](../Lec07_Lists-and-Dictionaries/Concepts_Lecture.md#11-dictionaries)). Settings absent from the file therefore remain at their defaults. The default settings are copied with `copy.deepcopy()`, because one of the values of `DEFAULTS` is a list.

**Code:**

```python
import copy
import json
from pathlib import Path

DEFAULTS = {"user": "guest", "volume": 5, "recent": []}

def load_settings(path):
    settings = copy.deepcopy(DEFAULTS)    # never share the default list
    p = Path(path)
    if p.exists():
        with open(p, encoding="utf-8") as f:
            settings.update(json.load(f))
    return settings

def save_settings(path, settings):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(settings, f, ensure_ascii=False, indent=2)

s = load_settings("settings.json")
print("불러온 설정:", s)
s["volume"] += 1
s["recent"].append("보고서" + str(s["volume"]) + ".txt")
save_settings("settings.json", s)
print("저장한 설정:", s)
print("기본값:", DEFAULTS)
```

**Output:** The results of the first run and of the second run.

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

After the second run, `settings.json` is as follows.

```text
{
  "user": "guest",
  "volume": 7,
  "recent": [
    "보고서6.txt",
    "보고서7.txt"
  ]
}
```

- **Why a deep copy is needed:** `dict(DEFAULTS)` and `DEFAULTS.copy()` are shallow copies, so `settings["recent"]` and `DEFAULTS["recent"]` refer to the same list ([Lecture 7, Section 9.3](../Lec07_Lists-and-Dictionaries/Concepts_Lecture.md#93-shallow-copy)). If `s["recent"].append(...)` is done in the first run, `DEFAULTS["recent"]` also becomes `['보고서6.txt']`, and defaults loaded again in the same run are contaminated. `deepcopy()` creates the inner list anew as well.
- **`ensure_ascii=False` and `indent=2`:** The Hangul file names are not escaped, and the file is saved in a form that people can open and edit directly ([Lecture 10, Section 8.2](Concepts_Lecture.md#82-jsondump-and-jsonload)).
- **A broken file:** If a user edits the settings file by hand and breaks the JSON syntax, `json.load()` raises a `JSONDecodeError`. A way to start from the defaults even in that case is built with the exception handling of Lecture 11.
