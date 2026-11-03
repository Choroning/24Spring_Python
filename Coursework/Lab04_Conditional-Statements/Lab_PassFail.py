"""
@file    Lab_PassFail.py
@brief   점수를 입력받아 60점 이상이면 합격, 미만이면 불합격을 출력
@author  박철원 (Cheolwon Park)
@date    2024-03-28
"""

score = float(input("점수를 입력하세요: "))

if score >= 60 :
    print("합격입니다.")

# if (score >= 60) :
# 괄호 삽입 가능

else :
    print("불합격입니다.")
