"""
@file    Lab_DefaultArgument.py
@brief   기본값이 있는 매개변수(디폴트 인수)
@author  박철원 (Cheolwon Park)
@date    2024-05-02
"""

def greet(name, msg="별일없죠?"):
    print("안녕 ", name+', '+msg)

greet("영희")

#msg=" ~ "를 통해 디폴트 인수로 설정
#따로 매개변수에 대한 인자를 주지 않아도
#기본값을 출력함
