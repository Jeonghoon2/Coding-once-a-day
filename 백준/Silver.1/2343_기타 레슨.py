n, m = map(int, input().split())
blueRay = list(map(int, input().split()))

answer = 0

left, right = max(blueRay), sum(blueRay)

while left <= right:
    mid = (left + right) // 2

    cnt, s = 0, 0
    for i in range(n):
        if s + blueRay[i] > mid:
            cnt += 1
            s = 0

        s += blueRay[i]

    if s:
        cnt += 1

    if cnt > m:
        left = mid + 1

    else:
        right = mid - 1
        answer = mid
print(answer)
