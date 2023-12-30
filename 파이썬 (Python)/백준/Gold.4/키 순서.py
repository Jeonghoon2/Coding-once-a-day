import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, m = map(int, input().split())

tall = [[] for _ in range(n)]
small = [[] for _ in range(n)]
answer = 0

for _ in range(m):
    s, b = map(int, input().split())
    tall[s - 1].append(b - 1)
    small[b - 1].append(s - 1)


def s_dfs(start_node, visit, cnt):
    global s_cnt
    for i in small[start_node]:
        if not visit[i]:
            s_cnt += 1
            visit[i] = True
            s_dfs(i, visit, cnt)


def t_dfs(start_node, visit, cnt):
    global t_cnt
    for i in tall[start_node]:
        if not visit[i]:
            t_cnt += 1
            visit[i] = True
            t_dfs(i, visit, cnt)


for i in range(n):
    t_cnt, s_cnt = 0, 0
    t_v, s_v = [False] * n, [False] * n
    t_dfs(i, t_v, 0)
    s_dfs(i, s_v, 0)

    if t_cnt + s_cnt == n - 1:
        answer += 1

print(answer)