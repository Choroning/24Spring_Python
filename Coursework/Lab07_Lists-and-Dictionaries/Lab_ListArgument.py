"""
@file    Lab_ListArgument.py
@brief   함수에 전달한 리스트를 함수 안에서 바꾸면 호출한 쪽의 리스트도 바뀜
@author  박철원 (Cheolwon Park)
@date    2024-05-13
"""

# 리턴받지 않고 하는 함수
def f_c(list_):
    list_[0]=100

def f_c2(list_): # 이렇게 작성하지 않음.
    list_a[0]=1

##main##
list_a=[1,2,3,4,5]
f_c(list_a)
print(list_a)
f_c2(list_a)
print(list_a)
