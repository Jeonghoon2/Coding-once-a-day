from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    orders.sort(key=len)

    # 지정된 코스
    for c in course:
        temp = []

        for order in orders:
            combo = combinations(sorted(order), c)
            temp += combo
        counter = Counter(temp)

        # Counter 중 가장 큰 Counter를 가지고 있는 조합
        if len(counter) != 0 and max(counter.values()) != 1:
            answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]

    return sorted(answer)


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]
print(solution(orders, course))
