"""
@file    Lab_AgeHeightCheck.py
@brief   나이와 키가 모두 기준 이상인지 and 연산자로 판별
@author  박철원 (Cheolwon Park)
@date    2024-03-28
"""

a = int(input("a: "))
h = float(input("h: "))

if a  >= 10 and h >= 165 :
    print("ok")

else :
    print("no")

# 10과 165를 변수에 담아서 if문에서 대치 가능
# if문 속에 다시 if문이 종속될 수 있음
#   ㄴ if( if( ~ ) else( ~ ) ) else ( ~ ) 구조
