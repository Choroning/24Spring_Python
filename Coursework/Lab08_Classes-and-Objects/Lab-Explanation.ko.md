# 실습 8 해설 — 클래스와 객체

[레포지토리 안내](../../README.ko.md) | [English](Lab-Explanation.md) | [한국어](Lab-Explanation.ko.md)

> **최종 수정일:** 2026-11-04

> **학습 목표:**
> 1. 클래스를 정의하고 객체를 만들어 메서드를 호출할 수 있다
> 2. `self`와 인스턴스 변수의 역할을 설명할 수 있다
> 3. 생성자 `__init__()`으로 객체를 만들 때 인스턴스 변수를 초기화할 수 있다
> 4. 접근자와 설정자로 인스턴스 변수를 다루고, `__`로 시작하는 이름이 정보 은닉에 쓰이는 원리를 설명할 수 있다
> 5. 한 객체의 메서드가 다른 객체의 인스턴스 변수를 바꾸는 프로그램을 작성할 수 있다

---

## 목차

- [1. 실습 구성과 실행 방법](#1-실습-구성과-실행-방법)
- [2. 클래스와 객체](#2-클래스와-객체)
  - [2.1 생성자가 없는 Counter 클래스](#21-생성자가-없는-counter-클래스)
  - [2.2 생성자 `__init__()`](#22-생성자-__init__)
- [3. 접근자, 설정자, 정보 은닉](#3-접근자-설정자-정보-은닉)
  - [3.1 get()과 set()](#31-get과-set)
  - [3.2 `__`로 시작하는 인스턴스 변수](#32-__로-시작하는-인스턴스-변수)
- [4. 객체 사이의 상호 작용](#4-객체-사이의-상호-작용)
  - [4.1 공격과 회복](#41-공격과-회복)
- [요약](#요약)
- [점검 문제](#점검-문제)

---

<br>

## 1. 실습 구성과 실행 방법

[8강 클래스와 객체](../../Lecture-Notes/Lec08_Classes-and-Objects/Concepts_Lecture.ko.md)를 따라 작성한 코드이다. 2절은 클래스의 정의와 생성자를, 3절은 접근자, 설정자와 정보 은닉을, 4절은 여러 객체가 서로의 상태를 바꾸는 프로그램을 다룬다.

```text
Coursework/Lab08_Classes-and-Objects/
├── Lab-Explanation.ko.md       # 이 문서 (한국어)
├── Lab-Explanation.md          # 이 문서 (영어)
├── Lab_Counter.py              # 2.1 생성자가 없는 Counter 클래스
├── Lab_CounterConstructor.py   # 2.2 생성자 __init__()
├── Lab_CounterAccessors.py     # 3.1 get()과 set()
├── Lab_CounterPrivate.py       # 3.2 __로 시작하는 인스턴스 변수
└── Lab_AttackAndHeal.py        # 4.1 공격과 회복
```

*그림 1. 실습 8의 디렉토리 구성*

모든 프로그램은 표준 라이브러리만 쓰므로 파이썬 3에서 그대로 실행된다. 각 파일의 맨 위에는 파일 이름, 한 줄 설명, 작성자, 작성일을 적은 문서화 문자열(docstring)이 있으며, 이 문서의 코드 블록에서는 그 부분을 생략한다.

```bash
cd Coursework/Lab08_Classes-and-Objects
python3 Lab_Counter.py
```

---

<br>

## 2. 클래스와 객체

### 2.1 생성자가 없는 Counter 클래스

**코드:** [Lab_Counter.py](Lab_Counter.py)

```python
class Counter:
    def reset(self):
        self.count = 0
    def increment(self):
        self.count += 1
    def get(self):
        return self.count

## main ##
a = Counter()
a.reset()
a.increment()
print("카운터 a의 값은", a.get())
```

- **클래스와 객체:** **클래스(class)** 는 객체의 설계도이고, `Counter()`처럼 클래스를 호출하면 그 설계도에 따라 **객체(object)** 가 하나 만들어진다. 이렇게 만든 객체를 그 클래스의 **인스턴스(instance)** 라고 한다. `Counter`는 경기장이나 콘서트에 입장하는 관객 수를 세는 데 쓸 수 있는 기계식 계수기를 나타낸다.
- **메서드와 `self`:** 클래스 안에 정의한 함수를 **메서드(method)** 라고 한다. 메서드의 첫 매개변수 `self`는 그 메서드를 호출한 객체 자신이다. `a.reset()`을 호출하면 파이썬이 `a`를 `self`에 넣어 `Counter.reset(a)`처럼 실행한다.
- **인스턴스 변수:** `self.count = 0`처럼 `self.`을 붙인 변수에 대입하면 그 객체에 속한 **인스턴스 변수(instance variable)** 가 만들어진다. 객체마다 따로 가지므로 `b = Counter()`를 하나 더 만들면 `b.count`는 `a.count`와 별개이다.
- **실행 순서:** `reset()`이 `count`를 만들고 0으로 두며, `increment()`가 1을 더하고, `get()`이 그 값을 반환한다.

**실행 결과:** "카운터 a의 값은 1"이 출력된다.

```text
카운터 a의 값은 1
```

> **주의:** 이 클래스에는 생성자가 없으므로 `count`는 `reset()`을 호출해야 비로소 만들어진다. `reset()` 없이 `a.increment()`를 먼저 호출하면 아직 없는 `self.count`를 읽으려 하므로 `AttributeError: 'Counter' object has no attribute 'count'`가 발생한다. 2.2절의 생성자가 이 문제를 없앤다.

### 2.2 생성자 `__init__()`

**코드:** [Lab_CounterConstructor.py](Lab_CounterConstructor.py)

```python
class Counter:
    def __init__(self): #자동호출
        self.count = 0
    def increment(self):
        self.count += 1
    def reset(self):
        self.count = 0
    def get(self):
        print(self.count)

## main ##        #절차지향ver.
C = Counter()
C.get()               #print(C.count)
C.increment()    #C.count += 1
C.increment()    #C.count += 1
C.get()               #print(C.count)
C.reset()            #C.count = 0
C.get()
print(C.count)
#객체지향처럼 짜는 것이 더 나음
```

- **생성자(constructor):** 이름이 `__init__`인 메서드는 객체가 만들어질 때 자동으로 호출된다(주석의 "자동호출"). `C = Counter()`를 실행하는 순간 `count`가 0으로 초기화되므로, 객체를 만든 직후부터 언제나 `count`가 있다.
- **이 `get()`:** 2.1절과 달리 값을 반환하지 않고 출력한다. 그래서 `C.get()`만 호출해도 값이 화면에 나온다.
- **메서드 호출과 직접 접근:** 오른쪽 주석은 각 메서드 호출이 인스턴스 변수를 직접 다루는 문장 `C.count += 1` 등과 같은 일을 한다는 대응이다. 마지막 `print(C.count)`는 메서드를 거치지 않고 인스턴스 변수를 직접 읽는다. 끝의 주석은 객체 밖에서 변수를 직접 다루기보다 메서드로 다루는 객체 지향 방식이 낫다는 뜻이다.

**실행 결과:** 생성 직후 0, 두 번 증가한 뒤 2, `reset()` 뒤 0을 `get()`이 출력하고, 마지막 줄이 직접 읽은 0을 출력한다.

```text
0
2
0
0
```

---

<br>

## 3. 접근자, 설정자, 정보 은닉

### 3.1 get()과 set()

**코드:** [Lab_CounterAccessors.py](Lab_CounterAccessors.py)

```python
class Counter:
    def __init__(self):
        self.count = 0
    def reset(self):
        self.count = 0
    def increment(self):
        self.count += 1
    def get(self):
        return self.count
    def set(self, a):
        self.count = a

## main ##
C = Counter() # 객체 생성

print(C.count)
C_count = C.get() # C_count는 main에서 선언된 별개의 변수이다
print(C_count)
C.count = 100
print(C.count)
C.set(10)
C_count = C.get()
print(C_count)
```

- **접근자와 설정자:** 인스턴스 변수의 값을 돌려주는 메서드 `get()`을 **접근자(getter)**, 값을 바꾸는 메서드 `set()`을 **설정자(setter)** 라고 한다. 객체 밖의 코드가 변수를 직접 건드리지 않고 메서드를 거치게 하면, 설정자 안에서 음수를 거부하는 것처럼 값의 검사를 한곳에 모을 수 있다.
- **반환값을 담은 변수:** `C_count = C.get()`은 그 순간의 값 0을 메인 부분의 변수 `C_count`에 복사한다. `C_count`는 객체와 별개의 변수이므로, 그 뒤에 객체의 `count`가 바뀌어도 `C_count`는 다시 `get()`을 호출해야 바뀐다.
- **직접 대입:** `C.count = 100`처럼 객체 밖에서 인스턴스 변수에 바로 대입할 수도 있다. 이 클래스는 `count`를 감추지 않으므로 막을 방법이 없으며, 3.2절이 이를 다룬다.
- **설정자 사용:** `C.set(10)`이 `count`를 10으로 바꾸고, `get()`이 그 값을 돌려준다.

**실행 결과:**

```text
0
0
100
10
```

### 3.2 `__`로 시작하는 인스턴스 변수

**코드:** [Lab_CounterPrivate.py](Lab_CounterPrivate.py)

```python
class Counter:
    def __init__(self):
        self.__count = 0
    def reset(self):
        self.__count = 0
    def increment(self):
        self.__count += 1
    def get(self):
        return self.__count
    def set(self, a):
        self.__count = a

## main ##
C = Counter() # 객체 생성

try:
    print(C.__count)
except AttributeError as e:
    print("AttributeError:", e)
C_count = C.get() # C_count는 main에서 선언된 별개의 변수이다
print(C_count)
C.__count = 100
print(C.__count) #main에서 class로 접근 vs. class에서 접근해서 main으로 값 전송
C.set(10)
C_count = C.get()
print(C_count)
```

- **정보 은닉(information hiding):** 객체의 내부 상태를 밖에서 직접 다루지 못하게 감추고 메서드로만 다루게 하는 원칙이다. 파이썬에서는 인스턴스 변수의 이름을 `__`(밑줄 두 개)로 시작하면 클래스 밖에서 그 이름으로 접근할 수 없게 된다.
- **이름 맹글링(name mangling):** 클래스 안에서 쓴 `self.__count`는 파이썬이 `self._Counter__count`로 이름을 바꾸어 저장한다. 그래서 클래스 밖의 `C.__count`는 그런 속성을 찾지 못해 `AttributeError`를 일으키고, `try-except`가 그 메시지를 출력한다. 클래스 안의 메서드 `get()`은 같은 변환을 거치므로 값 0을 정상으로 읽는다.
- **밖에서 대입한 `__count`:** 클래스 밖의 `C.__count = 100`은 이름 맹글링을 거치지 않으므로 감춰진 변수를 바꾸지 않고, 이름이 `__count`인 새 인스턴스 변수를 하나 더 만든다. 그래서 바로 뒤의 `print(C.__count)`는 100을 출력하지만, 이 시점에 `C.get()`은 여전히 0이다. `C.__dict__`를 출력하면 `{'_Counter__count': 0, '__count': 100}`처럼 두 변수가 따로 있다.
- **메서드를 통한 접근:** `C.set(10)`과 `C.get()`은 감춰진 `_Counter__count`를 다루므로 10이 출력된다. 주석은 메인 부분에서 직접 접근하는 방식과 클래스의 메서드가 값을 전해 주는 방식을 비교한 메모이다.

**실행 결과:**

```text
AttributeError: 'Counter' object has no attribute '__count'
0
100
10
```

> **참고:** 이름 맹글링은 실수로 인한 접근을 막는 장치일 뿐 완전한 보호는 아니며, `C._Counter__count`처럼 바뀐 이름을 쓰면 밖에서도 접근할 수 있다. 파이썬에는 밑줄 하나로 시작하는 이름(`_count`)을 내부용으로 보고 클래스 밖에서 쓰지 않는 관례도 있다.

---

<br>

## 4. 객체 사이의 상호 작용

### 4.1 공격과 회복

**코드:** [Lab_AttackAndHeal.py](Lab_AttackAndHeal.py)

```python
class person():
    def __init__(self):
        self.hp=100
        self.r=50
    def a(self, person): #공격
        person.hp-=10
    def heal(self, person): #힐 (인스턴스 변수 r과 이름이 겹치지 않게 함)
        self.hp+=person.r

## main ##
A=person()
B=person()
C=person()
A.a(B)
C.heal(B)
print("A:", A.hp, "B:", B.hp, "C:", C.hp)
```

- **상태:** 생성자가 객체마다 체력 `hp`를 100, 회복량 `r`을 50으로 정한다. 세 객체 `A`, `B`, `C`는 같은 클래스에서 만들었지만 인스턴스 변수를 따로 가진다.
- **공격:** `A.a(B)`에서 `self`는 `A`, 매개변수 `person`은 `B`이므로 `B.hp`가 10 줄어 90이 된다. 메서드가 자신이 아닌 다른 객체의 인스턴스 변수를 바꿀 수 있음을 보여 준다.
- **회복:** `C.heal(B)`는 `self.hp += person.r`이므로 호출한 `C`의 체력에 `B`의 회복량 50을 더하여 `C.hp`가 150이 된다. `B`를 회복시키려면 `person.hp += self.r`로 써야 하므로, 메서드 안에서 `self`와 매개변수 중 어느 쪽을 바꾸는지 구별해야 한다.
- **이름:** 클래스 이름 `person`과 매개변수 이름 `person`이 같아, 메서드 안에서는 `person`이 매개변수(넘겨받은 객체)를 가리킨다. 클래스 이름은 `Person`처럼 대문자로 시작하는 것이 관례이며, 그러면 둘이 구별된다.

**실행 결과:**

```text
A: 100 B: 90 C: 150
```

> **주의:** 메서드와 인스턴스 변수가 같은 이름을 가지면 안 된다. 회복 메서드의 이름을 `r`로 지으면, 생성자의 `self.r=50`이 객체에 정수 `r`을 만들고, 객체에서 이름을 찾을 때는 인스턴스 변수가 클래스의 메서드보다 먼저 찾아지므로 `C.r(B)`는 정수 50을 호출하려다 `TypeError: 'int' object is not callable`을 일으킨다.

---

<br>

## 요약

| 개념 | 핵심 요약 |
|:-----|:-----|
| 클래스와 객체 | 클래스는 객체의 설계도이고, 클래스를 호출하면 인스턴스 변수를 따로 가진 객체가 만들어진다. |
| `self` | 메서드의 첫 매개변수로, 메서드를 호출한 객체 자신을 가리킨다. |
| 인스턴스 변수 | `self.이름`에 대입하면 그 객체에 속한 변수가 만들어지며, 대입하기 전에 읽으면 `AttributeError`가 발생한다. |
| 생성자 | `__init__()`은 객체를 만들 때 자동으로 호출되어 인스턴스 변수를 초기화한다. |
| 접근자와 설정자 | `get()`처럼 값을 돌려주는 메서드와 `set()`처럼 값을 바꾸는 메서드로 인스턴스 변수를 다룬다. |
| 정보 은닉 | `__`로 시작하는 인스턴스 변수는 `_클래스이름__이름`으로 바뀌어 클래스 밖에서 원래 이름으로 접근할 수 없다. |
| 이름의 충돌 | 객체에서 이름을 찾을 때 인스턴스 변수가 메서드보다 먼저 찾아지므로 둘의 이름을 다르게 짓는다. |

---

<br>

## 점검 문제

1. **객체마다의 인스턴스 변수:** `Lab_Counter.py`의 클래스로 `a = Counter()`, `b = Counter()`를 만들고 둘 다 `reset()`한 뒤 `a.increment()`를 두 번, `b.increment()`를 한 번 호출하면 `a.get()`과 `b.get()`은 각각 얼마인가?

   <details>
   <summary>정답</summary>

   `a.get()`은 2, `b.get()`은 1이다. `count`는 객체마다 따로 있는 인스턴스 변수이므로 한 객체의 메서드 호출은 다른 객체의 값에 영향을 주지 않는다.

   </details>

2. **생성자의 역할:** `Lab_Counter.py`에서 `a.reset()` 줄을 지우면 어떻게 되는가? `Lab_CounterConstructor.py`의 클래스로 같은 일을 하면 어떻게 되는가?

   <details>
   <summary>정답</summary>

   `Lab_Counter.py`의 클래스에는 생성자가 없으므로 `count`가 만들어지지 않은 채 `increment()`가 `self.count`를 읽어 `AttributeError`가 발생한다. `Lab_CounterConstructor.py`의 클래스는 생성자가 객체를 만들 때 `count`를 0으로 초기화하므로 `reset()` 없이도 `increment()`가 정상으로 동작한다.

   </details>

3. **반환값과 출력:** `Lab_CounterConstructor.py`의 `get()`은 값을 출력하고 반환하지 않는다. 이 클래스에서 `x = C.get()`을 실행하면 `x`에는 무엇이 저장되는가?

   <details>
   <summary>정답</summary>

   `get()`에는 `return`문이 없으므로 `None`이 저장된다. 값을 다른 계산에 쓰려면 `Lab_CounterAccessors.py`처럼 `return self.count`로 반환해야 한다.

   </details>

4. **이름 맹글링:** `Lab_CounterPrivate.py`의 객체 `C`에서 `C._Counter__count = 5`를 실행한 뒤 `C.get()`을 호출하면 무엇이 반환되는가?

   <details>
   <summary>정답</summary>

   5가 반환된다. 클래스 안의 `self.__count`는 `self._Counter__count`로 바뀌어 저장되므로, 바뀐 이름으로 대입하면 감춰진 변수의 값이 바뀐다. 이름 맹글링은 실수로 인한 접근을 막을 뿐 완전한 보호가 아니다.

   </details>

5. **self와 매개변수:** `Lab_AttackAndHeal.py`에서 `C.heal(B)`가 `B`의 체력을 `C`의 회복량만큼 늘리도록 `heal` 메서드의 본체를 고쳐 쓰고, 그때의 출력을 쓰라.

   <details>
   <summary>정답</summary>

   본체를 `person.hp += self.r`로 쓴다. 그러면 `B.hp`는 공격으로 90이 된 뒤 50이 더해져 140이 되고 `C.hp`는 100 그대로이므로 `A: 100 B: 140 C: 100`이 출력된다.

   </details>
