# 10강 연습 문제 풀이 — 파일 입출력

[레포지토리 안내](../../README.ko.md) | [English](Solutions.md) | [한국어](Solutions.ko.md)

> **최종 수정일:** 2026-11-19

---

<br>

## 목차

- [연습 문제 1: 인코딩별 바이트 수](#연습-문제-1-인코딩별-바이트-수)
- [연습 문제 2: 줄, 단어, 문자 세기](#연습-문제-2-줄-단어-문자-세기)
- [연습 문제 3: 성적 파일의 집계](#연습-문제-3-성적-파일의-집계)
- [연습 문제 4: 번호를 붙이는 로그](#연습-문제-4-번호를-붙이는-로그)
- [연습 문제 5: 두 파일의 첫 차이](#연습-문제-5-두-파일의-첫-차이)
- [연습 문제 6: 파일 종류의 판별](#연습-문제-6-파일-종류의-판별)
- [연습 문제 7: CSV 성적표의 변환](#연습-문제-7-csv-성적표의-변환)
- [연습 문제 8: JSON 설정 파일](#연습-문제-8-json-설정-파일)

---

<br>

## 연습 문제 1: 인코딩별 바이트 수

**문제:** 문자열의 문자 수와 UTF-8, cp949 바이트 수를 출력하는 `byte_report()`를 작성하고, `"한"`의 UTF-8 바이트를 직접 계산하라. 문제 전문과 실행 예시는 [연습 문제 1](Exercises.ko.md#연습-문제-1-인코딩별-바이트-수)에 있다.

### 풀이

**접근 방법:** `len()`은 `str`에서 문자 수를, `bytes`에서 바이트 수를 센다([10강 1.3절](Concepts_Lecture.ko.md#13-문자-인코딩과-utf-8)). 문자열을 두 인코딩으로 각각 `encode()`하여 그 길이를 잰다.

**코드:**

```python
def byte_report(text):
    u = text.encode("utf-8")
    c = text.encode("cp949")
    print("%s: 문자 %d, UTF-8 %d바이트, cp949 %d바이트" % (text, len(text), len(u), len(c)))

for t in ["Python", "파이썬", "Py파이썬3", "가나다 ABC"]:
    byte_report(t)
print("한".encode("utf-8").hex(" "), hex(ord("한")))
```

**실행 결과:**

```text
Python: 문자 6, UTF-8 6바이트, cp949 6바이트
파이썬: 문자 3, UTF-8 9바이트, cp949 6바이트
Py파이썬3: 문자 6, UTF-8 12바이트, cp949 9바이트
가나다 ABC: 문자 7, UTF-8 13바이트, cp949 10바이트
ed 95 9c 0xd55c
```

- **바이트 수의 규칙:** ASCII 문자(영문, 숫자, 공백)는 두 인코딩 모두 1바이트, 한글 음절은 UTF-8에서 3바이트, cp949에서 2바이트이다. `"가나다 ABC"`는 한글 3자와 ASCII 4자이므로 UTF-8은 $3 \times 3 + 4 = 13$, cp949는 $3 \times 2 + 4 = 10$바이트이다.
- **`ord()`:** 문자의 코드 포인트를 정수로 돌려준다. `hex()`로 바꾸면 `0xd55c`이다.

**직접 계산:** U+D55C는 U+0800\~U+FFFF 범위이므로 3바이트 틀 `1110xxxx 10xxxxxx 10xxxxxx`를 쓴다. `0xD55C`를 16비트 2진수로 쓰면 `1101 0101 0101 1100`이고, 앞에서부터 4, 6, 6비트로 나누면 `1101`, `010101`, `011100`이다. 틀에 채우면 `11101101`, `10010101`, `10011100`이므로 16진수로 `ED 95 9C`가 되어 출력과 같다.

---

<br>

## 연습 문제 2: 줄, 단어, 문자 세기

**문제:** 파일 전체를 메모리에 올리지 않고 줄 수, 단어 수, 문자 수를 세는 `count_file(path)`를 작성하라. 문제 전문과 실행 예시는 [연습 문제 2](Exercises.ko.md#연습-문제-2-줄-단어-문자-세기)에 있다.

### 풀이

**접근 방법:** 파일 객체를 `for`문으로 순회하면 한 번에 한 줄만 메모리에 둔다([10강 3.3절](Concepts_Lecture.ko.md#33-파일-객체의-순회)). 줄마다 줄 수에 1을, 단어 수에 `len(line.split())`을, 문자 수에 `len(line)`을 더한다. 인수 없는 `split()`은 줄바꿈도 공백으로 보므로 빈 줄은 단어가 0개이다.

**코드:**

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

**실행 결과:**

```text
(4, 11, 48)
```

| 줄 | 단어 수 | 문자 수 (줄바꿈 포함) |
|:-----|-----:|-----:|
| `파일은 바이트의 나열이다` | 3 | 14 |
| `텍스트 파일은 인코딩을 따른다` | 4 | 17 |
| 빈 줄 | 0 | 1 |
| `with 문은 파일을 닫는다` | 4 | 16 |
| 합계 | 11 | 48 |

*표 1. notes.txt의 줄별 단어 수와 문자 수*

- **문자 수:** 첫 줄은 한글 11자, 공백 2자, 줄바꿈 1자로 14자이다. 빈 줄도 줄바꿈 문자 하나가 있으므로 1자이다.
- **바이트 수와의 차이:** `len(line)`은 문자를 센다. 파일의 크기(바이트)를 알고 싶다면 이진 모드로 읽은 `bytes`의 길이나 `Path(path).stat().st_size`를 쓴다.

---

<br>

## 연습 문제 3: 성적 파일의 집계

**문제:** 빈 줄과 주석 줄을 건너뛰며 `scores.txt`를 읽고 인원, 평균, 최고점인 사람을 `print(file=)`로 `result.txt`에 쓰라. 문제 전문과 실행 예시는 [연습 문제 3](Exercises.ko.md#연습-문제-3-성적-파일의-집계)에 있다.

### 풀이

**접근 방법:** 줄마다 `strip()`으로 앞뒤 공백을 없앤 뒤, 빈 문자열이거나 `startswith("#")`이면 `continue`로 건너뛴다. 나머지 줄은 `split()`으로 이름과 점수로 나누어 두 리스트에 넣는다. 최고점인 사람은 최댓값의 인덱스로 찾는다.

**코드:**

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

**실행 결과:**

```text
인원: 4
평균: 86.25
최고: Lee 92
```

- **건너뛴 줄:** 주석 두 줄과 빈 줄 하나를 건너뛰었으므로 남은 줄은 4개이다. `# 이름 점수`를 건너뛰지 않으면 `split()`이 세 조각을 만들어 `ValueError`가 난다.
- **평균:** $(85 + 92 + 78 + 90) / 4 = 86.25$이다.
- **최고점:** `max(scores)`는 92이고 `scores.index(92)`는 1이므로 `names[1]`인 Lee이다([7강 4.1절](../Lec07_Lists-and-Dictionaries/Concepts_Lecture.ko.md#41-요소-탐색)).
- **`print(file=out)`:** 숫자를 직접 문자열로 바꾸지 않아도 되고 줄바꿈도 자동으로 붙는다([10강 4.2절](Concepts_Lecture.ko.md#42-print로-파일에-쓰기)).

---

<br>

## 연습 문제 4: 번호를 붙이는 로그

**문제:** 기존 줄 수에 1을 더한 세 자리 번호를 붙여 로그 파일 끝에 한 줄씩 덧붙이는 `log()`를 작성하라. 문제 전문과 실행 예시는 [연습 문제 4](Exercises.ko.md#연습-문제-4-번호를-붙이는-로그)에 있다.

### 풀이

**접근 방법:** 먼저 `Path(path).exists()`로 파일이 있는지 확인하고, 있으면 읽기 모드로 열어 줄 수를 센다. 없는 파일을 `"r"`로 열면 `FileNotFoundError`가 나므로 이 확인이 필요하다. 그다음 `"a"` 모드로 열어 끝에 덧붙인다([10강 2.2절](Concepts_Lecture.ko.md#22-파일-모드)). 세 자리 번호는 형식 지정자 `%03d`(빈자리를 0으로 채운 3자리 정수)로 만든다.

**코드:**

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

**실행 결과:** 로그 파일이 없는 상태에서 처음 실행한 결과이다.

```text
[001] 프로그램 시작
[002] 파일 3개 처리
[003] 프로그램 종료
```

- **두 번째 실행:** 파일에 이미 세 줄이 있으므로 번호가 `[004]`부터 이어지고, 마지막에 출력되는 파일 내용은 여섯 줄이다. `"w"`로 열었다면 실행할 때마다 기록이 지워졌을 것이다.
- **`open()`과 `Path`:** `open()`은 경로로 문자열 대신 `Path` 객체도 받는다.
- **한계:** 로그를 쓸 때마다 파일 전체를 읽어 줄 수를 세므로, 로그가 매우 길어지면 느려진다. 번호를 별도의 파일에 저장하거나, 번호 대신 시각을 쓰는 것이 실제 로그 파일의 일반적인 방법이다.

---

<br>

## 연습 문제 5: 두 파일의 첫 차이

**문제:** 두 텍스트 파일을 한 줄씩 비교하여 처음으로 다른 줄의 번호와 내용을 반환하는 `first_difference()`를 작성하라. 문제 전문과 실행 예시는 [연습 문제 5](Exercises.ko.md#연습-문제-5-두-파일의-첫-차이)에 있다.

### 풀이

**접근 방법:** 한 `with`문에서 두 파일을 함께 연다([10강 4.3절](Concepts_Lecture.ko.md#43-두-파일을-함께-열기)). 반복할 때마다 두 파일에서 `readline()`으로 한 줄씩 읽는다. 파일이 끝나면 `readline()`은 `''`을 반환하므로, 먼저 끝난 파일의 줄은 자동으로 빈 문자열이 된다([10강 3.2절](Concepts_Lecture.ko.md#32-readline과-readlines)). 두 줄이 모두 `''`이면 두 파일이 동시에 끝난 것이므로 같은 파일이다.

**코드:**

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

**실행 결과:**

```text
(3, '포도', '귤')
None
(3, '포도', '')
```

- **첫 비교:** 1, 2행은 같고 3행에서 `포도`와 `귤`이 다르다.
- **같은 파일:** 같은 파일을 두 번 열어 비교하면 4번째 반복에서 두 줄이 모두 `''`이 되어 `None`을 반환한다. 같은 파일을 읽기 모드로 두 번 여는 것은 문제가 없으며, 두 파일 객체는 각자의 파일 위치를 가진다.
- **길이가 다른 파일:** `v3.txt`는 2행에서 끝나므로 3행을 읽은 `b`가 `''`이 되어 `포도`와 다르다고 판정된다.
- **`return`과 `with`:** `with` 블록 안에서 `return`으로 함수를 끝내도 두 파일은 닫힌다.

---

<br>

## 연습 문제 6: 파일 종류의 판별

**문제:** 이진 모드로 읽은 바이트로 PNG, BOM이 있는 UTF-8, ASCII, UTF-8, 그 밖의 이진 파일을 판별하는 `detect()`를 작성하라. 문제 전문과 실행 예시는 [연습 문제 6](Exercises.ko.md#연습-문제-6-파일-종류의-판별)에 있다.

### 풀이

**접근 방법:** 텍스트 모드로 열면 디코딩 오류가 날 수 있으므로 모든 파일을 `"rb"`로 열어 `bytes`로 읽는다([10강 5.1절](Concepts_Lecture.ko.md#51-바이트의-읽기와-쓰기)). `bytes`의 `startswith()`로 서명과 BOM을 검사하고, `isascii()`로 모든 바이트가 0\~127인지 검사한다. UTF-8로 디코딩되는지는 `errors="replace"`로 디코딩한 결과에 대체 문자 U+FFFD가 생겼는지로 판단한다.

**코드:**

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

**실행 결과:**

```text
a.png PNG 그림
b.txt UTF-8 텍스트 (BOM)
c.txt ASCII 텍스트
d.txt UTF-8 텍스트
e.txt 알 수 없는 이진 파일
f.bin 알 수 없는 이진 파일
```

- **`bytes(8)`:** 정수 하나를 받은 `bytes()`는 그 길이만큼 0으로 채운 `bytes`를 만든다.
- **규칙의 순서:** ASCII만으로 된 파일은 UTF-8로도 디코딩되므로, 3번 규칙을 4번보다 먼저 검사해야 `c.txt`가 `ASCII 텍스트`로 판별된다.
- **cp949 파일:** `e.txt`의 바이트는 UTF-8의 규칙에 맞지 않아 대체 문자가 생기므로 이진 파일로 판별되었다. 바이트만으로는 cp949 텍스트와 이진 데이터를 확실히 구별할 수 없다는 [10강 1.4절](Concepts_Lecture.ko.md#14-인코딩이-맞지-않을-때)의 설명이 이 결과에 나타난다.
- **한계:** `data = f.read()`는 파일 전체를 읽는다. 서명만 검사한다면 `f.read(8)`로 충분하고, 텍스트 여부는 앞부분 수 KB만 읽어 추정하는 방법을 쓸 수 있다.

---

<br>

## 연습 문제 7: CSV 성적표의 변환

**문제:** `grades.csv`를 읽어 총점과 평균 열을 더하고 총점 순으로 정렬하여 `report.csv`에 쓰라. 문제 전문과 실행 예시는 [연습 문제 7](Exercises.ko.md#연습-문제-7-csv-성적표의-변환)에 있다.

### 풀이

**접근 방법:** `csv.DictReader`가 주는 행은 딕셔너리이므로 `row["total"] = ...`처럼 새 키를 더할 수 있다. 읽은 값은 문자열이므로 점수는 `int()`로 바꾸어 더한다([10강 7.3절](Concepts_Lecture.ko.md#73-dictwriter와-dictreader)). 정렬은 `key`에 총점을, `reverse=True`로 내림차순을 지정한다. 쓸 때는 더한 열까지 포함한 `fieldnames`를 `DictWriter`에 준다. 두 파일 모두 `newline=""`로 연다.

**코드:**

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

**실행 결과:**

```text
name,korean,english,math,total,average
Lee,92,88,95,275,91.7
Kim,85,90,78,253,84.3
Park,70,65,80,215,71.7
```

- **총점과 평균:** Lee는 $92 + 88 + 95 = 275$, $275 / 3 = 91.66...$이므로 91.7이다. Kim은 253과 84.3, Park은 215와 71.7이다.
- **정렬의 기준:** `row["total"]`은 정수로 저장했으므로 숫자 크기로 정렬된다. 문자열로 저장했다면 사전 순으로 비교되어, 예를 들어 `"95"`가 `"215"`보다 크다고 판정된다.
- **줄 끝:** `report.csv`의 각 줄은 실제로 `\r\n`으로 끝난다(`csv` 모듈의 기본값). `newline=""`로 읽어 출력했으므로 `\r`이 화면에 보이지 않는 문자로 함께 출력된다.

---

<br>

## 연습 문제 8: JSON 설정 파일

**문제:** 기본 설정에서 시작하여 JSON 설정 파일의 내용으로 덮어쓰는 `load_settings()`와 설정을 저장하는 `save_settings()`를 작성하라. 문제 전문과 실행 예시는 [연습 문제 8](Exercises.ko.md#연습-문제-8-json-설정-파일)에 있다.

### 풀이

**접근 방법:** 설정 파일이 없을 수 있으므로 `Path.exists()`로 확인한 뒤에 연다. 딕셔너리의 `update()`는 다른 딕셔너리의 항목으로 같은 키의 값을 덮어쓰고 없는 키를 더한다([7강 11절](../Lec07_Lists-and-Dictionaries/Concepts_Lecture.ko.md#11-딕셔너리)). 그래서 파일에 없는 설정은 기본값으로 남는다. 기본 설정의 복사에는 `copy.deepcopy()`를 쓴다. `DEFAULTS`의 값 가운데 리스트가 있기 때문이다.

**코드:**

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

**실행 결과:** 처음 실행한 결과와 두 번째 실행한 결과이다.

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

두 번째 실행 뒤의 `settings.json`은 다음과 같다.

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

- **깊은 복사가 필요한 이유:** `dict(DEFAULTS)`나 `DEFAULTS.copy()`는 얕은 복사이므로 `settings["recent"]`와 `DEFAULTS["recent"]`가 같은 리스트를 가리킨다([7강 9.3절](../Lec07_Lists-and-Dictionaries/Concepts_Lecture.ko.md#93-얕은-복사)). 첫 실행에서 `s["recent"].append(...)`를 하면 `DEFAULTS["recent"]`도 `['보고서6.txt']`가 되어, 같은 실행 안에서 다시 불러온 기본값이 오염된다. `deepcopy()`는 안쪽 리스트까지 새로 만든다.
- **`ensure_ascii=False`와 `indent=2`:** 한글 파일 이름이 이스케이프되지 않고, 사람이 직접 열어 고칠 수 있는 모양으로 저장된다([10강 8.2절](Concepts_Lecture.ko.md#82-jsondump와-jsonload)).
- **잘못된 파일:** 사용자가 설정 파일을 직접 고치다 JSON 문법을 틀리면 `json.load()`가 `JSONDecodeError`를 낸다. 이 경우에도 기본값으로 시작하게 하는 방법은 11강의 예외 처리로 만든다.
