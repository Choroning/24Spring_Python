"""
@file    Lab_ModuleAlias.py
@brief   import ... as로 별칭을 붙인 모듈의 함수를 조합하여 호출
@author  박철원 (Cheolwon Park)
@date    2024-05-02
"""

import Lab_ArithmeticModule as t8

a=10
b=20
c=30

print(t8.add(a, t8.mul(b,c)))
