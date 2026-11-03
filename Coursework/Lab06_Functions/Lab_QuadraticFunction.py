"""
@file    Lab_QuadraticFunction.py
@brief   이차식 f(x)=x**2+2x+3을 함수로 정의하고 반환값을 사용
@author  박철원 (Cheolwon Park)
@date    2024-04-15
"""

#f(x)=a*x**2+b*x+c를 함수로 정의하기

def f(x):
    y=1*x**2+2*x+3
    return y #리턴 안하면 그냥 사라짐

##main##
x=10
y=1*x**2+2*x+3 #함수 속의 y와 메인문의 y는 다름(지역변수이므로)
f(x) #정의한 함수 이름을 적어주면 그냥 메인문에서 호출한 것이 됨
z=f(x)

#x를 따로 10이라고 정의하지 않고 그냥 f(10)으로 해도 됨

print(y)
print(1*x**2+2*x+3)
print(f(x))
print(z)
