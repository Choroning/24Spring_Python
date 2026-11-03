"""
@file    library_seat_reservation.py
@brief   세종학술정보원 열람실 3곳의 좌석을 예약하는 콘솔 프로그램 (2024-04-18 자율 발표)
@author  박철원 (Cheolwon Park)
@date    2024-04-17
"""

import random

seat1 = ["○", "○", "○", "○", "○", "○", "○", "○"]
seat2 = ["○", "○", "○", "○", "○", "○", "○", "○"]
seat3 = ["○", "○", "○", "○", "○", "○", "○", "○"]

while True:
    print("=======================================================")
    print("            [ 세종학술정보원 열람실 예약 시스템 ]\n")
    print("   제1열람실 ", seat1)
    print("   제2열람실 ", seat2)
    print("   제3열람실 ", seat3)
    print("=======================================================")
    print("                 시스템을 종료하시려면 성명란에 '종료'를 입력하세요.\n")

    username = input("예약자 성명을 입력해주세요: ")
    if (username == '종료'):
        break
    userid = int(input("예약자 학번을 입력해주세요: "))
    libnum = int(input("예약하실 열람실을 선택해주세요(1~3): "))
    if (libnum == 1):
        print("제1열람실을 선택하였습니다.")
        print("예약하실 좌석 번호(1~8)를 입력해주세요.")
        select = int(input("0을 입력하면 무작위로 배정됩니다: "))
        if (select == 0):
            select = random.randint(1, 8)
        elif (select < 0 or select > 8):
            print("유효하지 않은 좌석 번호입니다. 다시 한 번 확인해주세요.")
            continue
        time = int(input("이용하실 시간을 입력해주세요: "))
        if seat1[select-1] == "●":
            print("좌석이 이미 사용 중입니다. 다른 좌석을 선택해주세요.")
            continue
        else:
            seat1[select-1] = "●"
            print("\n[ 예약자 정보 ]")
            print("성명: ", username)
            print("학번: ", userid, "\n")
            print(select, "번 좌석이", time, "시간 예약되었습니다.")
            print("좌석예약 후 10분 이내에 입실확인하시기 바랍니다.")
            print("1. 앱 실행 및 블루투스 활성화 후 인증")
            print("2. 키오스크를 통한 학생증 인증\n")
    elif (libnum == 2):
        print("제2열람실을 선택하였습니다.")
        print("예약하실 좌석 번호(1~8)를 입력해주세요.")
        select = int(input("0을 입력하면 무작위로 배정됩니다: "))
        if (select == 0):
            select = random.randint(1, 8)
        elif (select < 0 or select > 8):
            print("유효하지 않은 좌석 번호입니다. 다시 한 번 확인해주세요.")
            continue
        time = int(input("이용하실 시간을 입력해주세요: "))
        if seat2[select-1] == "●":
            print("좌석이 이미 사용 중입니다. 다른 좌석을 선택해주세요.")
            continue
        else:
            seat2[select-1] = "●"
            print("\n[ 예약자 정보 ]")
            print("성명: ", username)
            print("학번: ", userid, "\n")
            print(select, "번 좌석이", time, "시간 예약되었습니다.")
            print("좌석예약 후 10분 이내에 입실확인하시기 바랍니다.")
            print("1. 앱 실행 및 블루투스 활성화 후 인증")
            print("2. 키오스크를 통한 학생증 인증\n")
    elif (libnum == 3):
        print("제3열람실을 선택하였습니다.")
        print("예약하실 좌석 번호(1~8)를 입력해주세요.")
        select = int(input("0을 입력하면 무작위로 배정됩니다: "))
        if (select == 0):
            select = random.randint(1, 8)
        elif (select < 0 or select > 8):
            print("유효하지 않은 좌석 번호입니다. 다시 한 번 확인해주세요.")
            continue
        time = int(input("이용하실 시간을 입력해주세요: "))
        if seat3[select-1] == "●":
            print("좌석이 이미 사용 중입니다. 다른 좌석을 선택해주세요.")
            continue
        else:
            seat3[select-1] = "●"
            print("\n[ 예약자 정보 ]")
            print("성명: ", username)
            print("학번: ", userid, "\n")
            print(select, "번 좌석이", time, "시간 예약되었습니다.")
            print("좌석예약 후 10분 이내에 입실확인하시기 바랍니다.")
            print("1. 앱 실행 및 블루투스 활성화 후 인증")
            print("2. 키오스크를 통한 학생증 인증\n")
    else:
        print("유효하지 않은 열람실 번호입니다. 다시 한 번 확인해주세요.")
        continue
