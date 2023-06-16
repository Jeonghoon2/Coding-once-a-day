n, m = map(int, input().split())
trees = list(map(int, input().split()))
low, high = 1, max(trees)

while low <= high:
    mid = (low + high) // 2
    log = 0

    for i in trees:
        if i >= mid:
            log += i - mid

    if log >= m:
        low = mid +1
    else:
        high = mid - 1


print(high)