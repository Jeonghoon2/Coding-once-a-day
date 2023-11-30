from collections import deque


def solution(land):
    n, m = len(land), len(land[0])
    visit = [[0] * m for i in range(n)]
    dr = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    oil_section = [0] * (m + 1)

    def bfs(x, y):
        d = deque()
        d.append((x, y))
        visit[x][y] = 1
        cnt = 0
        min_y, max_y = y, y
        while d:
            x, y = d.popleft()
            cnt += 1

            min_y, max_y = min(y, min_y), max(y, max_y)
            for mx, my in dr:
                nx, ny = x + mx, y + my

                if 0 <= nx < len(land) and 0 <= ny < len(land[0]):
                    if visit[nx][ny] == 0 and land[nx][ny] == 1:
                        d.append((nx, ny))
                        visit[nx][ny] = 1

        for i in range(min_y, max_y + 1):
            oil_section[i] += cnt

    for ly in range(len(land[0])):
        for lx in range(len(land)):
            if land[lx][ly] == 1 and visit[lx][ly] == 0:
                bfs(lx, ly)
    return max(oil_section)


print(solution([[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1],
                [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]))
