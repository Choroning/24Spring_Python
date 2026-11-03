"""
@file    Lab_DictionaryBasics.py
@brief   딕셔너리 값의 조회, 변경, 추가, 삭제
@author  박철원 (Cheolwon Park)
@date    2024-05-27
"""

person = {
    "name": "John",
    "age": 30,
    "city": "New York",
}

print(person["name"])
print(person["age"])

# 값 변경
person["age"] = 31
print(person["age"])

# 새로운 키-값 쌍 추가
person["job"] = "Developer"
print(person)

#키-값 쌍 삭제
del person["city"]
print(person)

# 키를 인덱스처럼 사용할 수 있는 것이
# 리스트와의 큰 차이
