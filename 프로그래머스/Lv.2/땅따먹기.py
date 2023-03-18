# 열의 개수는 4개이고, 땅(land)은 2차원 배열로 주어집니다.

# DP
def solution(land):
    for i in range(len(land) - 1):
        for j in range(len(land[0])):
            land[i + 1][j] += max(land[i][:j] + land[i][j + 1:])

    return max(land[-1])


print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))
