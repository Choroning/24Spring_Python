"""
@file    Lab_Scholarship.py
@brief   점수가 90점을 넘으면 합격과 장학금 안내를 출력하는 if-else문
@author  박철원 (Cheolwon Park)
@date    2024-03-28
"""

score = float(input("점수를 입력하세요."))

if score > 90 :
    print("합격입니다.")
    print("장학금도 받을 수 있습니다.")

else :
    print("에휴")
