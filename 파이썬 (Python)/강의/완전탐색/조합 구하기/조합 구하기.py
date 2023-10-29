import sys
from itertools import permutations

sys.stdin = open('in1.txt', 'r')


def dfs(l, s):
    global cnt

    if l == m:
        for j in range(l):
            print(res[j], end=' ')
        cnt += 1
        print()
    else:
        for i in range(s, n + 1):
            res[l] = i
            dfs(l + 1, i + 1)


if __name__ == '__main__':
    n, m = map(int, input().split())

    res = [0] * (n + 1)
    cnt = 0
    dfs(0, 1)

    print(cnt)
