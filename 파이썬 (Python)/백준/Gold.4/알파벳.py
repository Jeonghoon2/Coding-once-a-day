r, c = map(int, input().split())
maps = []
for _ in range(r):
    maps.append(list(input()))
ans = 0
alphas = set()
dm = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def dfs(x, y, count):
    global ans
    ans = max(ans, count)
    for nx, ny in dm:
        nx = x + nx
        ny = y + ny
        if 0 <= nx < r and 0 <= ny < c and not maps[nx][ny] in alphas:
            alphas.add(maps[nx][ny])
            dfs(nx, ny, count + 1)
            alphas.remove(maps[nx][ny])


alphas.add(maps[0][0])
dfs(0, 0, 1)
print(ans)
