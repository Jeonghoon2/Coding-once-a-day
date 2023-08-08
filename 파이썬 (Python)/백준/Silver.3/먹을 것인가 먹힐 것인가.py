for _ in range(int(input())):
    N, M = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    answer =0

    def bs(n):
        start, end = 0, M-1
        res = 0
        while start <= end:
            mid = (start + end) // 2

            if b[mid] < n:
                res = mid
                start = mid + 1
            else:
                end = mid-1
        return res + 1


    for i in a:
        if i > b[0]:
            answer += bs(i)

    print(answer)


