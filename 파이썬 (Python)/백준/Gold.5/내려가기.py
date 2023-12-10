import sys

input = sys.stdin.readline

n = int(input())

max_dp = [0] * 3
min_dp = [0] * 3

for i in range(0, n):
    n1, n2, n3 = map(int, input().split())

    min_d0 = n1 + min(min_dp[0], min_dp[1])
    max_d0 = n1 + max(max_dp[0], max_dp[1])

    min_d1 = n2 + min(min_dp[0], min_dp[1], min_dp[2])
    max_d1 = n2 + max(max_dp[0], max_dp[1], max_dp[2])

    min_d2 = n3 + min(min_dp[1], min_dp[2])
    max_d2 = n3 + max(max_dp[1], max_dp[2])

    min_dp[0], min_dp[1], min_dp[2] = min_d0, min_d1, min_d2
    max_dp[0], max_dp[1], max_dp[2] = max_d0, max_d1, max_d2

print(max(max_dp), min(min_dp))
