def check_remove(m, n, board):
    tmp = set()
    for x in range(m - 1):
        for y in range(n - 1):
            if board[x][y] != "" and board[x][y] == board[x + 1][y] == board[x][y + 1] == board[x + 1][y + 1]:
                tmp.add((x, y))
                tmp.add((x, y + 1))
                tmp.add((x + 1, y))
                tmp.add((x + 1, y + 1))

    return tmp


def remove(board, tmp):
    for x, y in tmp:
        board[x][y] = ""
    return board


def falling(m, n, board):
    for x in range(m):
        for y in range(n):
            if board[x][y] == "":
                for j in range(x, m):
                    if board[j][y] != "":
                        board[x][y] = board[j][y]
                        board[j][y] = ""
                        break

    return board


def solution(m, n, board):
    answer = 0

    # 2차원 배열로 재배열
    tmp = []
    for i in range(m):
        tmp.append(list(board.pop()))

    board = tmp

    while True:
        # 삭제 가능 좌표 검사
        tmp = check_remove(m, n, board)

        if len(tmp) == 0:
            break
        else:
            answer += len(tmp)

            # 조건에 일치하는 좌표 초기화
            board = remove(board, tmp)

            # 초기화된 Board 재 배열
            board = falling(m, n, board)
    return answer


m = 6
n = 6
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]

print(solution(m, n, board))
