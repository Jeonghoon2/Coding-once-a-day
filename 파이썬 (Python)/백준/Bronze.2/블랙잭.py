# 첫째 줄에 카드의 개수 N(3 ≤ N ≤ 100)과 M(10 ≤ M ≤ 300,000)이 주어진다
# 둘째 줄에는 카드에 쓰여 있는 수가 주어지며, 이 값은 100,000을 넘지 않는 양의 정수이다.

from itertools import combinations


def solution(n, value, l):
    l = combinations(l, 3)
    max = 0
    for i in l:
        if max < sum(i) <= value:
            max = sum(i)

    return max



n, value = map(int, input().split())
l = list(map(int, input().split()))

print(solution(n, value, l))
