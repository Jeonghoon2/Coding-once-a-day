# 행, 방향, 횟수 정보가 주어진다. ex) 2 0 3

import sys

sys.stdin = open("in1.txt", 'r')


def solution():
    n = int(input())

    arr = [list(map(int, input().split())) for _ in range(n)]

    c = int(input())

    rule = [list(map(int, input().split())) for _ in range(c)]

    for c, r, t in rule:
        from collections import deque

        tmp1 = deque(arr[c-1])
        for i in range(t):

            if r == 0:
                x = tmp1.popleft()
                tmp1.append(x)
            else:
                x = tmp1.pop()
                tmp1.appendleft(x)
        arr[c-1] = list(tmp1)

    s, e = 0, n
    ans = 0
    for i in range(n):
        tmp2 = []
        for j in range(s, e):
            tmp2.append(arr[i][j])

        ans += sum(tmp2)
        if i < n // 2:
            s += 1
            e -= 1
        else:
            s -= 1
            e += 1

    return ans


print(solution())
