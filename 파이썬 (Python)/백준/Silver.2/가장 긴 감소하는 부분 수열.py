n = int(input())
lst = list(map(int, input().split()))

dp = [0] * n
dp[0] = 1
for i in range(1, len(lst)):
    for j in range(0, i):
        if lst[i] < lst[j]:
            dp[i] = max(dp[j] + 1, dp[i])
        else:
            dp[i] = max(dp[i], 1)

print(max(dp))
