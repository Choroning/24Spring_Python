"""
@file    Lab_CoinToss.py
@brief   random.randrange(2)로 0과 1 중 하나를 뽑아 맞히는 동전 던지기 게임
@author  박철원 (Cheolwon Park)
@date    2024-03-28
"""

import random

print("동전 던지기 게임을 시작합니다.")
coin = random.randrange(2)

answer = int(input("나온 숫자는 0과 1 중 무엇일까요?"))

if answer == coin :
             print("맞았습니다.")
else :
    print("틀렸습니다.")

print("게임이 종료되었습니다.")
