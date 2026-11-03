"""
@file    Lab_AttackAndHeal.py
@brief   체력을 가진 객체끼리 공격하고 회복하는 클래스
@author  박철원 (Cheolwon Park)
@date    2024-05-30
"""

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
