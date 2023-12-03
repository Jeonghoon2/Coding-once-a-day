import copy


def check(x1, y1, x2, y2):
    global section

    for i in range(x1, x2):
        for j in range(y1, y2):
            section[j][i] = 1


def bfs(x, y) -> int:
    from collections import deque

    d = deque()
    d.append((x, y))
    section[x][y] = 1
    cnt = 1

    while d:
        cur_x, cur_y = d.popleft()

        for mx, my in dr:
            nx, ny = cur_x + mx, cur_y + my

            if 0 <= nx < n and 0 <= ny < m:
                if section[nx][ny] == 0:
                    d.append((nx, ny))
                    section[nx][ny] =1
                    cnt += 1

    return cnt


n, m, k = map(int, input().split())

rct = [list(map(int, input().split())) for _ in range(k)]
dr = [[1, 0], [-1, 0], [0, 1], [0, -1]]
section = [[0] * m for _ in range(n)]
for lst in rct:
    x1, y1, x2, y2 = lst

    check(x1, y1, x2, y2)

ans = []
for i in range(n):
    for j in range(m):
        if section[i][j] == 0:
            ans.append(bfs(i, j))

print(len(ans))

ans.sort()
print(*ans)
