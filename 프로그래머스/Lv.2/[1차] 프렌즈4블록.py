def solution(m, n, board):
    answer = 0

    for i in range(m):
        board[i] = list(board[i])

    def search():
        aSet = set()

        for i in range(m - 1):
            for j in range(n - 1):
                # 2X2의 조건이 만족할 때
                if (board[i][j] == board[i + 1][j] == board[i][j + 1] == board[i + 1][j + 1]) and board[i][j] != 0:
                    aSet.add((i, j))
                    aSet.add((i + 1, j))
                    aSet.add((i, j + 1))
                    aSet.add((i + 1, j + 1))
        return aSet

    def remove(lst):
        for tup in lst:
            board[tup[0]][tup[1]] = 0

    def down():
        # 아래칸 부터 검사
        for i in range(m - 1, -1, -1):
            for j in range(n):
                # 0일 때
                if board[i][j] == 0:
                    # 아래 조건의 값과 위 조건의 값이 일치 할때 SWAP
                    for k in range(i - 1, -1, -1):
                        if board[k][j] != 0:
                            board[i][j] = board[k][j]
                            board[k][j] = 0
                            break

    while True:
        answerList = list(search())
        if len(answerList) == 0:
            break
        answer += len(answerList)
        remove(answerList)
        down()

    return answer


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
