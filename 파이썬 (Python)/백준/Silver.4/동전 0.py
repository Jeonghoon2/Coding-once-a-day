n,k = map(int, input().split())
a = []
cnt = 0
for _ in range(n):
    a.append(int(input()))
a.sort(reverse=True)
for unit in a:
    cnt += k // unit
    k = k % unit
print(cnt)
