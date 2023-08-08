for _ in range(int(input())):
    # 층수
    k = int(input())
    # 호수
    n = int(input())

    floor = [x for x in range(1, n+1)]

    # 층 계산
    for _ in range(k):
        before_floor = floor.copy()
        # 호 계산
        for i in range(n):
            floor[i] = sum(before_floor[0:i+1])

    print(floor[n-1])


