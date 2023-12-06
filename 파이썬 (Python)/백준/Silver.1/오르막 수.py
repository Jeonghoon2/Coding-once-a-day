import sys

n = int(input())

# 맨처음 0은 첫번 째 해당 값의 수를 위한 값
dp = [[0] + ([1] * 10) for _ in range(n)]

if n == 1:
    print(sum(dp[0]) % 10007)
    sys.exit(0)

for i in range(1, n):
    for j in range(1, 11):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

print(sum(dp[n - 1]) % 10007)
