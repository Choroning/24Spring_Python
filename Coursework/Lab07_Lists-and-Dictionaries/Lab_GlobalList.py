"""
@file    Lab_GlobalList.py
@brief   함수 안에서 전역 리스트에 원소를 추가
@author  박철원 (Cheolwon Park)
@date    2024-05-16
"""

global_list = [1, 2, 3, 4]

def modify_global_list():
    global global_list
    print("Before modification:", global_list)
    global_list.append(5)
    global_list.extend([6, 7])
    print("After modification:", global_list)

def access_global_list():
    print("Accessing global variable:", global_list)

# 함수 실행
access_global_list()
modify_global_list()
access_global_list()
