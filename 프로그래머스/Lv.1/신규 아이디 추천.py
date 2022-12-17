from hashlib import new
import re


def oneStep(new_id):
    new_id = new_id.lower()
    return new_id

# 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
def twoStep(new_id):
    return re.sub(r"[^a-z0-0-_.]","",new_id)

# new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
def threeStep(new_id):
    while new_id.find("..") == 0:
        new_id = new_id.replace("..",".")
    return new_id

# new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
def fourStep(new_id):
    if new_id[:1] == '.':
        new_id = new_id[1:]
    if new_id[len(new_id)-1:] == '.':
        new_id = new_id[:-1]
    return new_id

def solution(new_id):

    new_id=fourStep(threeStep(twoStep(oneStep(new_id))))

    answer = new_id
    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))