from collections import deque


# 둘러싼 0의 개수 구하기
def zero_count(tmp):
    for x in range(1, n - 1):
        for y in range(1, m - 1):
            if maps[x][y] == 0:
                continue
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if maps[nx][ny] == 0:
                    tmp[x][y] += 1
    return tmp


# 높이 낮추기
def down_height(tmp):
    for x in range(1, n - 1):
        for y in range(1, m - 1):
            if maps[x][y] != 0:
                maps[x][y] = max(0, maps[x][y] - tmp[x][y])


# 덩어리 구하기
def is_count(sx, sy, v):
    d = deque()
    d.append((sx, sy))
    v[sx][sy] = 1

    while d:
        cur_x, cur_y = d.popleft()

        for dx, dy in directions:
            nx, ny = cur_x + dx, cur_y + dy
            if maps[nx][ny] > 0 and v[nx][ny] == 0:
                v[nx][ny] = 1
                d.append((nx, ny))

    return v


def sol():
    for year in range(1, 900000):
        # 둘러싼 0의 개수 구하기
        sub = [[0] * m for _ in range(n)]
        sub = zero_count(sub)

        # 높이 낮추기
        down_height(sub)

        # 덩어리 구하기
        cnt = 0
        visit = [[0] * m for _ in range(n)]
        for x in range(1, n - 1):
            for y in range(1, m - 1):
                if maps[x][y] > 0 and visit[x][y] == 0:
                    visit = is_count(x, y, visit)
                    cnt += 1
        if cnt > 1:
            return year
        if cnt == 0:
            return 0

    return -1


n, m = map(int, input().split())

maps = []

for _ in range(n):
    maps.append(list(map(int, input().split())))

directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

rst = sol()

print(rst)