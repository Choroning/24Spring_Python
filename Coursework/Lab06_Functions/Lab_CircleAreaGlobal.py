"""
@file    Lab_CircleAreaGlobal.py
@brief   global 선언으로 함수 안에서 전역 변수에 원의 넓이를 저장
@author  박철원 (Cheolwon Park)
@date    2024-05-02
"""

def calculate_area(radius):
    global area
    area = 3.14*radius**2
    return

area=0
r=float(input("원의 반지름: "))
calculate_area(r)
print(area)
