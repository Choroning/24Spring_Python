"""
@file    Lab_CounterPrivate.py
@brief   이름이 __로 시작하는 인스턴스 변수의 정보 은닉
@author  박철원 (Cheolwon Park)
@date    2024-06-03
"""

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
