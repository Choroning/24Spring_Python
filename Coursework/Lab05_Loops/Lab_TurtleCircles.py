"""
@file    Lab_TurtleCircles.py
@brief   거북이 그래픽으로 원 12개를 30도씩 돌려 그리기
@author  박철원 (Cheolwon Park)
@date    2024-04-08
"""

import turtle
t = turtle.Turtle()

for count in range(12):
    t.circle(100)
    t.left(360/12)
