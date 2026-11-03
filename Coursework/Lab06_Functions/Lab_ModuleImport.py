"""
@file    Lab_ModuleImport.py
@brief   직접 만든 모듈 Lab_AddMinusModule을 import하여 함수 호출
@author  박철원 (Cheolwon Park)
@date    2024-05-02
"""

import Lab_AddMinusModule

a=10
b=20
Lab_AddMinusModule.add(a,b)
Lab_AddMinusModule.minus(a,b)

#모듈명이 Lab_AddMinusModule로 너무 길 때는
#import Lab_AddMinusModule as t로 작성하면
#t.add(a,b)처럼 사용할 수 있음

#또는 from Lab_AddMinusModule import *로
#작성하면 모듈명 빼고 그냥
#add(a,b) 사용 가능하지만 이름이 겹칠 수 있으므로 가능하면 쓰지 않음
