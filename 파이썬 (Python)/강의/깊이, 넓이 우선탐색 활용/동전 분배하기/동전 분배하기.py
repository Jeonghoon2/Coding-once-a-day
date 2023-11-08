import sys

sys.stdin = open('in5.txt', 'r')


def dfs(l, s1, s2, s3):
    global rst

    if l == n:
        if s1 == s2 or s1 == s3 or s3 == s2:
            return
        rst = min(max(s1, s2, s3) - min(s1, s2, s3), rst)
        return
    else:
        dfs(l + 1, s1 + coins[l], s2, s3)
        dfs(l + 1, s1, s2 + coins[l], s3)
        dfs(l + 1, s1, s2, s3 + coins[l])


if __name__ == '__main__':
    n = int(input())

    coins = []
    for _ in range(n):
        coins.append(int(input()))
    rst = int(1e9)
    dfs(0, 0, 0, 0)

    print(rst)
