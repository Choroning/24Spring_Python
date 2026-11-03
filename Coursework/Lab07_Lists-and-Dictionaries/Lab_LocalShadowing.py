"""
@file    Lab_LocalShadowing.py
@brief   함수 안의 지역 변수가 같은 이름의 전역 변수를 가리는 경우와 UnboundLocalError
@author  박철원 (Cheolwon Park)
@date    2024-05-16
"""

global_var = 10

def modify_global():
    #global global_var
    print("Before modification:",global_var)
    global_var = 20
    print("After modification:",global_var)

def access_global():
    global_var = 200
    print("Accessing global variable:",global_var)

# 함수 실행
access_global()
try:
    modify_global()
except UnboundLocalError as e:
    print("UnboundLocalError:", e)
access_global()
