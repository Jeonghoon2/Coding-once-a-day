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


def solution3(numbers, target):
    answer = 0

    def dfs(idx, cur_num):
        nonlocal answer
        if idx == len(numbers) - 1:
            for i in [1, -1]:
                num = numbers[idx]
                total = cur_num + num * i

                if total == target:
                    answer += 1
            return
        else:
            num = numbers[idx]
            for i in [1, -1]:
                dfs(idx + 1, cur_num + num * i)

    dfs(0, 0)

    return answer



print(solution3([4, 1, 2, 1], 2))
