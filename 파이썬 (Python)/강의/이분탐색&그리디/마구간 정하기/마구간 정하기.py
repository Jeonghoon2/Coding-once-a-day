import sys

sys.stdin = open('in5.txt', 'r')


def solution():
    n, c = map(int, input().split())

    x = []

    for _ in range(n):
        x.append(int(input()))

    x.sort()

    s, e = min(x), max(x)
    ans = 0
    while s <= e:
        mid = (s + e) // 2

        batch = 1
        l, r = 0, 1

        while r < n:
            if x[r] - x[l] >= mid:
                batch += 1
                l = r
                r = r + 1
            else:
                r += 1

        if batch >= c:
            ans = mid
            s = mid + 1
        else:
            e = mid - 1

    return ans


print(solution())
