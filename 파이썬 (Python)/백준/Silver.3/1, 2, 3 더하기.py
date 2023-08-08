
for i in range(int(input())):
    sum_result = int(input())
    answer = 0

    def dp(c_n, r_n):
        ans = 0
        if c_n == r_n:
            return 1
        elif c_n > r_n:
            pass
        else:
            for i in range(1, 4):
                ans += dp(c_n + i, r_n)

        return ans


    print(dp(0,sum_result))
