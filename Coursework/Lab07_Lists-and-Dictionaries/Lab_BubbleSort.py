"""
@file    Lab_BubbleSort.py
@brief   난수 5개를 버블 정렬로 오름차순 정렬
@author  박철원 (Cheolwon Park)
@date    2024-05-13
"""

import random
datalist=[]

for i in range (0, 5, 1):
    datalist.append(random.randint(1, 100))

print(datalist)

for j in range(len(datalist)-1): # 비효율적인 방법
    for i in range(len(datalist)-1):
        if datalist[i] > datalist[i+1]:
            temp=datalist[i]
            datalist[i]=datalist[i+1]
            datalist[i+1]=temp
    print(datalist)

print(datalist)
