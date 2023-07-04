# 입력은 여러 개의 테스트 케이스로 이루어져 있다.
# 상근이와 선영이가 같은 CD를 가지고 있는 경우는 없다. = Set 필요 X
# 오름차순으로 주어진다 = sort 필요 X
# N과 M은 최대 백만개 = O(N)으로 해결 필요

while True:
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        break

    arr = []
    for _ in range(n + m):
        arr.append(int(input()))

    # arr의 0번째 부터 n번 까지는 n, arr의 m번부터 끝까지는 m
    n, m = arr[0:n], arr[m:]
    cnt = 0

    for cd in m:
        start, end = 0, len(n) - 1

        while start <= end:
            mid = (start + end) // 2

            if n[mid] == cd:
                cnt += 1
                break
            else:
                if n[mid] > cd:
                    end = mid - 1
                else:
                    start = mid + 1

    print(cnt)

