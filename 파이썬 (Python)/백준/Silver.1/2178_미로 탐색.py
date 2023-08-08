from collections import deque


def bfs(x, y, miro):
    answer = -1
    visit = [[False] * y for _ in range(x)]
    d = deque()
    d.append((0, 0, 1))
    visit[0][0] = True

    move = [[-1, 0],  # 상
            [1, 0],  # 하
            [0, -1],  # 좌
            [0, 1]]  # 우 ]

    while d:
        cur_x, cur_y, cur_count = d.popleft()
        if cur_x == x - 1 and cur_y == y - 1:
            answer = cur_count
            break
        for m_x, m_y in move:
            next_x = cur_x + m_x
            next_y = cur_y + m_y
            if 0 <= next_x < x and 0 <= next_y < y:
                if miro[next_x][next_y] == '1' and visit[next_x][next_y] == False:
                    d.append((next_x, next_y, cur_count+1))
                    visit[next_x][next_y] = True

    return answer


x, y = map(int, input().split())
miro = []
for i in range(x):
    miro.append(list(input()))

print(bfs(x, y, miro))
