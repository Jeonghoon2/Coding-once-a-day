from collections import deque


def baechu(x, y, section):
    visit = [[0] * y for i in range(x)]
    answer = 0

    move = [[-1, 0],  # 상
            [1, 0],  # 하
            [0, -1],  # 좌
            [0, 1]]  # 우

    for s_x, s_y in section:
        visit[s_x][s_y] = 1

    def bfs(i, j):
        d = deque()
        d.append((i, j))
        visit[i][j] = -1

        while d:
            cur_x, cur_y = d.popleft()

            for m_x, m_y in move:
                next_x = cur_x + m_x
                next_y = cur_y + m_y

                if 0 <= next_x < x and 0 <= next_y < y:
                    if visit[next_x][next_y] == 1:
                        d.append((next_x, next_y))
                        visit[next_x][next_y] = 0

    for i in range(x):
        for j in range(y):
            if visit[i][j] == 1:
                bfs(i, j)
                answer += 1

    return answer


n = int(input())

for _ in range(n):
    x, y, num = map(int, input().split())
    position = []

    for _ in range(num):
        p_x, p_y = map(int, input().split())
        position.append([p_x, p_y])

    print(baechu(x, y, position))
