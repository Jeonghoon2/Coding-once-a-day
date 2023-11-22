n = int(input())

t = [list(map(int, input().split())) for _ in range(n)]

dp = []

for i in range(1, n + 1):
    dp.append([0] * i)

dp[0] = t[0]

dr = [[1, 0], [1, 1]]

for x in range(n-1):
    for y in range(len(t[x])):

        for dx, dy in dr:
            nx, ny = x + dx, y + dy

            dp[nx][ny] = max(dp[nx][ny], dp[x][y] + t[nx][ny])

print(max(dp[n-1]))
