import sys

# 런타임 에러 (RecursionError) 방지
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n, m = map(int, input().split())

pictures = [list(map(int, input().split())) for _ in range(n)]

dr = [[1, 0], [-1, 0], [0, 1], [0, -1]]
visit = [[0] * m for _ in range(n)]


def dfs(x, y):
    global p_cnt
    p_cnt += 1
    visit[x][y] = 1

    for mx, my in dr:
        nx, ny = x + mx, y + my
        if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0:
            if pictures[nx][ny] == 1:
                visit[nx][ny] = 1
                dfs(nx, ny)


count = 0
max_ans = 0
for i in range(n):
    for j in range(m):

        if pictures[i][j] == 1 and visit[i][j] == 0:
            p_cnt = 0
            dfs(i, j)
            count += 1
            max_ans = max(max_ans, p_cnt)

print(count)
print(max_ans)
