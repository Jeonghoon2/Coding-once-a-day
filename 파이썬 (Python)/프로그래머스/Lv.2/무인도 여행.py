from collections import deque


def solution(maps):
    answer = []
    l_maps = []
    for i in maps:
        l_maps.append(list(i))

    visit = [[False] * len(maps[0]) for _ in range(len(maps))]

    def bfs(x, y):

        d = deque()
        d.append((x, y))
        visit[x][y] = True

        # move 지정
        move = [[-1, 0],  # 상
                [1, 0],  # 하
                [0, -1],  # 좌
                [0, 1]  # 우
                ]
        n = []

        while d:
            cur_x, cur_y = d.popleft()

            n.append(int(l_maps[cur_x][cur_y]))

            for x, y in move:
                next_x = cur_x + x
                next_y = cur_y + y
                if 0 <= next_x < len(maps) and 0 <= next_y < len(maps[0]):
                    if l_maps[next_x][next_y] != 'X' and not visit[next_x][next_y]:
                        visit[next_x][next_y] = True
                        d.append((next_x, next_y))

        return sum(n)

    for i in range(len(l_maps)):
        for j in range(len(l_maps[0])):
            if l_maps[i][j] == 'X':
                continue
            elif visit[i][j] == True:
                continue
            else:
                answer.append(bfs(i, j))

    return sorted(answer) if len(answer) != 0 else [-1]


maps = ["XXX","XXX","XXX"]
print(solution(maps))
