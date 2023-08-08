from collections import deque

def solution(maps):
    answer = -1
    visit = [[0] * len(maps[0]) for i in range(len(maps))]

    move = [
        [-1, 0],
        [1, 0],
        [0, -1],
        [0, 1]
    ]

    d = deque()
    d.append((0, 0))
    visit[0][0] = True

    while d:

        cur_x, cur_y = d.popleft()

        for mx, my in move:
            nx = cur_x + mx
            ny = cur_y + my

            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and not visit[nx][ny]:
                if nx == len(maps) - 1 and ny == len(maps[0]) - 1:
                    return visit[cur_x][cur_y] + 1
                if maps[nx][ny] == 1:
                    d.append((nx, ny))
                    visit[nx][ny] = visit[cur_x][cur_y] + 1

    return answer


maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]
print(solution(maps))
