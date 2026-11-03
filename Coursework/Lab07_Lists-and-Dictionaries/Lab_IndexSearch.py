"""
@file    Lab_IndexSearch.py
@brief   입력한 값의 인덱스를 반복문, 직접 만든 함수, index()로 찾기
@author  박철원 (Cheolwon Park)
@date    2024-05-09
"""

def index_(list_, g):
    f_index=0
    for i in range(len(h)):
        if g==h[i]:
            f_index=i
    return f_index

h=["아","토","헐","스","헐"]
g=input("i:")
for i in range(len(h)):
    if g==h[i]:
        print(i)

print(index_(h,g))
print(h.index(g))

#수식에 따라 "헐"이 두개일때 모두 출력하거나
#마지막 값만 출력하게 됨
