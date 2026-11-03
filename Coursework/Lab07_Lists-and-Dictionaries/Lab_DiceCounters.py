"""
@file    Lab_DiceCounters.py
@brief   주사위를 1000번 던져 눈마다 변수 6개로 횟수를 세고 상대 빈도를 계산
@author  박철원 (Cheolwon Park)
@date    2024-05-23
"""

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
