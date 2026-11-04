# 8강 연습 문제 풀이 — 클래스와 객체

[레포지토리 안내](../../README.ko.md) | [English](Solutions.md) | [한국어](Solutions.ko.md)

> **최종 수정일:** 2026-11-04

---

<br>

## 목차

- [연습 문제 1: 원 클래스](#연습-문제-1-원-클래스)
- [연습 문제 2: 은행 계좌 클래스](#연습-문제-2-은행-계좌-클래스)
- [연습 문제 3: 고양이 클래스](#연습-문제-3-고양이-클래스)
- [연습 문제 4: 상자 클래스](#연습-문제-4-상자-클래스)
- [연습 문제 5: 자동차 클래스](#연습-문제-5-자동차-클래스)
- [연습 문제 6: 식별 번호를 가진 카운터](#연습-문제-6-식별-번호를-가진-카운터)

---

<br>

## 연습 문제 1: 원 클래스

**문제:** 반지름을 비공개 인스턴스 변수로 가지고, 반지름의 설정자와 접근자, 넓이와 둘레를 계산하는 메서드를 가진 `Circle` 클래스를 만들어 반지름이 10인 원의 정보를 출력하라. 문제 전문과 실행 예시는 [연습 문제 1](Exercises.ko.md#연습-문제-1-원-클래스)에 있다.

### 풀이

**접근 방법:** 원의 상태는 반지름 하나이므로 인스턴스 변수는 `self.__radius` 하나이다([8강 7.1절](Concepts_Lecture.ko.md#71-비공개-인스턴스-변수)). 넓이와 둘레는 반지름으로 계산할 수 있으므로 인스턴스 변수로 저장하지 않고, 호출할 때마다 계산하여 반환하는 메서드로 만든다.

- **넓이:** 반지름이 $r$인 원의 넓이는 $\pi r^2$이다.
- **둘레:** 반지름이 $r$인 원의 둘레는 $2 \pi r$이다.
- **원주율:** `math` 모듈의 상수 `math.pi`(약 3.141592653589793)를 쓴다.

**코드:**

```python
import math

class Circle:
    def __init__(self, radius=1.0):
        self.__radius = radius

    def setRadius(self, r):
        self.__radius = r

    def getRadius(self):
        return self.__radius

    def calcArea(self):
        area = math.pi * self.__radius * self.__radius
        return area

    def calcCircum(self):
        circumference = 2.0 * math.pi * self.__radius
        return circumference

c1 = Circle(10)
print("원의 반지름=", c1.getRadius())
print("원의 넓이=", c1.calcArea())
print("원의 둘레=", c1.calcCircum())
```

**실행 결과:**

```text
원의 반지름= 10
원의 넓이= 314.1592653589793
원의 둘레= 62.83185307179586
```

- **생성자:** `Circle(10)`은 `radius`에 10을 전달하여 `self.__radius`를 10으로 초기화한다. `radius=1.0`은 기본값이므로 `Circle()`로 만들면 반지름이 1.0인 원이 된다.
- **넓이:** $\pi \times 10 \times 10 = 100\pi \approx 314.1592653589793$이다.
- **둘레:** $2 \times \pi \times 10 = 20\pi \approx 62.83185307179586$이다.
- **비공개 변수:** 클래스 밖에서는 `c1.__radius`로 반지름을 읽을 수 없으므로 접근자 `getRadius()`를 쓴다.

기본값과 설정자를 쓰는 예는 다음과 같다. 출력 자릿수를 줄이려면 `%.2f` 형식을 쓴다.

```python
c2 = Circle()
print(c2.getRadius(), c2.calcArea())
c2.setRadius(2.5)
print(c2.getRadius(), c2.calcArea(), c2.calcCircum())
print('%.2f' % c2.calcArea())
```

```text
1.0 3.141592653589793
2.5 19.634954084936208 15.707963267948966
19.63
```

설정자로 반지름을 2.5로 바꾸면 넓이와 둘레도 바뀐 반지름으로 계산된다. 넓이와 둘레를 인스턴스 변수에 미리 저장해 두었다면 반지름을 바꿀 때마다 그 값들도 함께 고쳐야 하지만, 메서드로 계산하면 상태가 반지름 하나뿐이어서 서로 어긋날 일이 없다.

---

<br>

## 연습 문제 2: 은행 계좌 클래스

**문제:** 잔액만을 비공개 인스턴스 변수로 가지고, 생성자와 `deposit()`, `withdraw()` 메서드를 가진 `BankAccount` 클래스를 만들어 100원을 저금하고 10원을 인출하라. 문제 전문과 실행 예시는 [연습 문제 2](Exercises.ko.md#연습-문제-2-은행-계좌-클래스)에 있다.

### 풀이

**접근 방법:** 새 계좌의 잔액은 0이므로 생성자는 매개변수 없이 `self.__balance = 0`만 한다. 저금은 잔액에 금액을 더하고, 인출은 잔액에서 금액을 뺀다. 잔액을 비공개로 두어 계좌 밖에서는 두 메서드로만 잔액을 바꿀 수 있게 한다([8강 7.3절](Concepts_Lecture.ko.md#73-접근자와-설정자)).

**코드:**

```python
class BankAccount:
    def __init__(self):
        self.__balance = 0             # every new account starts with 0

    def withdraw(self, amount):
        self.__balance -= amount
        print("통장에서 %d원이 출금되었음" % amount)
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount
        print("통장에 %d원이 입금되었음" % amount)
        return self.__balance

a = BankAccount()
a.deposit(100)
a.withdraw(10)
```

**실행 결과:**

```text
통장에 100원이 입금되었음
통장에서 10원이 출금되었음
```

- **`a.deposit(100)`:** 잔액이 0에서 100이 되고, `%d` 자리에 금액 100이 들어간 문구를 출력한 뒤 100을 반환한다.
- **`a.withdraw(10)`:** 잔액이 100에서 90이 되고 90을 반환한다.
- **반환값:** 두 메서드는 바뀐 잔액을 반환하지만, 위 코드는 반환값을 쓰지 않으므로 화면에 나타나지 않는다. `print("잔액:", a.deposit(100))`처럼 쓰면 잔액도 출력된다.

> **주의:** 이 `withdraw()`는 잔액보다 큰 금액도 인출하여 잔액이 음수가 된다. 실제 계좌처럼 동작하려면 인출하기 전에 잔액을 검사해야 한다. 잔액을 비공개로 두었으므로 이 검사를 `withdraw()` 한곳에만 넣으면 모든 인출에 적용된다.

```python
class BankAccount:
    def __init__(self):
        self.__balance = 0

    def withdraw(self, amount):
        if amount > self.__balance:    # refuse to go below zero
            print("잔액이 부족합니다.")
            return self.__balance
        self.__balance -= amount
        print("통장에서 %d원이 출금되었음" % amount)
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount
        print("통장에 %d원이 입금되었음" % amount)
        return self.__balance

a = BankAccount()
print("잔액:", a.deposit(100))
print("잔액:", a.withdraw(10))
print("잔액:", a.withdraw(500))
```

```text
통장에 100원이 입금되었음
잔액: 100
통장에서 10원이 출금되었음
잔액: 90
잔액이 부족합니다.
잔액: 90
```

`a.withdraw(500)`은 500이 잔액 90보다 크므로 잔액을 바꾸지 않고 안내 문구만 출력한 뒤 90을 반환한다. `print("잔액:", a.deposit(100))`에서는 인수인 `a.deposit(100)`이 먼저 실행되어 입금 문구가 출력되고, 그 반환값 100이 `"잔액:"`과 함께 출력된다.

---

<br>

## 연습 문제 3: 고양이 클래스

**문제:** 이름과 나이를 비공개 속성으로 가지고 각 속성의 설정자와 접근자를 가진 `Cat` 클래스를 만들어, Missy(3살)와 Lucky(5살)의 이름과 나이를 출력하라. 문제 전문과 실행 예시는 [연습 문제 3](Exercises.ko.md#연습-문제-3-고양이-클래스)에 있다.

### 풀이

**접근 방법:** 고양이마다 이름과 나이가 다르므로 생성자에서 두 값을 받아 비공개 인스턴스 변수에 저장한다. 고양이 두 마리는 같은 클래스로 만든 서로 다른 객체이다([8강 3.3절](Concepts_Lecture.ko.md#33-하나의-클래스로-여러-객체-만들기)).

**코드:**

```python
class Cat:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setAge(self, age):
        self.__age = age

    def getAge(self):
        return self.__age

missy = Cat('Missy', 3)
lucky = Cat('Lucky', 5)

print(missy.getName(), missy.getAge())
print(lucky.getName(), lucky.getAge())
```

**실행 결과:**

```text
Missy 3
Lucky 5
```

- **객체 생성:** `Cat('Missy', 3)`과 `Cat('Lucky', 5)`는 각자 이름과 나이를 가진 객체 두 개를 만든다. 두 객체는 메서드를 함께 쓰지만 인스턴스 변수는 따로 가진다.
- **출력:** `print()`에 접근자의 반환값 두 개를 넘기므로 이름과 나이가 공백으로 구분되어 출력된다.

설정자로 한 객체의 속성을 바꾸어도 다른 객체는 영향을 받지 않는다.

```python
missy.setAge(4)
print(missy.getName(), missy.getAge())
print(lucky.getName(), lucky.getAge())
```

```text
Missy 4
Lucky 5
```

---

<br>

## 연습 문제 4: 상자 클래스

**문제:** 가로, 세로, 높이를 비공개 인스턴스 변수로 가지고, 세 값의 설정자와 부피를 반환하는 `getVolume()`, `(가로, 세로, 높이)`를 반환하는 `__str__()`을 가진 `Box` 클래스를 만들어 사용하라. 문제 전문과 실행 예시는 [연습 문제 4](Exercises.ko.md#연습-문제-4-상자-클래스)에 있다.

### 풀이

**접근 방법:** 직육면체 상자의 부피는 가로 × 세로 × 높이이다. 객체를 `print()`로 출력할 때 원하는 형태가 나오게 하려면 특수 메서드 `__str__()`이 그 문자열을 반환하게 한다([8강 6.3절](Concepts_Lecture.ko.md#63-문자열-표현-메서드)).

**코드:**

```python
class Box:
    def __init__(self, width=0, length=0, height=0):
        self.__width = width
        self.__length = length
        self.__height = height

    def setWidth(self, width):
        self.__width = width

    def setLength(self, length):
        self.__length = length

    def setHeight(self, height):
        self.__height = height

    def getVolume(self):
        return self.__width * self.__length * self.__height

    def __str__(self):
        return '(%d, %d, %d)' % (self.__width, self.__length, self.__height)

box = Box(100, 100, 100)
print(box)
print('상자의 부피는', box.getVolume())
```

**실행 결과:**

```text
(100, 100, 100)
상자의 부피는 1000000
```

- **`print(box)`:** `print()`가 `box.__str__()`을 호출하고, 그 메서드가 `%` 형식화로 만든 문자열 `'(100, 100, 100)'`을 출력한다.
- **부피:** $100 \times 100 \times 100 = 1000000$이다.
- **기본값:** 생성자의 매개변수가 모두 기본값 0을 가지므로 `Box()`로 만들고 설정자로 나중에 크기를 정할 수도 있다.

```python
b = Box()
print(b, b.getVolume())
b.setWidth(2)
b.setLength(3)
b.setHeight(4)
print(b, b.getVolume())
```

```text
(0, 0, 0) 0
(2, 3, 4) 24
```

> **참고:** `%d`는 정수를 출력하는 형식이므로 `Box(2.5, 1, 1)`처럼 실수를 주면 `__str__()`이 소수점 이하를 버린 `(2, 1, 1)`을 반환한다. 실수 크기도 다루려면 `'(%g, %g, %g)'`처럼 실수를 간결하게 출력하는 `%g` 형식을 쓴다.

---

<br>

## 연습 문제 5: 자동차 클래스

**문제:** 속도, 기어, 색상을 비공개 인스턴스 변수로 가지고(기본값 0, 1, `"white"`), 세 속성의 설정자와 `__str__()`을 가진 `Car` 클래스를 만들어, 기어를 3, 속도를 100으로 바꾼 자동차를 출력하라. 문제 전문과 실행 예시는 [연습 문제 5](Exercises.ko.md#연습-문제-5-자동차-클래스)에 있다.

### 풀이

**접근 방법:** 기본값이 있는 생성자로 자동차를 만들고, 설정자로 상태를 바꾼 뒤 `__str__()`으로 상태를 문자열로 만든다. 색상은 문자열이므로 `%s` 형식으로 넣는다.

**코드:**

```python
class Car:
    def __init__(self, speed=0, gear=1, color="white"):
        self.__speed = speed
        self.__gear = gear
        self.__color = color

    def setSpeed(self, speed):
        self.__speed = speed

    def setGear(self, gear):
        self.__gear = gear

    def setColor(self, color):
        self.__color = color

    def __str__(self):
        return '(%d, %d, %s)' % (self.__speed, self.__gear, self.__color)

myCar = Car()
myCar.setGear(3)
myCar.setSpeed(100)
print(myCar)
```

**실행 결과:**

```text
(100, 3, white)
```

- **`Car()`:** 인수가 없으므로 속도 0, 기어 1, 색상 `"white"`인 자동차가 만들어진다.
- **설정자:** `setGear(3)`과 `setSpeed(100)`이 기어와 속도를 바꾸고, 색상은 기본값 그대로이다.
- **`__str__()`:** `'(%d, %d, %s)'`의 세 자리에 속도, 기어, 색상이 차례로 들어가 `'(100, 3, white)'`가 된다.

생성자의 기본값은 일부만 바꿀 수도 있다. 키워드 인수 `color="red"`는 색상만 바꾸고 나머지는 기본값을 쓴다([6강 6.2절](../Lec06_Functions/Concepts_Lecture.ko.md#62-키워드-인수)).

```python
print(Car(), Car(color="red"), Car(30, 2, "black"))
```

```text
(0, 1, white) (0, 1, red) (30, 2, black)
```

---

<br>

## 연습 문제 6: 식별 번호를 가진 카운터

**문제:** `count`와 `id`를 인스턴스 변수로 가지는 클래스로 `id_set = [3, 6, 10, 5, 2]`의 값마다 객체를 만들고, 각 객체의 `count`를 `id`번 증가시킨 뒤 `id`가 짝수인 객체의 값을 출력하라. 같은 문제를 리스트만으로 다시 풀라. 문제 전문과 실행 예시는 [연습 문제 6](Exercises.ko.md#연습-문제-6-식별-번호를-가진-카운터)에 있다.

### 풀이

**접근 방법:** [8강 4절](Concepts_Lecture.ko.md#4-counter-클래스)의 `Counter` 클래스에 식별 번호 `id`를 더한 클래스를 만든다. 생성자는 `id`를 받아 저장하고 `count`를 0으로 초기화하며, `increment()`는 `count`를 1 늘린다.

- **객체 생성:** `id_set`을 순회하며 값마다 객체를 하나씩 만들고 리스트 `objects`에 담는다.
- **증가:** 객체마다 `range(obj.id)`만큼 반복하여 `increment()`를 호출하므로, 반복이 끝나면 `count`는 `id`와 같아진다.
- **선택 출력:** `obj.id % 2 == 0`이면 `id`가 짝수이다.

**코드 (클래스 사용):**

```python
class IdCounter:
    def __init__(self, id_value):
        self.id = id_value            # identifier taken from id_set
        self.count = 0                # every object starts counting from 0

    def increment(self):
        self.count += 1

id_set = [3, 6, 10, 5, 2]
objects = []

for v in id_set:
    obj = IdCounter(v)
    for _ in range(obj.id):           # increase count id times
        obj.increment()
    objects.append(obj)

for obj in objects:
    if obj.id % 2 == 0:               # only objects with an even id
        print("id = %d, count = %d" % (obj.id, obj.count))
```

**실행 결과:**

```text
id = 6, count = 6
id = 10, count = 10
id = 2, count = 2
```

- **객체의 리스트:** `objects`는 `IdCounter` 객체 5개를 요소로 가지는 리스트이며, 두 번째 반복문은 이 리스트를 순회하며 각 객체의 인스턴스 변수를 읽는다.
- **매개변수 이름:** 생성자의 매개변수 이름은 `id`가 아니라 `id_value`이다. `id`는 내장 함수 `id()`의 이름이므로 매개변수로 쓰면 함수 안에서 내장 함수를 가린다. 인스턴스 변수 `self.id`는 객체의 속성이므로 내장 함수와 충돌하지 않는다.

**코드 (리스트만 사용):**

```python
id_set = [3, 6, 10, 5, 2]
counts = [0] * len(id_set)            # counts[k] belongs to id_set[k]

for k in range(len(id_set)):
    for _ in range(id_set[k]):        # increase count id times
        counts[k] += 1

for k in range(len(id_set)):
    if id_set[k] % 2 == 0:
        print("id = %d, count = %d" % (id_set[k], counts[k]))
```

**실행 결과:**

```text
id = 6, count = 6
id = 10, count = 10
id = 2, count = 2
```

리스트 풀이는 `id_set`과 `counts`를 같은 인덱스 `k`로 짝짓는 병렬 리스트이다([8강 1.1절](Concepts_Lecture.ko.md#11-문제-상황)). 이 문제처럼 데이터가 두 종류뿐이면 리스트 풀이도 짧지만, 객체를 정렬하거나 삭제하거나 속성을 더하면 두 리스트를 늘 함께 고쳐야 한다. 클래스 풀이는 `id`와 `count`가 한 객체 안에 있으므로 이런 동기화가 필요 없고, `count`를 늘리는 동작도 `increment()` 메서드로 데이터와 함께 클래스 안에 정의된다.
