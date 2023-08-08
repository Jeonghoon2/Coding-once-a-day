def solution(numbers, target):
    sup = [0]
    for i in numbers:
        sub = []
        for j in sup:
            sub.append(j + i)
            sub.append(j - i)
        sup = sub
    return sup.count(target)


# BFS
from collections import deque

def solution2(numbers, target):
    answer = 0

    d = deque()
    d.append((numbers[0], 0))
    d.append((-1 * numbers[0], 0))

    while d:
        x, index = d.popleft()
        index += 1
        if index < len(numbers):
            d.append((x + numbers[index], index))
            d.append((x - numbers[index], index))
        else:
            if x == target:
                answer += 1

    return answer


print(solution2([1, 1, 1, 1, 1], 3))
