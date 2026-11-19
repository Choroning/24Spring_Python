# Lecture 10 — File Input and Output

[Repository Guide](../../README.md) | [English](Concepts_Lecture.md) | [한국어](Concepts_Lecture.ko.md)

> **Last Updated:** 2026-11-19

> **Learning Objectives:**
> 1. Distinguish text files from binary files, and compute how a string becomes bytes when encoded in UTF-8 and cp949
> 2. Choose the `open()` mode that fits a purpose and open and close files safely with the `with` statement
> 3. Read files with `read()`, `readline()`, `readlines()`, and iteration over the file object, and compare the uses of each method
> 4. Write to files with `write()`, `writelines()`, and `print(file=)`, and explain how newline translation and buffering behave
> 5. Build paths with the `Path` objects of `pathlib` and work with files and folders
> 6. Save and read back tabular data and structured data with the `csv` and `json` modules

---

## Table of Contents

- [1. Files and Character Encodings](#1-files-and-character-encodings)
  - [1.1 Why Files Are Needed](#11-why-files-are-needed)
  - [1.2 Text Files and Binary Files](#12-text-files-and-binary-files)
  - [1.3 Character Encodings and UTF-8](#13-character-encodings-and-utf-8)
  - [1.4 When Encodings Do Not Match](#14-when-encodings-do-not-match)
- [2. Opening and Closing Files](#2-opening-and-closing-files)
  - [2.1 The open() Function and File Objects](#21-the-open-function-and-file-objects)
  - [2.2 File Modes](#22-file-modes)
  - [2.3 Closing Files with the with Statement](#23-closing-files-with-the-with-statement)
  - [2.4 Relative Paths and the Working Directory](#24-relative-paths-and-the-working-directory)
- [3. Reading Files](#3-reading-files)
  - [3.1 Reading Everything with read()](#31-reading-everything-with-read)
  - [3.2 readline() and readlines()](#32-readline-and-readlines)
  - [3.3 Iterating over a File Object](#33-iterating-over-a-file-object)
  - [3.4 Processing the Lines Read](#34-processing-the-lines-read)
- [4. Writing Files](#4-writing-files)
  - [4.1 write() and writelines()](#41-write-and-writelines)
  - [4.2 Writing to Files with print()](#42-writing-to-files-with-print)
  - [4.3 Opening Two Files Together](#43-opening-two-files-together)
  - [4.4 Newline Translation](#44-newline-translation)
  - [4.5 Buffering and flush()](#45-buffering-and-flush)
- [5. Binary Files](#5-binary-files)
  - [5.1 Reading and Writing Bytes](#51-reading-and-writing-bytes)
  - [5.2 seek() and tell()](#52-seek-and-tell)
  - [5.3 Copying a Large File in Pieces](#53-copying-a-large-file-in-pieces)
- [6. Handling Paths with pathlib](#6-handling-paths-with-pathlib)
  - [6.1 Path Objects](#61-path-objects)
  - [6.2 Working with Files and Folders](#62-working-with-files-and-folders)
- [7. CSV Files](#7-csv-files)
  - [7.1 The CSV Format](#71-the-csv-format)
  - [7.2 csv.writer and csv.reader](#72-csvwriter-and-csvreader)
  - [7.3 DictWriter and DictReader](#73-dictwriter-and-dictreader)
- [8. JSON Files](#8-json-files)
  - [8.1 The JSON Format and Python Data Types](#81-the-json-format-and-python-data-types)
  - [8.2 json.dump() and json.load()](#82-jsondump-and-jsonload)
- [Concept Applications](#concept-applications)
- [Summary](#summary)
- [Self-Check Questions](#self-check-questions)
- [References](#references)

---

<br>

## 1. Files and Character Encodings

### 1.1 Why Files Are Needed

The programs so far received data with `input()` at every run and showed results on the screen with `print()`. Values stored in variables and lists live in main memory (RAM), so they disappear when the program ends ([Lecture 1](../Lec01_Computer-Architecture-and-Introduction-to-Python/Concepts_Lecture.md)). Data that must survive to the next run, such as grade sheets, settings, and game records, is stored in secondary storage (SSDs, hard disks) as a **file**.

A file is a sequence of bytes stored under a name in secondary storage. The operating system organizes files into folders (directories), and a program asks the operating system to open a file in order to read or write its bytes. In Python the built-in function `open()` makes this request.

| Aspect | Variables and Lists | Files |
|:-----|:-----|:-----|
| Location | Main memory | Secondary storage |
| Lifetime | Disappear when the program ends | Remain until deleted |
| Access | Used directly by name | Opened with `open()`, then read and write methods are called |
| Sharing with other programs | Impossible | Other programs can read the same file |

*Table 1. Comparison of data stored in variables and data stored in files*

### 1.2 Text Files and Binary Files

Every file is ultimately a sequence of bytes, but files fall into two kinds depending on how those bytes are interpreted.

> **Definition:** A **text file** is a file whose bytes are stored so that they represent characters according to a fixed character encoding. `.txt`, `.py`, `.csv`, `.json`, and `.html` files are text files.

> **Definition:** A **binary file** is a file whose bytes are not interpreted as characters but stored with the meaning that its format defines. Photographs (`.png`, `.jpg`), music, executables, and compressed files are binary files.

Python expresses this distinction with two data types. Text is `str`, a sequence of characters, and a sequence of bytes is `bytes`. A `bytes` value is written with `b` before the quotation marks, as `b"..."`, and each of its elements is an integer from 0 to 255. When a text file is opened in text mode, Python performs the conversion between bytes and strings, and when it is opened in binary mode, `bytes` pass through unconverted (Section 5) [1].

### 1.3 Character Encodings and UTF-8

> **Definition:** A **character encoding** is a rule that turns characters into a sequence of bytes. Turning a string into bytes is called encoding, and turning bytes back into a string is called decoding.

A Python string is a sequence of Unicode characters. Unicode is a standard that assigns a number called a code point to every character in the world's scripts; for example, `A` is U+0041 and `가` is U+AC00. There are several rules for storing the same code points as bytes, and the most widely used today is **UTF-8**. The rule long used by Korean Windows is **cp949** (Microsoft code page 949, an extension of EUC-KR) [2].

```python
s = "A가"
b = s.encode("utf-8")
print(type(s), type(b))
print(b, len(s), len(b))
print(list(b))
print(b.hex(" "))
c = s.encode("cp949")
print(c, len(c), c.hex(" "))
print(b.decode("utf-8"), c.decode("cp949"))
print(len("한글 파이썬".encode("utf-8")), len("한글 파이썬".encode("cp949")))
```

```text
<class 'str'> <class 'bytes'>
b'A\xea\xb0\x80' 2 4
[65, 234, 176, 128]
41 ea b0 80
b'A\xb0\xa1' 3 41 b0 a1
A가 A가
16 11
```

- **`encode()` and `decode()`:** `str.encode(encoding)` turns a string into `bytes`, and `bytes.decode(encoding)` turns `bytes` into a string. Encoding and decoding with the same encoding returns the original string.
- **The difference in length:** `"A가"` has 2 characters, but it is 4 bytes in UTF-8 and 3 bytes in cp949. `len()` counts characters for a `str` and bytes for a `bytes`.
- **How `bytes` are displayed:** As in `b'A\xea\xb0\x80'`, printable ASCII characters appear as they are and other bytes appear as `\x` followed by two hexadecimal digits. `list(b)` shows each byte as an integer, and `b.hex(" ")` shows them in hexadecimal. The form `hex(" ")`, which inserts a separator, is available from Python 3.8 [3]; in 3.7, `b.hex()` without arguments gives the hexadecimal digits joined without separators, as in `41eab080`.
- **The size of Hangul:** `"한글 파이썬"`, made of one space and five Hangul syllables, is $1 + 5 \times 3 = 16$ bytes in UTF-8 and $1 + 5 \times 2 = 11$ bytes in cp949. All 11,172 Hangul syllables (from U+AC00 `가` to U+D7A3 `힣`) are 3 bytes each in UTF-8 and 2 bytes each in cp949.

UTF-8 is a variable-length encoding that uses 1-4 bytes depending on the size of the code point [4].

| Code Point Range | Bytes | Bit Layout | Examples |
|:-----|-----:|:-----|:-----|
| U+0000 ~ U+007F | 1 | `0xxxxxxx` | `A`, digits, English punctuation |
| U+0080 ~ U+07FF | 2 | `110xxxxx 10xxxxxx` | `é`, Greek letters |
| U+0800 ~ U+FFFF | 3 | `1110xxxx 10xxxxxx 10xxxxxx` | Hangul, Chinese characters |
| U+10000 ~ U+10FFFF | 4 | `11110xxx 10xxxxxx 10xxxxxx 10xxxxxx` | Emoji |

*Table 2. Byte counts and bit layouts of UTF-8*

`가` (U+AC00) is in the third range, so it takes 3 bytes. Writing the code point `0xAC00` as a 16-bit binary number, splitting it from the front into 4, 6, and 6 bits, and filling the `x` positions of the bit layout gives `EA B0 80`.

```text
U+AC00 = 1010 1100 0000 0000 (16 binary bits)

                 ┌4 bits┐    ┌6 bits┐       ┌6 bits┐
  split bits         1010      110000         000000
  template       1110xxxx    10xxxxxx       10xxxxxx
  result         11101010    10110000       10000000
  hexadecimal       EA          B0             80
```

*Figure 1. Encoding 가 (U+AC00) into three UTF-8 bytes*

The leading `1110` of the first byte means "this character is 3 bytes long," and the `10` of the following bytes means "this byte continues the preceding character." As a result, a UTF-8 byte sequence lets character boundaries be found even when reading starts in the middle, and ASCII characters (U+0000-U+007F) are stored as the same single bytes as in ASCII.

### 1.4 When Encodings Do Not Match

Bytes do not record which encoding wrote them. Reading with an encoding different from the one used for writing garbles the text or causes an error. The following `mismatch.py` shows both cases.

```python
data = "한글".encode("utf-8")
print(data.hex(" "))
print(data.decode("cp949", errors="replace"))
legacy = "한글".encode("cp949")
print(legacy.hex(" "))
legacy.decode("utf-8")
```

```text
ed 95 9c ea b8 80
�븳湲�
c7 d1 b1 db
Traceback (most recent call last):
  File "mismatch.py", line 6, in <module>
    legacy.decode("utf-8")
    ~~~~~~~~~~~~~^^^^^^^^^
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xc7 in position 0: invalid continuation byte
```

- **Reading UTF-8 bytes as cp949:** The six bytes are wrongly grouped into cp949's 2-byte units, producing entirely different characters. `errors="replace"` means replace bytes that cannot be interpreted with `�` (U+FFFD); without this argument an error occurs. Meaningless characters that result from reading with the wrong encoding in this way are commonly called garbled text (mojibake).
- **Reading cp949 bytes as UTF-8:** The first byte `0xC7` is `11000111` in binary, the start of a 2-byte character, but the next byte `0xD1` (`11010001`) does not start with `10`, which violates the rules of UTF-8. Hence the `UnicodeDecodeError`.

The same thing happens when opening files. If `open()` is not given an `encoding`, Python 3.13 uses the operating system's locale encoding [1]. On macOS and most Linux systems this is UTF-8, but on Korean Windows it is cp949. The following `win_default.py` reproduces, with `encoding="cp949"`, the situation of reading a UTF-8 file as cp949.

```python
with open("memo.txt", "w", encoding="utf-8") as f:
    f.write("첫째 줄\n둘째 줄\n")

with open("memo.txt", encoding="cp949") as f:
    print(f.read())
```

```text
Traceback (most recent call last):
  File "win_default.py", line 5, in <module>
    print(f.read())
          ~~~~~~^^
UnicodeDecodeError: 'cp949' codec can't decode byte 0x84 in position 9: illegal multibyte sequence
```

A file saved without `encoding` on macOS and read without `encoding` on Korean Windows produces exactly this error. Conversely, writing a character that cp949 cannot represent (such as an emoji) to a cp949 file causes a `UnicodeEncodeError`. Therefore, **always state `encoding="utf-8"` explicitly** when opening text files [5]. Every example in this unit does so.

> **Caution:** Old text files made on Korean Windows and CSV files exported by some programs may be stored in cp949. Such files must be read with `encoding="cp949"`, and if the encoding is unknown, the bytes must be read and examined to decide. Because the encoding cannot be determined with certainty from a file's contents, the surest approach is for the parties exchanging files to agree on the encoding.

---

<br>

## 2. Opening and Closing Files

### 2.1 The open() Function and File Objects

Working with a file always takes three steps: **open** the file, read or **write** it, and **close** it.

```python
f = open("memo.txt", "w", encoding="utf-8")
n1 = f.write("첫째 줄\n")
n2 = f.write("둘째 줄\n")
f.close()
print(n1, n2)

f = open("memo.txt", "r", encoding="utf-8")
text = f.read()
f.close()
print(repr(text))
print(text, end="")
```

```text
5 5
'첫째 줄\n둘째 줄\n'
첫째 줄
둘째 줄
```

`open(file name, mode, encoding=encoding)` opens a file and returns an object that handles it.

> **Definition:** A **file object** is an object that represents an open file and lets the file's data be read and written through methods such as `read()` and `write()` [6]. A file object remembers the **file position**, the place where the next read or write happens.

- **Opening with `"w"` and writing:** `write()` writes a string to the file and returns the **number of characters** written. `"첫째 줄\n"` has 5 characters: 3 Hangul syllables, 1 space, and 1 newline. The file stores the $3 \times 3 + 1 + 1 = 11$ bytes of its UTF-8 encoding.
- **`write()` does not end the line:** Unlike `print()`, `write()` writes only the string it receives. To end a line, put `\n` at the end of the string explicitly.
- **Opening with `"r"` and reading:** `read()` returns everything from the file position to the end as one string. `repr(text)` shows the newline characters as `\n`, which confirms the exact contents of the file.
- **`close()`:** Closes the file, returns its resources to the operating system, and writes out any data not yet written to the file (Section 4.5).

### 2.2 File Modes

The mode, the second argument of `open()`, decides what is done with the file. If omitted, it is `"r"` [1].

| Mode | Meaning | If the File Does Not Exist | If the File Exists |
|:-----|:-----|:-----|:-----|
| `"r"` | Read (default) | `FileNotFoundError` | Reads from the beginning |
| `"w"` | Write | Creates it | **Erases all contents** and writes from the beginning |
| `"a"` | Append | Creates it | Writes after the existing contents |
| `"x"` | Create and write | Creates it | `FileExistsError` |
| `"b"` | Binary mode (combined with another mode, as in `"rb"`, `"wb"`) | Follows the other mode | Follows the other mode |
| `"t"` | Text mode (default; `"rt"` is the same as `"r"`) | Follows the other mode | Follows the other mode |
| `"+"` | Read and write together (`"r+"`, `"w+"`, and so on) | Follows the other mode | Follows the other mode |

*Table 3. The modes of open()*

The difference between `"w"` and `"a"` shows in the following program.

```python
with open("log.txt", "w", encoding="utf-8") as f:
    f.write("1번째 실행\n")
with open("log.txt", "w", encoding="utf-8") as f:
    f.write("2번째 실행\n")
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("3번째 실행\n")
with open("log.txt", encoding="utf-8") as f:
    print(f.read(), end="")
```

```text
2번째 실행
3번째 실행
```

The second `"w"` erased the first contents, so `1번째 실행` did not survive, and the line written with `"a"` was attached after the existing contents. A log file that accumulates a record at every run uses `"a"`. `with ... as f:` is discussed in Section 2.3; here it suffices to know that the file is closed when the indented part ends.

Opening a file that does not exist with `"r"` causes a `FileNotFoundError`.

```python
f = open("no_such_file.txt", encoding="utf-8")
```

```text
Traceback (most recent call last):
  File "missing.py", line 1, in <module>
    f = open("no_such_file.txt", encoding="utf-8")
FileNotFoundError: [Errno 2] No such file or directory: 'no_such_file.txt'
```

`[Errno 2]` is the error number reported by the operating system. The `"x"` mode prevents an existing file from being overwritten by mistake.

```python
with open("report.txt", "x", encoding="utf-8") as f:
    f.write("처음 만든 보고서\n")
print("report.txt를 만들었다")
with open("report.txt", "x", encoding="utf-8") as f:
    f.write("덮어쓰려는 내용\n")
```

```text
report.txt를 만들었다
Traceback (most recent call last):
  File "exclusive.py", line 4, in <module>
    with open("report.txt", "x", encoding="utf-8") as f:
         ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileExistsError: [Errno 17] File exists: 'report.txt'
```

How to handle such errors without stopping the program is covered in Lecture 11.

> **Caution:** Opening with `"w"` erases the existing contents at that moment. Even if the program stops with an error before writing anything, the file is already empty. Opening a file meant for reading with `"w"` by mistake loses data, so open files that are only read with the mode omitted or with `"r"`.

### 2.3 Closing Files with the with Statement

An open file must always be closed. If it is not, the data written last may not be recorded in the file (Section 4.5), and the operating system limits how many files one program can have open at once. Calling `f.close()` directly, however, has two weaknesses: it is easy to forget, and if an error occurs before `close()` is reached, it is never called.

The `with` statement closes the file automatically when the indented block ends. It closes the file even if an error occurs in the block [5].

```python
with open("memo.txt", encoding="utf-8") as f:
    print(f.closed)
    first = f.readline()
print(f.closed)
print(repr(first))
f.read()
```

```text
False
True
'첫째 줄\n'
Traceback (most recent call last):
  File "with_demo.py", line 6, in <module>
    f.read()
    ~~~~~~^^
ValueError: I/O operation on closed file.
```

- **`with open(...) as f:`:** Binds the file object returned by `open()` to the name `f` and runs the block.
- **Inside the block:** `f.closed` is `False`, so the file is open.
- **Outside the block:** The file was closed as the block ended, so `f.closed` is `True`. The name `f` and `first`, read inside the block, remain available outside it.
- **A closed file:** Trying to read a closed file causes a `ValueError`. Keep all code that works with the file inside the `with` block.

The `with` statement is used not only for files but for resources in general that "must always be cleaned up after use," and how it works is covered in Lecture 11 together with exceptions.

### 2.4 Relative Paths and the Working Directory

When only a file name is written without a folder, as in `open("memo.txt")`, Python looks for the file in the **current working directory**. A path written relative to the current working directory, such as `"data/scores.txt"`, is a **relative path**, and a path written from the top folder, such as `/Users/...` on macOS and Linux or `C:\Users\...` on Windows, is an **absolute path**.

The current working directory is not the folder containing the program file but **the place from which the program was run**. If a program is run from a terminal with `python proj/script.py`, the working directory is the folder outside `proj`, so opening the file next to `script.py` with `open("settings.txt")` fails to find it. When a file is opened and run in IDLE, the working directory becomes that file's folder, so the same code can work in IDLE and fail in a terminal. To find data next to the program file regardless of where it is run, build the path relative to the program file's folder with `Path(__file__).parent`, as in Section 6.1.

> **[Operating Systems]** A file system organizes files into a tree of folders and keeps one current working directory per process, interpreting relative paths with respect to it. When a file is opened, the operating system gives the process a number that refers to the file (a file descriptor), and subsequent reads and writes are requested with that number. The structure of file systems, the implementation of directories, and access permissions are covered in Operating Systems.

---

<br>

## 3. Reading Files

The examples in this section read the following `scores.txt`. The fourth line is blank.

```text
Kim 85
Lee 92
Park 78

Choi 90
```

### 3.1 Reading Everything with read()

```python
with open("scores.txt", encoding="utf-8") as f:
    text = f.read()
print(repr(text))
print(len(text))

with open("scores.txt", encoding="utf-8") as f:
    print(repr(f.read(6)))
    print(repr(f.read(6)))
    print(f.tell())
```

```text
'Kim 85\nLee 92\nPark 78\n\nChoi 90\n'
31
'Kim 85'
'\nLee 9'
12
```

- **`read()`:** Reads the entire file as one string. Newlines are included as `\n` characters, so the length is $7 + 7 + 8 + 1 + 8 = 31$ characters.
- **`read(n)`:** Reads at most `n` characters from the file position. The first `read(6)` read `'Kim 85'` and moved the file position past it, so the second `read(6)` starts reading at the newline.
- **`tell()`:** Reports the current file position. This file contains only ASCII characters, so 12 equals the number of bytes read, but in general the value that text-mode `tell()` returns is neither a character count nor a byte count; it is only good for passing back to `seek()` [6].

`read()` is simple, but it loads the whole file into memory. Reading a log file of several gigabytes with `read()` can exhaust memory, so large files are processed one line at a time as in Section 3.3.

### 3.2 readline() and readlines()

```python
with open("scores.txt", encoding="utf-8") as f:
    print(repr(f.readline()))
    print(repr(f.readline()))
    rest = f.readlines()
    print(rest)
    print(repr(f.readline()))
```

```text
'Kim 85\n'
'Lee 92\n'
['Park 78\n', '\n', 'Choi 90\n']
''
```

- **`readline()`:** Reads and returns one line, up to and including the newline character. The returned string ends with `\n`.
- **`readlines()`:** Reads all remaining lines and returns a list whose elements are the lines. Two lines were already read, so the list starts from the third line.
- **End of file:** When nothing is left to read, `readline()` returns the empty string `''`. A blank line is `'\n'`, so it is distinguishable from the end of the file [5].

This property allows a file to be read one line at a time with a `while` statement.

```python
with open("scores.txt", encoding="utf-8") as f:
    line = f.readline()
    while line != "":
        print(line.rstrip("\n"))
        line = f.readline()
```

```text
Kim 85
Lee 92
Park 78

Choi 90
```

When a blank line is met, `line` is `'\n'`, so the loop does not stop; it stops only at the `''` of the end of the file. `rstrip("\n")` removes newline characters from the right end of a string.

### 3.3 Iterating over a File Object

A file object can be iterated over with a `for` statement, giving one line per iteration. It does the same job as the `while` statement of Section 3.2 more briefly, and it keeps only one line in memory at a time, so it works for large files too [5]. This is the default way to process a text file line by line.

```python
with open("scores.txt", encoding="utf-8") as f:
    for line in f:
        print(repr(line))
```

```text
'Kim 85\n'
'Lee 92\n'
'Park 78\n'
'\n'
'Choi 90\n'
```

Printing each line as read with `print(line)` adds an extra blank line between lines, because the `\n` at the end of `line` and the `\n` that `print()` appends overlap. Write `print(line, end="")`, or remove the newline first with `line.rstrip("\n")`.

| Method | Return Value | Memory | When It Fits |
|:-----|:-----|:-----|:-----|
| `f.read()` | One string holding the whole file | The whole file | Processing a small file at once |
| `f.read(n)` | A string of at most `n` characters | `n` characters | Reading in pieces of a fixed size |
| `f.readline()` | One line (including the final `\n`), `''` at the end of the file | One line | Reading only the first line (a header) separately |
| `f.readlines()` | A list of all lines | The whole file | Moving among lines by index |
| `for line in f` | One line per iteration | One line | Processing lines in order (the default) |

*Table 4. Comparison of the ways to read a text file*

### 3.4 Processing the Lines Read

What is read from a file is always a string. Even a score `85` is read as the string `'85'`, so it must be converted with `int()` before computing ([Lecture 3](../Lec03_Data-Types/Concepts_Lecture.md)). The following program computes the average score while skipping blank lines.

```python
total = 0
count = 0
with open("scores.txt", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line == "":                   # skip blank lines
            continue
        name, score = line.split()
        total += int(score)
        count += 1
        print(name, score)
print("평균:", total / count)
```

```text
Kim 85
Lee 92
Park 78
Choi 90
평균: 86.25
```

- **`line.strip()`:** Removes whitespace and newlines at both ends. A blank line becomes `''`.
- **`continue`:** For a blank line, skips the rest and moves to the next line ([Lecture 5](../Lec05_Loops/Concepts_Lecture.md)).
- **`name, score = line.split()`:** Unpacks the two pieces split at whitespace into two variables ([Lecture 7, Section 7.4](../Lec07_Lists-and-Dictionaries/Concepts_Lecture.md#74-tuple-unpacking)). If a line does not have exactly two pieces, a `ValueError` occurs, so files of uncertain format are handled together with the exception handling of Lecture 11.
- **The average:** $(85 + 92 + 78 + 90) / 4 = 345 / 4 = 86.25$. The blank line was not counted, so the denominator is 4.

---

<br>

## 4. Writing Files

### 4.1 write() and writelines()

`write(string)` writes one string, and `writelines(list)` writes the strings of a list in turn.

```python
names = ["Kim", "Lee", "Park"]
with open("names.txt", "w", encoding="utf-8") as f:
    f.writelines(names)
with open("names.txt", encoding="utf-8") as f:
    print(repr(f.read()))

with open("names.txt", "w", encoding="utf-8") as f:
    f.writelines([name + "\n" for name in names])
with open("names.txt", encoding="utf-8") as f:
    print(repr(f.read()))

with open("nums.txt", "w", encoding="utf-8") as f:
    f.write(str(3.14) + "\n")
    f.write(3.14)
```

```text
'KimLeePark'
'Kim\nLee\nPark\n'
Traceback (most recent call last):
  File "write_lines.py", line 14, in <module>
    f.write(3.14)
    ~~~~~~~^^^^^^
TypeError: write() argument must be str, not float
```

- **`writelines()` does not end lines:** Despite its name, it adds no newline after each element, so the first result is `'KimLeePark'`. Passing a list made with a list comprehension that appends `"\n"` to each name stores one name per line ([Lecture 7, Section 5](../Lec07_Lists-and-Dictionaries/Concepts_Lecture.md#5-list-comprehensions)).
- **Only strings can be written:** Text-mode `write()` accepts only `str`, so passing the float 3.14 directly is a `TypeError`. Convert numbers with `str()` or string formatting before writing.

### 4.2 Writing to Files with print()

Given `file=file object`, `print()` writes to that file instead of the screen. `print()` takes care of the spaces between values, the final newline, and converting numbers to strings, so it is more convenient than `write()` for writing a mixture of values.

```python
with open("table.txt", "w", encoding="utf-8") as f:
    for i in range(1, 4):
        print(i, "x 7 =", i * 7, file=f)
    print("끝", file=f)
    print("a", "b", "c", sep=",", end=";\n", file=f)

with open("table.txt", encoding="utf-8") as f:
    print(f.read(), end="")
```

```text
1 x 7 = 7
2 x 7 = 14
3 x 7 = 21
끝
a,b,c;
```

`sep` and `end` behave exactly as they do when printing to the screen. Printing to the screen is in fact writing to the file object `sys.stdout`, the standard output that is the default value of `file`. Therefore a function that takes the output destination as a parameter writes to the screen when given `sys.stdout` and to a file when given an open file ([Lecture 9, Section 3.2](../Lec09_Inheritance-and-Polymorphism/Concepts_Lecture.md#32-duck-typing)).

### 4.3 Opening Two Files Together

One `with` statement can open several files separated by commas. The following program reads `memo.txt` and writes each line with a line number in front of it to a new file.

```python
with open("memo.txt", encoding="utf-8") as src, open("memo_numbered.txt", "w", encoding="utf-8") as dst:
    for no, line in enumerate(src, start=1):
        dst.write(str(no) + ": " + line)

with open("memo_numbered.txt", encoding="utf-8") as f:
    print(f.read(), end="")
```

```text
1: 첫째 줄
2: 둘째 줄
```

- **Two files:** The source `src` is opened for reading and the result `dst` for writing. Both files are closed when the block ends.
- **`enumerate(src, start=1)`:** A built-in function that gives a `(number, element)` pair at each iteration. The number starts at `start` and increases by 1, so the first line is `(1, '첫째 줄\n')`.
- **Newlines:** The `line` read already ends with `\n`, so no newline is added in `write()`.

> **Caution:** Opening the file being read with `"w"` at the same time erases its contents the moment `"w"` opens it, leaving nothing to read. To rewrite a file, write the result to another file and then swap them, or read all the contents first and then open the same file with `"w"`.

### 4.4 Newline Translation

The bytes that mark the end of a line differ by operating system convention. macOS and Linux use a single `\n` (LF, 0x0A), and Windows uses the two bytes `\r\n` (CR LF, 0x0D 0x0A). Python's text mode hides this difference. When reading, it translates `\n`, `\r`, and `\r\n` all to `\n` (universal newlines), and when writing, it translates `\n` to the operating system's newline `os.linesep` [1]. The `newline` parameter of `open()` controls this translation.

```python
import os
print(repr(os.linesep))

with open("crlf.txt", "w", encoding="utf-8", newline="\r\n") as f:
    f.write("a\nb\n")

with open("crlf.txt", "rb") as f:
    print(f.read())
with open("crlf.txt", encoding="utf-8") as f:
    print(repr(f.read()))
with open("crlf.txt", encoding="utf-8", newline="") as f:
    print(repr(f.read()))
```

```text
'\n'
b'a\r\nb\r\n'
'a\nb\n'
'a\r\nb\r\n'
```

- **`os.linesep`:** On the macOS system that produced this output it is `'\n'`. On Windows it is `'\r\n'`.
- **Writing with `newline="\r\n"`:** Each `\n` was stored as `\r\n`. Reading in binary mode (`"rb"`) shows the actual bytes without translation.
- **Reading with the default:** If `newline` is omitted, `\r\n` is read as `\n`. Therefore files made on Windows can be processed with the same code.
- **Reading with `newline=""`:** Lines are still split, but newline characters are not translated. The `csv` module of Section 7 handles newlines itself, so it requires this value.

### 4.5 Buffering and flush()

Writing to the disk directly at every `write()` call would be very slow, because disk access takes far longer than memory access. Therefore a file object collects the data to be written in a **buffer** in memory and hands it to the operating system all at once when the buffer fills or the file is closed. `flush()` sends the data collected in the buffer out immediately [6].

```python
f = open("buf.txt", "w", encoding="utf-8")
f.write("저장할 내용\n")

with open("buf.txt", encoding="utf-8") as g:
    print(repr(g.read()))

f.flush()
with open("buf.txt", encoding="utf-8") as g:
    print(repr(g.read()))
f.close()
```

```text
''
'저장할 내용\n'
```

Even after `write()` has finished, reading through another file object finds the file empty, because the written contents are still in the buffer. After `flush()` is called, the contents are visible. If a program ends abnormally without `close()`, data left in the buffer can be lost, which is another reason why closing with the `with` statement is safer. For a log file that another program must read in real time, call `flush()` after writing important lines.

> **[Systems Programming]** Python's buffer is a buffer on the application side, and `flush()` merely hands that data to the operating system. The operating system also keeps its own buffer inside the kernel (the page cache), so there is one more stage before the data is actually recorded on the disk, and forcing that stage requires a system call such as `os.fsync()`. The buffering schemes of the standard I/O library and their relationship with system I/O are covered in Systems Programming.

---

<br>

## 5. Binary Files

### 5.1 Reading and Writing Bytes

Adding `b` to the mode opens a file in binary mode. In binary mode there is no encoding and no newline translation; `read()` returns `bytes` and `write()` accepts `bytes` [5]. The following program creates and reads a file that imitates the beginning of a PNG image file. Every PNG file begins with the fixed 8 bytes `89 50 4E 47 0D 0A 1A 0A`, and programs check this signature to decide whether a file is a PNG [7].

```python
header = b"\x89PNG\r\n\x1a\n"
with open("fake.png", "wb") as f:
    f.write(header + bytes([0, 0, 0, 13]) + "데이터".encode("utf-8"))

with open("fake.png", "rb") as f:
    sig = f.read(8)
    print(sig)
    print(sig == header, f.tell())
    rest = f.read()
    print(rest, len(rest))
    f.seek(0)
    print(f.read(4))
    f.seek(-9, 2)
    print(f.read().decode("utf-8"))
```

```text
b'\x89PNG\r\n\x1a\n'
True 8
b'\x00\x00\x00\r\xeb\x8d\xb0\xec\x9d\xb4\xed\x84\xb0' 13
b'\x89PNG'
데이터
```

- **Writing:** A `b"..."` literal, `bytes([0, 0, 0, 13])` made from a list of integers, and the `bytes` of an encoded string are joined with `+`, writing 21 bytes.
- **`read(8)`:** In binary mode, `read(n)` reads `n` **bytes**. The signature matches, so the result is `True`, and the file position is 8.
- **`b'...\r...'`:** Byte 13 (0x0D) is merely displayed as `\r`; its value is 13.
- **`seek()`:** Covered in Section 5.2. The last 9 bytes are `"데이터"` encoded in UTF-8, so decoding them gives back the string.

Mixing binary mode and text mode causes errors.

```python
with open("fake.png", "rb") as f:
    data = f.read()
print(type(data), data[0], data[1:4])
with open("copy.png", "wb") as f:
    f.write("문자열")
```

```text
<class 'bytes'> 137 b'PNG'
Traceback (most recent call last):
  File "bin_err.py", line 5, in <module>
    f.write("문자열")
    ~~~~~~~^^^^^^^^^^
TypeError: a bytes-like object is required, not 'str'
```

Indexing `bytes` gives an integer from 0 to 255 (`0x89` is 137), and slicing gives `bytes`. To write a string to a file opened in binary mode, it must first be converted with `encode()`. Also, binary mode accepts no `encoding`; `open("x.bin", "rb", encoding="utf-8")` causes `ValueError: binary mode doesn't take an encoding argument`.

> **Caution:** Opening a binary file such as an image, music, or compressed file in text mode causes decoding errors or corrupts the file because newline translation changes bytes [5]. Handle files that are not text with `"rb"` and `"wb"`, whatever their contents.

### 5.2 seek() and tell()

`f.tell()` reports the current file position, and `f.seek(offset, whence)` moves it. A `whence` of 0 counts from the beginning of the file, 1 from the current position, and 2 from the end of the file. `f.seek(0)` in Section 5.1 returns to the beginning, and `f.seek(-9, 2)` moves to 9 bytes before the end of the file.

```text
byte offset  0                       8           12                          21
             ├──signature, 8 bytes───┼─length 4──┼──"데이터" UTF-8, 9 bytes──┤
              89 50 4E 47 0D 0A 1A 0A 00 00 00 0D EB 8D B0 EC 9D B4 ED 84 B0
             ▲                                   ▲                           ▲
          seek(0)                           seek(-9, 2)                 end of file
```

*Figure 2. File positions that seek() moves to in a 21-byte file*

In binary mode the file position is measured in bytes, so it can be moved freely to any position. In text mode a single character can span several bytes, so `seek()` should be given only `seek(0)`, which goes to the beginning, `seek(0, 2)`, which goes to the end, or a value previously returned by `tell()` [6].

### 5.3 Copying a Large File in Pieces

Reading a large binary file at once with `read()` loads the whole file into memory. Reading and writing in pieces of a fixed size uses only that much memory however large the file is. To show the behavior, the following function copies 4 bytes at a time. In practice, sizes from several kilobytes to several megabytes are used.

```python
def copy_file(src_path, dst_path, chunk_size=4):
    count = 0
    with open(src_path, "rb") as src, open(dst_path, "wb") as dst:
        while True:
            chunk = src.read(chunk_size)
            if not chunk:               # empty bytes means end of file
                break
            dst.write(chunk)
            count += 1
    return count

print(copy_file("fake.png", "copy.png"))
with open("fake.png", "rb") as a, open("copy.png", "rb") as b:
    print(a.read() == b.read())
```

```text
6
True
```

- **Detecting the end of the file:** Binary-mode `read()` returns the empty `bytes` `b''` at the end of the file, and empty `bytes` is false in a condition. Therefore `if not chunk:` ends the loop.
- **The number of pieces:** Reading 21 bytes 4 bytes at a time takes $\lceil 21 / 4 \rceil = 6$ reads, and the last piece is 1 byte.
- **Checking:** Comparing the bytes of the two files gives `True`, so the copy is identical to the original.

---

<br>

## 6. Handling Paths with pathlib

### 6.1 Path Objects

Joining paths as strings, as in `"data" + "/" + "scores.txt"`, requires dealing directly with separators that differ by operating system (`/` and `\`) and with duplicated separators. `Path` from the standard module `pathlib` handles paths as objects [8]. Joining `Path` objects, or a `Path` and a string, with the `/` operator creates a child path. This `/` is an instance of the operator overloading covered in Lecture 9.

```python
from pathlib import Path

p = Path("data") / "2024" / "scores.txt"
print(p)
print(p.name, p.stem, p.suffix)
print(p.parent, p.parent.parent)
print(p.parts)
print(p.with_suffix(".csv"))
print(p.exists(), p.is_absolute(), p.resolve().is_absolute())
```

```text
data/2024/scores.txt
scores.txt scores .txt
data/2024 data
('data', '2024', 'scores.txt')
data/2024/scores.csv
False False True
```

| Attribute or Method | Meaning | Value for `p` |
|:-----|:-----|:-----|
| `p.name` | The last part (the file name) | `'scores.txt'` |
| `p.stem` | The file name without the extension | `'scores'` |
| `p.suffix` | The extension | `'.txt'` |
| `p.parent` | The path of the folder directly above | `data/2024` |
| `p.parts` | A tuple of the parts that make up the path | `('data', '2024', 'scores.txt')` |
| `p.with_suffix(s)` | A new path with the extension changed to `s` | `data/2024/scores.csv` |
| `p.exists()` | Whether a file or folder exists at the path | `False` |
| `p.resolve()` | The absolute path with the current working directory prepended | `/.../data/2024/scores.txt` |

*Table 5. Main attributes and methods of Path objects*

Merely creating a `Path` object does not create a file. `p.exists()` is `False` because only the name of a path was created. The output is separated by `/` because it was obtained on macOS; on Windows the same code prints `data\2024\scores.txt`. `open()` also accepts a `Path` object instead of a string.

The problem of Section 2.4, finding data next to the program file regardless of where it is run, is solved with `Path(__file__).parent`. `__file__` is the path of the program file currently running.

```python
from pathlib import Path

here = Path(__file__).parent
data_file = here / "settings.txt"
data_file.write_text("level=3\n", encoding="utf-8")
print(data_file.name, data_file.parent == here)
print(Path.cwd() == here)
```

Saving this program as `proj/script_dir.py` and running it first from the outer folder with `python proj/script_dir.py` and then inside `proj` with `python script_dir.py` gives the following.

```text
settings.txt True
False
settings.txt True
True
```

Both times, `settings.txt` is created in the same `proj` folder as `script_dir.py`. The current working directory `Path.cwd()` is the outer folder in the first run, so it differs from `here`, and it is `proj` in the second run, so it is the same.

### 6.2 Working with Files and Folders

`Path` has methods that create folders, look inside folders, and read, write, and delete files [8].

```python
from pathlib import Path

folder = Path("data") / "2024"
folder.mkdir(parents=True, exist_ok=True)
for name in ["a.txt", "b.txt", "c.csv"]:
    (folder / name).write_text(name + "의 내용\n", encoding="utf-8")

print(sorted([p.name for p in folder.iterdir()]))
print(sorted([p.name for p in folder.glob("*.txt")]))
print((folder / "a.txt").read_text(encoding="utf-8"), end="")
print((folder / "a.txt").exists(), (folder / "z.txt").exists())
print(folder.is_dir(), (folder / "a.txt").is_file())
(folder / "c.csv").unlink()
print(sorted([p.name for p in folder.iterdir()]))
print((folder / "a.txt").stat().st_size)
```

```text
['a.txt', 'b.txt', 'c.csv']
['a.txt', 'b.txt']
a.txt의 내용
True False
True True
['a.txt', 'b.txt']
16
```

- **`mkdir(parents=True, exist_ok=True)`:** Creates a folder. `parents=True` also creates the intermediate folder `data` if it is missing, and `exist_ok=True` raises no error if the folder already exists. Without these two arguments, an existing folder causes a `FileExistsError` and a missing intermediate folder causes a `FileNotFoundError` [8].
- **`write_text()` and `read_text()`:** Open the file, write or read it, and close it in one call. They suit short files, and `encoding` is stated explicitly just as with `open()`.
- **`iterdir()` and `glob()`:** `iterdir()` gives every entry in the folder, and `glob("*.txt")` gives only the entries whose names match the pattern, one `Path` at a time. `*` matches any characters. The order is not fixed, so the names were sorted with `sorted()` before printing [8].
- **`unlink()`:** Deletes a file. A deleted file does not go to the trash and cannot be recovered.
- **`stat().st_size`:** Reports the size of the file in bytes. `"a.txt의 내용\n"` has 6 ASCII characters, 3 Hangul syllables, and 1 newline, so it is $6 + 3 \times 3 + 1 = 16$ bytes.

---

<br>

## 7. CSV Files

### 7.1 The CSV Format

> **Definition:** **CSV (comma-separated values)** is a text file format that writes one row of a table per line and separates the values within a row with commas.

It is the format most often used when spreadsheet programs and data analysis tools exchange tables. If a value contains a comma, a double quotation mark, or a newline, the value is enclosed in double quotation marks, and double quotation marks inside the value are doubled. Because of these rules, splitting CSV directly with `split(",")` gives wrong results. The standard module `csv` handles the rules [9].

### 7.2 csv.writer and csv.reader

```python
import csv

rows = [
    ["이름", "점수", "메모"],
    ["Kim", 85, "성실함"],
    ["Lee, Jr.", 92, '별명은 "번개"'],
    ["Park", 78, "두 줄\n메모"],
]
with open("scores.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

with open("scores.csv", encoding="utf-8", newline="") as f:
    print(repr(f.read()))
```

```text
'이름,점수,메모\r\nKim,85,성실함\r\n"Lee, Jr.",92,"별명은 ""번개"""\r\nPark,78,"두 줄\n메모"\r\n'
```

- **`csv.writer(f)`:** Takes a file object and creates an object that writes CSV. `writerow(list)` writes one row, and `writerows(list of lists)` writes several rows. The number 85 is written automatically as the string `85`.
- **Quoting:** The value `Lee, Jr.`, which contains a comma, the value containing double quotation marks, and the value containing a newline were enclosed in double quotation marks, and each `"` inside a value was written as `""`.
- **End of a row:** The `csv` module writes `\r\n` at the end of each row by default [9].
- **`newline=""`:** The `csv` module handles newlines itself, so the file must be opened without newline translation. Without this argument, newlines inside quoted values are misinterpreted, and on Windows an extra `\r` is added when writing [9].

```python
import csv

with open("scores.csv", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)
    print(header)
    for row in reader:
        print(row)

with open("scores.csv", encoding="utf-8", newline="") as f:
    lines = f.read().split("\n")
print(lines[2].split(","))
```

```text
['이름', '점수', '메모']
['Kim', '85', '성실함']
['Lee, Jr.', '92', '별명은 "번개"']
['Park', '78', '두 줄\n메모']
['"Lee', ' Jr."', '92', '"별명은 ""번개"""\r']
```

- **`csv.reader(f)`:** Gives one row per iteration as a list of strings. The commas and newlines inside quoted values have been restored.
- **`next(reader)`:** A built-in function that takes out the next row. Taking out the header row first leaves the `for` statement to loop over the data rows only.
- **Every value is a string:** Even the score is read as `'85'`, so convert it with `int()` before computing [9].
- **The failure of splitting directly:** Splitting lines and commas by hand, as in the last line, cuts `Lee, Jr.` into two pieces and mixes quotation marks and `\r` into the values.

### 7.3 DictWriter and DictReader

Handling rows as dictionaries instead of lists lets columns be referred to by name rather than by number.

```python
import csv

students = [
    {"name": "Kim", "score": 85},
    {"name": "Lee", "score": 92},
    {"name": "Park", "score": 78},
]
with open("students.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "score"])
    writer.writeheader()
    writer.writerows(students)

total = 0
with open("students.csv", encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        print(row)
        total += int(row["score"])
print(total)
```

```text
{'name': 'Kim', 'score': '85'}
{'name': 'Lee', 'score': '92'}
{'name': 'Park', 'score': '78'}
255
```

- **`DictWriter`:** The names and order of the columns must be given with `fieldnames`. `writeheader()` writes the column names on the first line, and `writerows()` writes the values of each dictionary in that order. If a dictionary has a key not in `fieldnames`, a `ValueError` occurs by default [9].
- **`DictReader`:** Uses the first row as the column names and gives the remaining rows as `{column name: value}` dictionaries. The values are still strings.
- **The total:** $85 + 92 + 78 = 255$.

> **Note:** Some programs prepend the 3 bytes `EF BB BF` (a BOM) to a UTF-8 file to mark it as UTF-8. In Python, the encoding `"utf-8-sig"` writes these 3 bytes when writing and skips them when reading if they are at the start [2]. Reading a file with a BOM as `"utf-8"` makes the first value start with the invisible character U+FEFF, as in `'\ufeff이름'`, so `row["이름"]` becomes a `KeyError`. Read such files with `encoding="utf-8-sig"`.

---

<br>

## 8. JSON Files

### 8.1 The JSON Format and Python Data Types

> **Definition:** **JSON (JavaScript Object Notation)** is a text format that represents structured data by nesting objects (sets of name-value pairs), arrays, strings, numbers, true and false, and null.

While CSV suits tables in which every row has the same columns, JSON suits nested data, such as a list containing dictionaries that contain lists in turn. It is widely used as the format in which web services exchange data, and also for configuration files. The standard module `json` maps Python values and JSON text as follows [10].

| Python | JSON | Example |
|:-----|:-----|:-----|
| `dict` | Object | `{"age": 20}` |
| `list`, `tuple` | Array | `[85, 92]` |
| `str` | String | `"홍길동"` |
| `int`, `float` | Number | `20`, `3.5` |
| `True`, `False` | `true`, `false` | `false` |
| `None` | `null` | `null` |

*Table 6. Correspondence between Python data types and JSON*

JSON strings must be enclosed in double quotation marks, and true and false are the lowercase `true` and `false`. This resembles the way a Python dictionary looks when printed (`{'name': 'Kim', 'ok': True}`), but it is not the same.

### 8.2 json.dump() and json.load()

`json.dump(value, file)` writes a Python value to a file as JSON text, and `json.load(file)` reads JSON text from a file and returns it as a Python value. There are also `json.dumps()` and `json.loads()`, which exchange strings instead of files (the final `s` stands for string). JSON files are written and read in UTF-8 [5].

```python
import json

profile = {
    "name": "홍길동",
    "age": 20,
    "scores": [85, 92],
    "graduated": False,
    "advisor": None,
}
print(json.dumps(profile))
print(json.dumps(profile, ensure_ascii=False))

with open("profile.json", "w", encoding="utf-8") as f:
    json.dump(profile, f, ensure_ascii=False, indent=2)

with open("profile.json", encoding="utf-8") as f:
    print(f.read())

with open("profile.json", encoding="utf-8") as f:
    loaded = json.load(f)
print(loaded == profile, type(loaded["scores"]))
```

```text
{"name": "\ud64d\uae38\ub3d9", "age": 20, "scores": [85, 92], "graduated": false, "advisor": null}
{"name": "홍길동", "age": 20, "scores": [85, 92], "graduated": false, "advisor": null}
{
  "name": "홍길동",
  "age": 20,
  "scores": [
    85,
    92
  ],
  "graduated": false,
  "advisor": null
}
True <class 'list'>
```

- **`ensure_ascii`:** With the default `True`, non-ASCII characters are replaced by escapes such as `\ud64d`. The meaning is the same but people cannot read it, so JSON containing Hangul is written with `ensure_ascii=False` [10].
- **`indent=2`:** Indents nested structures by two spaces per level so that people can read them easily. If omitted, everything is written on one line [10].
- **Value correspondence:** `False` was written as `false` and `None` as `null`, and reading turns them back into `False` and `None`.
- **Round trip:** The `loaded` value read back equals the original dictionary.

Not every value comes back unchanged.

```python
import json

data = {1: "one", "pt": (3, 4)}
text = json.dumps(data)
print(text)
back = json.loads(text)
print(back)
print(back == data)
```

```text
{"1": "one", "pt": [3, 4]}
{'1': 'one', 'pt': [3, 4]}
False
```

- **Keys are always strings:** The keys of a JSON object can only be strings, so the integer key 1 becomes `"1"` and comes back as the string `'1'` when read [10].
- **Tuples become lists:** JSON has no tuples, so a tuple is written as an array and becomes a list when read.
- **Values that cannot be represented:** Sets and objects of user-defined classes have no corresponding JSON form. `json.dumps({"s": {1, 2}})` causes `TypeError: Object of type set is not JSON serializable`, so convert such values to lists or dictionaries before saving.

> **Caution:** A string made from a Python dictionary with `str()` is not JSON. Passing `"{'name': 'Kim'}"`, which uses single quotation marks, to `json.loads()` causes `json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)`. Always write JSON files with `json.dump()`.

---

<br>

## Concept Applications

When saving data to a file, choose the format and the way of opening the file according to the shape of the data and who will read the file.

| Situation | Choice |
|:-----|:-----|
| Accumulate one line with the time and result at every run of a program. | Open with `open(path, "a", encoding="utf-8")` and append one line at a time with `print(..., file=f)`. |
| Store the names and three subject scores of 1,000 students so that they can also be opened in a spreadsheet. | Every row has the same columns, so save as CSV with `csv.DictWriter`, opening the file with `newline=""`. |
| Save user settings (name, volume, list of recent files) and load them unchanged at the next run. | The structure is nested, so save with `json.dump(..., ensure_ascii=False, indent=2)` and read with `json.load()`. |
| Count only the lines containing `ERROR` in a log file of several gigabytes. | Read one line at a time with `for line in f:` and count. `read()` and `readlines()` load the whole file into memory. |
| Copy a photo file to another folder. | Open with `"rb"` and `"wb"` and copy in pieces of a fixed size. |
| Read on macOS an old Notepad file made on Korean Windows. | Open with `encoding="cp949"`. Reading as UTF-8 causes a `UnicodeDecodeError`. |
| Find the `config.json` next to the program file regardless of where it is run. | Build the path with `Path(__file__).parent / "config.json"`. |

*Table 7. File formats and ways of opening files that fit each situation*

**True/False Check:**

| Statement | Judgment and Reason |
|:-----|:-----|
| `len("한글".encode("utf-8"))` is 2. | **F.** A Hangul syllable is 3 bytes in UTF-8, so it is 6. The character count 2 is `len("한글")` (Section 1.3). |
| Opening a file with `open("data.txt", "w")` and closing it without writing anything keeps the original contents. | **F.** `"w"` erases the contents at the moment of opening, so the file becomes empty (Section 2.2). |
| If an error occurs inside a `with` statement, the file is not closed. | **F.** The `with` statement closes the file however the block ends (Section 2.3). |
| If `readline()` returns `''`, a blank line was read. | **F.** A blank line is `'\n'`, and `''` is the end of the file (Section 3.2). |
| `f.writelines(["a", "b"])` writes `a` and `b` on two lines. | **F.** `writelines()` adds no newlines, so `ab` is written (Section 4.1). |
| Scores read with `csv.reader` can be added directly as integers. | **F.** Every value read from CSV is a string, so it must be converted with `int()` (Section 7.2). |
| A dictionary with integer keys saved as JSON and read back equals the original dictionary. | **F.** JSON keys are strings, so integer keys become string keys (Section 8.2). |

---

<br>

## Summary

| Concept | Key Summary |
|:-----|:-----|
| File | A sequence of bytes stored under a name in secondary storage, so the data remains after the program ends. |
| Text and binary files | A text file holds bytes that represent characters according to an encoding and is handled as `str`; a binary file holds bytes defined by its format and is handled as `bytes`. |
| Character encoding | A rule that turns characters into bytes; UTF-8 stores a Hangul syllable in 3 bytes and cp949 in 2 bytes. |
| Encoding mismatch | Reading with an encoding different from the one used for writing garbles text or causes a `UnicodeDecodeError`, so always state `encoding="utf-8"`. |
| `open()` and file objects | `open(path, mode, encoding=...)` returns a file object that remembers the file position, and the modes `r`, `w`, `a`, `x`, `b`, and `+` set its purpose. |
| The `with` statement | Closes the file automatically when the block ends, even if an error occurred. |
| Relative path | Interpreted relative to the current working directory, which is the place from which the program was run, not the location of the program file. |
| Reading files | `read()` gives everything, `readline()` one line, and `readlines()` a list of lines, and `for line in f` is the default for line-by-line processing. |
| Writing files | `write()` and `writelines()` add no newlines and accept only strings, while `print(file=f)` performs conversion and adds the newline. |
| Newlines and buffering | Text mode unifies newlines as `\n`, and written data collects in a buffer until `flush()` or `close()` hands it to the operating system. |
| Binary mode | `"rb"` and `"wb"` exchange `bytes` without conversion, and `seek()` and `tell()` handle positions in bytes. |
| `pathlib` | Join `Path` objects with `/` to build paths, and work with files and folders through `name`, `suffix`, `parent`, `mkdir()`, `glob()`, and `read_text()`. |
| CSV | A comma-separated table format; the `csv` module handles the quoting rules, files are opened with `newline=""`, and every value read is a string. |
| JSON | A text format for nested data, saved and read with `json.dump()` and `json.load()`, in which keys become strings. |

---

<br>

## Self-Check Questions

1. **Computing encodings:** Find the number of bytes of the string `"Py파이썬3"` encoded in UTF-8 and in cp949. Also decide from Table 2 how many bytes `"é"` (U+00E9) takes in UTF-8.

   <details>
   <summary>Answer</summary>

   The ASCII characters `P`, `y`, and `3` are 1 byte each in both encodings, and the three Hangul syllables are 3 bytes each in UTF-8 and 2 bytes each in cp949. UTF-8 therefore takes $3 + 3 \times 3 = 12$ bytes and cp949 $3 + 3 \times 2 = 9$ bytes. U+00E9 is in the range U+0080-U+07FF, so it takes 2 bytes in UTF-8 (`C3 A9`).

   </details>

2. **Choosing a mode:** Write the appropriate mode for each of the following three cases. (1) Append today's record after the existing records. (2) Fail rather than overwrite if a file with the same name already exists. (3) Read the first 8 bytes of an image file.

   <details>
   <summary>Answer</summary>

   (1) `"a"`. It creates the file if it is missing and writes at the end if it exists. (2) `"x"`. If the file already exists, a `FileExistsError` occurs. (3) `"rb"`. In binary mode, `read(8)` reads 8 bytes as `bytes`.

   </details>

3. **The with statement:** In the following code, the program stopped with an error at `int("x")` on the line after `f.write()`. Explain what would differ if the same thing were done without the `with` statement, using `f = open(...)` and `f.close()`.

   ```python
   with open("out.txt", "w", encoding="utf-8") as f:
       f.write("결과\n")
       n = int("x")
   ```

   <details>
   <summary>Answer</summary>

   The `with` statement closes the file even when an error occurs in the block, so the `"결과\n"` in the buffer is recorded in the file. If `f.close()` had been written at the end of the block, the error would prevent reaching that line, and the file would not be closed. It may be cleaned up when the program ends, but this is not guaranteed, and in long-running programs unclosed files accumulate.

   </details>

4. **End of file:** What problem arises if the termination condition of a loop that reads a file with `readline()` is written as `if line.strip() == "": break`?

   <details>
   <summary>Answer</summary>

   A blank line `'\n'` also becomes `''` after `strip()`, so the loop ends at a blank line in the middle of the file and the lines after it are never read. The end of the file is when `line` as returned by `readline()` is itself `''`, so the test must be `if line == "": break`. Using `for line in f:` makes such a test unnecessary.

   </details>

5. **Printing newlines:** Write how many lines the following code prints and why. The contents of the file `a.txt` are `'x\ny\n'`.

   ```python
   with open("a.txt", encoding="utf-8") as f:
       for line in f:
           print(line)
   ```

   <details>
   <summary>Answer</summary>

   Four lines are printed: `x`, a blank line, `y`, and a blank line. Each `line` read, `'x\n'` and `'y\n'`, ends with a newline, and `print()` adds one more. Writing `print(line, end="")` or `print(line.rstrip("\n"))` prints only two lines.

   </details>

6. **CSV:** How is a row with the name `"Kim, Minsu"` and the score 90 stored in the file when written with `csv.writer`? What happens when this line is split with `split(",")`?

   <details>
   <summary>Answer</summary>

   The name contains a comma, so it is enclosed in double quotation marks and stored as `"Kim, Minsu",90`. Splitting with `split(",")` gives three pieces, `['"Kim', ' Minsu"', '90']`, cutting the name apart and leaving quotation marks in the values. Reading with `csv.reader` splits it correctly into `['Kim, Minsu', '90']`.

   </details>

7. **JSON:** What value results when `{"scores": (90, 85), 2024: True}` is saved with `json.dump()` and read with `json.load()`? Write every difference from the original value.

   <details>
   <summary>Answer</summary>

   The result is `{'scores': [90, 85], '2024': True}`. The tuple `(90, 85)` is written as a JSON array and comes back as a list, and the integer key 2024 becomes `'2024'` because JSON object keys must be strings. `True` is written as `true` and becomes `True` again, so it is unchanged.

   </details>

8. **Paths:** Write the `name`, `stem`, `suffix`, and `parent` of `Path("report/2024/final.txt")`, and write the code that must run first if the folders may not exist before the file at this path is written.

   <details>
   <summary>Answer</summary>

   They are `'final.txt'`, `'final'`, `'.txt'`, and `report/2024` in order. If the folders are missing, `open()` raises a `FileNotFoundError`, so first create `report` and `report/2024` with `p.parent.mkdir(parents=True, exist_ok=True)`. Because of `exist_ok=True`, no error occurs if the folders already exist.

   </details>

---

<br>

## References

1. Python Software Foundation, "Built-in Functions: open()," *The Python Standard Library*, Python 3.13. https://docs.python.org/3.13/library/functions.html#open
2. Python Software Foundation, "codecs - Codec registry and base classes," *The Python Standard Library*, Python 3.13. https://docs.python.org/3.13/library/codecs.html
3. Python Software Foundation, "Built-in Types," *The Python Standard Library*, Python 3.13. https://docs.python.org/3.13/library/stdtypes.html
4. F. Yergeau, "UTF-8, a transformation format of ISO 10646," RFC 3629, Nov. 2003. https://www.rfc-editor.org/rfc/rfc3629
5. Python Software Foundation, "Input and Output," *The Python Tutorial*, Python 3.13. https://docs.python.org/3.13/tutorial/inputoutput.html
6. Python Software Foundation, "io - Core tools for working with streams," *The Python Standard Library*, Python 3.13. https://docs.python.org/3.13/library/io.html
7. W3C, "Portable Network Graphics (PNG) Specification (Third Edition)," W3C Recommendation, 2025. https://www.w3.org/TR/png-3/
8. Python Software Foundation, "pathlib - Object-oriented filesystem paths," *The Python Standard Library*, Python 3.13. https://docs.python.org/3.13/library/pathlib.html
9. Python Software Foundation, "csv - CSV File Reading and Writing," *The Python Standard Library*, Python 3.13. https://docs.python.org/3.13/library/csv.html
10. Python Software Foundation, "json - JSON encoder and decoder," *The Python Standard Library*, Python 3.13. https://docs.python.org/3.13/library/json.html
