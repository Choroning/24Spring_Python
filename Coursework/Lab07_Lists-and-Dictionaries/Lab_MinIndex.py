"""
@file    Lab_MinIndex.py
@brief   리스트에서 가장 작은 값의 인덱스 찾기
@author  박철원 (Cheolwon Park)
@date    2024-05-09
"""

list_=[1, 3, 67, 8, 3, 5, -1, 3, -9, 10]
temp=list_[0]

#가장 작은 값의 인덱스 구하기
min=0
for i in range (len(list_)):
    if list_[i] < temp:
        min=i
        temp=list_[i]

print("min index: ", min)
