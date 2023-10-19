import sys

sys.stdin = open('in5.txt', 'r')

n, m = map(int, input().split())

c = list(map(int, input().split()))
visit = [0] * n
c.sort()

cnt = 0
for i in range(0, n):
    if 0 not in visit:
        break
    f = False
    for j in range(n-1, 0, -1):
        if c[i] + c[j] <= m and visit[i] != 1 and visit[j] != 1:
            visit[i], visit[j] = 1, 1
            cnt += 1
            f = True
            break

    if not f and visit[i] == 0:
        cnt += 1

print(cnt)
