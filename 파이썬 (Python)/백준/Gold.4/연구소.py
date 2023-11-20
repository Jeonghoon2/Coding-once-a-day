# 1. 벽을 만든다.
# 2. 벽 3개가 만들어 지면 안전 영역을 검사
# 계산식 : (n*m) - (벽 개수 + 3 + virus 퍼진 수)
import copy
from collections import deque

n, m = map(int, input().split())

ft = [list(map(int, input().split())) for _ in range(n)]

dr = [[1, 0], [-1, 0], [0, 1], [0, -1]]
rst = 0

cw = 0
# 벽 개수 구하기
for i in range(n):
    for j in range(m):
        if ft[i][j] == 1:
            cw += 1

def bfs():
    global rst
    d = deque()
    sub_ft = copy.deepcopy(ft)

    virus = 0
    for i in range(n):
        for j in range(m):
            if sub_ft[i][j] == 2:
                d.append((i, j))
                virus += 1

    while d:
        cx, cy = d.popleft()
        for mx, my in dr:
            nx, ny = cx + mx, cy + my

            if 0 <= nx < n and 0 <= ny < m:
                if sub_ft[nx][ny] == 0:
                    sub_ft[nx][ny] = 2
                    virus += 1
                    d.append((nx, ny))

    rst = max(rst, int((n * m) - (cw + 3 + virus)))


def wall(c):
    if c == 3:
        bfs()
        return
    else:
        for i in range(n):
            for j in range(m):
                if ft[i][j] == 0:
                    ft[i][j] = 1
                    wall(c + 1)
                    ft[i][j] = 0


wall(0)
print(rst)
