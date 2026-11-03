"""
@file    Lab_CounterConstructor.py
@brief   생성자 __init__()으로 인스턴스 변수를 초기화하는 Counter 클래스
@author  박철원 (Cheolwon Park)
@date    2024-05-30
"""

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
