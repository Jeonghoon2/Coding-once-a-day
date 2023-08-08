tmp = []
while True:
    tmp = list(map(int, input().split()))

    if tmp[0] == 0:
        break

    cnt = 0
    for i in tmp:
        if cnt < tmp.count(i):
            cnt = tmp.count(i)
    m = tmp.pop(tmp.index(max(tmp)))
    if m < sum(tmp):
        if cnt == 3:
            print("Equilateral")
        elif cnt == 2:
            print("Isosceles")
        elif cnt == 1:
            print("Scalene")
    else:
        print("Invalid")
