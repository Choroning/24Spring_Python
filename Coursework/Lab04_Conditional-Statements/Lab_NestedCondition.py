"""
@file    Lab_NestedCondition.py
@brief   기준값을 변수에 담아 and 조건과 중첩 if문으로 같은 판별을 두 번 수행
@author  박철원 (Cheolwon Park)
@date    2024-03-28
"""

a=int(input("a:"))
a_th=10
h=float(input("h"))
h_th=165

if ((a>=a_th) and (h>=h_th)) :
    print("ok")
else :
    print("no")

if (a>=a_th) :
    if (h>=h_th) :
        print("ok")
    else :
        print("no")
else :
    print("no")
