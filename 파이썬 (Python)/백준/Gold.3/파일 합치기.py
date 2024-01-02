import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

for _ in range(int(input())):

    n = int(input())

    arr = [int(x) for x in input().split()]
    rst = [[0 for _ in range(n)] for _ in range(n)]

    for j in range(1, n):
        for i in range(j - 1, -1, -1):
            small = int(1e9)
            for k in range(j - i):
                small = min(small, rst[i][i + k] + rst[i + k + 1][j])
            rst[i][j] = small + sum(arr[i:j + 1])
    print(rst[0][n - 1])
