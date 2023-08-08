import itertools

def solution(numbers):
    answer = []
    tmp = itertools.permutations(numbers,2)
    for i in tmp:
        answer.append(sum(i))
    return list(set(answer))

print(solution([5,0,2,7]))