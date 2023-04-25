# 10101번

tmp = []
for _ in range(3):
    tmp.append(int(input()))

cnt = 1
for i in tmp:
    if cnt < tmp.count(i):
        cnt = tmp.count(i)

if sum(tmp) == 180:
    if tmp[0] == 60 and cnt == 3:
        print("Equilateral")
    elif cnt == 1:
        print("Scalene")
    elif cnt == 2:
        print("Isosceles")
else:
    print("Error")


