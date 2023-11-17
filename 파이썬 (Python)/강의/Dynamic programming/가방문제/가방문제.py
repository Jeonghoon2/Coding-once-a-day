import sys

sys.stdin = open('in5.txt', 'r')

mw, mv = map(int, input().split())

bags = []
dp = [0] * (mv + 1)
for _ in range(mw):
    bags.append(list(map(int, input().split())))

for w, v in bags:
    for i in range(w, len(dp)):
        dp[i] = max(dp[i - w] + v, dp[i])

print(max(dp))
