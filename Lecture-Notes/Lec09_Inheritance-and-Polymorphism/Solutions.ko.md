# 9강 연습 문제 풀이 — 상속과 다형성

[레포지토리 안내](../../README.ko.md) | [English](Solutions.md) | [한국어](Solutions.ko.md)

> **최종 수정일:** 2026-11-19

---

<br>

## 목차

- [연습 문제 1: 직원과 관리자](#연습-문제-1-직원과-관리자)
- [연습 문제 2: 동적 디스패치의 추적](#연습-문제-2-동적-디스패치의-추적)
- [연습 문제 3: 추상 도형 클래스](#연습-문제-3-추상-도형-클래스)
- [연습 문제 4: 협력적 super()와 MRO](#연습-문제-4-협력적-super와-mro)
- [연습 문제 5: 덕 타이핑으로 만든 출력 대상](#연습-문제-5-덕-타이핑으로-만든-출력-대상)
- [연습 문제 6: 재생 목록의 합성](#연습-문제-6-재생-목록의-합성)
- [연습 문제 7: sum()과 함께 쓰는 금액 클래스](#연습-문제-7-sum과-함께-쓰는-금액-클래스)
- [연습 문제 8: 분수 클래스](#연습-문제-8-분수-클래스)

---

<br>

## 연습 문제 1: 직원과 관리자

**문제:** 이름과 월급을 가지는 `Employee`와, 보너스를 더 가지며 지급액이 월급과 보너스의 합인 하위 클래스 `Manager`를 정의하고 두 사람의 지급액과 합계를 출력하라. 문제 전문과 실행 예시는 [연습 문제 1](Exercises.ko.md#연습-문제-1-직원과-관리자)에 있다.

### 풀이

**접근 방법:** 관리자는 직원의 한 종류(is-a)이므로 상속이 알맞다([9강 1.2절](Concepts_Lecture.ko.md#12-상위-클래스와-하위-클래스)). `Manager`는 생성자에서 `super().__init__()`으로 이름과 월급의 저장을 `Employee`에 맡기고 보너스만 더한다. 지급액은 `pay()`를 재정의하되 `super().pay()`로 월급을 얻어 보너스를 더하므로, 월급의 계산 방식이 바뀌어도 `Manager`는 고칠 필요가 없다([9강 2.2절](Concepts_Lecture.ko.md#22-super로-상위-클래스의-메서드-호출하기)).

**코드:**

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def pay(self):
        return self.salary

    def __str__(self):
        return self.name + ": " + str(self.pay()) + "원"

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)      # reuse Employee's initialization
        self.bonus = bonus

    def pay(self):
        return super().pay() + self.bonus   # extend, not replace

staff = [Employee("Kim", 3000000), Manager("Lee", 4000000, 1000000)]
total = 0
for e in staff:
    print(e)
    total += e.pay()
print("총 급여: " + str(total) + "원")
```

**실행 결과:**

```text
Kim: 3000000원
Lee: 5000000원
총 급여: 8000000원
```

- **`__str__()`의 공유:** `__str__()`은 `Employee`에만 있지만, 그 안의 `self.pay()`는 동적 디스패치에 따라 객체의 실제 클래스의 `pay()`를 부른다. 그래서 Lee의 줄에는 보너스를 더한 5000000원이 나온다.
- **반복문:** `print(e)`와 `e.pay()`는 직원과 관리자를 구분하지 않는다. 계약직 같은 새 종류를 더해도 이 반복문은 그대로이다.
- **합계:** $3000000 + (4000000 + 1000000) = 8000000$이다.

---

<br>

## 연습 문제 2: 동적 디스패치의 추적

**문제:** `A`, `B`, `C` 세 클래스에서 `A().f()`, `B().f()`, `C().f()`의 출력을 쓰고, 세 번째 호출에서 각 메서드가 어느 클래스의 것인지 설명하라. 문제 전문은 [연습 문제 2](Exercises.ko.md#연습-문제-2-동적-디스패치의-추적)에 있다.

### 풀이

**실행 결과:**

```text
A.f > A.g
A.f > B.g
C.f > A.f > B.g
```

**추적:** 세 호출 모두에서 `self.g()`는 `self`의 실제 클래스부터 `g`를 찾는다([9강 2.4절](Concepts_Lecture.ko.md#24-동적-디스패치의-추적)).

| 호출 | `f`를 찾은 곳 | `self.g()`를 찾은 곳 | 결과 |
|:-----|:-----|:-----|:-----|
| `A().f()` | `A` | `A` | `A.f > A.g` |
| `B().f()` | `B`에 없어 `A` | `B` | `A.f > B.g` |
| `C().f()` | `C` | `C`에 없어 `B` | `C.f > A.f > B.g` |

*표 1. 세 호출에서 메서드를 찾은 클래스*

- **`C().f()`의 `f`:** `C`가 `f`를 재정의했으므로 `C.f()`가 실행되어 `"C.f > "`를 만든다.
- **`super().f()`:** `C`의 MRO는 `C, B, A, object`이므로 `C` 다음인 `B`부터 `f`를 찾는다. `B`에는 `f`가 없어 `A.f()`가 실행되며, 이때 `self`는 여전히 `C`의 객체이다.
- **`A.f()` 안의 `self.g()`:** `self`가 `C`의 객체이므로 `C`부터 찾고, `C`에는 없어 `B.g()`가 실행된다. `A.f()`의 코드가 같은 클래스의 `A.g()`가 아니라 `B.g()`를 부르는 것이 동적 디스패치의 결과이다.

---

<br>

## 연습 문제 3: 추상 도형 클래스

**문제:** `area()`와 `perimeter()`를 추상 메서드로 가진 `Shape`와, 하위 클래스 `Rectangle`, `Rectangle`을 상속하는 `Square`, `Circle`을 정의하고 넓이 순으로 출력하라. 문제 전문과 실행 예시는 [연습 문제 3](Exercises.ko.md#연습-문제-3-추상-도형-클래스)에 있다.

### 풀이

**접근 방법:** `ABC`를 상속하고 두 메서드에 `@abstractmethod`를 붙인다([9강 5.2절](Concepts_Lecture.ko.md#52-abc-모듈)). 출력 형식은 모든 도형에 공통이므로 `Shape`의 `__str__()`에 한 번만 두고, 클래스 이름은 `type(self).__name__`으로 얻는다. 정사각형은 가로와 세로가 같은 직사각형이므로 생성자에서 `super().__init__(side, side)`만 호출하면 넓이와 둘레를 모두 물려받는다.

- **직사각형:** 넓이는 $wh$, 둘레는 $2(w + h)$이다.
- **원:** 넓이는 $\pi r^2$, 둘레는 $2 \pi r$이다.

**코드:**

```python
import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def __str__(self):
        return "%s: 넓이 %.2f, 둘레 %.2f" % (type(self).__name__, self.area(), self.perimeter())

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)        # a square is a rectangle with w == h

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r ** 2

    def perimeter(self):
        return 2 * math.pi * self.r

shapes = [Rectangle(2, 5), Square(3), Circle(1.5)]
shapes.sort(key=lambda s: s.area())
for s in shapes:
    print(s)
print(isinstance(Square(3), Rectangle), issubclass(Square, Shape))
```

**실행 결과:**

```text
Circle: 넓이 7.07, 둘레 9.42
Square: 넓이 9.00, 둘레 12.00
Rectangle: 넓이 10.00, 둘레 14.00
True True
```

- **넓이:** 원은 $\pi \times 1.5^2 = 2.25\pi \approx 7.07$, 정사각형은 $3 \times 3 = 9$, 직사각형은 $2 \times 5 = 10$이므로 정렬 순서는 원, 정사각형, 직사각형이다.
- **둘레:** 원은 $2 \pi \times 1.5 = 3\pi \approx 9.42$, 정사각형은 $2(3 + 3) = 12$, 직사각형은 $2(2 + 5) = 14$이다.
- **정렬:** `sort()`의 `key`에 넓이를 돌려주는 람다 함수를 주었다([7강 4.3절](../Lec07_Lists-and-Dictionaries/Concepts_Lecture.ko.md#43-정렬)). `Shape`에 `__lt__()`가 없어도 `key`가 숫자를 돌려주므로 정렬할 수 있다.
- **`Square`의 클래스 이름:** `Square`는 `__str__()`을 `Shape`에서, 넓이와 둘레를 `Rectangle`에서 물려받지만, `type(self).__name__`이 실제 클래스 이름 `"Square"`를 돌려준다.
- **관계 검사:** 정사각형은 직사각형이고 직사각형은 도형이므로 두 검사 모두 참이다.

> **참고:** 정사각형을 직사각형의 하위 클래스로 두는 것은 객체가 만든 뒤 바뀌지 않을 때만 자연스럽다. 직사각형에 가로만 바꾸는 `set_width()`가 있다면, 그 메서드를 물려받은 정사각형은 가로와 세로가 달라져 정사각형이 아니게 된다. 이처럼 상위 클래스의 연산이 하위 클래스의 조건을 깰 수 있으면 [9강 6.3절](Concepts_Lecture.ko.md#63-상속과-합성을-고르는-기준)의 기준에 따라 상속 관계를 다시 생각해야 한다.

---

<br>

## 연습 문제 4: 협력적 super()와 MRO

**문제:** `Logger`와 `Saver`가 모두 `Base`를 상속하고 `App(Logger, Saver)`가 둘을 상속할 때 `App`의 MRO와 `App().setup()`의 출력을 구하고, 상위 클래스의 순서를 바꾼 `App2(Saver, Logger)`와 비교하라. 문제 전문은 [연습 문제 4](Exercises.ko.md#연습-문제-4-협력적-super와-mro)에 있다.

### 풀이

**MRO의 계산:** `L[Base] = [Base, object]`, `L[Logger] = [Logger, Base, object]`, `L[Saver] = [Saver, Base, object]`이다([9강 4.2절](Concepts_Lecture.ko.md#42-다이아몬드-상속과-mro)).

| 단계 | merge에 남은 리스트 | 고른 클래스 |
|:-----|:-----|:-----|
| 1 | `[Logger, Base, object]`, `[Saver, Base, object]`, `[Logger, Saver]` | `Logger` |
| 2 | `[Base, object]`, `[Saver, Base, object]`, `[Saver]` | `Base`는 꼬리에 있어 건너뛰고 `Saver` |
| 3 | `[Base, object]`, `[Base, object]` | `Base` |
| 4 | `[object]`, `[object]` | `object` |

*표 2. App의 MRO를 계산하는 merge 과정*

따라서 `App`의 MRO는 `App, Logger, Saver, Base, object`이다.

**확인 코드:**

```python
class Base:
    def setup(self):
        print("Base.setup")

class Logger(Base):
    def setup(self):
        print("Logger.setup")
        super().setup()

class Saver(Base):
    def setup(self):
        print("Saver.setup")
        super().setup()

class App(Logger, Saver):
    def setup(self):
        print("App.setup")
        super().setup()

App().setup()
print([c.__name__ for c in App.__mro__])

class App2(Saver, Logger):
    def setup(self):
        print("App2.setup")
        super().setup()

App2().setup()
print([c.__name__ for c in App2.__mro__])
```

**실행 결과:**

```text
App.setup
Logger.setup
Saver.setup
Base.setup
['App', 'Logger', 'Saver', 'Base', 'object']
App2.setup
Saver.setup
Logger.setup
Base.setup
['App2', 'Saver', 'Logger', 'Base', 'object']
```

- **`Logger` 안의 `super()`:** `App`의 객체에서는 MRO의 `Logger` 다음인 `Saver`를 가리킨다. `Logger`의 상위 클래스는 `Base`이지만, `Saver`를 건너뛰고 `Base`로 가지 않는다([9강 4.3절](Concepts_Lecture.ko.md#43-협력적-super-호출)).
- **`Base.setup`이 한 번:** 네 클래스가 모두 `super()`로 다음 클래스를 부르므로 다이아몬드의 꼭대기 `Base`는 정확히 한 번 실행된다.
- **순서를 바꾼 경우:** `App2(Saver, Logger)`는 지역 우선순위에 따라 `Saver`가 `Logger`보다 앞에 오므로, 같은 클래스들이 `Saver`, `Logger`, `Base` 순으로 실행된다. 상위 클래스를 쓰는 순서가 실행 순서를 바꾼다.

---

<br>

## 연습 문제 5: 덕 타이핑으로 만든 출력 대상

**문제:** `out.write()`만 호출하는 함수 `save_report(lines, out)`과, `write()`를 가진 두 클래스 `ListWriter`, `CountingWriter`를 만들어 같은 보고서를 세 출력 대상에 저장하라. 문제 전문과 실행 예시는 [연습 문제 5](Exercises.ko.md#연습-문제-5-덕-타이핑으로-만든-출력-대상)에 있다.

### 풀이

**접근 방법:** `save_report()`가 출력 대상에 요구하는 것은 문자열을 받는 `write()` 메서드 하나뿐이다. 덕 타이핑에 따라 이 메서드를 가진 객체라면 무엇이든 출력 대상이 될 수 있으므로, 공통 상위 클래스를 두지 않는다([9강 3.2절](Concepts_Lecture.ko.md#32-덕-타이핑)). 화면 출력 객체 `sys.stdout`도 `write()`를 가진 객체이므로 그대로 넘길 수 있다.

**코드:**

```python
import sys

def save_report(lines, out):
    for line in lines:
        out.write(line + "\n")      # only requires a write() method

class ListWriter:
    def __init__(self):
        self.lines = []

    def write(self, text):
        self.lines.append(text)

class CountingWriter:
    def __init__(self):
        self.chars = 0

    def write(self, text):
        self.chars += len(text)

report = ["1분기 매출 120", "2분기 매출 150"]
w1 = ListWriter()
w2 = CountingWriter()
save_report(report, w1)
save_report(report, w2)
save_report(report, sys.stdout)
print(w1.lines)
print(w2.chars)
```

**실행 결과:**

```text
1분기 매출 120
2분기 매출 150
['1분기 매출 120\n', '2분기 매출 150\n']
22
```

- **`sys.stdout`:** 첫 두 줄은 `save_report(report, sys.stdout)`이 화면에 쓴 것이다. `print()`도 내부에서 `sys.stdout.write()`를 호출한다.
- **문자 수:** `"1분기 매출 120\n"`은 한글 4자, 숫자 4자, 공백 2자, 줄바꿈 1자로 11자이고, 두 번째 줄도 11자이므로 합은 22이다. `len()`은 바이트가 아니라 문자를 센다.
- **확장:** 10강의 파일 객체도 `write()`를 가지므로, `open()`으로 연 파일을 넘기면 같은 함수로 보고서를 파일에 저장할 수 있다.

---

<br>

## 연습 문제 6: 재생 목록의 합성

**문제:** `Song`과, 곡들을 가지는 `Playlist`를 정의하고 `add()`, `total_seconds()`, `longest()`, `len()`, 진릿값, 문자열 표현이 동작하게 하라. 문제 전문과 실행 예시는 [연습 문제 6](Exercises.ko.md#연습-문제-6-재생-목록의-합성)에 있다.

### 풀이

**접근 방법:** 재생 목록은 곡들을 가지는(has-a) 관계이므로 합성으로 만든다([9강 6.1절](Concepts_Lecture.ko.md#61-is-a-관계와-has-a-관계)). 곡들은 인스턴스 변수인 리스트에 담고, 곡의 수는 `__len__()`으로 알린다. `__bool__()`을 따로 정의하지 않아도 `__len__()`이 0을 반환하면 거짓이 된다([9강 7.3절](Concepts_Lecture.ko.md#73-문자열-표현과-길이)). 전체 시간을 분과 초로 나누는 데는 몫과 나머지를 함께 돌려주는 내장 함수 `divmod()`를 쓴다.

**코드:**

```python
class Song:
    def __init__(self, title, seconds):
        self.title = title
        self.seconds = seconds

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []                 # a Playlist has Songs

    def add(self, song):
        self.songs.append(song)

    def total_seconds(self):
        total = 0
        for s in self.songs:
            total += s.seconds
        return total

    def longest(self):
        return max(self.songs, key=lambda s: s.seconds)

    def __len__(self):
        return len(self.songs)

    def __str__(self):
        m, s = divmod(self.total_seconds(), 60)
        return "%s (%d곡, %d분 %d초)" % (self.name, len(self), m, s)

p = Playlist("출근길")
p.add(Song("Song A", 215))
p.add(Song("Song B", 187))
p.add(Song("Song C", 242))
print(p)
print(p.longest().title)
print(len(p), bool(Playlist("빈 목록")))
```

**실행 결과:**

```text
출근길 (3곡, 10분 44초)
Song C
3 False
```

- **전체 시간:** $215 + 187 + 242 = 644$초이고 `divmod(644, 60)`은 `(10, 44)`이므로 10분 44초이다.
- **가장 긴 곡:** `max()`의 `key`에 곡의 길이를 돌려주는 람다 함수를 주었으므로 242초인 `Song C`가 반환된다. 곡끼리의 크기 비교(`__lt__()`)를 정의하지 않아도 된다.
- **진릿값:** 빈 재생 목록은 `__len__()`이 0이므로 `bool()`이 `False`이다.

---

<br>

## 연습 문제 7: sum()과 함께 쓰는 금액 클래스

**문제:** 덧셈, `sum()`, 같음 비교, 크기 비교, 표현 문자열이 동작하는 `Money` 클래스를 정의하라. 문제 전문과 실행 예시는 [연습 문제 7](Exercises.ko.md#연습-문제-7-sum과-함께-쓰는-금액-클래스)에 있다.

### 풀이

**접근 방법:** 내장 함수 `sum(리스트)`는 시작값 0에 요소를 차례로 더한다. 첫 덧셈 `0 + Money(5000)`에서 정수의 `__add__()`는 `Money`를 모르므로 `NotImplemented`를 반환하고, 파이썬은 오른쪽 피연산자의 `Money.__radd__(Money(5000), 0)`을 호출한다([9강 7.4절](Concepts_Lecture.ko.md#74-notimplemented와-반사-연산)). 따라서 `__radd__()`가 0을 받았을 때 자기 자신을 반환하면 `sum()`이 동작한다. 지원하지 않는 피연산자에는 `NotImplemented`를 반환하여 파이썬이 알맞은 `TypeError`를 내게 한다.

**코드:**

```python
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        if isinstance(other, Money):
            return Money(self.amount + other.amount)
        return NotImplemented

    def __radd__(self, other):
        if other == 0:                  # sum() starts from 0
            return self
        return NotImplemented

    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return self.amount == other.amount

    def __lt__(self, other):
        return self.amount < other.amount

    def __repr__(self):
        return "Money(" + str(self.amount) + ")"

wallet = [Money(5000), Money(1000), Money(10000)]
print(Money(5000) + Money(1000))
print(sum(wallet))
print(sorted(wallet))
print(Money(3000) == Money(3000), Money(3000) == 3000)
print(min(wallet), max(wallet))
```

**실행 결과:**

```text
Money(6000)
Money(16000)
[Money(1000), Money(5000), Money(10000)]
True False
Money(1000) Money(10000)
```

- **`sum(wallet)`의 과정:** `0 + Money(5000)`은 `__radd__()`로 `Money(5000)`이 되고, 이어서 `Money(5000) + Money(1000)`과 `Money(6000) + Money(10000)`은 `__add__()`로 계산되어 `Money(16000)`이 된다.
- **`Money(3000) == 3000`:** `Money.__eq__()`가 `NotImplemented`를 반환하고 정수의 `__eq__()`도 `Money`와의 비교를 모르므로, 파이썬은 두 객체가 같은 객체인지(`is`)로 판정하여 `False`를 낸다([9강 7.2절](Concepts_Lecture.ko.md#72-비교-연산자의-정의)).
- **정렬과 최솟값, 최댓값:** `sorted()`, `min()`, `max()`는 `<`만 쓰므로 `__lt__()`로 충분하다.
- **해시:** `__eq__()`를 정의했으므로 `Money`의 객체는 세트에 넣을 수 없다. 금액을 세트나 딕셔너리의 키로 써야 한다면 `__hash__()`를 `hash(self.amount)`로 정의하고 금액을 바꾸지 않는다.

`Money(1000) + 500`을 계산하면 `__add__()`와 정수의 `__radd__()`가 모두 `NotImplemented`를 반환하므로 `TypeError: unsupported operand type(s) for +: 'Money' and 'int'`가 난다. `__radd__()`가 받아들이는 정수는 `sum()`의 시작값 0뿐이므로 `0 + Money(1000)`만 예외로 계산되고, `500 + Money(1000)`은 `TypeError: unsupported operand type(s) for +: 'int' and 'Money'`이다.

---

<br>

## 연습 문제 8: 분수 클래스

**문제:** 기약분수로 저장하고 `+`, `*`, `==`, 표현 문자열이 동작하는 `Fraction` 클래스를 정의하고 표준 모듈 `fractions`와 결과를 비교하라. 문제 전문과 실행 예시는 [연습 문제 8](Exercises.ko.md#연습-문제-8-분수-클래스)에 있다.

### 풀이

**접근 방법:** 분수 $\frac{a}{b}$와 $\frac{c}{d}$의 합과 곱은 다음과 같다.

```math
\frac{a}{b} + \frac{c}{d} = \frac{ad + cb}{bd}, \qquad \frac{a}{b} \times \frac{c}{d} = \frac{ac}{bd}
```

결과를 생성자에 넘기면 생성자가 기약분수로 줄이므로, 연산 메서드는 공식대로 분자와 분모만 계산한다. 기약분수로 줄이려면 분자와 분모를 최대공약수로 나눈다. 최대공약수는 `math.gcd()`로 구하며, 이 함수는 인수의 부호와 관계없이 0 이상의 값을 돌려준다. 분모가 음수이면 먼저 분자와 분모의 부호를 함께 바꾸어 부호를 분자에 둔다. 모든 분수가 같은 규칙으로 줄여져 있으므로 `==`는 분자끼리, 분모끼리 비교하면 된다.

**코드:**

```python
import math

class Fraction:
    def __init__(self, num, den):
        if den < 0:                     # keep the sign in the numerator
            num, den = -num, -den
        g = math.gcd(num, den)
        self.num = num // g
        self.den = den // g

    def __add__(self, other):
        return Fraction(self.num * other.den + other.num * self.den,
                        self.den * other.den)

    def __mul__(self, other):
        return Fraction(self.num * other.num, self.den * other.den)

    def __eq__(self, other):
        return self.num == other.num and self.den == other.den

    def __repr__(self):
        return str(self.num) + "/" + str(self.den)

print(Fraction(1, 2) + Fraction(1, 3))
print(Fraction(2, 3) * Fraction(3, 4))
print(Fraction(2, 4) == Fraction(1, 2))
print(Fraction(1, -2), Fraction(-3, -6))
print(Fraction(1, 6) + Fraction(1, 3))

import fractions
print(fractions.Fraction(1, 2) + fractions.Fraction(1, 3))
```

**실행 결과:**

```text
5/6
1/2
True
-1/2 1/2
1/2
5/6
```

- **덧셈:** $\frac{1}{2} + \frac{1}{3} = \frac{1 \times 3 + 1 \times 2}{2 \times 3} = \frac{5}{6}$이고, 최대공약수가 1이므로 그대로이다.
- **곱셈:** $\frac{2}{3} \times \frac{3}{4} = \frac{6}{12}$이고, 최대공약수 6으로 나누어 $\frac{1}{2}$이다.
- **같음:** `Fraction(2, 4)`는 생성자에서 최대공약수 2로 나누어 1/2로 저장되므로 `Fraction(1, 2)`와 같다.
- **부호:** `Fraction(1, -2)`는 분모가 음수이므로 부호를 바꾸어 $\frac{-1}{2}$로, `Fraction(-3, -6)`은 $\frac{3}{6}$을 거쳐 $\frac{1}{2}$로 저장된다.
- **결과의 약분:** $\frac{1}{6} + \frac{1}{3} = \frac{1 \times 3 + 1 \times 6}{18} = \frac{9}{18}$이고, 최대공약수 9로 나누어 $\frac{1}{2}$이다.
- **표준 모듈:** `fractions.Fraction`도 같은 결과 `5/6`을 낸다. 표준 모듈의 분수는 이 풀이의 연산 외에도 뺄셈, 나눗셈, 크기 비교, 해시, 정수와의 혼합 연산을 모두 지원하므로 실제 계산에는 표준 모듈을 쓴다.
