import sys

n = int(input())

if n == 1:
    print(1)
    sys.exit(0)

dp = [0] * (n + 1)
dp[1], dp[2] = 1, 3

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + (dp[i - 2] * 2)

print(dp[n] % 10007)
