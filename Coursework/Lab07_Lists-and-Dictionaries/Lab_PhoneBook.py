"""
@file    Lab_PhoneBook.py
@brief   딕셔너리로 만든 전화번호부의 항목 추가와 조회
@author  박철원 (Cheolwon Park)
@date    2024-05-23
"""

pb = {}
pb["홍길동"] = "010-1234-5678"
print("1: ", pb)

pb2 = {"홍길동": "010-1234-5678"}
pb2["강감찬"] = "010-1234-5679"
print("2: ", pb2)

print("3: ", pb2["강감찬"])

print("4: 이 부분은 결과창에 한 줄씩 입력하면 나옴")
pb2.keys()
pb2.values()

print("5: ")
dict = {'Name': '홍길동', 'Age': 7, 'Class': '초급'}
print(dict['Name'])
print(dict['Age'])
