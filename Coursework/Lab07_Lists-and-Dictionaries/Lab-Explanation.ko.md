# 실습 7 해설 — 리스트와 딕셔너리

[레포지토리 안내](../../README.ko.md) | [English](Lab-Explanation.md) | [한국어](Lab-Explanation.ko.md)

> **최종 수정일:** 2026-11-04

> **학습 목표:**
> 1. 리스트의 요소를 인덱스로 읽고 바꾸며, `append()`, `insert()`, `remove()`, `del`, `pop()`, `index()`를 사용할 수 있다
> 2. 함수에 전달한 리스트가 함수 안에서 바뀌면 호출한 쪽에도 반영되는 이유를 참조로 설명할 수 있다
> 3. 버블 정렬과 리스트 컴프리헨션으로 리스트를 정렬하고 만들 수 있다
> 4. 2차원 리스트를 만들어 채우고, 대입과 복사의 차이를 구별할 수 있다
> 5. 딕셔너리의 키로 값을 조회, 변경, 추가, 삭제하고 주요 메서드를 사용할 수 있다
> 6. 전역 변수와 전역 리스트를 함수 안에서 다룰 때 `global` 선언이 필요한 경우를 판단할 수 있다

---

## 목차

- [1. 실습 구성과 실행 방법](#1-실습-구성과-실행-방법)
- [2. 리스트의 생성과 기본 연산](#2-리스트의-생성과-기본-연산)
  - [2.1 리스트의 자료형](#21-리스트의-자료형)
  - [2.2 요소의 변경, 추가, 삭제와 탐색](#22-요소의-변경-추가-삭제와-탐색)
  - [2.3 인덱스 찾기의 세 방법](#23-인덱스-찾기의-세-방법)
  - [2.4 가장 작은 값의 인덱스](#24-가장-작은-값의-인덱스)
- [3. 함수와 리스트](#3-함수와-리스트)
  - [3.1 함수 안에서 바꾼 리스트](#31-함수-안에서-바꾼-리스트)
  - [3.2 요소를 바꾸는 두 방법](#32-요소를-바꾸는-두-방법)
  - [3.3 함수로 나눈 평균 계산](#33-함수로-나눈-평균-계산)
- [4. 정렬과 리스트 컴프리헨션](#4-정렬과-리스트-컴프리헨션)
  - [4.1 버블 정렬](#41-버블-정렬)
  - [4.2 리스트 컴프리헨션](#42-리스트-컴프리헨션)
- [5. 전역 변수와 전역 리스트](#5-전역-변수와-전역-리스트)
  - [5.1 global 선언 없이 전역 변수에 대입하기](#51-global-선언-없이-전역-변수에-대입하기)
  - [5.2 지역 변수가 전역 변수를 가리는 경우](#52-지역-변수가-전역-변수를-가리는-경우)
  - [5.3 전역 리스트의 변경](#53-전역-리스트의-변경)
- [6. 2차원 리스트와 리스트의 복사](#6-2차원-리스트와-리스트의-복사)
  - [6.1 리스트를 요소로 갖는 리스트](#61-리스트를-요소로-갖는-리스트)
  - [6.2 리스트의 반복과 접합](#62-리스트의-반복과-접합)
  - [6.3 2차원 리스트 채우기](#63-2차원-리스트-채우기)
  - [6.4 대입과 복사](#64-대입과-복사)
- [7. 딕셔너리](#7-딕셔너리)
  - [7.1 전화번호부](#71-전화번호부)
  - [7.2 물건 개수 조회](#72-물건-개수-조회)
  - [7.3 값의 조회, 변경, 추가, 삭제](#73-값의-조회-변경-추가-삭제)
  - [7.4 딕셔너리의 메서드](#74-딕셔너리의-메서드)
- [8. 주사위 던지기 시뮬레이션](#8-주사위-던지기-시뮬레이션)
  - [8.1 변수 여섯 개로 세기](#81-변수-여섯-개로-세기)
  - [8.2 리스트로 세기](#82-리스트로-세기)
- [요약](#요약)
- [점검 문제](#점검-문제)

---

<br>

## 1. 실습 구성과 실행 방법

[7강 리스트와 딕셔너리](../../Lecture-Notes/Lec07_Lists-and-Dictionaries/Concepts_Lecture.ko.md)를 따라 작성한 코드이다. 5절의 전역 변수는 [6강 함수](../../Lecture-Notes/Lec06_Functions/Concepts_Lecture.ko.md)의 지역 변수와 전역 변수를 리스트로 넓힌 내용이다. 2\~4절과 6절은 리스트를, 7절은 딕셔너리를, 8절은 두 자료형을 활용한 시뮬레이션을 다룬다.

```text
Coursework/Lab07_Lists-and-Dictionaries/
├── Lab-Explanation.ko.md              # 이 문서 (한국어)
├── Lab-Explanation.md                 # 이 문서 (영어)
├── Lab_ListType.py                    # 2.1 리스트의 자료형
├── Lab_ListOperations.py              # 2.2 요소의 변경, 추가, 삭제와 탐색
├── Lab_IndexSearch.py                 # 2.3 인덱스 찾기의 세 방법
├── Lab_MinIndex.py                    # 2.4 가장 작은 값의 인덱스
├── Lab_ListArgument.py                # 3.1 함수 안에서 바꾼 리스트
├── Lab_ModifyListInFunction.py        # 3.2 요소를 바꾸는 두 방법
├── Lab_AverageWithFunctions.py        # 3.3 함수로 나눈 평균 계산
├── Lab_BubbleSort.py                  # 4.1 버블 정렬
├── Lab_ListComprehension.py           # 4.2 리스트 컴프리헨션
├── Lab_GlobalVariableAssignment.py    # 5.1 global 선언 없이 전역 변수에 대입하기
├── Lab_LocalShadowing.py              # 5.2 지역 변수가 전역 변수를 가리는 경우
├── Lab_GlobalList.py                  # 5.3 전역 리스트의 변경
├── Lab_ListOfLists.py                 # 6.1 리스트를 요소로 갖는 리스트
├── Lab_ListRepetition.py              # 6.2 리스트의 반복과 접합
├── Lab_TwoDimensionalList.py          # 6.3 2차원 리스트 채우기
├── Lab_ListCopy.py                    # 6.4 대입과 복사
├── Lab_PhoneBook.py                   # 7.1 전화번호부
├── Lab_ItemLookup.py                  # 7.2 물건 개수 조회
├── Lab_DictionaryBasics.py            # 7.3 값의 조회, 변경, 추가, 삭제
├── Lab_DictionaryMethods.py           # 7.4 딕셔너리의 메서드
├── Lab_DiceCounters.py                # 8.1 변수 여섯 개로 세기
└── Lab_DiceList.py                    # 8.2 리스트로 세기
```

*그림 1. 실습 7의 디렉토리 구성*

모든 프로그램은 표준 라이브러리만 쓰므로 파이썬 3에서 그대로 실행된다. 난수를 쓰는 프로그램(4.1절, 8절)은 실행할 때마다 결과가 달라지며, 이 문서에는 한 번의 실행 예를 싣는다. 각 파일의 맨 위에는 파일 이름, 한 줄 설명, 작성자, 작성일을 적은 문서화 문자열(docstring)이 있으며, 이 문서의 코드 블록에서는 그 부분을 생략한다.

```bash
cd Coursework/Lab07_Lists-and-Dictionaries
python3 Lab_ListOperations.py
```

---

<br>

## 2. 리스트의 생성과 기본 연산

### 2.1 리스트의 자료형

**코드:** [Lab_ListType.py](Lab_ListType.py)

```python
#<class 'list'>라고 출력되는 것들
a=[]
print(type(a))

b=list()
print(type(b))

c=[1,2,'4']
print(type(c))

d=[1,2,3,c] #c가 존재하므로 오류 발생 X
print(type(d)) #리스트 안에 리스트가 존재할 수 있음
```

- **리스트를 만드는 방법:** 빈 대괄호 `[]`와 `list()`는 모두 빈 리스트를 만든다. `type()`은 값의 자료형을 돌려주므로 네 줄 모두 `<class 'list'>`가 출력된다.
- **여러 자료형의 요소:** `c`처럼 한 리스트에 정수 `1`, `2`와 문자열 `'4'`를 함께 담을 수 있다.
- **중첩 리스트:** `d`의 마지막 요소는 리스트 `c`이다. 리스트는 다른 리스트를 요소로 가질 수 있으며, `c`가 미리 정의되어 있으므로 오류가 나지 않는다는 것이 주석의 뜻이다. `d[3][2]`는 `c`의 세 번째 요소 `'4'`이다.

**실행 결과:**

```text
<class 'list'>
<class 'list'>
<class 'list'>
<class 'list'>
```

### 2.2 요소의 변경, 추가, 삭제와 탐색

**코드:** [Lab_ListOperations.py](Lab_ListOperations.py)

```python
#리스트 항목 변경법
print("리스트 항목 변경법")
heroes=["아이언맨","토르"]
print(heroes)

#변경
print("\n변경")
heroes[1]="닥터 스트레인지"
print(heroes)

#추가
print("\n추가")
heroes.append("스파이더맨")
heroes.insert(2, "배트맨") #위치(인덱스) 지정
print(heroes)

#삭제
print("\n삭제")
heroes.remove("닥터 스트레인지")
del heroes[0] #위치(인덱스) 지정
print(heroes)

#pop은 리스트에서 마지막 항목을 삭제함
print("\npop 활용")
heroes9=["아이언맨","토르","헐크","스칼렛 위치"]
last_hero=heroes9.pop()
print(last_hero)

#조건문 활용 예
print("\n조건문 활용 예")
if "슈퍼맨" in heroes:
    heroes.remove("슈퍼맨")

#탐색
heroes8=["아이언맨","토르","헐크","스칼렛 위치"]
print(heroes8.index("헐크"))

#index를 직접 구현
for i in range (len(heroes8)):
    if "헐크" in heroes8[i]:
        print("인덱스: ", i)

#입력받은 데이터의 인덱스 출력
heroes7=["아이언맨","토르","헐크","스칼렛 위치"]
ans=input("찾고자 하는 데이터: ")
for i in range(len(heroes7)):
    if ans == heroes7[i]:
        print(i)
```

- **변경:** `heroes[1] = 값`은 인덱스 1의 요소를 새 값으로 바꾼다. 리스트는 만든 뒤에도 요소를 바꿀 수 있는 **변경 가능(mutable)** 한 자료형이다.
- **추가:** `append(x)`는 끝에 `x`를 붙이고, `insert(2, x)`는 인덱스 2의 자리에 `x`를 넣고 원래 그 자리부터의 요소를 한 칸씩 뒤로 민다.
- **삭제:** `remove(x)`는 값이 `x`인 첫 요소를 지우고, `del heroes[0]`은 인덱스 0의 요소를 지운다. 값으로 지울지, 위치로 지울지에 따라 고른다.
- **`pop()`:** 마지막 요소를 리스트에서 꺼내 반환한다. 그래서 `last_hero`에 `"스칼렛 위치"`가 저장되고 `heroes9`는 요소가 3개로 줄어든다.
- **`in`과 조건문:** `remove()`는 없는 값을 지우려 하면 `ValueError`를 일으키므로, `if "슈퍼맨" in heroes:`로 먼저 확인한다. `"슈퍼맨"`이 없으므로 아무것도 하지 않는다.
- **탐색:** `index("헐크")`는 `"헐크"`가 처음 나오는 인덱스 2를 반환한다. 이어지는 반복문은 같은 일을 직접 구현한 것이다. 이 반복문의 `"헐크" in heroes8[i]`는 두 문자열 사이의 `in`이므로 같은지가 아니라 포함되는지를 검사한다. 요소가 `"헐크버스터"`여도 참이 되므로, 정확히 같은 요소를 찾으려면 마지막 반복문처럼 `==`로 비교한다.

**실행 결과:** 마지막 입력에 `토르`를 입력한 경우이다. 각 단계의 제목은 순서대로 "리스트 항목 변경법", "변경", "추가", "삭제", "pop 활용", "조건문 활용 예"이다.

```text
리스트 항목 변경법
['아이언맨', '토르']

변경
['아이언맨', '닥터 스트레인지']

추가
['아이언맨', '닥터 스트레인지', '배트맨', '스파이더맨']

삭제
['배트맨', '스파이더맨']

pop 활용
스칼렛 위치

조건문 활용 예
2
인덱스:  2
찾고자 하는 데이터: 토르
1
```

추가 단계에서 `append()`로 `['아이언맨', '닥터 스트레인지', '스파이더맨']`이 된 뒤, `insert(2, ...)`가 인덱스 2에 `'배트맨'`을 넣어 `'스파이더맨'`이 인덱스 3으로 밀린다. 삭제 단계에서는 `remove()`가 `'닥터 스트레인지'`를, `del`이 인덱스 0의 `'아이언맨'`을 지운다.

### 2.3 인덱스 찾기의 세 방법

**코드:** [Lab_IndexSearch.py](Lab_IndexSearch.py)

```python
def index_(list_, g):
    f_index=0
    for i in range(len(h)):
        if g==h[i]:
            f_index=i
    return f_index

h=["아","토","헐","스","헐"]
g=input("i:")
for i in range(len(h)):
    if g==h[i]:
        print(i)

print(index_(h,g))
print(h.index(g))

#수식에 따라 "헐"이 두개일때 모두 출력하거나
#마지막 값만 출력하게 됨
```

- **반복문으로 모두 출력:** 메인 부분의 반복문은 `g`와 같은 요소를 만날 때마다 인덱스를 출력하므로 같은 값이 여러 번 있으면 모든 위치가 나온다.
- **직접 만든 함수 `index_`:** 같은 요소를 만날 때마다 `f_index`를 덮어쓰므로 마지막으로 일치한 인덱스를 반환한다. 일치하는 요소가 없으면 초기값 0을 반환하므로, 인덱스 0에서 찾은 경우와 구별되지 않는다.
- **`list.index()`:** 처음으로 일치한 인덱스를 반환한다. 주석의 말처럼 같은 값이 두 개일 때 방법에 따라 결과가 다르다.

**실행 결과:** `헐`을 입력한 경우이다. `"헐"`은 인덱스 2와 4에 있으므로 반복문은 2와 4를, `index_`는 4를, `index()`는 2를 출력한다.

```text
i:헐
2
4
4
2
```

> **참고:** 함수 `index_`는 매개변수 `list_`를 받지만 본체에서는 전역 변수 `h`를 쓴다. 이 프로그램은 `h`를 인수로 넘기므로 결과가 같지만, 다른 리스트를 넘기면 여전히 `h`를 탐색한다. 본체의 `h`를 모두 `list_`로 바꾸어야 넘긴 리스트를 탐색하는 함수가 된다. 또한 `h`에 없는 값을 입력하면 마지막 줄의 `h.index(g)`가 `ValueError`를 일으킨다.

### 2.4 가장 작은 값의 인덱스

**코드:** [Lab_MinIndex.py](Lab_MinIndex.py)

```python
list_=[1, 3, 67, 8, 3, 5, -1, 3, -9, 10]
temp=list_[0]

#가장 작은 값의 인덱스 구하기
min=0
for i in range (len(list_)):
    if list_[i] < temp:
        min=i
        temp=list_[i]

print("min index: ", min)
```

- **방법:** 첫 요소를 지금까지의 최솟값 `temp`로, 그 인덱스 0을 `min`으로 두고, 모든 요소를 차례로 보며 `temp`보다 작은 요소를 만나면 두 변수를 갱신한다.
- **추적:** `temp`는 1에서 시작하여 인덱스 6의 -1을 만나 -1이 되고, 인덱스 8의 -9를 만나 -9가 된다. 따라서 마지막 `min`은 8이다.
- **같은 최솟값:** 비교가 `<`이므로 같은 최솟값이 여러 번 있으면 처음 나온 인덱스가 남는다.

**실행 결과:**

```text
min index:  8
```

> **주의:** 변수 이름 `min`은 내장 함수 `min()`을 가린다. 내장 함수를 쓰면 `list_.index(min(list_))`로 같은 결과를 얻을 수 있으므로, 변수 이름은 `min_index`처럼 짓는 것이 안전하다.

---

<br>

## 3. 함수와 리스트

### 3.1 함수 안에서 바꾼 리스트

**코드:** [Lab_ListArgument.py](Lab_ListArgument.py)

```python
# 리턴받지 않고 하는 함수
def f_c(list_):
    list_[0]=100

def f_c2(list_): # 이렇게 작성하지 않음.
    list_a[0]=1

##main##
list_a=[1,2,3,4,5]
f_c(list_a)
print(list_a)
f_c2(list_a)
print(list_a)
```

- **참조의 전달:** 파이썬의 변수는 값 자체가 아니라 객체를 가리키는 **참조(reference)** 를 담는다. `f_c(list_a)`를 호출하면 매개변수 `list_`는 `list_a`와 같은 리스트 객체를 가리키므로, `list_[0]=100`은 그 객체를 바꾸고 호출한 쪽의 `list_a`에서도 바뀐 값이 보인다. 그래서 반환하지 않아도 결과가 전달된다.
- **`f_c2`의 문제:** 매개변수 `list_`를 쓰지 않고 전역 변수 `list_a`를 직접 바꾼다. 이 호출에서는 같은 리스트이므로 결과가 같지만, 다른 리스트를 넘겨도 언제나 `list_a`가 바뀌므로 주석처럼 이렇게 쓰지 않는다.

**실행 결과:**

```text
[100, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
```

### 3.2 요소를 바꾸는 두 방법

**코드:** [Lab_ModifyListInFunction.py](Lab_ModifyListInFunction.py)

```python
def func2(list):
    list[0] = 99

values = [0,1,1,2,3,5,8]
print(values)
func2(values)
print(values)

# 또는

def func1(list):
    return 99

value = [0,1,1,2,3,5,8]
print(value)
value[0] = func1(value)
print(value)
```

- **함수 안에서 바꾸기:** `func2`는 3.1절의 `f_c`와 같이 전달받은 리스트를 직접 바꾼다.
- **반환값으로 바꾸기:** `func1`은 새 값 99를 반환하기만 하고, 호출한 쪽이 `value[0] = func1(value)`로 대입한다. 함수가 인수를 바꾸지 않으므로 함수의 동작을 이해하기 쉽다.
- **결과:** 두 방법 모두 첫 요소가 99가 된다. 리스트는 피보나치 수열의 앞부분이다.

**실행 결과:**

```text
[0, 1, 1, 2, 3, 5, 8]
[99, 1, 1, 2, 3, 5, 8]
[0, 1, 1, 2, 3, 5, 8]
[99, 1, 1, 2, 3, 5, 8]
```

> **주의:** 매개변수 이름 `list`는 내장 함수 `list()`를 가린다. 함수 안에서 `list()`로 리스트를 만들 수 없게 되므로 `nums`처럼 다른 이름을 쓴다.

### 3.3 함수로 나눈 평균 계산

**코드:** [Lab_AverageWithFunctions.py](Lab_AverageWithFunctions.py)

```python
'''num = []
for i in range(5):
    num.append(int(input(":")))

sum_=0
for j in num: #num 리스트의 원소 중 하나가 들어감
    sum_ += j

avg = sum_ / 5
print(avg)
'''
#위 코드를 함수를 이용하여 작성

num=[]
def insert_():
    for i in range(5):
        num.append(int(input(":")))

def avg_():
    sum_ = 0
    for j in num:
        sum_ += j
    avg=sum_/5
    print(avg)

def main():
    insert_()
    avg_()

main()
```

- **문제:** 정수 5개를 입력받아 평균을 출력하는 코드(문자열로 남겨 둔 부분)를 입력과 계산의 두 함수로 나눈다.
- **전역 리스트:** `insert_`와 `avg_`는 전역 리스트 `num`을 함께 쓴다. `insert_`는 `append()`로 리스트 객체를 바꿀 뿐 `num`에 새 값을 대입하지 않으므로 `global` 선언이 필요 없다(5.3절).
- **요소 순회:** `for j in num:`은 인덱스 없이 요소를 하나씩 `j`에 꺼낸다. 주석의 말처럼 `j`에는 `num`의 요소가 차례로 들어간다.

**실행 결과:** 10, 20, 30, 40, 50을 입력한 경우이다. $150 / 5 = 30.0$이다.

```text
:10
:20
:30
:40
:50
30.0
```

---

<br>

## 4. 정렬과 리스트 컴프리헨션

### 4.1 버블 정렬

**코드:** [Lab_BubbleSort.py](Lab_BubbleSort.py)

```python
import random
datalist=[]

for i in range (0, 5, 1):
    datalist.append(random.randint(1, 100))

print(datalist)

for j in range(len(datalist)-1): # 비효율적인 방법
    for i in range(len(datalist)-1):
        if datalist[i] > datalist[i+1]:
            temp=datalist[i]
            datalist[i]=datalist[i+1]
            datalist[i+1]=temp
    print(datalist)

print(datalist)
```

- **데이터:** 1\~100의 난수 5개를 리스트에 담는다.
- **버블 정렬(bubble sort):** 이웃한 두 요소를 앞에서부터 비교하여 앞의 것이 크면 맞바꾸는 일을 리스트 끝까지 하는 것을 한 번의 **패스(pass)** 라고 한다. 한 패스가 끝나면 아직 정렬되지 않은 부분의 가장 큰 값이 맨 뒤로 옮겨진다. 큰 값이 거품처럼 뒤로 떠오른다는 뜻에서 이름이 붙었다.
- **맞바꾸기:** `temp`에 앞 요소를 잠시 담아 두고 두 요소를 맞바꾼다. 파이썬에서는 `datalist[i], datalist[i+1] = datalist[i+1], datalist[i]` 한 줄로도 쓸 수 있다.
- **패스의 수:** 요소가 $n$개이면 $n-1$번의 패스로 충분하다. $k$번째 패스가 끝나면 가장 큰 $k$개가 맨 뒤에 제자리를 잡으므로, $n-1$번 뒤에는 남은 하나도 맨 앞의 제자리에 있게 된다. 바깥 반복은 `range(len(datalist)-1)`로 이 $n-1$번을 실행하고, 패스마다 리스트를 출력한다.
- **비효율의 원인:** 주석의 말처럼 이 구현은 패스마다 비교를 $n-1$번씩, 모두 $(n-1)^2$번 한다. $k$번째 패스 뒤에는 뒤쪽 $k$개를 비교할 필요가 없으므로 안쪽 반복을 `range(len(datalist)-1-j)`로 줄이면 비교 횟수가 $n(n-1)/2$번이 되고, 한 패스에서 한 번도 맞바꾸지 않았으면 이미 정렬된 것이므로 반복을 끝낼 수 있다.

**실행 결과:** 한 번의 실행 예이다. 첫 줄은 정렬 전, 가운데 네 줄은 각 패스 뒤, 마지막 줄은 정렬 결과이다.

```text
[78, 37, 88, 72, 61]
[37, 78, 72, 61, 88]
[37, 72, 61, 78, 88]
[37, 61, 72, 78, 88]
[37, 61, 72, 78, 88]
[37, 61, 72, 78, 88]
```

> **주의:** 바깥 반복을 $n-2$번만 실행하면 정렬되지 않는 입력이 있다. 예를 들어 `[5, 4, 3, 2, 1]`은 패스마다 `[4, 3, 2, 1, 5]`, `[3, 2, 1, 4, 5]`, `[2, 1, 3, 4, 5]`가 되어, 세 번의 패스 뒤에도 맨 앞의 두 요소가 뒤바뀐 채 남는다. 가장 작은 값이 맨 뒤에 있으면 한 패스에 한 칸씩만 앞으로 오므로 $n-1$번의 패스가 필요하다.

### 4.2 리스트 컴프리헨션

**코드:** [Lab_ListComprehension.py](Lab_ListComprehension.py)

```python
# 예시1
s=[]
for x in range(10):
    s.append(x**2)
print(s)

ss=[x**2 for x in range(10)] # 함축
print(ss)


# 예시2
sss=[]
for x in range(10):
    if x%2==0:
        sss.append(x**2)
print(sss)

ssss=[x**2 for x in range(10) if x%2==0] # 함축
print(ssss)
```

- **리스트 컴프리헨션(list comprehension):** `[식 for 변수 in 반복대상]`은 반복 대상의 요소마다 식의 값을 계산하여 그 값들로 새 리스트를 만든다. 빈 리스트를 만들고 `for`문에서 `append()`하는 세 줄을 한 줄로 쓴 것과 같다.
- **조건 붙이기:** `[식 for 변수 in 반복대상 if 조건]`은 조건이 참인 요소에 대해서만 식을 계산한다. 예시 2는 0\~9 중 짝수(`x%2==0`)의 제곱만 모은다.

**실행 결과:** 각 예시의 두 방법이 같은 리스트를 만든다.

```text
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 4, 16, 36, 64]
[0, 4, 16, 36, 64]
```

---

<br>

## 5. 전역 변수와 전역 리스트

### 5.1 global 선언 없이 전역 변수에 대입하기

**코드:** [Lab_GlobalVariableAssignment.py](Lab_GlobalVariableAssignment.py)

```python
global_var = 10

def modify_global():
    #global global_var
    print("Before modification:", global_var)
    global_var = 20
    print("After modification:", global_var)

def access_global():
    print("Accessing global variable:", global_var)

# 함수 실행
access_global()
try:
    modify_global()
except UnboundLocalError as e:
    print("UnboundLocalError:", e)
access_global()
```

- **읽기만 하는 함수:** `access_global`은 `global_var`를 읽기만 하므로 전역 변수의 값 10을 출력한다.
- **대입하는 함수:** `modify_global`에는 `global_var = 20`이라는 대입이 있다. 파이썬은 함수를 실행하기 전에 본체 전체를 보고 함수 안에서 대입되는 이름을 그 함수의 지역 변수로 정한다. 그래서 첫 줄의 `print()`가 읽는 `global_var`도 아직 값이 없는 지역 변수가 되어 **`UnboundLocalError`** 가 발생한다. 대입이 읽기보다 뒤에 있어도 마찬가지이다.
- **오류 처리:** 오류를 보여 주기 위해 `global` 선언을 주석으로 막아 두었고, `try-except`가 오류를 잡아 메시지를 출력한 뒤 다음 문장으로 진행한다. 마지막 `access_global()`은 전역 변수가 그대로 10임을 보여 준다.
- **고치는 방법:** 주석 처리된 `global global_var`를 살리면 함수 안의 `global_var`가 전역 변수를 가리키므로 `Before modification: 10`, `After modification: 20`이 출력되고, 마지막 줄은 20을 출력한다.

**실행 결과:** 오류 메시지는 파이썬 3.11 이후의 문구이며, 이전 버전에서는 `local variable 'global_var' referenced before assignment`로 출력된다.

```text
Accessing global variable: 10
UnboundLocalError: cannot access local variable 'global_var' where it is not associated with a value
Accessing global variable: 10
```

### 5.2 지역 변수가 전역 변수를 가리는 경우

**코드:** [Lab_LocalShadowing.py](Lab_LocalShadowing.py)

```python
global_var = 10

def modify_global():
    #global global_var
    print("Before modification:",global_var)
    global_var = 20
    print("After modification:",global_var)

def access_global():
    global_var = 200
    print("Accessing global variable:",global_var)

# 함수 실행
access_global()
try:
    modify_global()
except UnboundLocalError as e:
    print("UnboundLocalError:", e)
access_global()
```

- **5.1절과의 차이:** `access_global` 안에서 `global_var = 200`을 대입하므로 이 `global_var`는 `access_global`의 지역 변수이다. 지역 변수가 같은 이름의 전역 변수를 가리므로 함수 안에서는 200이 출력되지만 전역 변수는 10 그대로이다.
- **결과:** `access_global`은 호출될 때마다 새 지역 변수에 200을 대입하므로 두 번 모두 200을 출력하고, `modify_global`은 5.1절과 같은 이유로 `UnboundLocalError`를 일으킨다. 출력 문구는 "Accessing global variable"이지만 실제로 출력되는 것은 지역 변수의 값이다.

**실행 결과:**

```text
Accessing global variable: 200
UnboundLocalError: cannot access local variable 'global_var' where it is not associated with a value
Accessing global variable: 200
```

### 5.3 전역 리스트의 변경

**코드:** [Lab_GlobalList.py](Lab_GlobalList.py)

```python
global_list = [1, 2, 3, 4]

def modify_global_list():
    global global_list
    print("Before modification:", global_list)
    global_list.append(5)
    global_list.extend([6, 7])
    print("After modification:", global_list)

def access_global_list():
    print("Accessing global variable:", global_list)

# 함수 실행
access_global_list()
modify_global_list()
access_global_list()
```

- **리스트 메서드:** `append(5)`는 요소 하나를, `extend([6, 7])`은 다른 리스트의 요소들을 끝에 붙인다. `append([6, 7])`로 쓰면 리스트 `[6, 7]` 자체가 요소 하나로 들어간다.
- **`global` 선언이 없어도 되는 이유:** `append()`와 `extend()`는 `global_list`가 가리키는 리스트 객체를 바꿀 뿐, 이름 `global_list`에 새 값을 대입하지 않는다. 대입이 없으므로 이름은 전역 변수로 찾아지고, `global global_list` 줄을 지워도 결과가 같다. 반면 `global_list = global_list + [5]`처럼 이름에 대입하면 `global` 선언이 필요하다.
- **결과:** 함수 안에서 바꾼 리스트가 함수 밖에서도 `[1, 2, 3, 4, 5, 6, 7]`로 보인다.

**실행 결과:**

```text
Accessing global variable: [1, 2, 3, 4]
Before modification: [1, 2, 3, 4]
After modification: [1, 2, 3, 4, 5, 6, 7]
Accessing global variable: [1, 2, 3, 4, 5, 6, 7]
```

---

<br>

## 6. 2차원 리스트와 리스트의 복사

### 6.1 리스트를 요소로 갖는 리스트

**코드:** [Lab_ListOfLists.py](Lab_ListOfLists.py)

```python
s=[]
s.append([1,2,3,4])
s.append([1,2,3,4])
s.append([5,6,7]) #열의 개수가 달라지면?
print(s)
print(len(s))
print(len(s[0])) #열의 개수
```

- **2차원 리스트:** 리스트를 요소로 갖는 리스트를 행과 열의 표처럼 쓸 수 있다. `s[i]`가 `i`번째 행이고 `s[i][j]`가 그 행의 `j`번째 요소이다.
- **길이:** `len(s)`는 행의 수 3이고, `len(s[0])`은 첫 행의 요소 수 4이다.
- **행마다 다른 길이:** 주석의 질문처럼 세 번째 행은 요소가 3개이다. 파이썬의 리스트는 행마다 길이가 달라도 되므로 오류가 나지 않지만, 이때 `len(s[0])`은 첫 행의 길이일 뿐 모든 행의 열 수가 아니며, `s[2][3]`은 `IndexError`를 일으킨다.

**실행 결과:**

```text
[[1, 2, 3, 4], [1, 2, 3, 4], [5, 6, 7]]
3
4
```

### 6.2 리스트의 반복과 접합

**코드:** [Lab_ListRepetition.py](Lab_ListRepetition.py)

```python
a=[1]
b=a*5
print(b)

c=a+b
print(c)
```

- **반복(`*`):** `리스트 * n`은 리스트의 요소를 `n`번 이어 붙인 새 리스트를 만든다. `[1] * 5`는 `[1, 1, 1, 1, 1]`이다.
- **접합(`+`):** 두 리스트를 이어 붙인 새 리스트를 만든다. `[1] + [1, 1, 1, 1, 1]`은 요소가 6개이다. 두 연산 모두 원래 리스트 `a`, `b`는 바꾸지 않는다.

**실행 결과:**

```text
[1, 1, 1, 1, 1]
[1, 1, 1, 1, 1, 1]
```

### 6.3 2차원 리스트 채우기

**코드:** [Lab_TwoDimensionalList.py](Lab_TwoDimensionalList.py)

```python
rows = 3
cols = 5

s = []
for row in range(rows):
    s += [[0]*cols]
#for i in range(r):
#    s.append([0]*5) 도 가능

print("s =", s)

for i in range(rows):
    for j in range(cols):
        data=int(input("추가할 값을 입력하세요:"))
        s[i][j] = data
#자동으로 0~14로 채우려면
#s[i][j]=n
#n+=1 을 for i, for j 안에 채우면 됨

print("s =", s)
```

- **행 만들기:** 반복마다 `[0]*cols`가 0이 5개인 새 리스트를 만들고, `s += [그 리스트]`가 그것을 한 행으로 붙인다. 주석처럼 `s.append([0]*5)`로 써도 같다.
- **중첩 반복:** 바깥 반복이 행 `i`를, 안쪽 반복이 열 `j`를 차례로 정하므로 `s[0][0]`, `s[0][1]`, ..., `s[2][4]`의 순서로 15개의 값을 입력받는다. 이 순서를 **행 우선 순서(row-major order)** 라고 한다.
- **자동으로 채우기:** 주석은 입력 대신 `n = 0`에서 시작하여 `s[i][j] = n`, `n += 1`을 안쪽 반복에 두면 0\~14가 차례로 채워진다는 메모이다. `s[i][j] = i * cols + j`로도 같은 값을 얻는다.

**실행 결과:** 0부터 14까지를 차례로 입력한 경우이며, 15번의 입력 줄은 앞의 두 줄과 마지막 줄만 보이고 가운데를 생략했다.

```text
s = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
추가할 값을 입력하세요:0
추가할 값을 입력하세요:1
(가운데 12줄 생략)
추가할 값을 입력하세요:14
s = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]]
```

> **주의:** 행을 `s = [[0]*cols]*rows`로 만들면 안 된다. 바깥의 `*`는 같은 행 리스트에 대한 참조를 `rows`번 복사하므로 세 행이 모두 한 객체이고, `s[0][0] = 7`이 세 행의 첫 요소를 모두 7로 바꾼다. 이 프로그램처럼 반복문이나 `[[0]*cols for _ in range(rows)]`로 행마다 새 리스트를 만들어야 한다.

### 6.4 대입과 복사

**코드:** [Lab_ListCopy.py](Lab_ListCopy.py)

```python
a=[1,2,3,4]
b=a
a[3]=1000
print(a)
print(b)

#리스트를 이렇게 복사하고 바꾸면
# a=[1,2,3,1000]
# b=[1,2,3,4]
#로 출력될 것이라고 예상할 수도 있지만
# a와 b가 같은 리스트 객체를 가리키므로 b도 [1,2,3,1000]으로 출력된다

b[3]=4
print(a)
print(b)

#따라서 복사할 때
c=list(b)
b[3]=10
print(b)
print(c)
#이렇게 복사해야 바뀐 값까지 복사되지 않음
```

- **대입은 복사가 아니다:** `b=a`는 리스트를 복사하지 않고, `b`가 `a`와 같은 리스트 객체를 가리키게 한다. 두 이름이 한 객체의 **별칭(alias)** 이 되므로 `a[3]`을 바꾸면 `b`에서도 바뀐 값이 보이고, `b[3]=4`로 되돌리면 `a`도 함께 되돌아간다.
- **`list()`로 복사:** `c=list(b)`는 `b`의 요소들로 새 리스트 객체를 만든다. 그 뒤에 `b[3]`을 10으로 바꾸어도 `c`는 `[1, 2, 3, 4]` 그대로이다. `b[:]`, `b.copy()`도 같은 복사를 만든다.
- **확인 방법:** `a is b`는 두 이름이 같은 객체를 가리키면 `True`이다. 이 프로그램에서 `a is b`는 `True`, `c is b`는 `False`이다.

**실행 결과:**

```text
[1, 2, 3, 1000]
[1, 2, 3, 1000]
[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 3, 10]
[1, 2, 3, 4]
```

> **참고:** `list()`, `[:]`, `copy()`는 **얕은 복사(shallow copy)** 이다. 바깥 리스트만 새로 만들고 요소는 같은 객체를 가리키므로, 2차원 리스트를 이렇게 복사하면 행 리스트는 공유된다. 행까지 따로 복사하려면 `copy` 모듈의 `deepcopy()`를 쓴다.

---

<br>

## 7. 딕셔너리

### 7.1 전화번호부

**코드:** [Lab_PhoneBook.py](Lab_PhoneBook.py)

```python
pb = {}
pb["홍길동"] = "010-1234-5678"
print("1: ", pb)

pb2 = {"홍길동": "010-1234-5678"}
pb2["강감찬"] = "010-1234-5679"
print("2: ", pb2)

print("3: ", pb2["강감찬"])

print("4: 이 부분은 결과창에 한 줄씩 입력하면 나옴")
pb2.keys()
pb2.values()

print("5: ")
dict = {'Name': '홍길동', 'Age': 7, 'Class': '초급'}
print(dict['Name'])
print(dict['Age'])
```

- **딕셔너리(dictionary):** 중괄호 안에 `키: 값` 쌍을 담는 자료형이다. 리스트가 0부터의 정수 인덱스로 요소를 찾는다면, 딕셔너리는 이름(키)으로 값을 찾는다. 이름을 키로, 전화번호를 값으로 두면 전화번호부가 된다.
- **추가와 조회:** `pb["홍길동"] = 값`은 키가 없으면 새 키-값 쌍을 추가하고, 있으면 값을 바꾼다. `pb2["강감찬"]`은 키에 대응하는 값을 돌려준다.
- **4번 부분:** `pb2.keys()`와 `pb2.values()`는 값을 돌려주는 식일 뿐 출력하지 않는다. IDLE의 셸 창에서 식을 한 줄씩 입력하면 그 값이 자동으로 표시되지만, 스크립트로 실행할 때는 `print()`로 감싸야 보인다는 것이 출력 문구의 뜻이다.
- **여러 자료형의 값:** 5번 부분의 딕셔너리는 문자열과 정수 값을 함께 담는다.

**실행 결과:**

```text
1:  {'홍길동': '010-1234-5678'}
2:  {'홍길동': '010-1234-5678', '강감찬': '010-1234-5679'}
3:  010-1234-5679
4: 이 부분은 결과창에 한 줄씩 입력하면 나옴
5: 
홍길동
7
```

> **주의:** 변수 이름 `dict`는 내장 자료형 `dict`를 가리므로, 그 뒤로는 `dict()`로 딕셔너리를 만들 수 없다. `student`처럼 다른 이름을 쓴다.

### 7.2 물건 개수 조회

**코드:** [Lab_ItemLookup.py](Lab_ItemLookup.py)

```python
items = {"커피음료": 7, "펜": 3, "종이컵": 2, "우유": 1, "콜라": 4, "책": 5}

item = input("물건의 이름을 입력하시오: ")
print(items[item])
```

- **입력값을 키로:** 입력한 문자열을 키로 써서 그 물건의 개수를 찾는다. 키의 개수와 관계없이 키 하나로 바로 값을 찾을 수 있다는 것이 딕셔너리의 장점이다.

**실행 결과:** `펜`을 입력한 경우이다.

```text
물건의 이름을 입력하시오: 펜
3
```

> **주의:** 없는 키(예: `연필`)를 입력하면 `items[item]`이 `KeyError`를 일으킨다. `items.get(item)`은 키가 없을 때 `None`을, `items.get(item, 0)`은 0을 돌려주므로 오류 없이 처리할 수 있다. `if item in items:`로 먼저 확인하는 방법도 있다.

### 7.3 값의 조회, 변경, 추가, 삭제

**코드:** [Lab_DictionaryBasics.py](Lab_DictionaryBasics.py)

```python
person = {
    "name": "John",
    "age": 30,
    "city": "New York",
}

print(person["name"])
print(person["age"])

# 값 변경
person["age"] = 31
print(person["age"])

# 새로운 키-값 쌍 추가
person["job"] = "Developer"
print(person)

#키-값 쌍 삭제
del person["city"]
print(person)

# 키를 인덱스처럼 사용할 수 있는 것이
# 리스트와의 큰 차이
```

- **여러 줄로 쓰기:** 키-값 쌍이 많으면 한 줄에 하나씩 쓰며, 마지막 쌍 뒤의 쉼표는 있어도 된다.
- **변경과 추가:** 있는 키 `"age"`에 대입하면 값이 바뀌고, 없는 키 `"job"`에 대입하면 새 쌍이 추가된다. 같은 문법이 키의 존재 여부에 따라 두 가지로 동작한다.
- **삭제:** `del person["city"]`는 키 `"city"`와 그 값을 함께 지운다.
- **순서:** 파이썬 3.7부터 딕셔너리는 키를 넣은 순서를 유지하므로, 새로 추가한 `"job"`이 맨 뒤에 출력된다. 주석의 말처럼 리스트의 정수 인덱스 대신 키로 값을 찾는다는 점이 리스트와의 큰 차이이다.

**실행 결과:**

```text
John
30
31
{'name': 'John', 'age': 31, 'city': 'New York', 'job': 'Developer'}
{'name': 'John', 'age': 31, 'job': 'Developer'}
```

### 7.4 딕셔너리의 메서드

**코드:** [Lab_DictionaryMethods.py](Lab_DictionaryMethods.py)

```python
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

keys = person.keys()
print(keys)

values = person.values()
print(values)

items = person.items()
print(items)

name = person.get("name")
# person["name"] 도 가능!
print(name)

person.update({"age": 31, "job": "Developer"})
print(person)
```

- **`keys()`, `values()`, `items()`:** 각각 키들, 값들, `(키, 값)` 튜플들을 보여 주는 뷰(view) 객체를 돌려준다. 뷰는 딕셔너리를 따라 바뀌며, `list(person.keys())`로 리스트로 바꿀 수 있다. `for k, v in person.items():`처럼 반복문에서 키와 값을 함께 꺼낼 때 쓴다.
- **`get()`:** `person.get("name")`은 `person["name"]`과 같은 값을 돌려주지만, 키가 없으면 오류 대신 `None`(또는 둘째 인수로 준 기본값)을 돌려준다.
- **`update()`:** 인수로 준 딕셔너리의 쌍들로 값을 바꾸거나 추가한다. `"age"`는 31로 바뀌고 `"job"`은 새로 추가된다.

**실행 결과:**

```text
dict_keys(['name', 'age', 'city'])
dict_values(['John', 30, 'New York'])
dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])
John
{'name': 'John', 'age': 31, 'city': 'New York', 'job': 'Developer'}
```

---

<br>

## 8. 주사위 던지기 시뮬레이션

### 8.1 변수 여섯 개로 세기

**코드:** [Lab_DiceCounters.py](Lab_DiceCounters.py)

```python
#주사위 1000번 던져서 각 숫자가 나올 확률 (1)
import random

pro1 = 0
pro2 = 0
pro3 = 0
pro4 = 0
pro5 = 0
pro6 = 0

for i in range(0, 1000, 1):
    a = random.randint(1,6)

    if (a == 1):
        pro1 += 1
    if (a == 2):
        pro2 += 1
    if (a == 3):
        pro3 += 1
    if (a == 4):
        pro4 += 1
    if (a == 5):
        pro5 += 1
    if (a == 6):
        pro6 += 1

print("주사위가 1인 확률은 ", pro1 / 1000)
print("주사위가 2인 확률은 ", pro2 / 1000)
print("주사위가 3인 확률은 ", pro3 / 1000)
print("주사위가 4인 확률은 ", pro4 / 1000)
print("주사위가 5인 확률은 ", pro5 / 1000)
print("주사위가 6인 확률은 ", pro6 / 1000)
```

- **시뮬레이션:** `random.randint(1,6)`으로 주사위를 1000번 던지고, 나온 눈마다 그 눈의 횟수를 담은 변수에 1을 더한다.
- **상대 빈도:** 횟수를 전체 시행 횟수 1000으로 나눈 값이 **상대 빈도(relative frequency)** 이다. 출력 문구는 이 값을 확률이라고 부르지만, 정확히는 확률을 추정한 값이다.
- **구조의 한계:** 눈마다 변수와 `if`문을 하나씩 두므로 눈의 종류가 늘어나면 코드도 그만큼 길어진다. 한 번 던질 때 `a`는 한 값뿐이므로 여섯 `if` 중 하나만 참이며, `if-elif`로 쓰면 참인 조건을 찾은 뒤 나머지 비교를 건너뛴다.

**실행 결과:** 한 번의 실행 예이다.

```text
주사위가 1인 확률은  0.181
주사위가 2인 확률은  0.168
주사위가 3인 확률은  0.182
주사위가 4인 확률은  0.157
주사위가 5인 확률은  0.159
주사위가 6인 확률은  0.153
```

> **[확률및통계]** 공정한 주사위에서 각 눈이 나올 확률은 $1/6 \approx 0.167$이다. 같은 시행을 독립적으로 반복할수록 상대 빈도가 확률에 가까워지는 경향을 큰 수의 법칙이라고 한다. 1000번 정도에서는 위처럼 0.15\~0.18 정도로 흩어지며, 던지는 횟수를 늘리면 여섯 값이 0.167 가까이로 모인다.

### 8.2 리스트로 세기

**코드:** [Lab_DiceList.py](Lab_DiceList.py)

```python
#주사위 1000번 던져서 각 숫자가 나올 확률 (2)
import random

pro_=[0]*6

for i in range(1000):
    num=random.randint(1, 6)
    pro_[num-1] += 1

for i in range(6):
    print("주사위가", i+1, "인 확률은", pro_[i] / 1000)
```

- **리스트를 계수기로:** 요소가 6개인 리스트 `pro_`의 인덱스 0\~5를 눈 1\~6에 대응시킨다. 눈 `num`이 나오면 `pro_[num-1]`에 1을 더하므로 `if`문 없이 한 줄로 센다.
- **출력:** 인덱스 `i`는 0\~5이므로 눈의 번호는 `i+1`로 출력하고, 상대 빈도는 `pro_[i] / 1000`으로 계산한다. 8.1절과 같은 일을 하지만 눈의 종류가 바뀌어도 리스트의 크기만 바꾸면 된다.

**실행 결과:** 한 번의 실행 예이다. 8.1절의 출력과 달리 `print()`에 숫자를 따로 넘기므로 숫자 뒤에 공백이 있다.

```text
주사위가 1 인 확률은 0.154
주사위가 2 인 확률은 0.165
주사위가 3 인 확률은 0.177
주사위가 4 인 확률은 0.166
주사위가 5 인 확률은 0.163
주사위가 6 인 확률은 0.175
```

---

<br>

## 요약

| 개념 | 핵심 요약 |
|:-----|:-----|
| 리스트의 변경 | 리스트는 변경 가능한 자료형이며, 인덱스 대입, `append()`, `insert()`, `remove()`, `del`, `pop()`으로 요소를 바꾸고 더하고 지운다. |
| 탐색 | `in`은 포함 여부를, `index()`는 처음 일치한 인덱스를 돌려주며, 없는 값에 `index()`나 `remove()`를 쓰면 `ValueError`가 발생한다. |
| 참조의 전달 | 함수에 전달한 리스트는 같은 객체이므로 함수 안에서 요소를 바꾸면 호출한 쪽에도 반영된다. |
| 버블 정렬 | 이웃한 요소를 비교하여 맞바꾸는 패스를 $n-1$번 하면 정렬되며, 패스마다 가장 큰 값이 뒤로 간다. |
| 리스트 컴프리헨션 | `[식 for 변수 in 반복대상 if 조건]`은 조건을 만족하는 요소마다 식의 값을 모은 새 리스트를 만든다. |
| `global`과 리스트 | 함수 안에서 이름에 대입하면 지역 변수가 되지만, `append()`처럼 객체를 바꾸기만 하면 `global` 선언이 필요 없다. |
| 2차원 리스트 | 행마다 새 리스트를 만들어야 하며, `[[0]*c]*r`은 같은 행을 공유하는 별칭을 만든다. |
| 대입과 복사 | `b = a`는 같은 객체의 별칭을 만들고, `list(a)`, `a[:]`, `a.copy()`는 얕은 복사를 만든다. |
| 딕셔너리 | 키로 값을 찾고, 있는 키에 대입하면 변경, 없는 키에 대입하면 추가이며, 없는 키를 `[]`로 읽으면 `KeyError`가 발생한다. |
| 딕셔너리 메서드 | `keys()`, `values()`, `items()`는 뷰를, `get()`은 키가 없을 때 기본값을, `update()`는 여러 쌍의 변경과 추가를 제공한다. |

---

<br>

## 점검 문제

1. **리스트 연산의 추적:** `x = [1, 2, 3]`에 `x.insert(1, 9)`, `x.remove(3)`, `x.append(x.pop(0))`를 차례로 실행한 뒤의 `x`를 쓰라.

   <details>
   <summary>정답</summary>

   `insert(1, 9)` 뒤에 `[1, 9, 2, 3]`, `remove(3)` 뒤에 `[1, 9, 2]`가 된다. `x.pop(0)`은 인덱스 0의 1을 꺼내 `[9, 2]`를 남기고, 그 1을 `append()`로 끝에 붙이므로 `[9, 2, 1]`이다.

   </details>

2. **함수와 리스트:** 다음 코드의 출력을 쓰고 이유를 설명하라.

   ```python
   def f(a):
       a.append(4)
       a = [0]
   x = [1, 2, 3]
   f(x)
   print(x)
   ```

   <details>
   <summary>정답</summary>

   `[1, 2, 3, 4]`이다. `a.append(4)`는 `x`와 같은 리스트 객체를 바꾸므로 호출한 쪽에 반영된다. 그 뒤의 `a = [0]`은 지역 변수 `a`가 새 리스트를 가리키게 할 뿐 `x`가 가리키는 객체를 바꾸지 않는다.

   </details>

3. **버블 정렬의 패스:** `[3, 1, 4, 2]`에 버블 정렬을 적용할 때 첫 번째 패스가 끝난 뒤의 리스트와 정렬에 필요한 패스의 수를 쓰라.

   <details>
   <summary>정답</summary>

   첫 패스에서 3과 1을 맞바꾸어 `[1, 3, 4, 2]`, 3과 4는 그대로, 4와 2를 맞바꾸어 `[1, 3, 2, 4]`가 된다. 두 번째 패스에서 3과 2를 맞바꾸어 `[1, 2, 3, 4]`가 되므로 이 입력은 두 번의 패스로 정렬된다. 요소가 4개이므로 어떤 입력이든 3번의 패스면 충분하다.

   </details>

4. **2차원 리스트의 별칭:** `s = [[0] * 3] * 2` 다음에 `s[1][2] = 5`를 실행하면 `s`는 어떻게 되는가?

   <details>
   <summary>정답</summary>

   `[[0, 0, 5], [0, 0, 5]]`이다. 바깥의 `* 2`가 같은 행 리스트에 대한 참조를 두 번 담으므로, 한 행을 바꾸면 두 행이 함께 바뀐다.

   </details>

5. **딕셔너리:** `d = {"a": 1}`에서 `d.get("b", 0)`과 `d["b"]`의 결과를 각각 쓰라. `d["b"] = 2`를 실행하면 `d`는 어떻게 되는가?

   <details>
   <summary>정답</summary>

   `d.get("b", 0)`은 키 `"b"`가 없으므로 기본값 0을 돌려주고, `d["b"]`는 `KeyError`를 일으킨다. `d["b"] = 2`는 없는 키에 대입하므로 새 쌍이 추가되어 `{"a": 1, "b": 2}`가 된다.

   </details>

6. **UnboundLocalError:** `Lab_GlobalVariableAssignment.py`에서 `modify_global`의 `global_var = 20` 줄만 지우면 출력은 어떻게 바뀌는가?

   <details>
   <summary>정답</summary>

   함수 안에 대입이 없어지므로 `global_var`는 전역 변수로 찾아지고 오류가 나지 않는다. 출력은 `Accessing global variable: 10`, `Before modification: 10`, `After modification: 10`, `Accessing global variable: 10`의 네 줄이다.

   </details>
