import sys

sys.stdin = open('in5.txt', 'r')


def dfs(l, sum):
    global res

    if l == n:
        if 0 < sum <= s:
            res.add(sum)
        return
    else:
        # 왼쪽에 놓을 경우
        dfs(l + 1, sum + g[l])
        # 오른쪽에 놓을 경우
        dfs(l + 1, sum - g[l])
        # 놓지 않을 경우
        dfs(l + 1, sum)


if __name__ == '__main__':
    n = int(input())
    g = list(map(int, input().split()))

    s = sum(g)

    res = set()
    dfs(0, 0)

    print(s-len(res))