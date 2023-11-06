import sys

sys.stdin = open("in5.txt", 'r')


def dfs(l, t, s):
    global ans

    if t > m:
        return
    if l == n:
        ans = max(ans, s)
        return
    else:
        dfs(l + 1, t + pt[l], s + pv[l])
        dfs(l + 1, t, s)


if __name__ == "__main__":
    n, m = map(int, input().split())
    tmp = []

    pv = []
    pt = []
    for _ in range(n):
        v, t = map(int, input().split())
        pv.append(v)
        pt.append(t)

    ans = 0

    dfs(0, 0, 0)

    print(ans)