"""
@file    Lab_GlobalVariableAssignment.py
@brief   global 선언 없이 함수 안에서 전역 변수에 대입하면 생기는 UnboundLocalError
@author  박철원 (Cheolwon Park)
@date    2024-05-16
"""

global_var = 10

def modify_global():
    #global global_var
    print("Before modification:", global_var)
    global_var = 20
    print("After modification:", global_var)

def access_global():
    print("Accessing global variable:", global_var)

# 함수 실행
access_global()
try:
    modify_global()
except UnboundLocalError as e:
    print("UnboundLocalError:", e)
access_global()
