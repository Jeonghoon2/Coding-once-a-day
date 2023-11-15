def dfs(x, y):
    if dp[x][y] != -1:
        return dp[x][y]

    if x == m - 1 and y == n - 1:
        return 1

    dp[x][y] = 0

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 0 <= nx < m and 0 <= ny < n and graph[x][y] > graph[nx][ny]:
            dp[x][y] += dfs(nx, ny)

    return dp[x][y]


m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]

dp = [[-1] * n for _ in range(m)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

result = dfs(0, 0)

print(result)
