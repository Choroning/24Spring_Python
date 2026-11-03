"""
@file    Lab_AbsoluteValue.py
@brief   절댓값 함수와 입력을 받아 그 함수를 호출하는 함수
@author  박철원 (Cheolwon Park)
@date    2024-04-18
"""

'''x = int(input("x:"))

if (x < 0):
    x = -x

print(x)'''


def abs(x): # 절댓값 함수
    if (x < 0):
        x = -x
    return x

def abs2(): # 값을 입력받아 abs(x)를 돌려서 출력하는 함수
    x = int(input("x:"))
    print(abs(x))

## main ##
abs2()
