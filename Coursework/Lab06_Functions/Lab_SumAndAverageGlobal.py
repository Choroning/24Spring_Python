"""
@file    Lab_SumAndAverageGlobal.py
@brief   global 선언으로 두 수의 합과 평균을 전역 변수에 저장
@author  박철원 (Cheolwon Park)
@date    2024-05-02
"""

def sumandavg(a, b):
    global sum, avg
    sum=a+b
    avg=(a+b)/2

sum=0 #주석처리해도 작동
avg=0 #주석처리해도 작동
a=50
b=60

sumandavg(a, b)
print("합=", sum)
print("평균=", avg)
