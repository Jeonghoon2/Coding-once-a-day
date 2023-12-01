# 1 : 빨간 수레의 시작 칸
# 2 : 파란 수레의 시작 칸
# 3 : 빨간 수레의 도착 칸
# 4 : 파란 수레의 도착 칸
import sys

sys.setrecursionlimit(10 ** 6)
answer = int(1e9)


# 초기 수레 값 찾기
def init(maps):
    red_wagon_start, red_wagon_goal = [0, 0], [0, 0]
    blue_wagon_st, blue_wagon_goal = [0, 0], [0, 0]

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 1:
                red_wagon_start = [i, j]
            elif maps[i][j] == 3:
                red_wagon_goal = [i, j]
            elif maps[i][j] == 2:
                blue_wagon_st = [i, j]
            elif maps[i][j] == 4:
                blue_wagon_goal = [i, j]
    return [red_wagon_start, red_wagon_goal, blue_wagon_st, blue_wagon_goal]


def solution(maze):
    global answer
    red_start, red_goal, blue_start, blue_goal = init(maze)
    red_visit = [[False] * len(maze[0]) for _ in range(len(maze))]
    blue_visit = [[False] * len(maze[0]) for _ in range(len(maze))]
    red_visit[red_start[0]][red_start[1]] = True
    blue_visit[blue_start[0]][blue_start[1]] = True
    dr = [[0, 1], [-1, 0], [1, 0], [0, -1]]  # 우 하 상 좌

    # 0 빨강, 1 파랑
    def is_bool_section(x, y, color):

        if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != 5:
            # 빨간색 겹침 검사 안함
            if color == 0:
                if not red_visit[x][y]:
                    return True
            # 파란색 겸침 검사 하고
            if color == 1:
                if not blue_visit[x][y]:
                    return True

        return False

    def dfs(rx, ry, bx, by, cnt):
        if [rx, ry] == [bx, by]:
            return

            # 수레가 모두 도착을 했을 경우
        if [rx, ry] == red_goal and [bx, by] == blue_goal:
            global answer
            answer = min(answer, cnt)
            return
        else:
            # 빨간 수레만 도착 했을 경우
            if [rx, ry] == red_goal and [bx, by] != blue_goal:
                for bmx, bmy in dr:
                    bnx, bny = bx + bmx, by + bmy
                    if is_bool_section(bnx, bny, 1):
                        blue_visit[bnx][bny] = True
                        dfs(rx, ry, bnx, bny, cnt + 1)
                        blue_visit[bnx][bny] = False

            # 파란 수레만 도착 했을 경우
            if [rx, ry] != red_goal and [bx, by] == blue_goal:
                for rmx, rmy in dr:
                    rnx, rny = rx + rmx, ry + rmy
                    if is_bool_section(rnx, rny, 0):
                        red_visit[rnx][rny] = True
                        dfs(rnx, rny, bx, by, cnt + 1)
                        red_visit[rnx][rny] = False

            # 둘다 도착 하지 못했을 경우
            if [rx, ry] != red_goal and [bx, by] != blue_goal:
                # 빨간색 수레를 먼저 움직 이고 파란색 수레를 움직 인다.
                # 빨강
                for rmx, rmy in dr:
                    rnx, rny = rx + rmx, ry + rmy

                    # 범위 검사, 방문 검사, 벽 검사
                    if is_bool_section(rnx, rny, 0):

                        # 빨간색이 움직 이고 파란색이 움직일 때
                        # 파랑
                        for bmx, bmy in dr:
                            bnx, bny = bx + bmx, by + bmy
                            # 범위 검사, 방문 검사, 벽 검사
                            if is_bool_section(bnx, bny, 1):
                                # 서로 위치 교환 검사
                                if bnx == rx and bny == ry and rnx == bx and rny == by:
                                    continue
                                # 겹침 검사
                                if [bnx, bny] != [rnx, rny]:
                                    red_visit[rnx][rny] = True
                                    blue_visit[bnx][bny] = True
                                    dfs(rnx, rny, bnx, bny, cnt + 1)
                                    blue_visit[bnx][bny] = False

                        red_visit[rnx][rny] = False

    dfs(red_start[0], red_start[1], blue_start[0], blue_start[1], 0)

    if answer == int(1e9):
        return 0

    return answer


print(solution([[1, 0, 2], [0, 0, 0], [5, 0, 5], [4, 0, 3]]))
