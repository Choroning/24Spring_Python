"""
@file    Lab_ItemLookup.py
@brief   입력한 물건 이름을 키로 딕셔너리에서 개수를 조회
@author  박철원 (Cheolwon Park)
@date    2024-05-23
"""

items = {"커피음료": 7, "펜": 3, "종이컵": 2, "우유": 1, "콜라": 4, "책": 5}

item = input("물건의 이름을 입력하시오: ")
print(items[item])
