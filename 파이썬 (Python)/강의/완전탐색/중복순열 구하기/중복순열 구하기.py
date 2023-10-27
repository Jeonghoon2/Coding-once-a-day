import sys

sys.stdin = open('in5.txt', 'r')


def dfs(arr):
    if len(arr) == m:
        if arr not in rst:
            rst.append(arr)
        return
    else:
        for i in range(1, n + 1):
            dfs(arr + [i])


if __name__ == '__main__':
    n, m = map(int, input().split())

    rst = []
    dfs([])

    for ans in rst:
        print(*ans)

    print(len(rst))
