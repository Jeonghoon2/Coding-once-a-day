# 전체 사람의 수
n = int(input())
# 촌수를 계산해야 하는 서로 다른 두 사람의 번호
p1, p2 = map(int, input().split())
# 부모 자식들 간의 관계의 수
r = int(input())
# 부모 자식간의 관계
rs = [[] for _ in range(n + 1)]
v = [0] * (r+1)
rst = []
for _ in range(r):
    a, b = map(int, input().split())
    rs[a].append(b)
    rs[b].append(a)


def dfs(p, cnt):
    cnt += 1
    v[p] = 1

    if p == p2:
        rst.append(cnt)

    for i in rs[p]:
        if not v[i]:
            dfs(i, cnt)


dfs(p1, 0)

if len(rst) == 0:
    print(-1)
else:
    print(rst[0] - 1)
