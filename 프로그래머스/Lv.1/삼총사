import itertools as it

def solution(number):
    answer = 0
    li = it.combinations(number,3)

    for i in li:
        if(sum(i) == 0):
            answer +=1

    return answer

print(solution([-3, -2, -1, 0, 1, 2, 3]))