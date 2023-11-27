n = int(input())

l = []

for i in range(n):
    l.append(list(map(int, input().split())))

dp = [1] * n

l.sort(key=lambda x: x[0])
print(l)

for i in range(1, n):
    for j in range(0, i):
        if l[j][1] < l[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
