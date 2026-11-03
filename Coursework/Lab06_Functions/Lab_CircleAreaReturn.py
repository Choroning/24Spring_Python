"""
@file    Lab_CircleAreaReturn.py
@brief   반지름을 받아 원의 넓이를 반환하는 함수
@author  박철원 (Cheolwon Park)
@date    2024-04-29
"""

def calculate_area(radius):
    area=3.14*radius**2
    return area

area=0
r=float(input("원의 반지름: "))
area=calculate_area(r)
print(area)
