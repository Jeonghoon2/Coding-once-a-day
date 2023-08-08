import math

T = int(input())

for idx in range(1, T + 1):
    N = int(input())
    tmp = []
    for i in range(1, int(math.sqrt(N))+1):
        if N % i == 0:
            tmp.append((i, int(N//i)))

    for i, (x,y) in enumerate(tmp):
        tmp[i] = (x-1) + (y-1)

    print("#{} {}".format(idx, min(tmp)))
