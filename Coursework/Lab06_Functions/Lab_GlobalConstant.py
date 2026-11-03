"""
@file    Lab_GlobalConstant.py
@brief   전역 상수 PI를 사용하는 원의 넓이 함수와 main() 함수
@author  박철원 (Cheolwon Park)
@date    2024-05-02
"""

PI=3.14159265358979 #전역상수

def area_c(r):
    return PI*r**2

def main():
    r=float(input("r:"))
    print(area_c(r))

main()
