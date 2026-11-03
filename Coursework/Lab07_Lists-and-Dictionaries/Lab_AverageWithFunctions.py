"""
@file    Lab_AverageWithFunctions.py
@brief   다섯 수를 입력받아 평균을 구하는 코드를 함수로 나누기
@author  박철원 (Cheolwon Park)
@date    2024-05-23
"""

'''num = []
for i in range(5):
    num.append(int(input(":")))

sum_=0
for j in num: #num 리스트의 원소 중 하나가 들어감
    sum_ += j

avg = sum_ / 5
print(avg)
'''
#위 코드를 함수를 이용하여 작성

num=[]
def insert_():
    for i in range(5):
        num.append(int(input(":")))

def avg_():
    sum_ = 0
    for j in num:
        sum_ += j
    avg=sum_/5
    print(avg)

def main():
    insert_()
    avg_()

main()
