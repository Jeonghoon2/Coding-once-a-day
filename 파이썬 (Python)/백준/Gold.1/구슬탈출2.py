import copy

n, m = map(int, input().split())

miro = [list(input()) for _ in range(n)]

sx, sy = 0, 0

ans = int(1e9)

for i in range(1, n):
    for j in range(1, m - 1):
        if miro[i][j] == 'R':
            sx, sy = i, j

visit = [[0] * n] * m
dr = [[-1, 0], [0, -1], [1, 0], [0, 1]]


def dfs(x, y, cnt):
    global ans

    for mx, my in dr:
        sub_x, sub_y = copy.deepcopy(x), copy.deepcopy(y)
        while True:
            nx, ny = x + mx, y + my

            # 방문한 곳이 거나 다음 지점이 벽인 경우
            if visit[nx][ny] == 1 or miro[nx + mx][ny + my] == '#':
                break
            else:
                # 출구를 만났을 경우
                if miro[nx][ny] == 'O':
                    pass

                # 'B'를 만났을 경우
                if miro[nx][ny] == 'B':
                    break


dfs(sx, sy, 0)

print(ans)
