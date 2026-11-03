"""
@file    Lab_DiceList.py
@brief   주사위를 1000번 던져 눈마다 리스트 원소로 횟수를 세고 상대 빈도를 계산
@author  박철원 (Cheolwon Park)
@date    2024-05-23
"""

#주사위 1000번 던져서 각 숫자가 나올 확률 (2)
import random

pro_=[0]*6

for i in range(1000):
    num=random.randint(1, 6)
    pro_[num-1] += 1

for i in range(6):
    print("주사위가", i+1, "인 확률은", pro_[i] / 1000)
