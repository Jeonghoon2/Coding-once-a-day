def check(n, mid, candies):
    total = 0

    if mid == 0:
        return False

    for c in candies:
        total += c // mid

    if total >= n:
        return True
    else:
        return False


n, m = map(int, input().split())
candies = list(map(int, input().split()))

start, end = 1, int(1e9)
result = 0

while start <= end:
    mid = (start + end) // 2

    if check(n, mid, candies):
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)
