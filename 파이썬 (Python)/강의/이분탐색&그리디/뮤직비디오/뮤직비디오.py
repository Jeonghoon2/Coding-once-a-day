import sys

sys.stdin = open('in2.txt', 'r')


def count(c):
    cnt = 0
    res = 0

    for i in arr:
        if res + i > c:
            cnt += 1
            res = i
        else:
            res += i

    if res > 0:
        cnt += 1

    return cnt


n, m = map(int, input().split())
arr = list(map(int, input().split()))

s, e = 1, sum(arr)
ans = 0
while s <= e:
    mid = (s + e) // 2

    if count(mid) <= m:
        ans = mid
        e = mid - 1
    else:
        s = mid + 1

print(ans)
