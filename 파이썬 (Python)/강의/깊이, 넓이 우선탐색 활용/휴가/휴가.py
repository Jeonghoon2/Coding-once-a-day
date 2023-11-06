import sys

sys.stdin = open('in5.txt', 'r')


def dfs(l, d, s):
    global rst

    if l == n:
        rst = max(rst, s)
        return
    else:
        # 맡은 상담이 일수가 끝나지 않았을 경우
        if d > 0:
            dfs(l + 1, d - 1, s)
        # 맡은 상담이 없는 경우
        else:
            if l + t[l]-1 > n-1:
                dfs(l + 1, d, s)
            else:
                # 해당 상담을 수행할 경우
                dfs(l + 1, d + t[l] - 1, s + p[l])

                # 해당 상담을 수행 하지 않을 경우
                dfs(l + 1, d, s)


if __name__ == "__main__":

    n = int(input())
    t = []
    p = []

    for _ in range(n):
        a, b = map(int, input().split())
        t.append(a)
        p.append(b)

    rst = 0

    dfs(0, 0, 0)

    print(rst)
