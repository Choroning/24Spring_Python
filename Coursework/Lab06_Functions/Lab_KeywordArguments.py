"""
@file    Lab_KeywordArguments.py
@brief   키워드 인수와 위치 인수로 같은 함수를 호출하여 비교
@author  박철원 (Cheolwon Park)
@date    2024-05-02
"""

def calc(x, y, z):
    print(x)
    print(y)
    print(z)

#입력창에 calc(y=20, x=10, z=30)
#calc(20, 10, 30)과 결과 비교

#키워드 인수는 인수의 이름을
#명시적으로 지정해서 전달하는 방법

## main ##
calc(y=20, x=10, z=30)
calc(20, 10, 30)
