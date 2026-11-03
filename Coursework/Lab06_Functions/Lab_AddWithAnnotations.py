"""
@file    Lab_AddWithAnnotations.py
@brief   타입 힌트를 붙인 함수에서 합과 인수를 함께 반환
@author  박철원 (Cheolwon Park)
@date    2024-04-18
"""

'''x=int(input("x:"))
y=int(input("y:"))
z=x+y
print(z)'''

def add(x : int,y : int) -> (int, int) :

# def add(x,y): 도 가능
# def add(x : int,y : int) -> int : 도 가능

    #x=int(input("x:"))
    #y=int(input("y:"))
    z=x+y
    #print(z)
    return z,x

## main ##
x=int(input("x:"))
y=int(input("y:"))
z,x=add(x,y)
# z=add(x,y)로 받으면 z에 튜플 (합, x)가 저장된다(합만 받으려면 return z로 쓴다)
print(z)
print(x)
