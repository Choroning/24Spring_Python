# 11강 연습 문제 풀이 — 예외 처리

[레포지토리 안내](../../README.ko.md) | [English](Solutions.md) | [한국어](Solutions.ko.md)

> **최종 수정일:** 2026-11-19

---

<br>

## 목차

- [연습 문제 1: 트레이스백으로 원인 찾기](#연습-문제-1-트레이스백으로-원인-찾기)
- [연습 문제 2: 범위가 있는 정수 입력](#연습-문제-2-범위가-있는-정수-입력)
- [연습 문제 3: 네 절의 실행 순서](#연습-문제-3-네-절의-실행-순서)
- [연습 문제 4: 사칙 연산 계산기](#연습-문제-4-사칙-연산-계산기)
- [연습 문제 5: 여러 파일의 합계](#연습-문제-5-여러-파일의-합계)
- [연습 문제 6: 입력 검증 예외의 계층](#연습-문제-6-입력-검증-예외의-계층)
- [연습 문제 7: 설정 오류로 바꾸어 알리기](#연습-문제-7-설정-오류로-바꾸어-알리기)
- [연습 문제 8: 되돌리는 컨텍스트 관리자](#연습-문제-8-되돌리는-컨텍스트-관리자)

---

<br>

## 연습 문제 1: 트레이스백으로 원인 찾기

**문제:** `grades.py`의 트레이스백에서 예외의 종류와 원인을 찾고, 해석할 수 없는 점수가 있어도 나머지 결과를 출력하도록 `summary()`를 고쳐라. 문제 전문과 실행 예시는 [연습 문제 1](Exercises.ko.md#연습-문제-1-트레이스백으로-원인-찾기)에 있다.

### 풀이

**(1) 예외와 원인:** 마지막 줄에 따르면 예외는 `ValueError`이고, `int()`가 문자열 `'7O'`을 정수로 바꾸지 못했다. Park의 점수가 숫자 0이 아니라 영문자 O를 쓴 `"7O"`로 입력되어 있다. 바로 위의 `File` 줄이 `summary()`의 11행을, `~~~^^^^^^^` 표시가 그 줄의 `int(score)`를 가리킨다([11강 1.3절](Concepts_Lecture.ko.md#13-트레이스백-읽기)).

**(2) Kim과 Lee가 출력되지 않은 이유:** `summary()`는 모든 사람의 결과를 리스트에 모은 뒤 반환하고, 출력은 반환된 리스트로 15\~16행에서 한다. Park에서 예외가 나자 `summary()`가 반환하지 못하고 빠져나왔으므로, 이미 만든 Kim과 Lee의 줄도 출력 단계에 이르지 못했다.

**(3) 고친 코드:** 사람 한 명의 점수를 해석하는 부분만 `try`로 감싸고, `ValueError`이면 대체 문자열을 쓴다. 표 2의 "대체값으로 복구"에 해당한다([11강 2.6절](Concepts_Lecture.ko.md#26-처리기가-할-수-있는-일)).

```python
def letter(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    return "C"

def summary(records):
    lines = []
    for name, score in records.items():
        try:
            grade = letter(int(score))
        except ValueError:
            grade = "점수 오류(" + repr(score) + ")"
        lines.append(name + ": " + grade)
    return lines

data = {"Kim": "95", "Lee": "88", "Park": "7O"}
for line in summary(data):
    print(line)
```

**실행 결과:**

```text
Kim: A
Lee: B
Park: 점수 오류('7O')
```

- **`try`문의 위치:** 반복문 안에 두었으므로 한 사람의 실패가 다른 사람의 처리에 영향을 주지 않는다. 반복문 전체를 감쌌다면 결과가 같은 방식으로 끊겼을 것이다.
- **`try`절의 범위:** `letter(int(score))` 한 줄만 넣었다. `lines.append()`까지 넣으면 그 줄에서 생길 수 있는 다른 `ValueError`도 점수 오류로 잘못 표시된다.
- **`repr(score)`:** 따옴표를 붙여 보여 주므로 값에 공백이나 비슷하게 생긴 문자가 섞였을 때 알아보기 쉽다.

---

<br>

## 연습 문제 2: 범위가 있는 정수 입력

**문제:** 정수가 아니거나 범위 밖이면 다시 묻는 `read_int(prompt, low, high)`를 작성하라. 문제 전문과 실행 예시는 [연습 문제 2](Exercises.ko.md#연습-문제-2-범위가-있는-정수-입력)에 있다.

### 풀이

**접근 방법:** [11강 2.5절](Concepts_Lecture.ko.md#25-올바른-입력을-받을-때까지-반복하기)의 반복을 함수로 만든다. 정수 변환은 `int()`를 시도하여 `ValueError`를 처리하고(EAFP), 범위는 비교 연결 `low <= value <= high`로 검사한다(LBYL). 올바른 값은 `return`으로 반환하므로 반복문을 끝내는 `break`가 따로 필요 없다.

**코드:**

```python
def read_int(prompt, low, high):
    while True:
        text = input(prompt)
        try:
            value = int(text)
        except ValueError:
            print("정수를 입력해야 한다:", repr(text))
            continue
        if not (low <= value <= high):
            print(low, "이상", high, "이하여야 한다")
            continue
        return value

month = read_int("월을 입력하시오 (1~12): ", 1, 12)
print("입력한 월:", month)
```

**실행 결과:** `삼월`, `13`, `3`을 차례로 입력한 결과이다.

```text
월을 입력하시오 (1~12): 삼월
정수를 입력해야 한다: '삼월'
월을 입력하시오 (1~12): 13
1 이상 12 이하여야 한다
월을 입력하시오 (1~12): 3
입력한 월: 3
```

- **`"삼월"`:** `int()`가 `ValueError`를 일으켜 안내를 출력하고 `continue`로 다시 묻는다.
- **`"13"`:** 정수로는 바뀌지만 `1 <= 13 <= 12`가 거짓이므로 범위 안내를 출력한다.
- **`"3"`:** 두 검사를 통과하여 3을 반환한다. `" 3 "`처럼 앞뒤에 공백을 넣어도 `int()`가 공백을 무시하므로 같은 결과이다.
- **함수로 만든 이점:** 같은 함수로 `read_int("나이: ", 0, 150)`처럼 다른 범위의 입력도 받을 수 있다.

---

<br>

## 연습 문제 3: 네 절의 실행 순서

**문제:** `try`, 두 `except`, `else`, `finally`를 가진 `check()`에 4, 0, `"4"`를 넣었을 때의 출력을 쓰라. 문제 전문은 [연습 문제 3](Exercises.ko.md#연습-문제-3-네-절의-실행-순서)에 있다.

### 풀이

**실행 결과:**

```text
가 나 마 바
25
가 다 바
zero
가 라 바
바깥에서 처리
```

**추적:**

| 호출 | 실행된 절 | 출력 | 결과 |
|:-----|:-----|:-----|:-----|
| `check(4)` | `try` 전체 → `else` → `finally` | `가 나 마 바` | `else`의 `return r`로 25를 반환 |
| `check(0)` | `try`의 앞부분 → `except ZeroDivisionError` → `finally` | `가 다 바` | `"zero"`를 반환 |
| `check("4")` | `try`의 앞부분 → `except TypeError` → `finally` | `가 라 바` | `raise`로 `TypeError`를 다시 일으킴 |

*표 1. check()의 세 호출에서 실행된 절*

- **`return`과 `finally`:** `check(4)`와 `check(0)`은 `else`절과 `except`절에서 `return`했지만, 함수가 끝나기 전에 `finally`절이 `바`와 줄바꿈을 출력했다. 반환값은 그 뒤에 바깥의 `print()`가 출력했으므로 `25`와 `zero`가 다음 줄에 나온다([11강 3.2절](Concepts_Lecture.ko.md#32-finally절)).
- **`100 // "4"`:** 정수를 문자열로 나눌 수 없어 `TypeError`가 났다. 처리기가 `라`를 출력하고 `raise`로 같은 예외를 다시 일으키자, `finally`절이 실행된 뒤 예외가 함수 밖으로 나갔다.
- **바깥의 `print()`:** `check("4")`가 값을 반환하지 못했으므로 `print(check("4"))`의 `print()`는 호출되지 않고, 바깥의 `except TypeError`가 `바깥에서 처리`를 출력했다.

---

<br>

## 연습 문제 4: 사칙 연산 계산기

**문제:** `"수 연산자 수"` 형태의 문자열을 계산하고, 0으로 나누기, 모르는 연산자, 형식 오류를 처리하는 `calc(expr)`를 작성하라. 문제 전문과 실행 예시는 [연습 문제 4](Exercises.ko.md#연습-문제-4-사칙-연산-계산기)에 있다.

### 풀이

**접근 방법:** `split()`으로 세 조각을 얻어 두 수를 `float()`로 바꾸고 연산자에 따라 계산한다. 조각의 수가 틀리거나 수로 바꿀 수 없으면 파이썬이 `ValueError`를 일으킨다. 모르는 연산자도 같은 처리기로 다루기 위해 `raise ValueError(...)`로 직접 일으킨다([11강 5.1절](Concepts_Lecture.ko.md#51-raise문)). 0으로 나누기는 다른 메시지를 쓰므로 별도의 처리기를 둔다.

**코드:**

```python
def calc(expr):
    try:
        a, op, b = expr.split()
        a = float(a)
        b = float(b)
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            return a / b
        else:
            raise ValueError("모르는 연산자 " + repr(op))
    except ZeroDivisionError:
        return "오류: 0으로 나눌 수 없다"
    except ValueError as e:
        return "오류: " + str(e)

for e in ["3 + 4", "10 / 4", "1 / 0", "2 ^ 3", "abc * 2", "1 +"]:
    print(e, "=>", calc(e))
```

**실행 결과:**

```text
3 + 4 => 7.0
10 / 4 => 2.5
1 / 0 => 오류: 0으로 나눌 수 없다
2 ^ 3 => 오류: 모르는 연산자 '^'
abc * 2 => 오류: could not convert string to float: 'abc'
1 + => 오류: not enough values to unpack (expected 3, got 2)
```

- **결과의 자료형:** 두 수를 `float()`로 바꾸었으므로 `3 + 4`도 실수 `7.0`이다.
- **같은 함수 안의 `raise`:** `raise ValueError(...)`로 일으킨 예외도 파이썬이 일으킨 예외와 똑같이 같은 `try`문의 `except ValueError`가 받는다.
- **`1 / 0`:** 실수 나눗셈 `1.0 / 0.0`도 `ZeroDivisionError`를 일으킨다.
- **처리기의 순서:** `ZeroDivisionError`와 `ValueError`는 상속 관계가 없으므로 두 절의 순서를 바꾸어도 결과가 같다.

---

<br>

## 연습 문제 5: 여러 파일의 합계

**문제:** 없는 파일과 수가 아닌 줄을 건너뛰며 여러 파일의 수를 모두 더하는 `total_of_files(paths)`를 작성하라. 문제 전문과 실행 예시는 [연습 문제 5](Exercises.ko.md#연습-문제-5-여러-파일의-합계)에 있다.

### 풀이

**접근 방법:** 실패의 단위가 둘이므로 `try`문을 두 겹으로 둔다. 바깥 `try`는 파일 하나를 열고 읽는 일을 감싸 `FileNotFoundError`이면 그 파일만 건너뛰고, 안쪽 `try`는 한 줄의 변환을 감싸 `ValueError`이면 그 줄만 건너뛴다. 표 2의 "기록하고 계속"에 해당한다([11강 2.6절](Concepts_Lecture.ko.md#26-처리기가-할-수-있는-일)).

**코드:**

```python
from pathlib import Path

def total_of_files(paths):
    total = 0
    bad_lines = 0
    missing = []
    for p in paths:
        try:
            with open(p, encoding="utf-8") as f:
                for line in f:
                    if line.strip() == "":      # skip blank lines
                        continue
                    try:
                        total += float(line)
                    except ValueError:
                        bad_lines += 1
        except FileNotFoundError:
            missing.append(p)
    return total, bad_lines, missing

Path("a.txt").write_text("10\n20\n\n", encoding="utf-8")
Path("b.txt").write_text("1.5\n둘\n2.5\n", encoding="utf-8")
print(total_of_files(["a.txt", "nothing.txt", "b.txt"]))
```

**실행 결과:**

```text
(34.0, 1, ['nothing.txt'])
```

- **합계:** $10 + 20 + 1.5 + 2.5 = 34.0$이다. `float()`는 줄 끝의 줄바꿈을 무시한다.
- **수가 아닌 줄:** `둘` 하나이다. 빈 줄은 먼저 건너뛰므로 세지 않는다. 빈 줄을 그대로 `float()`에 넘기면 `ValueError`가 나서 수가 아닌 줄로 세어진다.
- **없는 파일:** `nothing.txt`를 여는 순간 `FileNotFoundError`가 바깥 `try`에서 처리되고, 반복이 `b.txt`로 이어졌다.
- **두 겹의 이유:** 줄 변환의 `try`를 바깥 하나로 합치면 한 줄의 실패가 그 파일의 나머지 줄을 모두 건너뛰게 만든다. `try`의 범위가 곧 실패했을 때 건너뛰는 범위이다.

---

<br>

## 연습 문제 6: 입력 검증 예외의 계층

**문제:** `ValidationError`를 상위 클래스로 하는 `EmptyFieldError`, `RangeError`를 정의하고 학생 정보를 검사하는 `validate()`를 작성하라. 문제 전문과 실행 예시는 [연습 문제 6](Exercises.ko.md#연습-문제-6-입력-검증-예외의-계층)에 있다.

### 풀이

**접근 방법:** 공통 상위 클래스 `ValidationError`가 항목 이름을 속성으로 저장하고 `"항목: 설명"` 형태의 메시지를 만든다. 하위 클래스는 설명만 만들어 상위 클래스의 생성자에 넘긴다([11강 5.3절](Concepts_Lecture.ko.md#53-사용자-정의-예외)). 처리하는 쪽은 구체적인 `EmptyFieldError`를 먼저, 일반적인 `ValidationError`를 나중에 쓴다([11강 4.2절](Concepts_Lecture.ko.md#42-except절의-순서)).

**코드:**

```python
class ValidationError(Exception):
    def __init__(self, field, message):
        super().__init__(field + ": " + message)
        self.field = field

class EmptyFieldError(ValidationError):
    def __init__(self, field):
        super().__init__(field, "값이 비어 있다")

class RangeError(ValidationError):
    def __init__(self, field, value, low, high):
        super().__init__(field, "값 " + str(value) + ", 허용 범위 " + str(low) + "~" + str(high))

def validate(student):
    for field in ["name", "age"]:
        if student.get(field) in (None, ""):
            raise EmptyFieldError(field)
    if not (0 <= student["age"] <= 150):
        raise RangeError("age", student["age"], 0, 150)
    return True

tests = [{"name": "Kim", "age": 20}, {"name": "", "age": 20}, {"name": "Lee", "age": 200}]
for s in tests:
    try:
        validate(s)
        print(s, "-> 통과")
    except EmptyFieldError as e:
        print(s, "-> 빈 칸:", e.field)
    except ValidationError as e:
        print(s, "-> 검증 실패:", e)
```

**실행 결과:**

```text
{'name': 'Kim', 'age': 20} -> 통과
{'name': '', 'age': 20} -> 빈 칸: name
{'name': 'Lee', 'age': 200} -> 검증 실패: age: 값 200, 허용 범위 0~150
```

- **생성자의 사슬:** `EmptyFieldError("name")`은 `ValidationError.__init__(self, "name", "값이 비어 있다")`를 거쳐 `Exception.__init__(self, "name: 값이 비어 있다")`에 이른다. 그래서 모든 하위 클래스가 `field` 속성과 같은 형태의 메시지를 가진다.
- **`student.get(field)`:** 키가 없으면 `None`을 반환하므로, 항목이 없는 경우와 빈 문자열인 경우를 `in (None, "")` 하나로 검사한다.
- **처리기의 선택:** 둘째 학생은 `EmptyFieldError`이므로 첫 처리기가, 셋째 학생의 `RangeError`는 `ValidationError`의 하위 클래스이므로 둘째 처리기가 받았다. 새 검증 규칙을 위한 하위 클래스를 더해도 둘째 처리기가 그대로 받는다.

---

<br>

## 연습 문제 7: 설정 오류로 바꾸어 알리기

**문제:** 설정 문자열을 해석하면서 생기는 `ValueError`와 `KeyError`를 원인이 연결된 `ConfigError`로 바꾸어 일으키는 `parse_config(text)`를 작성하라. 문제 전문과 실행 예시는 [연습 문제 7](Exercises.ko.md#연습-문제-7-설정-오류로-바꾸어-알리기)에 있다.

### 풀이

**접근 방법:** 호출하는 쪽은 설정 해석이 어떤 내장 예외로 실패하는지 알 필요가 없다. 함수 안에서 낮은 수준의 예외를 잡아 `raise ConfigError(...) from e`로 바꾸면, 호출하는 쪽은 `ConfigError` 하나만 처리하면서도 `__cause__`로 원래 예외를 확인할 수 있다([11강 5.4절](Concepts_Lecture.ko.md#54-예외의-연결)). 줄 번호는 `enumerate()`로, 줄 나누기는 문자열의 `splitlines()`로 한다.

**코드:**

```python
class ConfigError(Exception):
    pass

def parse_config(text):
    settings = {}
    for no, line in enumerate(text.splitlines(), start=1):
        if line.strip() == "":
            continue
        try:
            key, value = line.split("=")
        except ValueError as e:
            raise ConfigError(str(no) + "번째 줄에 '='가 하나여야 한다: " + repr(line)) from e
        settings[key.strip()] = value.strip()
    try:
        port = int(settings["port"])
    except KeyError as e:
        raise ConfigError("port 설정이 없다") from e
    except ValueError as e:
        raise ConfigError("port는 정수여야 한다: " + repr(settings["port"])) from e
    return settings["host"], port

for text in ["host = example.com\nport = 8080", "host = a\nport = eighty", "host = a", "host a\nport = 1"]:
    try:
        print(parse_config(text))
    except ConfigError as e:
        print("설정 오류:", e, "| 원인:", type(e.__cause__).__name__)
```

**실행 결과:**

```text
('example.com', 8080)
설정 오류: port는 정수여야 한다: 'eighty' | 원인: ValueError
설정 오류: port 설정이 없다 | 원인: KeyError
설정 오류: 1번째 줄에 '='가 하나여야 한다: 'host a' | 원인: ValueError
```

- **`split("=")`의 실패:** `"host a"`에는 `=`가 없어 조각이 하나이므로 두 변수로 풀 때 `ValueError`가 난다. `=`가 둘인 줄도 같은 예외가 된다.
- **`strip()`:** `"host = example.com"`을 나눈 조각은 `"host "`, `" example.com"`이므로 앞뒤 공백을 없애고 저장한다.
- **두 처리기:** `int(settings["port"])`의 `KeyError`(키 없음)와 `ValueError`(정수가 아님)를 서로 다른 메시지로 바꾸었다. 원인 예외의 클래스 이름이 두 경우를 구별해 준다.
- **처리하지 않았다면:** 호출하는 쪽에 처리기가 없으면 트레이스백이 원래 예외와 `ConfigError`를 "The above exception was the direct cause of the following exception:"으로 이어 보여 준다.

---

<br>

## 연습 문제 8: 되돌리는 컨텍스트 관리자

**문제:** `with` 블록이 예외로 끝나면 리스트를 블록 전의 내용으로 되돌리는 `Transaction(data)`를 작성하고 이체 함수에 적용하라. 문제 전문과 실행 예시는 [연습 문제 8](Exercises.ko.md#연습-문제-8-되돌리는-컨텍스트-관리자)에 있다.

### 풀이

**접근 방법:** `__enter__()`에서 리스트의 복사본(스냅숏)을 저장하고 원래 리스트를 반환한다. `__exit__()`는 예외의 클래스를 받았을 때만 원래 리스트의 내용을 스냅숏으로 바꾸고, 거짓을 반환하여 예외를 바깥으로 보낸다([11강 7.2절](Concepts_Lecture.ko.md#72-with문과-컨텍스트-관리자)). 내용을 바꿀 때는 슬라이스 대입 `self.data[:] = ...`를 써서 같은 리스트 객체를 유지한다.

**코드:**

```python
class Transaction:
    def __init__(self, data):
        self.data = data

    def __enter__(self):
        self.snapshot = list(self.data)     # copy taken at the start
        return self.data

    def __exit__(self, exc_type, exc_value, tb):
        if exc_type is not None:
            self.data[:] = self.snapshot     # roll back in place
            print("롤백:", exc_type.__name__)
        return False                         # let the exception propagate

balances = [100, 50]

def transfer(amount):
    with Transaction(balances) as b:
        b[0] -= amount
        if b[0] < 0:
            raise ValueError("잔액 부족")
        b[1] += amount

transfer(30)
print(balances)
try:
    transfer(500)
except ValueError as e:
    print("이체 실패:", e)
print(balances)
```

**실행 결과:**

```text
[70, 80]
롤백: ValueError
이체 실패: 잔액 부족
[70, 80]
```

- **성공한 이체:** 30원 이체는 예외 없이 끝나 `__exit__()`가 아무것도 하지 않으므로 `[70, 80]`이 남는다.
- **실패한 이체:** 500원 이체는 `b[0]`을 $70 - 500 = -430$으로 바꾼 뒤 `ValueError`를 일으켰다. `__exit__()`가 리스트를 블록 전의 `[70, 80]`으로 되돌리고 예외를 내보냈으므로, 바깥의 처리기가 실패를 알린 뒤에도 잔액은 그대로이다.
- **슬라이스 대입의 이유:** `self.data = self.snapshot`으로 쓰면 컨텍스트 관리자의 인스턴스 변수만 다른 리스트를 가리키게 될 뿐, 바깥의 `balances`가 가리키는 리스트는 바뀐 상태로 남는다([7강 9.2절](../Lec07_Lists-and-Dictionaries/Concepts_Lecture.ko.md#92-별칭)).
- **얕은 복사의 한계:** `list(self.data)`는 얕은 복사이므로 요소가 리스트 같은 가변 객체이면 그 안쪽의 변경은 되돌리지 못한다. 그런 경우에는 `copy.deepcopy()`로 스냅숏을 만든다.
