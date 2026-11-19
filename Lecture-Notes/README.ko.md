# 강의 노트

[레포지토리 안내](../README.ko.md) | [English](README.md) | [한국어](README.ko.md)

> **최종 수정일:** 2026-11-19

## 강의 단원

| 단원 | 주제 | 문서 |
|:-----|:-----|:-----|
| [1강 컴퓨터 구조와 파이썬 소개](Lec01_Computer-Architecture-and-Introduction-to-Python/) | 폰 노이만 구조, 중앙처리장치의 산술논리장치와 제어장치, 명령어의 인출, 해독, 실행, 저장, 기억장치의 계층, 입출력 장치와 버스, 운영체제와 애플리케이션, 컴파일 방식과 인터프리트 방식의 프로그래밍 언어, 파이썬의 활용 분야, 비트와 바이트, 2진수와 16진수, 문자 코드와 UTF-8, 바이트코드와 `dis`, 구문 오류와 실행 시간 오류, 트레이스백 | [강의 노트](Lec01_Computer-Architecture-and-Introduction-to-Python/Concepts_Lecture.ko.md) |
| [2강 파이썬 시작하기](Lec02_Getting-Started-with-Python/) | 프로그램과 프로그래밍 언어, 파이썬의 특징, 파이썬 설치와 IDLE, 대화형 모드와 스크립트 모드, `print()` 함수, 터틀 그래픽, 변수와 이름 규칙, 산술 연산자와 나머지 연산자, `input()`을 이용한 정수와 문자열 입력, 복합 대입 연산자, 주석, 연산자 우선순위, 다중 대입과 값의 교환, 정수와 실수가 섞인 계산의 결과 자료형, `divmod()`, `ZeroDivisionError` | [강의 노트](Lec02_Getting-Started-with-Python/Concepts_Lecture.ko.md), [연습 문제](Lec02_Getting-Started-with-Python/Exercises.ko.md), [풀이](Lec02_Getting-Started-with-Python/Solutions.ko.md) |
| [3강 자료의 종류](Lec03_Data-Types/) | 파이썬의 자료형, 문자열, 자료형 변환, 문자열의 접합과 반복, `%` 연산자를 이용한 문자열 형식화, 인덱싱과 슬라이싱, 이스케이프 시퀀스, 터틀 그래픽의 문자열 입출력, 리스트의 기초, 객체, 이름, 참조, `is`와 `==`, 가변과 불변, 정수의 무한 정밀도, 부동소수점 오차와 `round()`의 짝수 반올림, f-문자열과 `format()`, 문자열 메서드, 증가값이 있는 슬라이싱 | [강의 노트](Lec03_Data-Types/Concepts_Lecture.ko.md), [연습 문제](Lec03_Data-Types/Exercises.ko.md), [풀이](Lec03_Data-Types/Solutions.ko.md) |
| [4강 조건문](Lec04_Conditional-Statements/) | 순차, 선택, 반복의 기본 제어 구조, 부울 자료형, 관계 연산자와 논리 연산자, `if-else`문과 들여쓰기, `if-elif-else`문, 중첩 `if`문, `random` 모듈의 난수, 조건문이 들어간 프로그램의 설계, `and`와 `or`의 반환값, 비교의 연결, 문자열의 사전식 비교, 조건부 식의 계산, 빠짐없고 겹치지 않는 조건, 드모르간의 법칙으로 조건 부정 | [강의 노트](Lec04_Conditional-Statements/Concepts_Lecture.ko.md), [연습 문제](Lec04_Conditional-Statements/Exercises.ko.md), [풀이](Lec04_Conditional-Statements/Solutions.ko.md) |
| [5강 반복문](Lec05_Loops/) | `for`문과 `range()`, 문자열과 리스트의 순회, 합과 곱의 누적, `while`문과 무한 루프, `for`문과 `while`문의 변환, 중첩 반복, `break`와 `continue`, 반복문의 `else` 절, `range` 객체의 성질, `enumerate()`, 개수와 최댓값의 누적, 반복 횟수를 모르는 `while`문의 추적, `else` 절과 `break`의 추적, 깃발 변수 | [강의 노트](Lec05_Loops/Concepts_Lecture.ko.md), [연습 문제](Lec05_Loops/Exercises.ko.md), [풀이](Lec05_Loops/Solutions.ko.md) |
| [6강 함수](Lec06_Functions/) | 함수의 정의와 호출, 인수와 매개변수, 반환값, 지역 변수와 전역 변수, `global`문, 상수, 여러 값의 반환, 디폴트 인수와 키워드 인수, 무명 함수(`lambda`), 모듈, 독스트링, LEGB 규칙과 중첩 함수, `nonlocal`문, 가변 객체를 기본값으로 쓸 때의 문제, 가변 길이 인수(`*args`, `**kwargs`) | [강의 노트](Lec06_Functions/Concepts_Lecture.ko.md), [연습 문제](Lec06_Functions/Exercises.ko.md), [풀이](Lec06_Functions/Solutions.ko.md) |
| [7강 리스트와 딕셔너리](Lec07_Lists-and-Dictionaries/) | 리스트의 인덱싱과 슬라이싱, 요소의 추가와 삭제, 탐색과 정렬, 리스트 컴프리헨션, 2차원 리스트, 튜플, 시퀀스 자료형, 별칭과 얕은 복사, 깊은 복사, 함수에 객체 참조 전달, 세트, 딕셔너리, 정렬의 `key`와 안정 정렬, 해시 가능성과 딕셔너리의 키, 세트 컴프리헨션, `frozenset`, 딕셔너리 뷰와 순회 중의 변경 | [강의 노트](Lec07_Lists-and-Dictionaries/Concepts_Lecture.ko.md), [연습 문제](Lec07_Lists-and-Dictionaries/Exercises.ko.md), [풀이](Lec07_Lists-and-Dictionaries/Solutions.ko.md) |
| [8강 클래스와 객체](Lec08_Classes-and-Objects/) | 병렬 리스트와 정렬 함수, 객체 지향 프로그래밍, 클래스와 인스턴스, 인스턴스 변수와 메서드, `self`, 생성자 `__init__()`, `__str__()`, 정보 은닉과 이름 맹글링, 접근자와 설정자, 클래스 변수, `__repr__()`, `__eq__()`와 `__len__()`, 메서드 정의의 흔한 실수 | [강의 노트](Lec08_Classes-and-Objects/Concepts_Lecture.ko.md), [연습 문제](Lec08_Classes-and-Objects/Exercises.ko.md), [풀이](Lec08_Classes-and-Objects/Solutions.ko.md) |

## 보충 단원

[진도 표](../Course-Information.ko.md#5-주차별-계획-및-진도)의 12주차, 13주차, 15주차에 계획되었지만 수업에서 진행하지 않은 상속과 다형성, 파일과 예외 처리, 재귀를 파이썬 공식 문서를 따라 보충한 단원입니다.

| 단원 | 주제 | 문서 |
|:-----|:-----|:-----|
| [9강 상속과 다형성](Lec09_Inheritance-and-Polymorphism/) | 상위 클래스와 하위 클래스, 속성 탐색의 순서, 메서드 재정의와 `super()`, 동적 디스패치, 다형성과 덕 타이핑, `isinstance()`와 `issubclass()`, 다중 상속과 MRO(C3 선형화), 협력적 `super()`, 추상 기반 클래스(`abc`), 상속과 합성, 연산자 오버로딩과 특수 메서드, `__bool__()`과 진릿값, `NotImplemented`와 반사 연산 | [강의 노트](Lec09_Inheritance-and-Polymorphism/Concepts_Lecture.ko.md), [연습 문제](Lec09_Inheritance-and-Polymorphism/Exercises.ko.md), [풀이](Lec09_Inheritance-and-Polymorphism/Solutions.ko.md) |
| [10강 파일 입출력](Lec10_File-Input-and-Output/) | 텍스트 파일과 이진 파일, 문자 인코딩(UTF-8, cp949)과 인코딩 불일치, `open()`의 모드와 파일 객체, `with`문, 상대 경로와 작업 폴더, `read()`, `readline()`, 파일 객체의 순회, `write()`와 `print(file=)`, 줄바꿈 변환과 버퍼링, 이진 파일과 `seek()`, `tell()`, `pathlib`, `csv`, `json` | [강의 노트](Lec10_File-Input-and-Output/Concepts_Lecture.ko.md), [연습 문제](Lec10_File-Input-and-Output/Exercises.ko.md), [풀이](Lec10_File-Input-and-Output/Solutions.ko.md) |
| [11강 예외 처리](Lec11_Exception-Handling/) | 구문 오류와 예외, 트레이스백 읽기, 예외 객체, `try`, `except`, `else`, `finally`, 예외의 전달, 예외 클래스의 계층과 `except`절의 순서, `raise`와 다시 일으키기, 사용자 정의 예외, 예외의 연결, `assert`문, EAFP와 LBYL, 반환값과 예외, 컨텍스트 관리자와 `with`문 | [강의 노트](Lec11_Exception-Handling/Concepts_Lecture.ko.md), [연습 문제](Lec11_Exception-Handling/Exercises.ko.md), [풀이](Lec11_Exception-Handling/Solutions.ko.md) |
| [12강 재귀](Lec12_Recursion/) | 기저 사례와 재귀 사례, 호출 스택과 스택 프레임, 재귀적으로 정의되는 구조, 거듭제곱, 회문과 최대공약수, 중첩 리스트, 피보나치 수와 호출 횟수, 메모이제이션과 `functools.lru_cache`, 이진 탐색, 순열, 하노이의 탑, 병합 정렬, 재귀 깊이의 한도와 `RecursionError`, 꼬리 재귀와 반복 | [강의 노트](Lec12_Recursion/Concepts_Lecture.ko.md), [연습 문제](Lec12_Recursion/Exercises.ko.md), [풀이](Lec12_Recursion/Solutions.ko.md) |
