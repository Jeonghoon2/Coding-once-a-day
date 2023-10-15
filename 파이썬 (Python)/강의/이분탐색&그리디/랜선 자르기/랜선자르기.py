import sys

sys.stdin = open('in0.txt', 'r')


def solution():
    k, n = map(int, input().split())
    ans = 0
    lens = []

    for _ in range(k):
        lens.append(int(input()))

    s, e = 0, max(lens)

    while s <= e:
        cnt = 0
        mid = (s + e) // 2

        for i in lens:
            cnt += i // mid

        if cnt == n:
            ans = max(ans, mid)

        if cnt > n:
            s = mid + 1
        else:
            e = mid - 1

    return ans


print(solution())
