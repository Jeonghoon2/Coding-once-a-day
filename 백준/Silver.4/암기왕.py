t = int(input())  # 테스트 케이스
for _ in range(t):
    answer = []
    M = int(input())
    note1 = list(map(int, input().split()))
    note1.sort()
    X = int(input())
    note2 = list(map(int, input().split()))


    def bs(n):
        start, end = 0, M - 1

        while start <= end:
            mid = (start + end) // 2
            if note1[mid] == n:
                answer.append(1)
                return
            elif note1[mid] < n:
                start = mid + 1
            else:
                end = mid - 1

        answer.append(0)


    for i in note2:
        bs(i)

    for i in answer:
        print(i)
