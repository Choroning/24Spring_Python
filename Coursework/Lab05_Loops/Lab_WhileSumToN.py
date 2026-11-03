"""
@file    Lab_WhileSumToN.py
@brief   while문으로 0부터 입력한 정수까지의 누적 합을 출력
@author  박철원 (Cheolwon Park)
@date    2024-04-08
"""

n = int(input("정수를 입력하시오: "))
Sum = 0

#for i in range(n+1):
#    print(i)
#    Sum += i

i = 0
while (i <= n):
    print(i)
    Sum += i
    print(Sum)
    i += 1
