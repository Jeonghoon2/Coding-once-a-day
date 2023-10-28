import sys

sys.stdin = open('in5.txt', 'r')


def dfs(cnt, sum):
    global res

    if cnt > res:
        return
    if sum > m:
        return
    if sum == m:
        if cnt < res:
            res = cnt
    else:
        for i in arr:
            dfs(cnt + 1, sum + i)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    m = int(input())
    res = int(1e9)
    dfs(0, 0)

    print(res)
