n = int(input())

lst = [0] + [int(input()) for i in range(n)]

dp = [0] * (n + 1)

for i in range(1, n + 1):
    if i == 1:
        dp[i] = lst[i]
    elif i == 2:
        dp[i] = dp[i - 1] + lst[i]
    elif i == 3:
        dp[i] = max(dp[i - 2] + lst[i], dp[i - 3] + lst[i - 1] + lst[i])
    else:
        dp[i] = max(max(dp[i - 2] + lst[i], dp[i - 3] + lst[i - 1] + lst[i]), dp[i - 4] + lst[i - 1] + lst[i])

print(max(max(dp[n], dp[n-1]), dp[n-2]))
