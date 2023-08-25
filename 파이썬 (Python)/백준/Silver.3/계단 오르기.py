def solution():
    n = int(input())
    stairs = []
    visit = [0] * n
    for _ in range(n):
        stairs.append(int(input()))

    def dfs(idx, cnt, dp, v):
        move = [1, 2]

        for m in move:
            c_v = v.copy()
            c_dp = dp.copy()
            n_idx = idx + m

            if n_idx >= len(dp):
                return

            if idx >= 1 and c_dp[n_idx - 1] > 0 and c_dp[n_idx - 2] > 0 and m == 1:
                continue
            else:
                c_v.append(stairs[n_idx])
                c_dp[n_idx] = sum(c_v)
            if n_idx < len(stairs):
                if visit[n_idx] < c_dp[n_idx]:
                    visit[n_idx] = c_dp[n_idx]
                dfs(n_idx, cnt + 1, c_dp, c_v)
            else:
                return

    dfs(-1, 0, [0] * n, [])

    return visit[-1]


# 인터넷 참조
def solution2():
    # input
    n = int(input())
    stairs = [int(input()) for _ in range(n)]
    dp = [0] * n

    if len(stairs) <= 2:
        print(sum(stairs))
    else:
        dp[0] = stairs[0]
        dp[1] = stairs[0] + stairs[1]

        for i in range(2,n):
            dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i], dp[i-2]+stairs[i])

    print(dp[-1])

print(solution2())
