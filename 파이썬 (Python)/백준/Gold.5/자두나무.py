import sys

input = sys.stdin.readline

t, w = map(int, input().split())

trees = [0]

dp = [[0] * (w + 1) for _ in range(t + 1)]

for _ in range(t):
    trees.append(int(input()))

for i in range(1, t + 1):

    if trees[i] == 1:
        dp[i][0] = dp[i - 1][0] + 1
    else:
        dp[i][0] = dp[i - 1][0]

    for j in range(1, w + 1):

        if trees[i] == 2 and j % 2 == 1:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + 1

        elif trees[i] == 1 and j % 2 == 0:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + 1

        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j])

print(max(dp[t]))