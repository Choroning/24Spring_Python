"""
@file    Lab_ListComprehension.py
@brief   for문과 리스트 함축으로 같은 리스트 만들기
@author  박철원 (Cheolwon Park)
@date    2024-05-13
"""

# 예시1
s=[]
for x in range(10):
    s.append(x**2)
print(s)

ss=[x**2 for x in range(10)] # 함축
print(ss)


# 예시2
sss=[]
for x in range(10):
    if x%2==0:
        sss.append(x**2)
print(sss)

ssss=[x**2 for x in range(10) if x%2==0] # 함축
print(ssss)
