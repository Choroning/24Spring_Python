"""
@file    Lab_SubjectCutoff.py
@brief   다섯 과목 점수 중 하나라도 40점 미만이면 과락으로 판별하고 평균을 출력
@author  박철원 (Cheolwon Park)
@date    2024-04-04
"""

kor = int(input("국어 점수: "))
eng = int(input("영어 점수: "))
his = int(input("한국사 점수: "))
se1 = int(input("선택과목1 점수: "))
se2 = int(input("선택과목2 점수: "))
ave = (kor + eng + his + se1 + se2) / 5

if (kor < 40 or eng < 40 or his < 40 or se1 < 40 or se2 < 40):  #조건 뒤집어서 and 사용도 가능
   print("과락")
else:
   print("과락 아님")
print("평균 점수: %f" %ave)

#아니면 int(input(~)) 하나마다 if문으로 판별할수도 있음

#if (kor < 40):
#    print("과락")
#else:
#    if (eng < 40):
#        print("과락")
#    else:
#        if (his < 40):
#            print("과락")
#        else:
#            if (se1 < 40):
#                print("과락")
#            else:
#                if (se2 < 40):
#                    print("과락")
#                else:
#                    print("과락 아님")
#print("평균 점수: %f" %ave)
