# F(1) = 1, F(2) = 2
# Bottom up

class Solution:
    def climbStairs(n):
        dp = [0] * (n + 1)
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            dp[0], dp[1] = 1, 2

            for i in range(2, n + 1):
                dp[i] = dp[i - 1] + dp[i - 2]

            return dp[n-1]


print(Solution.climbStairs(3))
