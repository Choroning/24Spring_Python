"""
@file    Lab_DictionaryMethods.py
@brief   딕셔너리의 keys(), values(), items(), get(), update() 메서드
@author  박철원 (Cheolwon Park)
@date    2024-05-30
"""

person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

keys = person.keys()
print(keys)

values = person.values()
print(values)

items = person.items()
print(items)

name = person.get("name")
# person["name"] 도 가능!
print(name)

person.update({"age": 31, "job": "Developer"})
print(person)
