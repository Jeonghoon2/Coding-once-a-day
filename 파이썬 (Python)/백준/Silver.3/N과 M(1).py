n, m = map(int, input().split())

v = [0] * (n + 1)


def dfs(arr):
    if len(arr) == m:
        print(*arr)
        return arr
    else:
        for j in range(1, n + 1):
            if v[j] == 0:
                v[j] = 1
                dfs(arr + [j])
                v[j] = 0


dfs([])

