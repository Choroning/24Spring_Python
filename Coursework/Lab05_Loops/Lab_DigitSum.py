"""
@file    Lab_DigitSum.py
@brief   네 자리 정수의 각 자리 숫자를 for문으로 분리하여 합을 계산
@author  박철원 (Cheolwon Park)
@date    2024-04-04
"""

num = int(input("네 자리 숫자를 입력하세요: "))

#S1 = num // 1000
#R = num - (1000*S1)
#S2 = R // 100
#R = R - (100*S2)
#S3 = R // 10
#R = R - (10 * S3)
#S4 = R
#nums = S1 + S2 + S3 + S4

nums = 0
for i in [3, 2, 1, 0]:
    S1 = num // (10 ** i)  # 10의 i제곱 자리의 숫자
    num -= S1 * (10 ** i)  # 그 자리의 값을 빼서 아래 자리만 남김
    nums += S1

print("각 자리 숫자의 합:", nums)
