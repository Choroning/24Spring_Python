"""
@file    Lab_Continue.py
@brief   i가 5일 때 continue로 출력을 건너뛰기
@author  박철원 (Cheolwon Park)
@date    2024-04-11
"""

for i in range(10):
    if i == 5: continue  # i가 5일 때 다음 문장을 실행하지 않고 넘어감
    print(i)
print("End of Program")
