"""
@file    Lab_NumberGuess.py
@brief   1~10의 난수와 입력값을 if-elif-else로 비교하는 숫자 맞히기
@author  박철원 (Cheolwon Park)
@date    2024-04-04
"""

import random
val = random.randint(1,10)
guess = int(input("정수를 입력하시오(0~10): "))

if guess > val:  #조건식 괄호의 삽입여부는 상관없음
    print("입력한 값보다 작습니다.")
elif guess < val:
    print("입력한 값보다 큽니다.")
else:
    print("정답입니다.")
#print("답은" + str(val) + "입니다.")
#print("답은 %s입니다." %val)
print("답은 %d입니다." %val)
