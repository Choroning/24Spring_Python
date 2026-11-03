"""
@file    Lab_TwoDimensionalList.py
@brief   3행 5열 2차원 리스트를 만들고 입력값으로 채우기
@author  박철원 (Cheolwon Park)
@date    2024-05-16
"""

rows = 3
cols = 5

s = []
for row in range(rows):
    s += [[0]*cols]
#for i in range(r):
#    s.append([0]*5) 도 가능

print("s =", s)

for i in range(rows):
    for j in range(cols):
        data=int(input("추가할 값을 입력하세요:"))
        s[i][j] = data
#자동으로 0~14로 채우려면
#s[i][j]=n
#n+=1 을 for i, for j 안에 채우면 됨

print("s =", s)
