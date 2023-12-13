from collections import deque
import sys

input = sys.stdin.readline

# 국가 간의 인구 공유는 L 이상 P 이하 경우에만 가능 하다.
n, l, p = map(int, input().split())

ca = [list(map(int, input().split())) for _ in range(n)]

dr = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def bfs(x, y):
    global flag
    d = deque()
    d.append((x, y))
    visit[x][y] = 1
    tmp = [[x, y]]

    while d:
        cur_x, cur_y = d.popleft()

        for mx, my in dr:
            nx, ny = cur_x + mx, cur_y + my
            # 범위를 벗어 나지 않고 방문 하지 않았 다면
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
                gap = abs(ca[cur_x][cur_y] - ca[nx][ny])
                # L과 P 사이의 조건을 만족할 경우
                if l <= gap <= p:
                    visit[nx][ny] = 1
                    d.append((nx, ny))
                    tmp.append([nx, ny])

    # 인구 이동 시작
    if len(tmp) > 1:
        flag = True
        total = 0
        for tx, ty in tmp:
            total += ca[tx][ty]

        for tx, ty in tmp:
            ca[tx][ty] = int(total / len(tmp))


day = 0

while True:
    visit = [[0] * n for _ in range(n)]
    flag = False
    for x in range(n):
        for y in range(n):
            if visit[x][y] == 0:
                bfs(x, y)

    if not flag:
        break

    day += 1

print(day)
