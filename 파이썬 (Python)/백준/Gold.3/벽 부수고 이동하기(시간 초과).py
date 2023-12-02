# 모든 벽을 한번씩 부쉈을 경우의 루트를 구하는 풀이 시간 초과

import copy

def init(arr):
    tmp = []
    for x in range(len(arr)):
        for y in range(len(arr[0])):
            if arr[x][y] == 1:
                arr[x][y] = 0
                tmp.append(copy.deepcopy(arr))
                arr[x][y] = 1

    return tmp


def bfs(route):
    from collections import deque
    global answer
    visit = [[False] * len(route[0]) for _ in range(len(route))]
    d = deque()
    d.append((0, 0, 0))
    visit[0][0] = True
    while d:
        cur_x, cur_y, cur_cnt = d.popleft()

        if cur_x == len(route) - 1 and cur_y == len(route[0]) - 1:
            answer = min(cur_cnt, answer)
            continue
        for mx, my in dr:
            nx, ny = cur_x + mx, cur_y + my

            # 범위를 벗어 나지 않고
            if 0 <= nx < len(route) and 0 <= ny < len(route[0]):
                # 다음 좌표의 값이 0이고 방문 하지 않았을 경우
                if route[nx][ny] == 0 and not visit[nx][ny]:
                    d.append((nx, ny, cur_cnt + 1))
                    visit[nx][ny] = True


n, m = map(int, input().split())
maps = [list(map(int, input())) for _ in range(n)]
answer = int(1e9)
maps = init(maps)
dr = [[0, 1], [-1, 0], [1, 0], [0, -1]]

for map in maps:
    bfs(map)

if answer >= int(1e9):
    print(-1)
else:
    print(answer+1)
