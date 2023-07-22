from collections import deque


def bfs(sx, sy, c):
    move = [
        [1, 0],
        [-1, 0],
        [0, 1],
        [0, -1]
    ]

    d = deque()
    d.append((sx, sy))

    while d:
        cur_x, cur_y = d.popleft()

        for mx, my in move:
            nx, ny = mx + cur_x, my + cur_y

            if 0 <= nx < N and 0 <= ny < N:
                if c[nx][ny] == 1:
                    c[nx][ny] = 0
                    d.append((nx,ny))

    return copy


N = int(input())
answer = []
maps = []

for _ in range(N):
    maps.append(list(map(int, input().split())))

for mh in range(0, 101):
    copy = [[0] * N for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(N):
            if maps[i][j] > mh:
                copy[i][j] = 1

    for x in range(N):
        for y in range(N):
            if copy[x][y] == 1:
                bfs(x, y, copy)
                cnt += 1
    answer.append(cnt)

print(max(answer))