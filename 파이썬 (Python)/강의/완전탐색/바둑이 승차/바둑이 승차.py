import sys

sys.stdin = open('in.txt', 'r')


def dfs(L, sum, tsum):
    global result

    if sum + (total - tsum) < result:
        return
    if sum > c:
        return
    if L == n:
        if sum > result:
            result = sum
    else:
        dfs(L + 1, sum + arr[L], tsum + arr[L])
        dfs(L + 1, sum, tsum + arr[L])


if __name__ == "__main__":
    c, n = map(int, input().split())

    arr = []
    result = 0
    for _ in range(n):
        arr.append(int(input()))
    total = sum(arr)

    dfs(0, 0, 0)

    print(result)
