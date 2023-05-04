# 상, 하, 좌, 우 4방향 중 하나를 선택해서 게임판 위의
# 장애물이나 맨 끝에 부딪힐 때까지 미끄러져 이동하는 것을 한 번의 이동으로 칩니다.

from collections import deque


def solution(board):
    answer = 0

    start_x, start_y = 0, 0
    move = [
        [1, 0],  # 상
        [-1, 0],  # 하
        [0, -1],  # 좌
        [0, 1]  # 우
    ]

    # 시작 위치 찾기
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                start_x = i
                start_y = j

    def bfs(x, y):
        visit = [[x, y]]
        d = deque()
        d.append((x, y, 0))

        while d:
            cur_x, cur_y, cur_cnt = d.popleft()

            if board[cur_x][cur_y] == 'G':
                return cur_cnt

            for mx, my in move:
                sub_x, sub_y = cur_x,cur_y
                # 벽 또는 D까지
                while True:
                    nx = sub_x + mx
                    ny = sub_y + my
                    # 범위를 벗어나는 경우
                    if 0 > nx or nx >= len(board) or 0 > ny or ny >= len(board[0]):
                        if [sub_x, sub_y] not in visit:
                            d.append((sub_x, sub_y, cur_cnt + 1))
                            visit.append([sub_x, sub_y])
                        break
                    # 장애물을 만나는 경우
                    if board[nx][ny] == "D":
                        if [sub_x, sub_y] not in visit:
                            d.append((sub_x, sub_y, cur_cnt + 1))
                            visit.append([sub_x, sub_y])
                        break
                    sub_x += mx
                    sub_y += my

    answer = bfs(start_x, start_y)
    if answer is None:
        answer = -1

    return answer


board = [".D.R", "....", ".G..", "...D"]
print(solution(board))
