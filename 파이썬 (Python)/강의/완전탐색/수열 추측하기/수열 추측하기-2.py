import sys

sys.stdin = open('in1.txt', 'r')


def dfs(L, sum):
    if L == n and sum == f:
        print(*p)
        sys.exit(0)
    else:
        for i in range(1, n + 1):
            if ch[i] == 0:
                ch[i] = 1
                p[L] = i
                dfs(L + 1, sum + (p[L] * b[L]))
                ch[i] = 0


if __name__ == '__main__':
    n, f = map(int, input().split())
    p = [0] * n
    b = [1] * n
    ch = [0] * (n + 1)

    for i in range(1, n):
        b[i] = b[i - 1] * (n - i) // i

    dfs(0, 0)
