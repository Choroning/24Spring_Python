"""
@file    Lab_ListOperations.py
@brief   리스트 항목의 변경, 추가, 삭제, pop, in, index와 탐색
@author  박철원 (Cheolwon Park)
@date    2024-05-09
"""

#리스트 항목 변경법
print("리스트 항목 변경법")
heroes=["아이언맨","토르"]
print(heroes)

#변경
print("\n변경")
heroes[1]="닥터 스트레인지"
print(heroes)

#추가
print("\n추가")
heroes.append("스파이더맨")
heroes.insert(2, "배트맨") #위치(인덱스) 지정
print(heroes)

#삭제
print("\n삭제")
heroes.remove("닥터 스트레인지")
del heroes[0] #위치(인덱스) 지정
print(heroes)

#pop은 리스트에서 마지막 항목을 삭제함
print("\npop 활용")
heroes9=["아이언맨","토르","헐크","스칼렛 위치"]
last_hero=heroes9.pop()
print(last_hero)

#조건문 활용 예
print("\n조건문 활용 예")
if "슈퍼맨" in heroes:
    heroes.remove("슈퍼맨")

#탐색
heroes8=["아이언맨","토르","헐크","스칼렛 위치"]
print(heroes8.index("헐크"))

#index를 직접 구현
for i in range (len(heroes8)):
    if "헐크" in heroes8[i]:
        print("인덱스: ", i)

#입력받은 데이터의 인덱스 출력
heroes7=["아이언맨","토르","헐크","스칼렛 위치"]
ans=input("찾고자 하는 데이터: ")
for i in range(len(heroes7)):
    if ans == heroes7[i]:
        print(i)
