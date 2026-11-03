"""
@file    Lab_ListCopy.py
@brief   대입으로 같은 리스트를 공유하는 경우와 list()로 복사하는 경우
@author  박철원 (Cheolwon Park)
@date    2024-05-16
"""

a=[1,2,3,4]
b=a
a[3]=1000
print(a)
print(b)

#리스트를 이렇게 복사하고 바꾸면
# a=[1,2,3,1000]
# b=[1,2,3,4]
#로 출력될 것이라고 예상할 수도 있지만
# a와 b가 같은 리스트 객체를 가리키므로 b도 [1,2,3,1000]으로 출력된다

b[3]=4
print(a)
print(b)

#따라서 복사할 때
c=list(b)
b[3]=10
print(b)
print(c)
#이렇게 복사해야 바뀐 값까지 복사되지 않음
