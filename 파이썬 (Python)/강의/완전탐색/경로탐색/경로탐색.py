import sys

sys.stdin = open('in5.txt', 'r')


def dfs(L, v):
    global cnt
    if L == n:
        cnt += 1
        return

    for i in range(1, n + 1):

        if arr[L][i] == 1:
            if L == i or i not in v:
                dfs(i, v + [i])


if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = [[0] * (n + 1) for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        arr[a][b] = 1

    cnt = 0
    dfs(1, [1])

    print(cnt)
