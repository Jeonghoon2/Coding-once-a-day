def sol(n):

    if n <= 1:
        return 1

    dp = [0] * n

    dp[0], dp[1] = 1, 1

    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n - 1]

n = int(input())
print(sol(n))