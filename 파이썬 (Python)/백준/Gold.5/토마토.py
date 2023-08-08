# 0 = 익지 않은 토마토, 1 = 익은 토마토, -1 = 비어 있는 칸
# M = 가로, N = 세로

from collections import deque

N, M = map(int, input().split())
basket = []
start_position = []
answer = int(1e9)
for _ in range(M):
    basket.append(list(map(int, input().split(' '))))


# BFS
def bfs(start_position, b):

    # move
    move = [
        [1, 0],
        [-1, 0],
        [0, 1],
        [0, -1]
    ]
    d = deque()
    for start_x,start_y in start_position:
        d.append((start_x, start_y, 0))

    cnt = 0

    while d:
        cur_x, cur_y, cur_cnt = d.popleft()

        if cnt < cur_cnt:
            cnt = cur_cnt

        for mx, my in move:
            nx = cur_x + mx
            ny = cur_y + my
            if 0 <= nx < len(b) and 0 <= ny < len(b[0]):
                if b[nx][ny] == 0:
                    if b[nx][ny] != -1 and b[nx][ny] != 1:
                        d.append((nx, ny, cur_cnt + 1))
                        b[nx][ny] = 1

    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == 0:
                return -1

    return cnt


# 시작 지점 찾기
for i in range(len(basket)):
    for j in range(len(basket[0])):
        if basket[i][j] == 1:
            start_position.append([i, j])

answer = bfs(start_position,basket)

print(answer)