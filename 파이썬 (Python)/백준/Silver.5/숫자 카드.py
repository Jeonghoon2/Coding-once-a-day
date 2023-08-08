n = int(input())
arr1 = sorted(list(map(int, input().split())))

m = int(input())
arr2 = list(map(int, input().split()))


def calc(start, end, n):
    mid = int((start + end) // 2)

    if arr1[start] == n or arr1[end] == n:
        return 1
    if end - start == 1:
        return 0

    if arr1[mid] < n:
        return calc(mid, end, n)
    else:
        return calc(start, mid, n)


answer = []
for i in arr2:
    answer.append(calc(0, len(arr1) - 1, i))

for i in answer:
    print(i, end=' ')
