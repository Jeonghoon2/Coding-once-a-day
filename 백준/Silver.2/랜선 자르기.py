k, n = map(int, input().split())
lan = []


def calc(start, end):
    if end - start <= 1:
        return start
    mid = (start + end) // 2
    rst = 0
    for item in lan:
        rst += (item // mid)
    if rst < n:
        return calc(start, mid)
    else:
        return calc(mid, end)


for _ in range(k):
    lan.append(int(input()))

print(calc(1, max(lan) + 1))
