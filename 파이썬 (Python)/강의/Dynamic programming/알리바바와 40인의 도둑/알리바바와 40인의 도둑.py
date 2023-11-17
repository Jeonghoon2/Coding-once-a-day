import sys

sys.stdin = open('in5.txt', 'r')


def dfs(x, y):
    if [x, y] == [n - 1, n - 1]:
        return
    for mx, my in dr:
        nx, ny = x + mx, y + my

        if 0 <= nx < n and 0 <= ny < n:
            if arr[nx][ny] + dp[x][y] < dp[nx][ny]:
                dp[nx][ny] = arr[nx][ny] + dp[x][y]
                dfs(nx, ny)


if __name__ == '__main__':
    n = int(input())

    dp = [[1000] * n for _ in range(n)]

    arr = [list(map(int, input().split())) for _ in range(n)]

    dp[0][0] = arr[0][0]
    dr = [[1, 0], [0, 1]]
    cnt = 0
    dfs(0, 0)

    print(dp[n - 1][n - 1])
