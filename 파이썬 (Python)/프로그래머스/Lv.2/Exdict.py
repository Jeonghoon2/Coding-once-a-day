#  회사 쇼핑몰 고객의 아이디에 부여된 마일리지 포인트를 딕셔너리에 저장하여 관리하고자 한다.
#   다음 물음에 답하시오.  (1번~4번 문제)

def solution(members):
    users = dict
    point = []

    for member in members:
        user, point = member[0], member[1]
        users[user] = point

    for i in users:
        print(i)

solution([{"kin","23123"},{"m","23523"}])
