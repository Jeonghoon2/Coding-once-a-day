# 0 = 익지 않은 토마토, 1 = 익은 토마토, -1 = 비어 있는 칸
# M = 가로, N = 세로

from collections import deque
import sys

m, n = map(int, input().split())

tomatoes = [list(map(int, input().split())) for _ in range(n)]

d = deque()

dr = [[-1, 0], [1, 0], [0, -1], [0, 1]]

rst = 0

# 기존 토마토
for i in range(n):
    for j in range(m):
        if tomatoes[i][j] == 1:
            d.append([i, j])


def bfs():
    while d:
        cur_x, cur_y = d.popleft()

        for mx, my in dr:
            nx, ny = cur_x + mx, cur_y + my

            if 0 <= nx < n and 0 <= ny < m and tomatoes[nx][ny] == 0:
                tomatoes[nx][ny] = tomatoes[cur_x][cur_y] + 1
                d.append([nx, ny])


bfs()
for i in tomatoes:
    for j in i:
        if j == 0:
            print(-1)
            sys.exit(0)
    rst = max(rst, max(i))

print(rst-1)
