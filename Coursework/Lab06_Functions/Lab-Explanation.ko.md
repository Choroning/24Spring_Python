# 실습 6 해설 — 함수

[레포지토리 안내](../../README.ko.md) | [English](Lab-Explanation.md) | [한국어](Lab-Explanation.ko.md)

> **최종 수정일:** 2026-11-04

> **학습 목표:**
> 1. 함수를 정의하고 호출하여 반환값을 변수에 저장하거나 출력할 수 있다
> 2. `return`이 없는 함수와 여러 값을 반환하는 함수의 동작을 설명할 수 있다
> 3. 지역 변수와 전역 변수를 구별하고 `global` 선언이 필요한 경우를 판단할 수 있다
> 4. 디폴트 인수, 키워드 인수, 무명 함수(`lambda`)를 사용할 수 있다
> 5. 직접 만든 모듈을 `import`하여 그 안의 함수를 호출할 수 있다

---

## 목차

- [1. 실습 구성과 실행 방법](#1-실습-구성과-실행-방법)
- [2. 함수의 정의와 반환값](#2-함수의-정의와-반환값)
  - [2.1 이차식을 계산하는 함수](#21-이차식을-계산하는-함수)
  - [2.2 반환하지 않는 함수](#22-반환하지-않는-함수)
  - [2.3 여러 값의 반환](#23-여러-값의-반환)
  - [2.4 타입 힌트와 튜플 반환](#24-타입-힌트와-튜플-반환)
  - [2.5 함수를 호출하는 함수](#25-함수를-호출하는-함수)
  - [2.6 main() 함수](#26-main-함수)
- [3. 지역 변수와 전역 변수](#3-지역-변수와-전역-변수)
  - [3.1 반환값으로 결과 전달하기](#31-반환값으로-결과-전달하기)
  - [3.2 global 선언](#32-global-선언)
  - [3.3 전역 상수](#33-전역-상수)
  - [3.4 여러 전역 변수의 갱신](#34-여러-전역-변수의-갱신)
- [4. 인수 전달 방식과 무명 함수](#4-인수-전달-방식과-무명-함수)
  - [4.1 디폴트 인수](#41-디폴트-인수)
  - [4.2 키워드 인수](#42-키워드-인수)
  - [4.3 lambda로 만든 무명 함수](#43-lambda로-만든-무명-함수)
- [5. 모듈](#5-모듈)
  - [5.1 모듈의 import](#51-모듈의-import)
  - [5.2 import as로 붙인 별칭](#52-import-as로-붙인-별칭)
- [요약](#요약)
- [점검 문제](#점검-문제)

---

<br>

## 1. 실습 구성과 실행 방법

[6강 함수](../../Lecture-Notes/Lec06_Functions/Concepts_Lecture.ko.md)를 따라 작성한 코드이다. 2절은 함수의 정의, 호출, 반환값을, 3절은 지역 변수와 전역 변수를, 4절은 디폴트 인수, 키워드 인수, `lambda`를, 5절은 모듈을 다룬다.

```text
Coursework/Lab06_Functions/
├── Lab-Explanation.ko.md          # 이 문서 (한국어)
├── Lab-Explanation.md             # 이 문서 (영어)
├── Lab_QuadraticFunction.py       # 2.1 이차식을 계산하는 함수
├── Lab_FunctionWithoutReturn.py   # 2.2 반환하지 않는 함수
├── Lab_MultipleReturnValues.py    # 2.3 여러 값의 반환
├── Lab_AddWithAnnotations.py      # 2.4 타입 힌트와 튜플 반환
├── Lab_AbsoluteValue.py           # 2.5 함수를 호출하는 함수
├── Lab_MainFunction.py            # 2.6 main() 함수
├── Lab_CircleAreaReturn.py        # 3.1 반환값으로 결과 전달하기
├── Lab_CircleAreaGlobal.py        # 3.2 global 선언
├── Lab_GlobalConstant.py          # 3.3 전역 상수
├── Lab_SumAndAverageGlobal.py     # 3.4 여러 전역 변수의 갱신
├── Lab_DefaultArgument.py         # 4.1 디폴트 인수
├── Lab_KeywordArguments.py        # 4.2 키워드 인수
├── Lab_Lambda.py                  # 4.3 lambda로 만든 무명 함수
├── Lab_ModuleImport.py            # 5.1 모듈의 import
├── Lab_AddMinusModule.py          # 5.1에서 가져다 쓰는 모듈
├── Lab_ModuleAlias.py             # 5.2 import as로 붙인 별칭
└── Lab_ArithmeticModule.py        # 5.2에서 가져다 쓰는 모듈
```

*그림 1. 실습 6의 디렉토리 구성*

모든 프로그램은 표준 라이브러리만 쓰므로 파이썬 3에서 그대로 실행된다. `Lab_AddMinusModule.py`와 `Lab_ArithmeticModule.py`는 단독으로 실행하는 프로그램이 아니라 `Lab_ModuleImport.py`와 `Lab_ModuleAlias.py`가 가져다 쓰는 모듈이므로, 네 파일을 같은 폴더에 두고 실행해야 한다. 각 파일의 맨 위에는 파일 이름, 한 줄 설명, 작성자, 작성일을 적은 문서화 문자열(docstring)이 있으며, 이 문서의 코드 블록에서는 그 부분을 생략한다.

```bash
cd Coursework/Lab06_Functions
python3 Lab_ModuleImport.py
```

---

<br>

## 2. 함수의 정의와 반환값

### 2.1 이차식을 계산하는 함수

**코드:** [Lab_QuadraticFunction.py](Lab_QuadraticFunction.py)

```python
#f(x)=a*x**2+b*x+c를 함수로 정의하기

def f(x):
    y=1*x**2+2*x+3
    return y #리턴 안하면 그냥 사라짐

##main##
x=10
y=1*x**2+2*x+3 #함수 속의 y와 메인문의 y는 다름(지역변수이므로)
f(x) #정의한 함수 이름을 적어주면 그냥 메인문에서 호출한 것이 됨
z=f(x)

#x를 따로 10이라고 정의하지 않고 그냥 f(10)으로 해도 됨

print(y)
print(1*x**2+2*x+3)
print(f(x))
print(z)
```

- **함수 정의:** `def 함수이름(매개변수):` 아래에 들여 쓴 블록이 함수의 본체이다. 정의만으로는 실행되지 않고, 호출될 때마다 본체가 실행된다. `f`는 수학의 이차식 $f(x) = x^2 + 2x + 3$을 계산한다.
- **`return`:** 계산한 `y`를 호출한 곳으로 돌려준다. 함수 안의 변수는 함수가 끝나면 사라지므로, 결과를 밖에서 쓰려면 반환해야 한다는 것이 주석의 뜻이다.
- **지역 변수:** 함수 안의 `y`와 메인 부분의 `y`는 이름만 같은 서로 다른 변수이다. 함수 안에서 대입한 변수는 그 함수의 **지역 변수(local variable)** 로, 함수 밖에 영향을 주지 않는다.
- **호출과 반환값:** `f(x)`만 쓴 줄은 함수를 호출하지만 반환값을 어디에도 저장하지 않으므로 결과가 버려진다. `z=f(x)`는 반환값 123을 `z`에 저장한다. 주석처럼 인수 자리에 `f(10)`으로 값을 직접 써도 된다.
- **결과:** $10^2 + 2 \times 10 + 3 = 123$이므로 네 줄 모두 123이다.

**실행 결과:**

```text
123
123
123
123
```

### 2.2 반환하지 않는 함수

**코드:** [Lab_FunctionWithoutReturn.py](Lab_FunctionWithoutReturn.py)

```python
def f(x):
    y=1*x**2+2*x+3
    print(y)
    #return y

##main##
x=10

f(x) #그냥 이렇게 쓰면 print됨(리턴 여부와 관계 없음)
```

- **함수 안의 출력:** 이 `f`는 결과를 반환하지 않고 함수 안에서 출력한다. 그래서 `f(x)`만 호출해도 123이 화면에 나타난다.
- **반환값 `None`:** `return`문이 없는 함수도 끝나면 값을 돌려주는데, 그 값은 값이 없음을 뜻하는 `None`이다. 예를 들어 `z = f(x)`라고 쓰면 123이 출력된 뒤 `z`에는 `None`이 저장된다.
- **출력과 반환의 차이:** 출력은 화면에 보여 줄 뿐 프로그램이 그 값을 다시 쓸 수 없고, 반환값은 변수에 저장하거나 다른 계산에 넣을 수 있다.

**실행 결과:**

```text
123
```

### 2.3 여러 값의 반환

**코드:** [Lab_MultipleReturnValues.py](Lab_MultipleReturnValues.py)

```python
def f(x):
    y=1*x**2+2*x+3
    return y,x #C언어는 리턴값 2개 이상이 불가능

## main ##
y, x = f(10)
print(y, x)
```

- **튜플 반환:** `return y,x`는 두 값을 묶은 **튜플(tuple)** `(y, x)` 하나를 반환한다. C 언어의 함수는 값을 하나만 반환하지만, 파이썬은 튜플로 묶어 여러 값을 한 번에 돌려줄 수 있다.
- **언패킹:** `y, x = f(10)`은 반환된 튜플 `(123, 10)`의 요소를 차례로 `y`와 `x`에 나누어 대입한다. 왼쪽 변수의 개수와 튜플 요소의 개수가 같아야 하며, 다르면 `ValueError`가 발생한다.

**실행 결과:**

```text
123 10
```

### 2.4 타입 힌트와 튜플 반환

**코드:** [Lab_AddWithAnnotations.py](Lab_AddWithAnnotations.py)

```python
'''x=int(input("x:"))
y=int(input("y:"))
z=x+y
print(z)'''

def add(x : int,y : int) -> (int, int) :

# def add(x,y): 도 가능
# def add(x : int,y : int) -> int : 도 가능

    #x=int(input("x:"))
    #y=int(input("y:"))
    z=x+y
    #print(z)
    return z,x

## main ##
x=int(input("x:"))
y=int(input("y:"))
z,x=add(x,y)
# z=add(x,y)로 받으면 z에 튜플 (합, x)가 저장된다(합만 받으려면 return z로 쓴다)
print(z)
print(x)
```

- **여러 줄 문자열:** 맨 위의 `'''...'''`는 어디에도 대입하지 않은 문자열이므로 실행에 영향을 주지 않는다. 함수로 바꾸기 전의 코드를 남겨 두는 주석처럼 쓰였다.
- **타입 힌트:** `x : int`는 매개변수 `x`에 정수를 기대한다는 표시이고, `-> (int, int)`는 반환값의 형태를 적은 표시이다. 이런 **타입 힌트(type hint)** 는 읽는 사람과 도구를 위한 정보일 뿐, 파이썬은 실행할 때 형을 검사하지 않는다. 주석처럼 힌트 없이 `def add(x,y):`로 써도 동작은 같다. 두 정수의 튜플을 나타내는 표준 표기는 `tuple[int, int]`이며, `(int, int)`는 실행에는 문제가 없지만 mypy 같은 타입 검사 도구는 올바른 타입 표기로 인정하지 않는다. 둘째 주석의 `-> int`도 실행은 되지만, 이 함수는 튜플을 반환하므로 실제 반환값과 맞지 않는 힌트가 된다.
- **반환과 언패킹:** `add`는 합 `z`와 첫 인수 `x`를 튜플로 반환하고, 메인 부분은 `z,x=add(x,y)`로 두 값을 나누어 받는다. `x`에는 원래 값이 다시 대입되므로 바뀌지 않는다.

**실행 결과:** 3과 4를 입력한 경우이다. 프롬프트 `x:`와 `y:` 뒤에 공백이 없으므로 입력값이 바로 붙는다.

```text
x:3
y:4
7
3
```

### 2.5 함수를 호출하는 함수

**코드:** [Lab_AbsoluteValue.py](Lab_AbsoluteValue.py)

```python
'''x = int(input("x:"))

if (x < 0):
    x = -x

print(x)'''


def abs(x): # 절댓값 함수
    if (x < 0):
        x = -x
    return x

def abs2(): # 값을 입력받아 abs(x)를 돌려서 출력하는 함수
    x = int(input("x:"))
    print(abs(x))

## main ##
abs2()
```

- **절댓값 함수:** `abs(x)`는 `x`가 음수이면 부호를 바꾸고, 그렇지 않으면 그대로 반환한다. 매개변수 `x`에 새 값을 대입해도 함수 안의 지역 변수가 바뀔 뿐 호출한 쪽의 변수는 바뀌지 않는다.
- **함수 안의 함수 호출:** `abs2()`는 매개변수 없이 입력을 받아 `abs(x)`를 호출하고 결과를 출력한다. 한 함수가 다른 함수를 호출하여 일을 나누는 구조이다.
- **호출 순서:** `abs2`가 `abs`를 호출하는 것은 `abs2()`가 실행될 때이고, 그때는 두 함수가 모두 정의되어 있다. 따라서 정의 순서는 호출 시점보다 앞서기만 하면 된다.

**실행 결과:** -7을 입력한 경우이다.

```text
x:-7
7
```

> **주의:** `abs`는 파이썬의 내장 함수 이름이다. 같은 이름으로 함수를 정의하면 그 프로그램 안에서는 내장 함수 `abs()`가 가려진다. 이 프로그램은 같은 일을 하므로 결과가 같지만, 내장 함수와 겹치지 않는 이름(예: `my_abs`)을 쓰는 것이 안전하다.

### 2.6 main() 함수

**코드:** [Lab_MainFunction.py](Lab_MainFunction.py)

```python
## main ##
'''
a=int(input('a:'))
b=a**2
print(b)
'''
def s(x): #함수를 꼭 활용하기 전 작성
    y=x**2
    return y

## main ##
def main():
    a=int(input('a:'))
    b=s(a)
    print(b)
    print(s(a))

main()
```

- **함수의 정의 위치:** 주석의 말처럼 함수는 호출되기 전에 정의되어 있어야 한다. `def`가 실행되어야 함수 이름이 만들어지기 때문이다.
- **`main()` 함수:** 프로그램의 실행 부분을 `main()`이라는 함수로 묶고 파일 끝에서 한 번 호출하는 관례이다. 실행 부분의 변수 `a`, `b`가 `main()`의 지역 변수가 되어 전역 이름과 섞이지 않는다. `main()` 호출을 빠뜨리면 함수를 정의만 하고 끝나므로 아무것도 출력되지 않는다.
- **두 출력:** `b`에 저장한 반환값과 `s(a)`를 다시 호출한 반환값을 출력하므로 같은 수가 두 번 나온다.

**실행 결과:** 6을 입력한 경우이다.

```text
a:6
36
36
```

---

<br>

## 3. 지역 변수와 전역 변수

### 3.1 반환값으로 결과 전달하기

**코드:** [Lab_CircleAreaReturn.py](Lab_CircleAreaReturn.py)

```python
def calculate_area(radius):
    area=3.14*radius**2
    return area

area=0
r=float(input("원의 반지름: "))
area=calculate_area(r)
print(area)
```

- **두 개의 `area`:** 함수 안의 `area`는 지역 변수이고, 메인 부분의 `area`는 함수 밖에서 만든 **전역 변수(global variable)** 이다. 이름은 같지만 서로 다른 변수이다.
- **결과 전달:** 함수는 지역 변수의 값을 `return`으로 돌려주고, 메인 부분이 그 값을 전역 변수 `area`에 대입한다. 함수가 바깥 변수를 직접 바꾸지 않으므로 흐름을 추적하기 쉽다.
- **계산:** 원의 넓이는 $\pi r^2$이며, 여기서는 $\pi$를 3.14로 근사한다. 반지름 5이면 $3.14 \times 25 = 78.5$이다.

**실행 결과:** 반지름 5를 입력한 경우이다.

```text
원의 반지름: 5
78.5
```

### 3.2 global 선언

**코드:** [Lab_CircleAreaGlobal.py](Lab_CircleAreaGlobal.py)

```python
def calculate_area(radius):
    global area
    area = 3.14*radius**2
    return

area=0
r=float(input("원의 반지름: "))
calculate_area(r)
print(area)
```

- **`global` 선언:** 함수 안에서 변수에 대입하면 기본적으로 지역 변수가 만들어진다. `global area`를 먼저 쓰면 함수 안의 `area`가 전역 변수 `area`를 가리키므로, 대입이 전역 변수의 값을 바꾼다.
- **반환값 없음:** 값 없이 쓴 `return`은 함수를 끝내고 `None`을 돌려준다. 결과는 반환값이 아니라 전역 변수로 전달되므로 메인 부분은 호출 뒤 `area`를 출력한다.
- **3.1절과의 비교:** 결과는 같지만, 여러 함수가 전역 변수를 바꾸면 어느 함수가 언제 값을 바꾸었는지 추적하기 어려우므로 3.1절처럼 반환값으로 전달하는 방식이 일반적으로 권장된다.

**실행 결과:** 반지름 5를 입력한 경우이다.

```text
원의 반지름: 5
78.5
```

### 3.3 전역 상수

**코드:** [Lab_GlobalConstant.py](Lab_GlobalConstant.py)

```python
PI=3.14159265358979 #전역상수

def area_c(r):
    return PI*r**2

def main():
    r=float(input("r:"))
    print(area_c(r))

main()
```

- **전역 상수:** 프로그램 전체에서 바뀌지 않는 값은 함수 밖에 한 번 정의하고 이름을 대문자로 쓰는 관례가 있다. 파이썬에는 값을 바꾸지 못하게 막는 상수 문법이 없으므로, 대문자 이름은 그 값을 바꾸지 않는다는 프로그래머 사이의 약속이다.
- **읽기에는 `global`이 필요 없다:** `area_c`는 `PI`를 읽기만 하므로 `global` 선언 없이 전역 변수의 값을 쓸 수 있다. 함수 안에서 대입하지 않은 이름은 함수 밖(전역)에서 찾는다.
- **정밀도:** 3.14 대신 소수 14자리까지의 값을 쓰므로 3.1절의 78.5보다 정확한 값이 나온다.

**실행 결과:** 반지름 5를 입력한 경우이다.

```text
r:5
78.53981633974475
```

### 3.4 여러 전역 변수의 갱신

**코드:** [Lab_SumAndAverageGlobal.py](Lab_SumAndAverageGlobal.py)

```python
def sumandavg(a, b):
    global sum, avg
    sum=a+b
    avg=(a+b)/2

sum=0 #주석처리해도 작동
avg=0 #주석처리해도 작동
a=50
b=60

sumandavg(a, b)
print("합=", sum)
print("평균=", avg)
```

- **여러 이름의 `global` 선언:** `global sum, avg`처럼 쉼표로 여러 이름을 한 번에 선언할 수 있다. 함수가 두 전역 변수에 합과 평균을 저장한다.
- **초기화가 없어도 되는 이유:** 주석의 말처럼 `sum=0`과 `avg=0`을 지워도 동작한다. `global`로 선언한 이름에 함수 안에서 대입하면 전역 변수가 그때 새로 만들어지고, `print()`는 함수 호출 뒤에 실행되기 때문이다.
- **계산:** $50 + 60 = 110$, $110 / 2 = 55.0$이다. `/`는 항상 실수를 돌려주므로 평균은 `55.0`으로 출력된다.

**실행 결과:**

```text
합= 110
평균= 55.0
```

> **주의:** `sum`은 내장 함수 이름이다. 이 프로그램은 전역 변수 `sum`에 정수를 대입하므로, 그 뒤로는 `sum([1, 2, 3])`처럼 내장 함수를 호출하면 `TypeError`가 발생한다. 변수 이름은 내장 함수와 겹치지 않게 짓는다(예: `total`).

---

<br>

## 4. 인수 전달 방식과 무명 함수

### 4.1 디폴트 인수

**코드:** [Lab_DefaultArgument.py](Lab_DefaultArgument.py)

```python
def greet(name, msg="별일없죠?"):
    print("안녕 ", name+', '+msg)

greet("영희")

#msg=" ~ "를 통해 디폴트 인수로 설정
#따로 매개변수에 대한 인자를 주지 않아도
#기본값을 출력함
```

- **디폴트 인수:** 매개변수 뒤에 `=값`을 쓰면 호출할 때 그 인수를 생략할 수 있고, 생략하면 그 값이 쓰인다. 이를 **디폴트 인수(default argument)** 라고 한다. `greet("영희")`에서는 `msg`가 생략되었으므로 `"별일없죠?"`가 쓰인다.
- **매개변수의 순서:** 기본값이 있는 매개변수는 기본값이 없는 매개변수 뒤에 와야 한다. `def greet(msg="...", name):`은 문법 오류이다.
- **출력의 공백:** `"안녕 "` 끝의 공백과 `print()`가 값 사이에 넣는 공백이 겹쳐 `안녕` 뒤에 공백이 두 개 출력된다.

**실행 결과:** `msg`에 기본값이 쓰인 출력이다.

```text
안녕  영희, 별일없죠?
```

`greet("철수", "반가워요")`처럼 두 번째 인수를 주면 기본값 대신 `반가워요`가 출력된다.

### 4.2 키워드 인수

**코드:** [Lab_KeywordArguments.py](Lab_KeywordArguments.py)

```python
def calc(x, y, z):
    print(x)
    print(y)
    print(z)

#입력창에 calc(y=20, x=10, z=30)
#calc(20, 10, 30)과 결과 비교

#키워드 인수는 인수의 이름을
#명시적으로 지정해서 전달하는 방법

## main ##
calc(y=20, x=10, z=30)
calc(20, 10, 30)
```

- **위치 인수:** `calc(20, 10, 30)`처럼 값만 쓰면 순서대로 `x`, `y`, `z`에 대입된다. 이를 **위치 인수(positional argument)** 라고 한다.
- **키워드 인수:** `calc(y=20, x=10, z=30)`처럼 `매개변수이름=값`으로 쓰면 순서와 관계없이 이름이 같은 매개변수에 대입된다. 이를 **키워드 인수(keyword argument)** 라고 하며, 인수가 많을 때 어떤 값이 어디로 가는지 분명해진다.
- **비교:** 첫 호출은 `x=10, y=20, z=30`, 둘째 호출은 `x=20, y=10, z=30`이 되어 출력 순서가 다르다. 주석의 "입력창"은 IDLE의 셸 창에서 직접 호출해 보라는 뜻이다.

**실행 결과:** 앞의 세 줄이 첫 호출, 뒤의 세 줄이 둘째 호출의 출력이다.

```text
10
20
30
20
10
30
```

> **참고:** 위치 인수와 키워드 인수를 섞어 쓸 때는 위치 인수가 앞에 와야 한다. `calc(10, z=30, y=20)`은 올바르지만 `calc(x=10, 20, 30)`은 문법 오류이다.

### 4.3 lambda로 만든 무명 함수

**코드:** [Lab_Lambda.py](Lab_Lambda.py)

```python
sum = lambda x, y: x+y;

print("정수의 합: ", sum(10,20))
print("정수의 합: ", sum(20,20))

#def sum_(x,y):
#    return x+y
#위 함수의 무명함수 버전
```

- **`lambda`:** `lambda 매개변수: 식`은 식 하나의 값을 반환하는 이름 없는 함수, 곧 **무명 함수(anonymous function)** 를 만든다. 주석의 `def sum_(x,y): return x+y`와 같은 일을 한 줄로 쓴 것이다.
- **변수에 대입:** 만든 함수 객체를 변수 `sum`에 대입하면 `sum(10,20)`처럼 일반 함수와 같이 호출할 수 있다.
- **세미콜론:** 줄 끝의 `;`는 한 줄에 여러 문장을 쓸 때의 구분자이며, 문장이 하나뿐인 여기서는 없어도 된다.

**실행 결과:**

```text
정수의 합:  30
정수의 합:  40
```

> **주의:** 3.4절과 같이 변수 이름 `sum`이 내장 함수 `sum()`을 가린다. 또한 `lambda`는 식 하나만 담을 수 있으므로, 여러 문장이 필요한 함수는 `def`로 정의한다.

---

<br>

## 5. 모듈

### 5.1 모듈의 import

**코드:** [Lab_ModuleImport.py](Lab_ModuleImport.py), [Lab_AddMinusModule.py](Lab_AddMinusModule.py)

```python
import Lab_AddMinusModule

a=10
b=20
Lab_AddMinusModule.add(a,b)
Lab_AddMinusModule.minus(a,b)

#모듈명이 Lab_AddMinusModule로 너무 길 때는
#import Lab_AddMinusModule as t로 작성하면
#t.add(a,b)처럼 사용할 수 있음

#또는 from Lab_AddMinusModule import *로
#작성하면 모듈명 빼고 그냥
#add(a,b) 사용 가능하지만 이름이 겹칠 수 있으므로 가능하면 쓰지 않음
```

```python
##module##

def add(a,b):
    print(a+b)

def minus(a,b):
    print(a-b)
```

- **모듈:** 함수와 변수를 담은 `.py` 파일 하나가 **모듈(module)** 이다. 두 번째 파일 `Lab_AddMinusModule.py`는 두 수의 합과 차를 출력하는 함수 두 개를 담은 모듈이다.
- **`import`:** `import Lab_AddMinusModule`은 같은 폴더(또는 파이썬이 모듈을 찾는 경로)에서 `Lab_AddMinusModule.py`를 찾아 실행하고, 그 안의 이름을 `모듈이름.함수이름` 형태로 쓸 수 있게 한다. 모듈 이름은 파일 이름에서 `.py`를 뺀 것이며, 식별자여야 하므로 하이픈이 들어가면 `import`할 수 없다.
- **두 가지 다른 방법:** 주석은 `import ... as t`로 짧은 별칭을 붙이는 방법(5.2절)과 `from ... import *`로 모듈 이름 없이 쓰는 방법을 설명한다. 뒤의 방법은 모듈의 모든 이름을 현재 파일로 가져오므로 같은 이름이 있으면 한쪽이 가려져 오류를 찾기 어렵다.

**실행 결과:** $10 + 20 = 30$, $10 - 20 = -10$이다.

```text
30
-10
```

> **참고:** 처음 `import`할 때 파이썬은 모듈을 컴파일한 결과를 같은 폴더의 `__pycache__`에 저장하여 다음 실행을 빠르게 한다. 이 폴더는 실행할 때 다시 만들어지므로 레포지토리에 두지 않는다.

### 5.2 import as로 붙인 별칭

**코드:** [Lab_ModuleAlias.py](Lab_ModuleAlias.py), [Lab_ArithmeticModule.py](Lab_ArithmeticModule.py)

```python
import Lab_ArithmeticModule as t8

a=10
b=20
c=30

print(t8.add(a, t8.mul(b,c)))
```

```python
##module##

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b
```

- **별칭:** `import 모듈 as 별칭`은 모듈을 짧은 이름 `t8`로 부를 수 있게 한다. `t8.add`는 `Lab_ArithmeticModule.add`와 같은 함수이다.
- **반환하는 모듈 함수:** 5.1절의 모듈 함수는 결과를 출력만 하지만, 이 모듈의 함수는 결과를 반환하므로 다른 함수의 인수로 넣어 조합할 수 있다.
- **계산 순서:** 안쪽 호출 `t8.mul(b,c)`가 먼저 계산되어 $20 \times 30 = 600$이 되고, 그 값이 `t8.add(a, 600)`의 인수로 들어가 $10 + 600 = 610$이 출력된다.

**실행 결과:**

```text
610
```

---

<br>

## 요약

| 개념 | 핵심 요약 |
|:-----|:-----|
| 함수 정의와 호출 | `def`로 정의한 본체는 호출될 때마다 실행되며, 함수는 호출하기 전에 정의되어 있어야 한다. |
| 반환값 | `return`은 값을 호출한 곳으로 돌려주고, `return`이 없거나 값 없이 쓰면 `None`을 돌려준다. |
| 여러 값의 반환 | `return a, b`는 튜플 하나를 반환하며, `x, y = f()`로 요소를 나누어 받는다. |
| 타입 힌트 | `x: int`, `-> int`는 기대하는 형을 적은 표시일 뿐 실행 중에 검사되지 않는다. |
| 지역 변수와 전역 변수 | 함수 안에서 대입한 이름은 지역 변수이고, 전역 변수를 바꾸려면 `global` 선언이 필요하며, 읽기만 할 때는 필요 없다. |
| 디폴트 인수와 키워드 인수 | 기본값이 있는 매개변수는 생략할 수 있고, `이름=값`으로 전달하면 순서와 관계없이 대입된다. |
| `lambda` | 식 하나의 값을 반환하는 무명 함수를 한 줄로 만든다. |
| 모듈 | `.py` 파일 하나가 모듈이며, `import`, `import as`, `from ... import`로 그 안의 이름을 가져온다. |

---

<br>

## 점검 문제

1. **반환값이 없는 함수:** `Lab_FunctionWithoutReturn.py`의 마지막 줄을 `z = f(x)`와 `print(z)` 두 줄로 바꾸면 무엇이 출력되는가?

   <details>
   <summary>정답</summary>

   `f(x)`가 실행되며 함수 안의 `print(y)`가 `123`을 출력하고, `f`에는 `return`이 없으므로 `z`에는 `None`이 저장되어 `None`이 출력된다. 출력은 `123`과 `None` 두 줄이다.

   </details>

2. **언패킹:** `def g(): return 1, 2, 3`일 때 `a, b = g()`를 실행하면 어떻게 되는가?

   <details>
   <summary>정답</summary>

   `g()`는 요소가 3개인 튜플 `(1, 2, 3)`을 반환하는데 왼쪽 변수는 2개이므로 `ValueError`(too many values to unpack)가 발생한다. `a, b, c = g()`처럼 변수의 개수를 맞추어야 한다.

   </details>

3. **global이 필요한 경우:** 다음 두 함수 중 `global count` 선언 없이 실행하면 오류가 나는 것은 어느 쪽이며, 그 이유는 무엇인가?

   ```python
   count = 0
   def show():
       print(count)
   def add_one():
       count = count + 1
   ```

   <details>
   <summary>정답</summary>

   `add_one`이다. 함수 안에서 `count`에 대입하므로 `count`는 그 함수 전체에서 지역 변수가 되고, 오른쪽의 `count`를 읽는 시점에는 아직 값이 없어 `UnboundLocalError`가 발생한다. `show`는 읽기만 하므로 전역 변수의 값 0을 출력한다.

   </details>

4. **키워드 인수:** `calc(z=1, x=2, y=3)`의 출력을 쓰라.

   <details>
   <summary>정답</summary>

   이름에 따라 `x=2, y=3, z=1`이 되므로 `x`, `y`, `z`의 순서로 2, 3, 1이 한 줄에 하나씩 출력된다.

   </details>

5. **모듈 함수의 조합:** `Lab_ModuleAlias.py`에서 `print(t8.sub(t8.div(c, a), b))`를 실행하면 무엇이 출력되는가?

   <details>
   <summary>정답</summary>

   `t8.div(30, 10)`은 `/` 연산이므로 실수 3.0이고, `t8.sub(3.0, 20)`은 -17.0이다. 따라서 `-17.0`이 출력된다.

   </details>
