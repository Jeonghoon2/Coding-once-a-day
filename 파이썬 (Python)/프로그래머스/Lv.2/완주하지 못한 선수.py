# 시간 초과 발생
import collections


def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for i in completion:
        participant.remove(i)
    return participant[-1]

# 혹시 이거 되나?
def solution3(participant, completion):
    participant.sort()
    completion.sort()
    for p,c in zip(participant,completion):
        if p != c:
            return p
    return list(set(participant)-set(completion)).pop()


# 다른사람 풀이 Zip 사용
def solution2(participant, completion):
    participant.sort()
    completion.sort()
    for p,c in zip(participant,completion):
        if p != c:
            return p
    return participant.pop()

# 제일 간결
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

print(solution3(["leo", "kiki", "eden"],["eden", "kiki"]))