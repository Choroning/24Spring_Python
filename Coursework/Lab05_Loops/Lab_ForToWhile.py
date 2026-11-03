"""
@file    Lab_ForToWhile.py
@brief   1부터 10까지의 합을 구하는 for문을 while문으로 바꾸기
@author  박철원 (Cheolwon Park)
@date    2024-04-11
"""

#sum = 0
#for i in range(1,11,1):  <- 1부터 11보다 작은 때까지 1씩 증가(1~10)
#   sum = sum + i

#while문으로 바꾸기

Sum = 0
i = 1
while (i < 11):
    Sum += i
    i+=1
print(Sum)
