n = int(input())

arr = []

for _ in range(n):
    arr.append(int(input()))

dp = [0] * (max(arr) + 1)
dp[0], dp[1], dp[2] = 1, 1, 1

for t in arr:
    for i in range(3, t):
        dp[i] = dp[i - 2] + dp[i - 3]
    print(dp[t - 1])
