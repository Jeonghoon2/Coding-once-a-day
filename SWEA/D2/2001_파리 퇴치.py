T = int(input())

for idx in range(T):
    N, M = map(int, input().split())
    maps = []
    sums = 0
    for _ in range(N):
        maps.append(list(map(int, input().split())))


    def sums_n(x, y):

        tmp = 0
        for _ in range(M):
            tmp += sum(maps[x][y:y + M])
            x += 1

        return tmp


    for i in range(N - (M-1)):
        for j in range(N - (M-1)):
            sums = max(sums, sums_n(i, j))

    print("#" + str(idx+1) + " " + str(sums))
