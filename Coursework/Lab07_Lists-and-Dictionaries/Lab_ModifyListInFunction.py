"""
@file    Lab_ModifyListInFunction.py
@brief   함수로 리스트의 첫 원소를 바꾸는 두 방법
@author  박철원 (Cheolwon Park)
@date    2024-05-20
"""

def func2(list):
    list[0] = 99

values = [0,1,1,2,3,5,8]
print(values)
func2(values)
print(values)

# 또는

def func1(list):
    return 99

value = [0,1,1,2,3,5,8]
print(value)
value[0] = func1(value)
print(value)
