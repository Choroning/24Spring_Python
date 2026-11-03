"""
@file    Lab_PasswordCheck.py
@brief   올바른 암호가 입력될 때까지 반복하는 while문
@author  박철원 (Cheolwon Park)
@date    2024-04-08
"""

password = ""
while password != "pythonisfun":
    password = input("암호를 입력하시오: ")
print("로그인 성공")
