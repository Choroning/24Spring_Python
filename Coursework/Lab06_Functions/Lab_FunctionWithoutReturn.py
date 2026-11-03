"""
@file    Lab_FunctionWithoutReturn.py
@brief   반환하지 않고 함수 안에서 결과를 출력하는 함수
@author  박철원 (Cheolwon Park)
@date    2024-04-15
"""

def f(x):
    y=1*x**2+2*x+3
    print(y)
    #return y

##main##
x=10

f(x) #그냥 이렇게 쓰면 print됨(리턴 여부와 관계 없음)
