import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())

# 친구 관계
relations = [[] for _ in range(n)]

answer = False

# 방문 [ 2001을 한 이유 조건의 1<=M<=2000 ]
visited = [False] * 2001

for _ in range(m):
    a, b = map(int, input().split())
    relations[a].append(b)
    relations[b].append(a)


def dfs(num: int, depth: int):
    global answer

    if depth == 4:
        answer = True
        return

    for c in relations[num]:
        if not visited[c]:
            visited[c] = True
            dfs(c, depth + 1)
            visited[c] = False


for i in range(n):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False
    if answer:
        break

if answer:
    print(1)
else:
    print(0)