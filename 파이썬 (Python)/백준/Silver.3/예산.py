n = int(input())
m = list(map(int, input().split()))
a = int(input())

start, end = 0, max(m)

while start <= end:
    mid = (start + end) // 2
    total = 0 # 총 지출양

    for i in m:
        if i > mid:
            total += mid
        else:
            total += i
    if total <= a:
        start = mid + 1
    else:
        end = mid -1

print(end)