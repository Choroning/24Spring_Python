"""
@file    Lab_MainFunction.py
@brief   제곱 함수를 정의하고 main() 함수에서 호출
@author  박철원 (Cheolwon Park)
@date    2024-04-29
"""

## main ##
'''
a=int(input('a:'))
b=a**2
print(b)
'''
def s(x): #함수를 꼭 활용하기 전 작성
    y=x**2
    return y

## main ##
def main():
    a=int(input('a:'))
    b=s(a)
    print(b)
    print(s(a))

main()
