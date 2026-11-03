"""
@file    Lab_MultipleReturnValues.py
@brief   return 문 하나로 두 값을 함께 반환
@author  박철원 (Cheolwon Park)
@date    2024-04-15
"""

def f(x):
    y=1*x**2+2*x+3
    return y,x #C언어는 리턴값 2개 이상이 불가능

## main ##
y, x = f(10)
print(y, x)
