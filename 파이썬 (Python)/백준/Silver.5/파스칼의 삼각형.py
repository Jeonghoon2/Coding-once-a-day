def sol():
    n, k = map(int, input().split())
    pascal = [[] for _ in range(n+1)]

    pascal[0] = [1]
    if n == 0:
        return 1
    pascal[1] = [1, 1]
    if n == 1:
        return 1

    for i in range(2, n):
        pascal[i] += [1]
        for j in range(0, i - 1):
            pascal[i] += [pascal[i - 1][j + 1] + pascal[i - 1][j]]
        pascal[i] += [1]

    return pascal[n - 1][k - 1]


print(sol())
