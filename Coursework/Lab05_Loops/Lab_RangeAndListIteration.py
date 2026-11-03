"""
@file    Lab_RangeAndListIteration.py
@brief   range()와 리스트로 같은 반복을 만들고 append()로 리스트를 채우기
@author  박철원 (Cheolwon Park)
@date    2024-04-08
"""

#for i in _____: => _____; range(s, stop, increase), list
#배웠던 내용 리뷰

for i in range(0,10,1):
    print(i)

for j in [0,1,2,3,4,5,6,7,8,9]:
    print(j)

a_list=[]
for i in range(0,10,1):
    a_list.append(i)
