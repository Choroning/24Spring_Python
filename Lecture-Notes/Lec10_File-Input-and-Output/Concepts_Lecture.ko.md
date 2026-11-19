# 10강 — 파일 입출력

[레포지토리 안내](../../README.ko.md) | [English](Concepts_Lecture.md) | [한국어](Concepts_Lecture.ko.md)

> **최종 수정일:** 2026-11-19

> **학습 목표:**
> 1. 텍스트 파일과 이진 파일을 구분하고, 문자열이 UTF-8과 cp949로 인코딩되어 바이트가 되는 과정을 계산할 수 있다
> 2. `open()`의 모드를 목적에 맞게 고르고 `with`문으로 파일을 안전하게 열고 닫을 수 있다
> 3. `read()`, `readline()`, `readlines()`, 파일 객체의 순회로 파일을 읽고 각 방법의 쓰임을 비교할 수 있다
> 4. `write()`, `writelines()`, `print(file=)`로 파일에 쓰고 줄바꿈 변환과 버퍼링의 동작을 설명할 수 있다
> 5. `pathlib`의 `Path` 객체로 경로를 조립하고 파일과 폴더를 다룰 수 있다
> 6. `csv`와 `json` 모듈로 표 형식의 데이터와 구조를 가진 데이터를 저장하고 다시 읽을 수 있다

---

## 목차

- [1. 파일과 문자 인코딩](#1-파일과-문자-인코딩)
  - [1.1 파일이 필요한 이유](#11-파일이-필요한-이유)
  - [1.2 텍스트 파일과 이진 파일](#12-텍스트-파일과-이진-파일)
  - [1.3 문자 인코딩과 UTF-8](#13-문자-인코딩과-utf-8)
  - [1.4 인코딩이 맞지 않을 때](#14-인코딩이-맞지-않을-때)
- [2. 파일 열고 닫기](#2-파일-열고-닫기)
  - [2.1 open() 함수와 파일 객체](#21-open-함수와-파일-객체)
  - [2.2 파일 모드](#22-파일-모드)
  - [2.3 with문으로 파일 닫기](#23-with문으로-파일-닫기)
  - [2.4 상대 경로와 작업 폴더](#24-상대-경로와-작업-폴더)
- [3. 파일 읽기](#3-파일-읽기)
  - [3.1 read()로 한꺼번에 읽기](#31-read로-한꺼번에-읽기)
  - [3.2 readline()과 readlines()](#32-readline과-readlines)
  - [3.3 파일 객체의 순회](#33-파일-객체의-순회)
  - [3.4 읽은 줄의 가공](#34-읽은-줄의-가공)
- [4. 파일 쓰기](#4-파일-쓰기)
  - [4.1 write()와 writelines()](#41-write와-writelines)
  - [4.2 print()로 파일에 쓰기](#42-print로-파일에-쓰기)
  - [4.3 두 파일을 함께 열기](#43-두-파일을-함께-열기)
  - [4.4 줄바꿈 문자의 변환](#44-줄바꿈-문자의-변환)
  - [4.5 버퍼링과 flush()](#45-버퍼링과-flush)
- [5. 이진 파일](#5-이진-파일)
  - [5.1 바이트의 읽기와 쓰기](#51-바이트의-읽기와-쓰기)
  - [5.2 seek()와 tell()](#52-seek와-tell)
  - [5.3 큰 파일을 나누어 복사하기](#53-큰-파일을-나누어-복사하기)
- [6. pathlib으로 경로 다루기](#6-pathlib으로-경로-다루기)
  - [6.1 Path 객체](#61-path-객체)
  - [6.2 파일과 폴더의 조작](#62-파일과-폴더의-조작)
- [7. CSV 파일](#7-csv-파일)
  - [7.1 CSV 형식](#71-csv-형식)
  - [7.2 csv.writer와 csv.reader](#72-csvwriter와-csvreader)
  - [7.3 DictWriter와 DictReader](#73-dictwriter와-dictreader)
- [8. JSON 파일](#8-json-파일)
  - [8.1 JSON 형식과 파이썬 자료형](#81-json-형식과-파이썬-자료형)
  - [8.2 json.dump()와 json.load()](#82-jsondump와-jsonload)
- [개념 적용](#개념-적용)
- [요약](#요약)
- [점검 문제](#점검-문제)
- [참고 문헌](#참고-문헌)

---

<br>

## 1. 파일과 문자 인코딩

### 1.1 파일이 필요한 이유

지금까지의 프로그램은 실행할 때마다 `input()`으로 데이터를 받고 결과를 `print()`로 화면에 보였다. 변수와 리스트에 저장한 값은 주기억장치(RAM)에 있으므로 프로그램이 끝나면 사라진다([1강](../Lec01_Computer-Architecture-and-Introduction-to-Python/Concepts_Lecture.ko.md)). 성적표, 설정, 게임의 기록처럼 다음 실행에도 남아야 하는 데이터는 보조기억장치(SSD, 하드 디스크)에 **파일(file)** 로 저장한다.

파일은 보조기억장치에 이름을 붙여 저장한 바이트의 나열이다. 운영체제는 파일을 폴더(디렉터리)로 묶어 관리하고, 프로그램은 운영체제에 파일을 열어 달라고 요청하여 그 바이트를 읽거나 쓴다. 파이썬에서는 내장 함수 `open()`이 이 요청을 맡는다.

| 구분 | 변수와 리스트 | 파일 |
|:-----|:-----|:-----|
| 저장 위치 | 주기억장치 | 보조기억장치 |
| 수명 | 프로그램이 끝나면 사라진다 | 지울 때까지 남는다 |
| 접근 방법 | 이름으로 바로 쓴다 | `open()`으로 열고 읽기, 쓰기 메서드를 호출한다 |
| 다른 프로그램과의 공유 | 할 수 없다 | 다른 프로그램이 같은 파일을 읽을 수 있다 |

*표 1. 변수에 저장한 데이터와 파일에 저장한 데이터의 비교*

### 1.2 텍스트 파일과 이진 파일

모든 파일은 결국 바이트의 나열이지만, 그 바이트를 어떻게 해석하느냐에 따라 두 종류로 나눈다.

> **용어 정의:** **텍스트 파일(text file)** 은 바이트가 정해진 문자 인코딩에 따라 문자를 나타내도록 저장한 파일이다. `.txt`, `.py`, `.csv`, `.json`, `.html` 파일이 텍스트 파일이다.

> **용어 정의:** **이진 파일(binary file)** 은 바이트를 문자로 해석하지 않고 그 형식이 정한 의미대로 저장한 파일이다. 사진(`.png`, `.jpg`), 음악, 실행 파일, 압축 파일이 이진 파일이다.

파이썬은 이 구분을 두 자료형으로 나타낸다. 텍스트는 문자의 나열인 `str`이고, 바이트의 나열은 `bytes`이다. `bytes`의 값은 따옴표 앞에 `b`를 붙여 `b"..."`로 쓰며, 각 요소는 0부터 255까지의 정수이다. 텍스트 파일을 텍스트 모드로 열면 파이썬이 바이트와 문자열 사이의 변환을 대신 해 주고, 이진 모드로 열면 변환 없이 `bytes`를 그대로 주고받는다(5절) [1].

### 1.3 문자 인코딩과 UTF-8

> **용어 정의:** **문자 인코딩(character encoding)** 은 문자를 바이트의 나열로 바꾸는 규칙이다. 문자열을 바이트로 바꾸는 것을 인코딩(encoding), 바이트를 문자열로 되돌리는 것을 디코딩(decoding)이라고 한다.

파이썬의 문자열은 유니코드(Unicode) 문자의 나열이다. 유니코드는 세계의 문자마다 코드 포인트(code point)라는 번호를 붙인 표준이며, 예를 들어 `A`는 U+0041, `가`는 U+AC00이다. 같은 코드 포인트를 바이트로 저장하는 규칙은 여럿이고, 오늘날 가장 널리 쓰이는 규칙이 **UTF-8**이다. 한국어 Windows가 오래 써 온 규칙은 **cp949**(EUC-KR을 확장한 Microsoft의 코드 페이지 949)이다 [2].

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

- **`encode()`와 `decode()`:** `str.encode(인코딩)`은 문자열을 `bytes`로, `bytes.decode(인코딩)`은 `bytes`를 문자열로 바꾼다. 같은 인코딩으로 인코딩하고 디코딩하면 원래 문자열로 돌아온다.
- **길이의 차이:** `"A가"`는 문자 2개이지만 UTF-8로는 4바이트, cp949로는 3바이트이다. `len()`은 `str`에서는 문자 수를, `bytes`에서는 바이트 수를 센다.
- **`bytes`의 표시:** `b'A\xea\xb0\x80'`처럼 출력 가능한 ASCII 문자는 그대로, 나머지 바이트는 `\x` 다음에 두 자리 16진수로 보인다. `list(b)`는 각 바이트를 정수로, `b.hex(" ")`는 16진수로 보여 준다. 구분 문자를 넣는 `hex(" ")`의 형태는 파이썬 3.8부터 쓸 수 있으며 [3], 3.7에서는 인수 없는 `b.hex()`가 `41eab080`처럼 구분 없이 이어진 16진수를 준다.
- **한글의 크기:** 공백 하나와 한글 5자로 된 `"한글 파이썬"`은 UTF-8로 $1 + 5 \times 3 = 16$바이트, cp949로 $1 + 5 \times 2 = 11$바이트이다. 한글 음절 11,172자(U+AC00 `가`부터 U+D7A3 `힣`까지)는 UTF-8에서 모두 3바이트, cp949에서 모두 2바이트이다.

UTF-8은 코드 포인트의 크기에 따라 1\~4바이트를 쓰는 가변 길이 인코딩이다 [4].

| 코드 포인트 범위 | 바이트 수 | 비트 배치 | 예 |
|:-----|-----:|:-----|:-----|
| U+0000 ~ U+007F | 1 | `0xxxxxxx` | `A`, 숫자, 영문 기호 |
| U+0080 ~ U+07FF | 2 | `110xxxxx 10xxxxxx` | `é`, 그리스 문자 |
| U+0800 ~ U+FFFF | 3 | `1110xxxx 10xxxxxx 10xxxxxx` | 한글, 한자 |
| U+10000 ~ U+10FFFF | 4 | `11110xxx 10xxxxxx 10xxxxxx 10xxxxxx` | 이모지 |

*표 2. UTF-8의 바이트 수와 비트 배치*

`가`(U+AC00)는 세 번째 범위이므로 3바이트이다. 코드 포인트 `0xAC00`을 16비트 2진수로 쓰고 앞에서부터 4, 6, 6비트로 나누어 비트 배치의 `x` 자리에 채우면 `EA B0 80`이 된다.

```text
U+AC00 = 1010 1100 0000 0000 (2진수 16비트)

             ┌─4비트┐    ┌─6비트┐       ┌─6비트┐
  나눈 비트      1010      110000         000000
  틀         1110xxxx    10xxxxxx       10xxxxxx
  결과       11101010    10110000       10000000
  16진수        EA          B0             80
```

*그림 1. 가(U+AC00)를 UTF-8의 3바이트로 인코딩하는 과정*

첫 바이트의 앞쪽 `1110`은 "이 문자는 3바이트이다"를, 뒤 바이트의 `10`은 "앞 문자에 이어지는 바이트이다"를 뜻한다. 그래서 UTF-8로 쓴 바이트열은 중간부터 읽어도 문자의 경계를 찾을 수 있고, ASCII 문자(U+0000\~U+007F)는 ASCII와 같은 1바이트로 저장된다.

### 1.4 인코딩이 맞지 않을 때

바이트에는 어떤 인코딩으로 썼는지가 적혀 있지 않다. 쓸 때와 다른 인코딩으로 읽으면 글자가 깨지거나 오류가 난다. 다음 `mismatch.py`로 두 경우를 확인한다.

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

- **UTF-8 바이트를 cp949로 읽기:** 6바이트를 cp949의 2바이트 단위로 잘못 묶어 전혀 다른 글자가 나왔다. `errors="replace"`는 해석할 수 없는 바이트를 `�`(U+FFFD)로 바꾸라는 뜻이며, 이 인수가 없으면 오류가 난다. 이처럼 잘못된 인코딩으로 읽어 뜻 없는 글자가 나오는 현상을 흔히 "글자가 깨진다"고 한다.
- **cp949 바이트를 UTF-8로 읽기:** 첫 바이트 `0xC7`은 2진수 `11000111`로 2바이트 문자의 시작인데, 다음 바이트 `0xD1`(`11010001`)이 `10`으로 시작하지 않으므로 UTF-8의 규칙에 어긋난다. 그래서 `UnicodeDecodeError`가 난다.

파일을 열 때도 같은 일이 생긴다. `open()`에 `encoding`을 주지 않으면 파이썬 3.13은 운영체제의 로캘 인코딩을 쓴다 [1]. macOS와 대부분의 리눅스에서 이 값은 UTF-8이지만, 한국어 Windows에서는 cp949이다. 다음 `win_default.py`는 UTF-8로 쓴 파일을 cp949로 읽는 상황을 `encoding="cp949"`로 재현한다.

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

macOS에서 `encoding` 없이 저장한 파일을 한국어 Windows에서 `encoding` 없이 읽으면 이 오류가 그대로 난다. 반대로 cp949로 쓸 수 없는 문자(이모지 등)를 cp949 파일에 쓰면 `UnicodeEncodeError`가 난다. 그래서 텍스트 파일을 열 때는 **항상 `encoding="utf-8"`을 밝혀 쓴다** [5]. 이 단원의 모든 예제가 그렇게 한다.

> **주의:** 한국어 Windows에서 만든 오래된 텍스트 파일이나 일부 프로그램이 내보낸 CSV 파일은 cp949로 저장되어 있을 수 있다. 그런 파일은 `encoding="cp949"`로 읽어야 하며, 어떤 인코딩인지 모르면 바이트를 읽어 보고 판단해야 한다. 인코딩은 파일의 내용에서 확실하게 알아낼 수 없으므로, 파일을 주고받는 쪽이 인코딩을 약속하는 것이 가장 확실하다.

> **참고:** 기본 인코딩을 다루는 기능은 파이썬 버전에 따라 다르다. `encoding="locale"`(로캘 인코딩을 명시적으로 쓰기)과 기본 인코딩이 쓰일 때 경고를 내는 `EncodingWarning`은 파이썬 3.10에서 [6], 로캘 인코딩을 알려 주는 `locale.getencoding()`은 3.11에서 추가되었으므로 [7] 파이썬 3.7에서는 쓸 수 없다. 또 파이썬 3.15부터는 UTF-8 모드가 기본값이 되어 `encoding`을 생략해도 UTF-8을 쓴다 [8]. 어느 버전에서나 같은 결과를 얻으려면 `encoding`을 직접 쓴다.

---

<br>

## 2. 파일 열고 닫기

### 2.1 open() 함수와 파일 객체

파일을 쓰는 과정은 항상 세 단계이다. 파일을 **열고**, 읽거나 **쓰고**, **닫는다**.

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

`open(파일 이름, 모드, encoding=인코딩)`은 파일을 열고 그 파일을 다루는 객체를 반환한다.

> **용어 정의:** **파일 객체(file object)** 는 열린 파일을 나타내며 `read()`, `write()` 같은 메서드로 그 파일의 데이터를 읽고 쓰게 하는 객체이다 [6]. 파일 객체는 다음에 읽거나 쓸 위치인 **파일 위치(file position)** 를 기억한다.

- **`"w"`로 열고 쓰기:** `write()`는 문자열을 파일에 쓰고 쓴 **문자 수**를 반환한다. `"첫째 줄\n"`은 한글 3자, 공백 1자, 줄바꿈 1자로 5자이다. 파일에는 UTF-8로 인코딩한 $3 \times 3 + 1 + 1 = 11$바이트가 저장된다.
- **`write()`는 줄을 바꾸지 않는다:** `print()`와 달리 `write()`는 받은 문자열만 쓴다. 줄을 바꾸려면 문자열 끝에 `\n`을 직접 넣는다.
- **`"r"`로 열고 읽기:** `read()`는 파일 위치부터 끝까지를 문자열 하나로 반환한다. `repr(text)`는 줄바꿈 문자가 `\n`으로 보이게 하여 파일의 정확한 내용을 확인하게 해 준다.
- **`close()`:** 파일을 닫아 운영체제에 자원을 돌려주고, 아직 파일에 쓰이지 않은 데이터를 마저 쓴다(4.5절).

### 2.2 파일 모드

`open()`의 두 번째 인수인 모드는 파일로 무엇을 할지 정한다. 생략하면 `"r"`이다 [1].

| 모드 | 뜻 | 파일이 없을 때 | 파일이 있을 때 |
|:-----|:-----|:-----|:-----|
| `"r"` | 읽기 (기본값) | `FileNotFoundError` | 처음부터 읽는다 |
| `"w"` | 쓰기 | 새로 만든다 | **내용을 모두 지우고** 처음부터 쓴다 |
| `"a"` | 덧붙이기 | 새로 만든다 | 기존 내용 뒤에 이어 쓴다 |
| `"x"` | 새로 만들어 쓰기 | 새로 만든다 | `FileExistsError` |
| `"b"` | 이진 모드 (`"rb"`, `"wb"`처럼 다른 모드와 함께) | 앞의 모드를 따른다 | 앞의 모드를 따른다 |
| `"t"` | 텍스트 모드 (기본값, `"rt"`는 `"r"`과 같다) | 앞의 모드를 따른다 | 앞의 모드를 따른다 |
| `"+"` | 읽기와 쓰기를 함께 (`"r+"`, `"w+"` 등) | 앞의 모드를 따른다 | 앞의 모드를 따른다 |

*표 3. open()의 모드*

`"w"`와 `"a"`의 차이는 다음 프로그램에서 드러난다.

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

두 번째 `"w"`가 첫 번째 내용을 지웠으므로 `1번째 실행`은 남지 않았고, `"a"`로 쓴 줄은 기존 내용 뒤에 붙었다. 실행할 때마다 기록을 쌓는 로그 파일에는 `"a"`를 쓴다. `with ... as f:`는 2.3절에서 다루며, 여기서는 들여 쓴 부분이 끝나면 파일이 닫힌다는 것만 알면 된다.

없는 파일을 `"r"`로 열면 `FileNotFoundError`가 난다.

```python
f = open("no_such_file.txt", encoding="utf-8")
```

```text
Traceback (most recent call last):
  File "missing.py", line 1, in <module>
    f = open("no_such_file.txt", encoding="utf-8")
FileNotFoundError: [Errno 2] No such file or directory: 'no_such_file.txt'
```

`[Errno 2]`는 운영체제가 알려 준 오류 번호이다. `"x"` 모드는 실수로 기존 파일을 덮어쓰는 것을 막는다.

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

이런 오류가 났을 때 프로그램을 멈추지 않고 처리하는 방법은 11강에서 다룬다.

> **주의:** `"w"`로 여는 순간 기존 내용이 지워진다. 무엇인가를 쓰기 전에 오류로 프로그램이 멈추어도 파일은 이미 빈 파일이다. 읽으려던 파일을 실수로 `"w"`로 열면 데이터를 잃으므로, 읽기만 할 파일은 모드를 생략하거나 `"r"`로 연다.

### 2.3 with문으로 파일 닫기

열린 파일은 반드시 닫아야 한다. 닫지 않으면 마지막에 쓴 데이터가 파일에 기록되지 않을 수 있고(4.5절), 한 프로그램이 동시에 열 수 있는 파일 수에는 운영체제의 한도가 있다. 그런데 `f.close()`를 직접 호출하는 방식은 두 가지 약점이 있다. 호출하는 것을 잊기 쉽고, `close()`에 도달하기 전에 오류가 나면 호출되지 않는다.

`with`문은 들여 쓴 블록이 끝날 때 파일을 자동으로 닫는다. 블록 안에서 오류가 나도 닫는다 [5].

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

- **`with open(...) as f:`:** `open()`이 반환한 파일 객체를 이름 `f`에 연결하고 블록을 실행한다.
- **블록 안:** `f.closed`가 `False`이므로 파일이 열려 있다.
- **블록 밖:** 블록이 끝나면서 파일이 닫혀 `f.closed`가 `True`이다. 이름 `f`와 블록 안에서 읽은 `first`는 블록 밖에서도 남아 있다.
- **닫힌 파일:** 닫힌 파일을 읽으려 하면 `ValueError`가 난다. 파일을 다루는 코드는 모두 `with` 블록 안에 둔다.

`with`문은 파일 말고도 "쓰고 나면 반드시 정리해야 하는 자원"에 두루 쓰이며, 그 동작 원리는 11강에서 예외와 함께 다룬다.

### 2.4 상대 경로와 작업 폴더

`open("memo.txt")`처럼 폴더 없이 파일 이름만 쓰면 파이썬은 **현재 작업 폴더(current working directory)** 에서 그 파일을 찾는다. `"data/scores.txt"`처럼 현재 작업 폴더를 기준으로 쓴 경로를 **상대 경로(relative path)**, macOS와 리눅스의 `/Users/...`나 Windows의 `C:\Users\...`처럼 맨 위 폴더부터 쓴 경로를 **절대 경로(absolute path)** 라고 한다.

현재 작업 폴더는 프로그램 파일이 있는 폴더가 아니라 **프로그램을 실행한 위치**이다. 터미널에서 `python proj/script.py`로 실행하면 작업 폴더는 `proj`의 바깥 폴더이므로, `script.py` 옆의 파일을 `open("settings.txt")`로 열면 찾지 못한다. IDLE에서 파일을 열어 실행하면 작업 폴더가 그 파일의 폴더가 되므로, 같은 코드가 IDLE에서는 되고 터미널에서는 안 되는 일이 생긴다. 프로그램 파일 옆의 데이터를 어디서 실행하든 찾으려면 6.1절처럼 `Path(__file__).parent`로 프로그램 파일의 폴더를 기준으로 경로를 만든다.

> **[운영체제]** 파일 시스템은 파일을 폴더의 트리로 조직하고, 프로세스마다 현재 작업 폴더를 하나씩 기억하여 상대 경로를 그 폴더 기준으로 해석한다. 파일을 열면 운영체제는 그 파일을 가리키는 번호(파일 디스크립터)를 프로세스에 주고, 이후의 읽기와 쓰기는 그 번호로 요청된다. 파일 시스템의 구조, 디렉터리의 구현, 접근 권한은 운영체제에서 다룬다.

---

<br>

## 3. 파일 읽기

이 절의 예제는 다음 `scores.txt`를 읽는다. 넷째 줄은 빈 줄이다.

```text
Kim 85
Lee 92
Park 78

Choi 90
```

### 3.1 read()로 한꺼번에 읽기

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

- **`read()`:** 파일 전체를 문자열 하나로 읽는다. 줄바꿈도 `\n` 문자로 들어 있으므로 길이는 $7 + 7 + 8 + 1 + 8 = 31$자이다.
- **`read(n)`:** 파일 위치부터 최대 `n`자만 읽는다. 첫 `read(6)`이 `'Kim 85'`를 읽어 파일 위치가 그 뒤로 옮겨졌으므로, 두 번째 `read(6)`은 줄바꿈부터 읽는다.
- **`tell()`:** 현재 파일 위치를 알려 준다. 이 파일은 ASCII 문자만 있어 12가 읽은 바이트 수와 같지만, 텍스트 모드의 `tell()`이 돌려주는 값은 일반적으로 문자 수도 바이트 수도 아닌, 다시 `seek()`에 넘길 때만 쓸 수 있는 값이다 [6].

`read()`는 간단하지만 파일 전체를 메모리에 올린다. 수 GB의 로그 파일을 `read()`로 읽으면 메모리가 부족해질 수 있으므로, 큰 파일은 3.3절처럼 한 줄씩 처리한다.

### 3.2 readline()과 readlines()

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

- **`readline()`:** 줄바꿈 문자까지 한 줄을 읽어 반환한다. 반환한 문자열 끝에 `\n`이 붙어 있다.
- **`readlines()`:** 남은 모든 줄을 읽어 각 줄을 요소로 하는 리스트를 반환한다. 앞에서 두 줄을 읽었으므로 셋째 줄부터 들어 있다.
- **파일 끝:** 더 읽을 것이 없으면 `readline()`은 빈 문자열 `''`을 반환한다. 빈 줄은 `'\n'`이므로 파일 끝과 구별된다 [5].

이 성질을 이용하면 `while`문으로 파일을 한 줄씩 읽을 수 있다.

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

빈 줄을 만나도 `line`은 `'\n'`이어서 반복이 멈추지 않고, 파일 끝의 `''`에서만 멈춘다. `rstrip("\n")`은 문자열 오른쪽 끝의 줄바꿈 문자를 없앤다.

### 3.3 파일 객체의 순회

파일 객체는 `for`문으로 순회할 수 있으며, 반복할 때마다 한 줄을 준다. 3.2절의 `while`문과 같은 일을 더 짧게 하고, 한 번에 한 줄만 메모리에 두므로 큰 파일에도 쓸 수 있다 [5]. 텍스트 파일을 줄 단위로 처리할 때는 이 방법이 기본이다.

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

읽은 줄을 그대로 `print(line)`으로 출력하면 줄 사이에 빈 줄이 하나씩 더 생긴다. `line` 끝의 `\n`과 `print()`가 덧붙이는 `\n`이 겹치기 때문이다. `print(line, end="")`로 쓰거나 `line.rstrip("\n")`으로 줄바꿈을 먼저 없앤다.

| 방법 | 반환값 | 메모리 | 알맞은 경우 |
|:-----|:-----|:-----|:-----|
| `f.read()` | 파일 전체를 담은 문자열 하나 | 파일 전체 | 작은 파일을 통째로 처리할 때 |
| `f.read(n)` | 최대 `n`자의 문자열 | `n`자 | 정해진 크기씩 나누어 읽을 때 |
| `f.readline()` | 한 줄(끝의 `\n` 포함), 파일 끝이면 `''` | 한 줄 | 첫 줄(머리글)만 따로 읽을 때 |
| `f.readlines()` | 모든 줄의 리스트 | 파일 전체 | 줄을 인덱스로 오가며 다룰 때 |
| `for line in f` | 반복마다 한 줄 | 한 줄 | 줄 단위로 차례로 처리할 때 (기본) |

*표 4. 텍스트 파일을 읽는 방법의 비교*

### 3.4 읽은 줄의 가공

파일에서 읽은 것은 항상 문자열이다. `85`라는 점수도 `'85'`라는 문자열로 읽히므로 계산하려면 `int()`로 바꾸어야 한다([3강](../Lec03_Data-Types/Concepts_Lecture.ko.md)). 다음 프로그램은 빈 줄을 건너뛰며 점수의 평균을 구한다.

```python
total = 0
count = 0
with open("scores.txt", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line == "":                   # 빈 줄은 건너뛴다
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

- **`line.strip()`:** 앞뒤의 공백 문자와 줄바꿈을 없앤다. 빈 줄은 `''`이 된다.
- **`continue`:** 빈 줄이면 나머지를 건너뛰고 다음 줄로 간다([5강](../Lec05_Loops/Concepts_Lecture.ko.md)).
- **`name, score = line.split()`:** 공백을 경계로 나눈 두 조각을 두 변수에 풀어 넣는다([7강 7.4절](../Lec07_Lists-and-Dictionaries/Concepts_Lecture.ko.md#74-튜플-언패킹)). 한 줄에 조각이 두 개가 아니면 `ValueError`가 나므로, 형식이 확실하지 않은 파일은 11강의 예외 처리와 함께 다룬다.
- **평균:** $(85 + 92 + 78 + 90) / 4 = 345 / 4 = 86.25$이다. 빈 줄을 세지 않았으므로 분모는 4이다.

---

<br>

## 4. 파일 쓰기

### 4.1 write()와 writelines()

`write(문자열)`은 문자열 하나를 쓰고, `writelines(리스트)`는 리스트의 문자열들을 차례로 쓴다.

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

- **`writelines()`는 줄을 바꾸지 않는다:** 이름과 달리 각 요소 뒤에 줄바꿈을 넣지 않으므로 첫 결과는 `'KimLeePark'`이다. 리스트 컴프리헨션으로 각 이름에 `"\n"`을 붙인 리스트를 넘기면 한 줄에 하나씩 저장된다([7강 5절](../Lec07_Lists-and-Dictionaries/Concepts_Lecture.ko.md#5-리스트-컴프리헨션)).
- **문자열만 쓸 수 있다:** 텍스트 모드의 `write()`는 `str`만 받으므로 실수 3.14를 그대로 넘기면 `TypeError`이다. 숫자는 `str()`이나 문자열 형식화로 바꾸어 쓴다.

### 4.2 print()로 파일에 쓰기

`print()`에 `file=파일 객체`를 주면 화면 대신 그 파일에 쓴다. 값 사이의 공백, 끝의 줄바꿈, 숫자의 문자열 변환을 `print()`가 해 주므로, 여러 값을 섞어 쓸 때는 `write()`보다 편하다.

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

`sep`과 `end`도 화면에 출력할 때와 똑같이 동작한다. 화면 출력도 사실은 `file`의 기본값인 표준 출력 `sys.stdout`이라는 파일 객체에 쓰는 것이다. 그래서 출력할 곳을 매개변수로 받는 함수는 `sys.stdout`을 넘기면 화면에, 열린 파일을 넘기면 파일에 쓴다([9강 3.2절](../Lec09_Inheritance-and-Polymorphism/Concepts_Lecture.ko.md#32-덕-타이핑)).

### 4.3 두 파일을 함께 열기

한 `with`문에 쉼표로 여러 파일을 열 수 있다. 다음 프로그램은 `memo.txt`를 읽으며 각 줄 앞에 줄 번호를 붙여 새 파일에 쓴다.

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

- **두 파일:** 원본 `src`는 읽기로, 결과 `dst`는 쓰기로 연다. 블록이 끝나면 두 파일이 모두 닫힌다.
- **`enumerate(src, start=1)`:** 반복할 때마다 `(번호, 요소)` 쌍을 주는 내장 함수이다. 번호는 `start`부터 1씩 늘어나므로 첫 줄은 `(1, '첫째 줄\n')`이다.
- **줄바꿈:** 읽은 `line`의 끝에 이미 `\n`이 있으므로 `write()`에 줄바꿈을 더하지 않는다.

> **주의:** 읽고 있는 파일과 같은 파일을 `"w"`로 동시에 열면, `"w"`가 여는 순간 내용을 지우므로 읽을 것이 남지 않는다. 파일을 고쳐 쓸 때는 결과를 다른 파일에 쓴 뒤 바꾸거나, 내용을 모두 읽어 둔 다음 같은 파일을 `"w"`로 연다.

### 4.4 줄바꿈 문자의 변환

줄의 끝을 나타내는 바이트는 운영체제마다 관례가 다르다. macOS와 리눅스는 `\n`(LF, 0x0A) 하나를, Windows는 `\r\n`(CR LF, 0x0D 0x0A) 두 바이트를 쓴다. 파이썬의 텍스트 모드는 이 차이를 숨긴다. 읽을 때는 `\n`, `\r`, `\r\n`을 모두 `\n`으로 바꾸고(universal newlines), 쓸 때는 `\n`을 운영체제의 줄바꿈 `os.linesep`으로 바꾼다 [1]. `open()`의 `newline` 매개변수로 이 변환을 조절할 수 있다.

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

- **`os.linesep`:** 이 결과를 얻은 macOS에서는 `'\n'`이다. Windows에서는 `'\r\n'`이다.
- **`newline="\r\n"`으로 쓰기:** `\n`이 `\r\n`으로 바뀌어 저장되었다. 이진 모드(`"rb"`)로 읽으면 변환 없이 실제 바이트가 보인다.
- **기본값으로 읽기:** `newline`을 생략하면 `\r\n`이 `\n`으로 바뀌어 읽힌다. 그래서 Windows에서 만든 파일도 같은 코드로 처리할 수 있다.
- **`newline=""`로 읽기:** 줄을 나누기는 하되 줄바꿈 문자를 바꾸지 않는다. 7절의 `csv` 모듈은 줄바꿈을 직접 처리하므로 이 값을 요구한다.

### 4.5 버퍼링과 flush()

`write()`를 호출할 때마다 디스크에 바로 쓰면 매우 느리다. 디스크 접근은 메모리 접근보다 훨씬 오래 걸리기 때문이다. 그래서 파일 객체는 쓸 데이터를 메모리의 **버퍼(buffer)** 에 모아 두었다가, 버퍼가 차거나 파일을 닫을 때 한꺼번에 운영체제에 넘긴다. `flush()`는 버퍼에 모인 데이터를 즉시 내보낸다 [6].

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

`write()`가 끝났는데도 다른 파일 객체로 읽어 보면 파일이 비어 있다. 쓴 내용이 아직 버퍼에 있기 때문이다. `flush()`를 호출한 뒤에는 내용이 보인다. 프로그램이 `close()` 없이 비정상적으로 끝나면 버퍼에 남은 데이터를 잃을 수 있으므로, 이 점에서도 `with`문으로 닫는 것이 안전하다. 진행 상황을 다른 프로그램이 실시간으로 읽어야 하는 로그 파일이라면 중요한 줄을 쓴 뒤 `flush()`를 호출한다.

> **[시스템프로그래밍]** 파이썬의 버퍼는 응용 프로그램 쪽의 버퍼이고, `flush()`는 그 데이터를 운영체제에 넘길 뿐이다. 운영체제도 커널 안에 자체 버퍼(페이지 캐시)를 두므로 데이터가 실제로 디스크에 기록되기까지는 한 단계가 더 있으며, 그 단계까지 강제하려면 `os.fsync()` 같은 시스템 호출을 쓴다. 표준 입출력 라이브러리의 버퍼링 방식과 시스템 I/O의 관계는 시스템프로그래밍에서 다룬다.

---

<br>

## 5. 이진 파일

### 5.1 바이트의 읽기와 쓰기

모드에 `b`를 붙이면 이진 모드로 열린다. 이진 모드에서는 인코딩과 줄바꿈 변환이 없고, `read()`는 `bytes`를 반환하며, `write()`는 `bytes`를 받는다 [5]. 다음 프로그램은 PNG 그림 파일의 시작 부분을 흉내 낸 파일을 만들어 읽는다. 모든 PNG 파일은 정해진 8바이트 `89 50 4E 47 0D 0A 1A 0A`로 시작하며, 프로그램은 이 서명(signature)을 보고 파일이 PNG인지 판단한다 [9].

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

- **쓰기:** `b"..."` 리터럴, 정수의 리스트로 만든 `bytes([0, 0, 0, 13])`, 문자열을 인코딩한 `bytes`를 `+`로 이어 21바이트를 쓴다.
- **`read(8)`:** 이진 모드의 `read(n)`은 `n`**바이트**를 읽는다. 서명이 일치하므로 `True`이고, 파일 위치는 8이다.
- **`b'...\r...'`:** 바이트 13(0x0D)은 출력할 때 `\r`로 보일 뿐 값은 13이다.
- **`seek()`:** 5.2절에서 다룬다. 마지막 9바이트는 UTF-8로 인코딩한 `"데이터"`이므로 디코딩하면 문자열로 돌아온다.

이진 모드와 텍스트 모드를 섞어 쓰면 오류가 난다.

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

`bytes`를 인덱싱하면 0\~255의 정수(`0x89`는 137)가, 슬라이싱하면 `bytes`가 나온다. 이진 모드로 연 파일에 문자열을 쓰려면 먼저 `encode()`로 바꾸어야 한다. 또 이진 모드에는 `encoding`을 줄 수 없으며, `open("x.bin", "rb", encoding="utf-8")`은 `ValueError: binary mode doesn't take an encoding argument`가 난다.

> **주의:** 그림, 음악, 압축 파일 같은 이진 파일을 텍스트 모드로 열면, 디코딩 오류가 나거나 줄바꿈 변환 때문에 바이트가 바뀌어 파일이 손상된다 [5]. 텍스트가 아닌 파일은 내용이 무엇이든 `"rb"`와 `"wb"`로 다룬다.

### 5.2 seek()와 tell()

`f.tell()`은 현재 파일 위치를, `f.seek(오프셋, 기준)`은 파일 위치를 옮긴다. 기준이 0이면 파일의 처음, 1이면 현재 위치, 2이면 파일의 끝에서 센다. 5.1절의 `f.seek(0)`은 처음으로 돌아가는 것이고, `f.seek(-9, 2)`는 파일 끝에서 9바이트 앞으로 옮기는 것이다.

```text
바이트 위치  0                       8           12                          21
             ├─────서명 8바이트──────┼──길이 4───┼──"데이터" UTF-8 9바이트───┤
              89 50 4E 47 0D 0A 1A 0A 00 00 00 0D EB 8D B0 EC 9D B4 ED 84 B0
             ▲                                   ▲                           ▲
          seek(0)                           seek(-9, 2)                   파일 끝
```

*그림 2. 21바이트 파일에서 seek()가 옮기는 파일 위치*

이진 모드에서 파일 위치는 바이트 단위이므로 원하는 위치로 자유롭게 옮길 수 있다. 텍스트 모드에서는 한 문자가 여러 바이트일 수 있으므로, `seek()`에는 처음으로 가는 `seek(0)`, 끝으로 가는 `seek(0, 2)`, 이전에 `tell()`이 돌려준 값만 넘겨야 한다 [6].

### 5.3 큰 파일을 나누어 복사하기

큰 이진 파일을 `read()`로 한꺼번에 읽으면 파일 전체가 메모리에 올라간다. 정해진 크기씩 나누어 읽고 쓰면 파일이 아무리 커도 그 크기만큼의 메모리만 쓴다. 다음 함수는 동작을 보이기 위해 4바이트씩 복사한다. 실제로는 수 KB에서 수 MB 단위를 쓴다.

```python
def copy_file(src_path, dst_path, chunk_size=4):
    count = 0
    with open(src_path, "rb") as src, open(dst_path, "wb") as dst:
        while True:
            chunk = src.read(chunk_size)
            if not chunk:               # 빈 bytes면 파일 끝이다
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

- **파일 끝의 판단:** 이진 모드의 `read()`는 파일 끝에서 빈 `bytes` `b''`를 반환하며, 빈 `bytes`는 조건식에서 거짓이다. 그래서 `if not chunk:`에서 반복을 끝낸다.
- **조각의 수:** 21바이트를 4바이트씩 읽으면 $\lceil 21 / 4 \rceil = 6$번이며, 마지막 조각은 1바이트이다.
- **확인:** 두 파일의 바이트를 비교한 결과가 `True`이므로 복사본이 원본과 같다.

---

<br>

## 6. pathlib으로 경로 다루기

### 6.1 Path 객체

경로를 `"data" + "/" + "scores.txt"`처럼 문자열로 이어 붙이면 운영체제마다 다른 구분자(`/`와 `\`)와 중복된 구분자를 직접 신경 써야 한다. 표준 모듈 `pathlib`의 `Path`는 경로를 객체로 다룬다 [10]. `Path`끼리 또는 `Path`와 문자열을 `/` 연산자로 이으면 하위 경로가 만들어진다. 이 `/`는 9강에서 다룬 연산자 오버로딩의 한 예이다.

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

| 속성과 메서드 | 뜻 | `p`의 값 |
|:-----|:-----|:-----|
| `p.name` | 마지막 부분(파일 이름) | `'scores.txt'` |
| `p.stem` | 확장자를 뺀 파일 이름 | `'scores'` |
| `p.suffix` | 확장자 | `'.txt'` |
| `p.parent` | 바로 위 폴더의 경로 | `data/2024` |
| `p.parts` | 경로를 이루는 부분들의 튜플 | `('data', '2024', 'scores.txt')` |
| `p.with_suffix(s)` | 확장자를 `s`로 바꾼 새 경로 | `data/2024/scores.csv` |
| `p.exists()` | 그 경로에 파일이나 폴더가 있는지 여부 | `False` |
| `p.resolve()` | 현재 작업 폴더를 붙인 절대 경로 | `/.../data/2024/scores.txt` |

*표 5. Path 객체의 주요 속성과 메서드*

`Path` 객체를 만드는 것만으로는 파일이 생기지 않는다. `p.exists()`가 `False`인 것은 경로라는 이름만 만들었기 때문이다. 출력이 `/`로 구분된 것은 이 결과를 macOS에서 얻었기 때문이며, Windows에서는 같은 코드가 `data\2024\scores.txt`를 출력한다. `open()`은 문자열 대신 `Path` 객체도 받는다.

2.4절의 문제, 곧 프로그램 파일 옆의 데이터를 어디서 실행하든 찾는 문제는 `Path(__file__).parent`로 푼다. `__file__`은 지금 실행 중인 프로그램 파일의 경로이다.

```python
from pathlib import Path

here = Path(__file__).parent
data_file = here / "settings.txt"
data_file.write_text("level=3\n", encoding="utf-8")
print(data_file.name, data_file.parent == here)
print(Path.cwd() == here)
```

이 프로그램을 `proj/script_dir.py`로 저장하고 바깥 폴더에서 `python proj/script_dir.py`로, `proj` 안에서 `python script_dir.py`로 차례로 실행한 결과는 다음과 같다.

```text
settings.txt True
False
settings.txt True
True
```

두 번 모두 `settings.txt`는 `script_dir.py`와 같은 `proj` 폴더에 만들어진다. 현재 작업 폴더 `Path.cwd()`는 첫 실행에서는 바깥 폴더여서 `here`와 다르고, 둘째 실행에서는 `proj`여서 같다.

### 6.2 파일과 폴더의 조작

`Path`는 폴더를 만들고, 폴더 안을 살피고, 파일을 읽고 쓰고 지우는 메서드를 가진다 [10].

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

- **`mkdir(parents=True, exist_ok=True)`:** 폴더를 만든다. `parents=True`는 중간 폴더 `data`가 없으면 함께 만들고, `exist_ok=True`는 폴더가 이미 있어도 오류를 내지 않는다. 두 인수가 없으면 이미 있는 폴더에 대해 `FileExistsError`가, 중간 폴더가 없으면 `FileNotFoundError`가 난다 [10].
- **`write_text()`와 `read_text()`:** 파일을 열고, 쓰거나 읽고, 닫는 일을 한 번에 한다. 짧은 파일에 알맞으며 `encoding`을 밝혀 쓰는 것은 `open()`과 같다.
- **`iterdir()`와 `glob()`:** `iterdir()`는 폴더 안의 모든 항목을, `glob("*.txt")`는 이름이 패턴에 맞는 항목만 `Path`로 하나씩 준다. `*`는 아무 글자들과 맞는다. 순서가 정해져 있지 않으므로 `sorted()`로 정렬하여 출력했다 [10].
- **`unlink()`:** 파일을 지운다. 지운 파일은 휴지통을 거치지 않으므로 되살릴 수 없다.
- **`stat().st_size`:** 파일의 크기를 바이트로 알려 준다. `"a.txt의 내용\n"`은 ASCII 6자, 한글 3자, 줄바꿈 1자이므로 $6 + 3 \times 3 + 1 = 16$바이트이다.

---

<br>

## 7. CSV 파일

### 7.1 CSV 형식

> **용어 정의:** **CSV(comma-separated values)** 는 표의 한 행을 한 줄에, 행 안의 값을 쉼표로 구분하여 쓰는 텍스트 파일 형식이다.

스프레드시트 프로그램과 데이터 분석 도구가 표를 주고받을 때 가장 흔히 쓰는 형식이다. 값 안에 쉼표, 큰따옴표, 줄바꿈이 있으면 그 값을 큰따옴표로 감싸고, 값 안의 큰따옴표는 두 번 겹쳐 쓴다. 이 규칙 때문에 CSV를 `split(",")`으로 직접 나누면 틀린다. 표준 모듈 `csv`가 규칙을 대신 처리한다 [11].

### 7.2 csv.writer와 csv.reader

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

- **`csv.writer(f)`:** 파일 객체를 받아 CSV를 쓰는 객체를 만든다. `writerow(리스트)`는 한 행을, `writerows(리스트의 리스트)`는 여러 행을 쓴다. 숫자 85는 자동으로 문자열 `85`로 쓰인다.
- **따옴표 처리:** 쉼표가 든 `Lee, Jr.`와 큰따옴표가 든 값, 줄바꿈이 든 값은 큰따옴표로 감싸이고, 값 안의 `"`는 `""`로 쓰였다.
- **행의 끝:** `csv` 모듈은 행 끝에 기본으로 `\r\n`을 쓴다 [11].
- **`newline=""`:** `csv` 모듈은 줄바꿈을 스스로 처리하므로 파일은 줄바꿈 변환 없이 열어야 한다. 이 인수가 없으면 따옴표 안의 줄바꿈이 잘못 해석되고, Windows에서는 쓸 때 `\r`이 하나 더 붙는다 [11].

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

- **`csv.reader(f)`:** 반복할 때마다 한 행을 문자열의 리스트로 준다. 따옴표로 감싼 값의 쉼표와 줄바꿈이 원래대로 돌아왔다.
- **`next(reader)`:** 다음 행 하나를 꺼내는 내장 함수이다. 머리글 행을 먼저 꺼내 두면 `for`문은 데이터 행만 돈다.
- **모든 값은 문자열:** 점수도 `'85'`로 읽히므로 계산하려면 `int()`로 바꾼다 [11].
- **직접 나누기의 실패:** 마지막 줄처럼 줄과 쉼표를 직접 나누면 `Lee, Jr.`가 두 조각으로 갈라지고, 따옴표와 `\r`이 값에 섞인다.

### 7.3 DictWriter와 DictReader

행을 리스트 대신 딕셔너리로 다루면 열을 번호가 아니라 이름으로 가리킬 수 있다.

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

- **`DictWriter`:** `fieldnames`로 열의 이름과 순서를 정해야 한다. `writeheader()`가 첫 줄에 열 이름을 쓰고, `writerows()`가 각 딕셔너리의 값을 그 순서대로 쓴다. `fieldnames`에 없는 키가 딕셔너리에 있으면 기본으로 `ValueError`가 난다 [11].
- **`DictReader`:** 첫 행을 열 이름으로 쓰고, 나머지 행을 `{열 이름: 값}` 딕셔너리로 준다. 값은 여전히 문자열이다.
- **합계:** $85 + 92 + 78 = 255$이다.

> **참고:** 일부 프로그램은 UTF-8 파일의 맨 앞에 3바이트 `EF BB BF`(BOM)를 붙여 UTF-8임을 표시한다. 파이썬에서는 인코딩 `"utf-8-sig"`가 쓸 때 이 3바이트를 붙이고, 읽을 때 맨 앞에 있으면 건너뛴다 [2]. BOM이 붙은 파일을 `"utf-8"`로 읽으면 첫 값이 `'\ufeff이름'`처럼 보이지 않는 문자 U+FEFF로 시작하므로 `row["이름"]`이 `KeyError`가 된다. 이런 파일은 `encoding="utf-8-sig"`로 읽는다.

---

<br>

## 8. JSON 파일

### 8.1 JSON 형식과 파이썬 자료형

> **용어 정의:** **JSON(JavaScript Object Notation)** 은 객체(이름과 값의 쌍들), 배열, 문자열, 수, 참과 거짓, null을 중첩하여 구조를 가진 데이터를 나타내는 텍스트 형식이다.

CSV가 모든 행의 열이 같은 표에 알맞다면, JSON은 리스트 안에 딕셔너리가 있고 그 안에 다시 리스트가 있는 것처럼 중첩된 데이터에 알맞다. 웹 서비스가 데이터를 주고받는 형식으로 널리 쓰이고, 설정 파일에도 쓰인다. 표준 모듈 `json`은 파이썬 값과 JSON 텍스트를 다음과 같이 대응시킨다 [12].

| 파이썬 | JSON | 예 |
|:-----|:-----|:-----|
| `dict` | 객체 | `{"age": 20}` |
| `list`, `tuple` | 배열 | `[85, 92]` |
| `str` | 문자열 | `"홍길동"` |
| `int`, `float` | 수 | `20`, `3.5` |
| `True`, `False` | `true`, `false` | `false` |
| `None` | `null` | `null` |

*표 6. 파이썬 자료형과 JSON의 대응*

JSON의 문자열은 반드시 큰따옴표로 감싸고, 참과 거짓은 소문자 `true`, `false`이다. 파이썬의 딕셔너리를 `print()`한 모양(`{'name': 'Kim', 'ok': True}`)과 비슷하지만 같지 않다.

### 8.2 json.dump()와 json.load()

`json.dump(값, 파일)`은 파이썬 값을 JSON 텍스트로 파일에 쓰고, `json.load(파일)`은 파일의 JSON 텍스트를 읽어 파이썬 값으로 돌려준다. 파일 대신 문자열을 주고받는 `json.dumps()`와 `json.loads()`도 있다(이름 끝의 `s`는 string의 뜻). JSON 파일은 UTF-8로 쓰고 읽는다 [5].

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

- **`ensure_ascii`:** 기본값 `True`에서는 ASCII가 아닌 문자를 `\ud64d` 같은 이스케이프로 바꾼다. 의미는 같지만 사람이 읽을 수 없으므로, 한글이 든 JSON은 `ensure_ascii=False`로 쓴다 [12].
- **`indent=2`:** 중첩된 구조를 한 단계마다 두 칸씩 들여 써서 사람이 읽기 좋게 한다. 생략하면 한 줄로 쓴다 [12].
- **값의 대응:** `False`는 `false`로, `None`은 `null`로 쓰였고, 읽을 때는 다시 `False`와 `None`이 된다.
- **되돌리기:** 다시 읽은 `loaded`는 원래 딕셔너리와 같다.

모든 값이 그대로 돌아오지는 않는다.

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

- **키는 항상 문자열:** JSON 객체의 키는 문자열뿐이므로 정수 키 1이 `"1"`로 바뀌고, 읽으면 문자열 `'1'`로 돌아온다 [12].
- **튜플은 리스트로:** JSON에는 튜플이 없어 배열로 쓰이고, 읽으면 리스트가 된다.
- **표현할 수 없는 값:** 세트나 직접 정의한 클래스의 객체는 대응하는 JSON 형식이 없다. `json.dumps({"s": {1, 2}})`는 `TypeError: Object of type set is not JSON serializable`이 나므로, 리스트나 딕셔너리로 바꾸어 저장한다.

> **주의:** 파이썬 딕셔너리를 `str()`로 바꾼 문자열은 JSON이 아니다. 작은따옴표를 쓴 `"{'name': 'Kim'}"`을 `json.loads()`에 넘기면 `json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)`이 난다. JSON 파일은 반드시 `json.dump()`로 쓴다.

---

<br>

## 개념 적용

데이터를 파일에 저장할 때는 데이터의 모양과 그 파일을 읽을 쪽에 따라 형식과 여는 방법을 고른다.

| 상황 | 고르는 방법 |
|:-----|:-----|
| 프로그램을 실행할 때마다 시각과 결과를 한 줄씩 쌓아 두고 싶다. | `open(경로, "a", encoding="utf-8")`로 열고 `print(..., file=f)`로 한 줄씩 덧붙인다. |
| 학생 1,000명의 이름과 세 과목 점수를 스프레드시트에서도 열고 싶다. | 모든 행의 열이 같은 표이므로 `csv.DictWriter`로 CSV에 저장하고, 파일은 `newline=""`로 연다. |
| 사용자 설정(이름, 볼륨, 최근 파일 목록)을 저장했다가 다음 실행에 그대로 불러오고 싶다. | 중첩된 구조이므로 `json.dump(..., ensure_ascii=False, indent=2)`로 저장하고 `json.load()`로 읽는다. |
| 수 GB의 로그 파일에서 `ERROR`가 든 줄만 세고 싶다. | `for line in f:`로 한 줄씩 읽으며 센다. `read()`나 `readlines()`는 파일 전체를 메모리에 올린다. |
| 사진 파일을 다른 폴더로 복사하고 싶다. | `"rb"`와 `"wb"`로 열고 정해진 크기씩 나누어 복사한다. |
| 한국어 Windows에서 만든 오래된 메모장 파일을 macOS에서 읽고 싶다. | `encoding="cp949"`로 연다. UTF-8로 읽으면 `UnicodeDecodeError`가 난다. |
| 프로그램 파일 옆의 `config.json`을 어디서 실행하든 찾고 싶다. | `Path(__file__).parent / "config.json"`으로 경로를 만든다. |

*표 7. 상황에 맞는 파일 형식과 여는 방법*

**T/F 점검:**

| 문장 | 판단과 근거 |
|:-----|:-----|
| `len("한글".encode("utf-8"))`은 2이다. | **F.** 한글 음절은 UTF-8에서 3바이트이므로 6이다. 문자 수 2는 `len("한글")`이다(1.3절). |
| `open("data.txt", "w")`로 연 파일에 아무것도 쓰지 않고 닫으면 원래 내용이 남는다. | **F.** `"w"`는 여는 순간 내용을 지우므로 빈 파일이 된다(2.2절). |
| `with`문 안에서 오류가 나면 파일이 닫히지 않는다. | **F.** `with`문은 블록이 어떻게 끝나든 파일을 닫는다(2.3절). |
| `readline()`이 `''`을 반환하면 빈 줄을 읽은 것이다. | **F.** 빈 줄은 `'\n'`이고, `''`은 파일 끝이다(3.2절). |
| `f.writelines(["a", "b"])`는 `a`와 `b`를 두 줄로 쓴다. | **F.** `writelines()`는 줄바꿈을 넣지 않으므로 `ab`가 쓰인다(4.1절). |
| `csv.reader`로 읽은 점수는 정수로 바로 더할 수 있다. | **F.** CSV에서 읽은 값은 모두 문자열이므로 `int()`로 바꾸어야 한다(7.2절). |
| 정수 키를 가진 딕셔너리를 JSON으로 저장했다 읽으면 원래 딕셔너리와 같다. | **F.** JSON의 키는 문자열이므로 정수 키가 문자열 키로 바뀐다(8.2절). |

---

<br>

## 요약

| 개념 | 핵심 요약 |
|:-----|:-----|
| 파일 | 보조기억장치에 이름을 붙여 저장한 바이트의 나열이며, 프로그램이 끝나도 데이터가 남는다. |
| 텍스트 파일과 이진 파일 | 텍스트 파일은 인코딩에 따라 문자를 나타내는 바이트이고 `str`로, 이진 파일은 형식이 정한 바이트이고 `bytes`로 다룬다. |
| 문자 인코딩 | 문자를 바이트로 바꾸는 규칙이며, UTF-8은 한글 음절을 3바이트로, cp949는 2바이트로 저장한다. |
| 인코딩 불일치 | 쓸 때와 다른 인코딩으로 읽으면 글자가 깨지거나 `UnicodeDecodeError`가 나므로 `encoding="utf-8"`을 항상 밝혀 쓴다. |
| `open()`과 파일 객체 | `open(경로, 모드, encoding=...)`은 파일 위치를 기억하는 파일 객체를 반환하고, 모드 `r`, `w`, `a`, `x`, `b`, `+`로 용도를 정한다. |
| `with`문 | 블록이 끝나면 오류가 났더라도 파일을 자동으로 닫는다. |
| 상대 경로 | 현재 작업 폴더를 기준으로 해석되며, 작업 폴더는 프로그램 파일의 위치가 아니라 실행한 위치이다. |
| 파일 읽기 | `read()`는 전체를, `readline()`은 한 줄을, `readlines()`는 줄의 리스트를 주며, 줄 단위 처리에는 `for line in f`가 기본이다. |
| 파일 쓰기 | `write()`와 `writelines()`는 줄바꿈을 넣지 않고 문자열만 받으며, `print(file=f)`는 변환과 줄바꿈을 해 준다. |
| 줄바꿈과 버퍼링 | 텍스트 모드는 줄바꿈을 `\n`으로 통일하고, 쓴 데이터는 버퍼에 모였다가 `flush()`나 `close()` 때 운영체제로 넘어간다. |
| 이진 모드 | `"rb"`, `"wb"`는 변환 없이 `bytes`를 주고받으며, `seek()`와 `tell()`로 바이트 단위의 위치를 다룬다. |
| `pathlib` | `Path`를 `/`로 이어 경로를 만들고, `name`, `suffix`, `parent`, `mkdir()`, `glob()`, `read_text()`로 파일과 폴더를 다룬다. |
| CSV | 쉼표로 구분한 표 형식이며, `csv` 모듈이 따옴표 규칙을 처리하고, 파일은 `newline=""`로 열고, 읽은 값은 모두 문자열이다. |
| JSON | 중첩된 데이터를 나타내는 텍스트 형식이며, `json.dump()`와 `json.load()`로 저장하고 읽고, 키는 문자열로 바뀐다. |

---

<br>

## 점검 문제

1. **인코딩의 계산:** 문자열 `"Py파이썬3"`을 UTF-8과 cp949로 인코딩한 바이트 수를 각각 구하라. 또 `"é"`(U+00E9)가 UTF-8에서 몇 바이트인지 표 2로 판단하라.

   <details>
   <summary>정답</summary>

   ASCII 문자 `P`, `y`, `3`은 두 인코딩 모두 1바이트이고, 한글 3자는 UTF-8에서 3바이트, cp949에서 2바이트이다. 따라서 UTF-8은 $3 + 3 \times 3 = 12$바이트, cp949는 $3 + 3 \times 2 = 9$바이트이다. U+00E9는 U+0080\~U+07FF 범위에 있으므로 UTF-8에서 2바이트(`C3 A9`)이다.

   </details>

2. **모드의 선택:** 다음 세 경우에 알맞은 모드를 쓰라. (1) 기존 기록 뒤에 오늘의 기록을 덧붙인다. (2) 같은 이름의 파일이 이미 있으면 덮어쓰지 말고 실패해야 한다. (3) 그림 파일의 처음 8바이트를 읽는다.

   <details>
   <summary>정답</summary>

   (1) `"a"`이다. 파일이 없으면 새로 만들고, 있으면 끝에 이어 쓴다. (2) `"x"`이다. 파일이 이미 있으면 `FileExistsError`가 난다. (3) `"rb"`이다. 이진 모드에서 `read(8)`은 8바이트를 `bytes`로 읽는다.

   </details>

3. **with문:** 다음 코드에서 `f.write()` 다음 줄의 `int("x")`에서 오류가 나 프로그램이 멈추었다. `with`문을 쓰지 않고 `f = open(...)`과 `f.close()`로 같은 일을 했다면 무엇이 달라지는지 설명하라.

   ```python
   with open("out.txt", "w", encoding="utf-8") as f:
       f.write("결과\n")
       n = int("x")
   ```

   <details>
   <summary>정답</summary>

   `with`문은 블록 안에서 오류가 나도 파일을 닫으므로, 버퍼에 있던 `"결과\n"`이 파일에 기록된다. `f.close()`를 블록 끝에 직접 썼다면 오류 때문에 그 줄에 도달하지 못해 파일이 닫히지 않는다. 프로그램이 끝날 때 정리될 수도 있지만 보장되지 않으며, 오래 실행되는 프로그램에서는 닫히지 않은 파일이 쌓인다.

   </details>

4. **파일 끝:** `readline()`으로 파일을 읽는 반복문의 종료 조건을 `if line.strip() == "": break`로 쓰면 어떤 문제가 생기는가?

   <details>
   <summary>정답</summary>

   빈 줄 `'\n'`도 `strip()`하면 `''`이 되므로, 파일 중간의 빈 줄에서 반복이 끝나 그 뒤의 줄을 읽지 못한다. 파일 끝은 `readline()`이 반환한 `line` 자체가 `''`일 때이므로 `if line == "": break`로 판단해야 한다. `for line in f:`를 쓰면 이런 판단이 필요 없다.

   </details>

5. **줄바꿈 출력:** 다음 코드가 출력하는 줄 수와 그 이유를 쓰라. 파일 `a.txt`의 내용은 `'x\ny\n'`이다.

   ```python
   with open("a.txt", encoding="utf-8") as f:
       for line in f:
           print(line)
   ```

   <details>
   <summary>정답</summary>

   `x`, 빈 줄, `y`, 빈 줄의 네 줄이 출력된다. 읽은 `line`은 `'x\n'`과 `'y\n'`으로 끝에 줄바꿈이 있고, `print()`가 줄바꿈을 하나 더 붙이기 때문이다. `print(line, end="")`나 `print(line.rstrip("\n"))`으로 쓰면 두 줄만 출력된다.

   </details>

6. **CSV:** 이름이 `"Kim, Minsu"`이고 점수가 90인 행을 `csv.writer`로 쓰면 파일에 어떻게 저장되는가? 이 줄을 `split(",")`으로 나누면 어떻게 되는가?

   <details>
   <summary>정답</summary>

   이름에 쉼표가 있으므로 큰따옴표로 감싸 `"Kim, Minsu",90`으로 저장된다. `split(",")`으로 나누면 `['"Kim', ' Minsu"', '90']`처럼 세 조각이 되어 이름이 갈라지고 따옴표가 값에 남는다. `csv.reader`로 읽으면 `['Kim, Minsu', '90']`으로 올바르게 나뉜다.

   </details>

7. **JSON:** `{"scores": (90, 85), 2024: True}`를 `json.dump()`로 저장했다가 `json.load()`로 읽으면 어떤 값이 되는가? 원래 값과 다른 점을 모두 쓰라.

   <details>
   <summary>정답</summary>

   `{'scores': [90, 85], '2024': True}`가 된다. 튜플 `(90, 85)`는 JSON 배열로 쓰여 리스트로 돌아오고, 정수 키 2024는 JSON 객체의 키가 문자열이어야 하므로 `'2024'`로 바뀐다. `True`는 `true`로 쓰였다가 다시 `True`가 되므로 그대로이다.

   </details>

8. **경로:** `Path("report/2024/final.txt")`의 `name`, `stem`, `suffix`, `parent`를 쓰고, 이 경로의 파일을 쓰기 전에 폴더가 없을 수 있다면 어떤 코드를 먼저 실행해야 하는지 쓰라.

   <details>
   <summary>정답</summary>

   차례로 `'final.txt'`, `'final'`, `'.txt'`, `report/2024`이다. 폴더가 없으면 `open()`이 `FileNotFoundError`를 내므로, 먼저 `p.parent.mkdir(parents=True, exist_ok=True)`로 `report`와 `report/2024`를 만든다. `exist_ok=True`이므로 폴더가 이미 있어도 오류가 나지 않는다.

   </details>

---

<br>

## 참고 문헌

1. Python Software Foundation, "Built-in Functions: open()," *The Python Standard Library*, Python 3.13. https://docs.python.org/3.13/library/functions.html#open
2. Python Software Foundation, "codecs - Codec registry and base classes," *The Python Standard Library*, Python 3.13. https://docs.python.org/3.13/library/codecs.html
3. Python Software Foundation, "Built-in Types," *The Python Standard Library*, Python 3.13. https://docs.python.org/3.13/library/stdtypes.html
4. F. Yergeau, "UTF-8, a transformation format of ISO 10646," RFC 3629, Nov. 2003. https://www.rfc-editor.org/rfc/rfc3629
5. Python Software Foundation, "Input and Output," *The Python Tutorial*, Python 3.13. https://docs.python.org/3.13/tutorial/inputoutput.html
6. Python Software Foundation, "io - Core tools for working with streams," *The Python Standard Library*, Python 3.13. https://docs.python.org/3.13/library/io.html
7. Python Software Foundation, "locale - Internationalization services," *The Python Standard Library*, Python 3.13. https://docs.python.org/3.13/library/locale.html
8. N. Inada, "PEP 686 - Make UTF-8 mode default," *Python Enhancement Proposals*, 2022. https://peps.python.org/pep-0686/
9. W3C, "Portable Network Graphics (PNG) Specification (Third Edition)," W3C Recommendation, 2025. https://www.w3.org/TR/png-3/
10. Python Software Foundation, "pathlib - Object-oriented filesystem paths," *The Python Standard Library*, Python 3.13. https://docs.python.org/3.13/library/pathlib.html
11. Python Software Foundation, "csv - CSV File Reading and Writing," *The Python Standard Library*, Python 3.13. https://docs.python.org/3.13/library/csv.html
12. Python Software Foundation, "json - JSON encoder and decoder," *The Python Standard Library*, Python 3.13. https://docs.python.org/3.13/library/json.html
