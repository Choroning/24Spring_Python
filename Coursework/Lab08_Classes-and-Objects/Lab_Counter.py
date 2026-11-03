"""
@file    Lab_Counter.py
@brief   생성자 없이 reset()으로 인스턴스 변수를 만드는 Counter 클래스
@author  박철원 (Cheolwon Park)
@date    2024-05-30
"""

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
