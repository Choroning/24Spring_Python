"""
@file    Lab_ListType.py
@brief   여러 방법으로 만든 리스트의 자료형 확인
@author  박철원 (Cheolwon Park)
@date    2024-05-09
"""

#<class 'list'>라고 출력되는 것들
a=[]
print(type(a))

b=list()
print(type(b))

c=[1,2,'4']
print(type(c))

d=[1,2,3,c] #c가 존재하므로 오류 발생 X
print(type(d)) #리스트 안에 리스트가 존재할 수 있음
