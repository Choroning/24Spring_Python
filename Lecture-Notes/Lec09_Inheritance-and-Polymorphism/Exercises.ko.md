# 9강 연습 문제 — 상속과 다형성

[레포지토리 안내](../../README.ko.md) | [English](Exercises.md) | [한국어](Exercises.ko.md)

> **최종 수정일:** 2026-11-19

연습 문제 1과 3은 상속과 재정의, 추상 기반 클래스로 클래스 계층을 만드는 문제이고, 연습 문제 2와 4는 주어진 코드의 실행 결과를 추적하는 문제이다. 연습 문제 5~8은 덕 타이핑, 합성, 연산자 특수 메서드로 객체가 다른 코드와 함께 동작하게 하는 문제이다.

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

**문제:** 직원을 나타내는 클래스 `Employee`와, 직원의 한 종류인 관리자 `Manager`를 정의하라.

- `Employee`는 이름 `name`과 월급 `salary`를 인스턴스 변수로 가지고, 실제 지급액을 반환하는 `pay()`와 `"이름: 지급액원"` 형태의 문자열을 반환하는 `__str__()`을 가진다. 직원의 지급액은 월급과 같다.
- `Manager`는 `Employee`를 상속하고 보너스 `bonus`를 더 가진다. 관리자의 지급액은 월급에 보너스를 더한 값이다.
- 월급과 이름을 저장하는 코드와 `__str__()`은 `Employee`에만 둔다.

월급 3000000원인 직원 Kim과 월급 4000000원, 보너스 1000000원인 관리자 Lee를 한 리스트에 담아 각자를 출력하고, 지급액의 합계를 출력한다.

**실행 예시:**

```text
Kim: 3000000원
Lee: 5000000원
총 급여: 8000000원
```

**[풀이](Solutions.ko.md#연습-문제-1-직원과-관리자)**

---

<br>

## 연습 문제 2: 동적 디스패치의 추적

**문제:** 다음 프로그램의 출력을 실행하지 않고 쓰라. 그리고 세 번째 `print()`에서 `f`, `super().f()`, `self.g()`가 각각 어느 클래스의 메서드를 실행하는지 설명하라.

```python
class A:
    def f(self):
        return "A.f > " + self.g()

    def g(self):
        return "A.g"

class B(A):
    def g(self):
        return "B.g"

class C(B):
    def f(self):
        return "C.f > " + super().f()

print(A().f())
print(B().f())
print(C().f())
```

**[풀이](Solutions.ko.md#연습-문제-2-동적-디스패치의-추적)**

---

<br>

## 연습 문제 3: 추상 도형 클래스

**문제:** `abc` 모듈로 추상 기반 클래스 `Shape`를 정의하라.

- `Shape`는 넓이를 반환하는 `area()`와 둘레를 반환하는 `perimeter()`를 추상 메서드로 가진다.
- `Shape`의 `__str__()`은 `"클래스이름: 넓이 0.00, 둘레 0.00"` 형태로 넓이와 둘레를 소수점 아래 둘째 자리까지 보여 준다. 클래스 이름은 객체의 실제 클래스 이름이다.
- 하위 클래스로 직사각형 `Rectangle(w, h)`, 정사각형 `Square(side)`, 원 `Circle(r)`을 정의한다. 정사각형은 가로와 세로가 같은 직사각형이므로 `Rectangle`을 상속하고, 넓이와 둘레를 다시 정의하지 않는다.

`Rectangle(2, 5)`, `Square(3)`, `Circle(1.5)`를 리스트에 담아 넓이가 작은 순서로 정렬하여 출력하고, 마지막 줄에 `isinstance(Square(3), Rectangle)`과 `issubclass(Square, Shape)`의 값을 출력한다.

**실행 예시:**

```text
Circle: 넓이 7.07, 둘레 9.42
Square: 넓이 9.00, 둘레 12.00
Rectangle: 넓이 10.00, 둘레 14.00
True True
```

**[풀이](Solutions.ko.md#연습-문제-3-추상-도형-클래스)**

---

<br>

## 연습 문제 4: 협력적 super()와 MRO

**문제:** 다음 프로그램에서 `App`의 MRO를 C3 선형화로 손으로 구하고, `App().setup()`의 출력을 쓰라. 그다음 `App`의 정의를 `class App2(Saver, Logger):`로 바꾸면 MRO와 출력이 어떻게 달라지는지 쓰라.

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
```

**[풀이](Solutions.ko.md#연습-문제-4-협력적-super와-mro)**

---

<br>

## 연습 문제 5: 덕 타이핑으로 만든 출력 대상

**문제:** 문자열의 리스트 `lines`와 출력 대상 `out`을 받아 각 문자열 뒤에 줄바꿈 문자를 붙여 `out.write()`로 쓰는 함수 `save_report(lines, out)`을 작성하라. 그리고 다음 두 클래스를 정의하라.

- `ListWriter`: `write(text)`가 받은 문자열을 인스턴스 변수 `lines` 리스트에 추가한다.
- `CountingWriter`: `write(text)`가 받은 문자열의 문자 수를 인스턴스 변수 `chars`에 누적한다.

`report = ["1분기 매출 120", "2분기 매출 150"]`을 `ListWriter`의 객체, `CountingWriter`의 객체, 화면 출력 객체 `sys.stdout`에 차례로 저장한 뒤, `ListWriter` 객체의 `lines`와 `CountingWriter` 객체의 `chars`를 출력한다. 세 출력 대상은 서로 상속 관계가 없어야 한다.

**실행 예시:**

```text
1분기 매출 120
2분기 매출 150
['1분기 매출 120\n', '2분기 매출 150\n']
22
```

**[풀이](Solutions.ko.md#연습-문제-5-덕-타이핑으로-만든-출력-대상)**

---

<br>

## 연습 문제 6: 재생 목록의 합성

**문제:** 곡 `Song(title, seconds)`과 재생 목록 `Playlist(name)`을 정의하라. 재생 목록은 곡의 한 종류가 아니라 곡들을 가지는 객체이다.

- `add(song)`: 곡을 목록 끝에 추가한다.
- `total_seconds()`: 모든 곡의 길이(초)의 합을 반환한다.
- `longest()`: 가장 긴 곡을 반환한다.
- `len()`으로 곡의 수를 얻을 수 있고, 곡이 없는 재생 목록은 조건식에서 거짓이어야 한다.
- `print()`로 출력하면 `"이름 (n곡, m분 s초)"` 형태가 나온다.

"출근길" 재생 목록에 215초, 187초, 242초인 곡 `Song A`, `Song B`, `Song C`를 넣고, 재생 목록, 가장 긴 곡의 제목, 곡의 수와 빈 재생 목록의 진릿값을 출력한다.

**실행 예시:**

```text
출근길 (3곡, 10분 44초)
Song C
3 False
```

**[풀이](Solutions.ko.md#연습-문제-6-재생-목록의-합성)**

---

<br>

## 연습 문제 7: sum()과 함께 쓰는 금액 클래스

**문제:** 원 단위 금액을 나타내는 클래스 `Money(amount)`를 정의하라.

- 두 `Money`의 `+`는 금액을 더한 새 `Money`를 반환한다. `Money`가 아닌 값을 더하면 파이썬의 규칙에 따라 `TypeError`가 나야 한다.
- `sum(지갑)`처럼 `Money`의 리스트를 내장 함수 `sum()`에 그대로 넘겨 합계를 구할 수 있어야 한다.
- `==`는 금액이 같은 `Money`끼리 참이고, `Money`와 정수의 비교는 거짓이다.
- `sorted()`, `min()`, `max()`로 금액 순서를 비교할 수 있어야 한다.
- `repr()`은 `Money(5000)` 형태이다.

**실행 예시:** 지갑 `[Money(5000), Money(1000), Money(10000)]`에 대해 다음을 출력한다.

```text
Money(6000)
Money(16000)
[Money(1000), Money(5000), Money(10000)]
True False
Money(1000) Money(10000)
```

첫 줄은 `Money(5000) + Money(1000)`, 둘째 줄은 지갑의 합계, 셋째 줄은 정렬한 지갑, 넷째 줄은 `Money(3000) == Money(3000)`과 `Money(3000) == 3000`, 다섯째 줄은 지갑의 최솟값과 최댓값이다.

**[풀이](Solutions.ko.md#연습-문제-7-sum과-함께-쓰는-금액-클래스)**

---

<br>

## 연습 문제 8: 분수 클래스

**문제:** 분자와 분모가 정수인 분수를 나타내는 클래스 `Fraction(num, den)`을 정의하라.

- 객체를 만들 때 분수를 기약분수로 줄이고, 음의 부호는 분자에 둔다. 분모는 0이 아니라고 가정한다.
- `+`와 `*`는 결과를 새 `Fraction`으로 반환한다.
- `==`는 값이 같은 분수끼리 참이다. 예를 들어 `Fraction(2, 4) == Fraction(1, 2)`는 참이다.
- `repr()`과 `print()`는 `분자/분모` 형태를 쓴다.

마지막으로 표준 모듈 `fractions`의 `Fraction`으로 $\frac{1}{2} + \frac{1}{3}$을 계산하여 직접 만든 클래스의 결과와 비교한다.

**실행 예시:**

```text
5/6
1/2
True
-1/2 1/2
1/2
5/6
```

차례로 $\frac{1}{2} + \frac{1}{3}$, $\frac{2}{3} \times \frac{3}{4}$, `Fraction(2, 4) == Fraction(1, 2)`, `Fraction(1, -2)`와 `Fraction(-3, -6)`, $\frac{1}{6} + \frac{1}{3}$, 표준 모듈로 계산한 $\frac{1}{2} + \frac{1}{3}$의 결과이다.

**[풀이](Solutions.ko.md#연습-문제-8-분수-클래스)**
