c, w = map(int, input().split())

bags = [map(int, input().split()) for _ in range(c)]

dp = [0] * (w + 1)

for iw, iv in bags:
    for i in range(w, iw - 1, -1):
        dp[i] = max(dp[i - iw] + iv, dp[i])

print(dp[-1])
