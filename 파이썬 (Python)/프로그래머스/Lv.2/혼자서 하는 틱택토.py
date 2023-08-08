
# 혼자서 선공과 후공을 둘 다 맡는다.
# 틱택토 게임을 시작한 후 "O"와 "X"를 혼자서 번갈아 가면서 표시를 하면서 진행한다.

# 예외 처리
# 1. "O"를 표시할 차례인데 "X"를 표시 또는 반대로 했을 경우
# 2. 선공이나 후공이 승리해서 게임이 종료 되었음에도 그 게임을 진행 할 경우.

def isWin(board, x, y):
    leftY, rightY = (y - 1) % 3, (y + 1) % 3
    if board[x][y] == board[x][leftY] == board[x][rightY]:
        return True

    upX, downX = (x - 1) % 3, (x + 1) % 3
    if board[x][y] == board[upX][y] == board[downX][y]:
        return True

    if (board[x][y] == board[upX][leftY] == board[downX][rightY]) or (
            board[x][y] == board[upX][rightY] == board[downX][leftY]):
        return True

    return False


def solution(board):
    answer = 1

    x_count, o_count, x_list, o_list = 0, 0, [], []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'X':
                x_count += 1
                x_list.append((i, j))
            elif board[i][j] == 'O':
                o_count += 1
                o_list.append((i, j))

    if x_count - o_count > 0 or len(o_list) >= (len(x_list) + 2):
        return 0

    for x, y in o_list :
        if isWin(board, x, y) and len(x_list) != (len(o_list) - 1):
            return 0

    for x, y in x_list:
        if isWin(board, x, y) and len(x_list) != (len(o_list)):
            return 0

    return answer


print(solution(["OOO", "...", "XXX"]))
