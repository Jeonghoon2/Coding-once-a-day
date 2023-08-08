# 세로 N, 가로 M, 0 빈칸, 1 벽, 2 바이러스
# 먼저 임의의 벽을 새운다.
# 새운 벽을 토대로 BFS를 돌린다.
import copy
from collections import deque

N, M = map(int, input().split())
factory = [list(map(int, input().split())) for _ in range(N)]
answer = 0

move = [[1, 0],
        [-1, 0],
        [0, 1],
        [0, -1]
        ]


# BFS
def bfs():
    q = deque()
    cp_f = copy.deepcopy(factory)

    for i in range(N):
        for j in range(M):
            if cp_f[i][j] == 2:
                q.append((i, j))

    while q:
        cx, cy = q.popleft()

        for mx, my in move:
            nx = cx + mx
            ny = cy + my

            if 0 <= nx < N and 0 <= ny < M:
                if cp_f[nx][ny] == 0:
                    cp_f[nx][ny] = 2
                    q.append((nx, ny))

    global answer
    cnt = 0
    for i in range(N):
        cnt += cp_f[i].count(0)

    answer = max(answer, cnt)


# 참고
def wall(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if factory[i][j] == 0:
                factory[i][j] = 1
                wall(cnt + 1)
                factory[i][j] = 0


wall(0)

print(answer)
