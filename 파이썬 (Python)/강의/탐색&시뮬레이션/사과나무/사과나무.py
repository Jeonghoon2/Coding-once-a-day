# 현수의 농장은 N*N 격자판으로 이루어져 있다.
# N의 크기는 항상 홀수

import sys

sys.stdin = open("in1.txt", 'r')


def solution():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]

    cnt = 0

    s = e = n // 2

    for i in range(n):
        tmp = []
        for j in range(s, e + 1):
            tmp.append(a[i][j])

        if i < n // 2:
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1

    return cnt


print(solution())
