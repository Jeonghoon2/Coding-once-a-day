def solution(triangle):
    answer = 0

    tmp = [[0]]

    for n in range(2,len(triangle)+1):
        arr = [0]* n
        tmp.append(arr)

    for i in range(len(triangle)-1):

        for j in range(len(triangle[i + 1]) - 1):
            op1 = triangle[i][j] + triangle[i+1][j]
            op2 = triangle[i][j] + triangle[i+1][j+1]

            if tmp[i+1][j] < op1:
                tmp[i+1][j] = op1

            if tmp[i+1][j+1] < op2:
                tmp[i+1][j+1] = op2

        triangle[i+1] = tmp[i+1]

    return max(tmp[len(tmp)-1])


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))
