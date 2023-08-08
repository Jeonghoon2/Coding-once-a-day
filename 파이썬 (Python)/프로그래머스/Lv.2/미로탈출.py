# 출구는 레버가 당겨지지 않아도 지나갈 수 있으며, 모든 통로, 출구, 레버, 시작점은 여러 번 지나갈 수 있습니다.
# 출발 지점에서 먼저 레버가 있는 칸으로 이동하여 레버를 당긴 후 미로를 빠져나가는 문이 있는 칸으로 이동하면 됩니다.
from collections import deque


def bfs(start_x, start_y, miro):
    # 방문 기록
    visit = [[False] * len(miro[0]) for _ in range(len(miro))]

    # move 지정
    move = [[-1, 0],  # 상
            [1, 0],  # 하
            [0, -1],  # 좌
            [0, 1]  # 우
            ]

    # 출발 지점 입력
    d = deque()
    d.append((start_x, start_y, 0))
    visit[start_x][start_y] = True

    # 레버 여부
    lever = False

    while d:
        cur_x, cur_y, cur_cnt = d.popleft()

        for m_x, m_y in move:
            next_x = m_x + cur_x
            next_y = m_y + cur_y

            if 0 <= next_x < len(miro) and 0 <= next_y < len(miro[0]) and not visit[next_x][next_y]:
                if miro[next_x][next_y] == 'X':
                    continue
                if miro[next_x][next_y] == 'L':
                    visit = [[False] * len(miro[0]) for _ in range(len(miro))]
                    visit[next_x][next_y] = True
                    d.clear()
                    d.append((next_x, next_y, cur_cnt + 1))
                    lever = True
                    break
                if miro[next_x][next_y] == 'E' and lever:
                    return cur_cnt + 1

                visit[next_x][next_y] = True
                d.append((next_x, next_y, cur_cnt + 1))

    return -1


def solution(maps):
    answer = 0

    # 미로 재배치
    miro = []
    for i in maps:
        miro.append(list(i))

    # 출발점 찾기
    s_x, s_y = 0, 0

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                s_x, s_y = i, j
                break

    answer = bfs(s_x, s_y, miro)
    return answer


maps = ["SOEOL", "XXXXO", "OOOOO", "OXXXX", "OOOOO"]

print(solution(maps))
