# 3차원 배열을 통해 벽을 부순 경우와 부수지 않은 경우를 나눈다.

n, m = map(int, input().split())

maps = [list(map(int, input())) for _ in range(n)]

dr = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def bfs() -> int:
    from collections import deque

    visit = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visit[0][0][0] = 1

    d = deque()
    d.append((0, 0, 0))

    while d:
        cur_x, cur_y, crash = d.popleft()

        # 도착지에 도달한 경우
        if cur_x == n - 1 and cur_y == m - 1:
            return visit[cur_x][cur_y][crash]

        for mx, my in dr:
            nx, ny = cur_x + mx, cur_y + my

            # 범위 검사
            if 0 <= nx < n and 0 <= ny < m:
                # 벽 X, 방문 X
                if maps[nx][ny] == 0 and visit[nx][ny][crash] == 0:
                    visit[nx][ny][crash] = visit[cur_x][cur_y][crash] + 1
                    d.append((nx, ny, crash))

                # 벽 O, 방문X
                elif maps[nx][ny] == 1 and visit[nx][ny][crash] == 0:

                    # 벽을 파괴 하지 않은 경우 파괴
                    if crash == 0:
                        visit[nx][ny][1] = visit[cur_x][cur_y][crash] + 1
                        d.append((nx, ny, 1))
    return -1

print(bfs())