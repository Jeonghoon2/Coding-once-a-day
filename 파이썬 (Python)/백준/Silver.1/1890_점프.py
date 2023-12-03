# 경로의 개수를 구한다.
# 규칙 : 오른쪽, 아래 만 이동 가능

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):

        # 도착 지점 도달 했을 경우
        if i == n - 1 and j == n - 1:
            print(dp[i][j])
            break

        # 우측 이동
        # 범위를 벗어 나지 않을 경우
        if j + lst[i][j] < n:
            dp[i][j + lst[i][j]] += dp[i][j]

        # 아래 이동
        # 범위를 벗어 나지 않을 경우
        if i + lst[i][j] < n:
            dp[i + lst[i][j]][j] += dp[i][j]