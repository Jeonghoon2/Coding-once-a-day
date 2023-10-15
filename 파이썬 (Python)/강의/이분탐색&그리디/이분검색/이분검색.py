import sys

sys.stdin = open('in1.txt', 'r')


def solution():
    n, m = map(int, input().split())

    arr = sorted(list(map(int, input().split())))

    s, e = 0, n - 1

    while s <= e:
        mid = (s + e) // 2
        if arr[mid] == m:
            return mid + 1

        elif arr[mid] > m:
            e = mid - 1
        else:
            s = mid + 1


print(solution())
