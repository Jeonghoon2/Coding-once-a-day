import sys

sys.setrecursionlimit(10**6)

n = int(input())

graph = [[] for i in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

v = [0] * (n + 1)

def dfs(r):
    for j in graph[r]:
        if v[j] == 0:
            v[j] = r
            dfs(j)


dfs(1)

for x in range(2, n + 1):
    print(v[x])
