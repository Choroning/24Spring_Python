"""
@file    Lab_SumToN.py
@brief   for문으로 1부터 입력한 정수까지의 합을 계산
@author  박철원 (Cheolwon Park)
@date    2024-04-08
"""

n = int(input("정수를 입력하시오: "))

plus = 0
for i in range(1, n+1):
    plus = plus + i  #입력한 값(n)까지의 합 구하기

print(n, "까지의 양의 정수를 모두 더하면", plus, "이다.")
