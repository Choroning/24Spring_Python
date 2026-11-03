"""
@file    Lab_CounterAccessors.py
@brief   접근자 get()과 설정자 set()을 둔 Counter 클래스
@author  박철원 (Cheolwon Park)
@date    2024-06-03
"""

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
