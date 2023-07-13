def mk_matrix(rows, colums):
    matrix = [[0 for i in range(colums+1)] for j in range(rows+1)]
    cnt = 1

    # 최대 10000번 (O(n^2))
    for x in range(1,rows+1):
        column = []
        for y in range(1, colums+1):
            matrix[x][y] = cnt
            cnt += 1
        matrix.append(column)
    return matrix


# from collections import deque
#
#
# def mv_matrix(matrix, queries):
#     x1, y1, x2, y2 = queries
#     rl_cnt = x2 - x1
#     ud_cnt = y2 - y1
#
#     tmp = deque()
#
#     move_rule = [['r', rl_cnt], ['d', ud_cnt], ['l', rl_cnt], ['u', ud_cnt]]
#
#
#
#     return matrix,mini


def solution(rows, columns, queries):
    answer = []

    matrix = mk_matrix(rows, columns)

    for x1, y1, x2, y2 in queries:
        tmp = matrix[x1][y1]
        mini = tmp

        for k in range(x1, x2):
            test = matrix[k + 1][y1]
            matrix[k][y1] = test
            mini = min(mini, test)

        for k in range(y1, y2):
            test = matrix[x2][k + 1]
            matrix[x2][k] = test
            mini = min(mini, test)

        for k in range(x2, x1, -1):
            test = matrix[k - 1][y2]
            matrix[k][y2] = test
            mini = min(mini, test)

        for k in range(y2, y1, -1):
            test = matrix[x1][k - 1]
            matrix[x1][k] = test
            mini = min(mini, test)

        matrix[x1][y1 + 1] = tmp
        answer.append(mini)

    return answer


rows = 6
colums = 6
queries = [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]

print(solution(rows, colums, queries))
