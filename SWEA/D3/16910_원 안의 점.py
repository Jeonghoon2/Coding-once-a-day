T = int(input())
answer = []
for _ in range(T):
    i = int(input())
    cnt = 0

    for x in range(-i, i+1):
        for y in range(-i, i+1):
            if (x ** 2) + (y ** 2) <= (i ** 2):
                cnt += 1
    answer.append(cnt)

for idx, a in enumerate(answer):
    print("#" + str(idx + 1), end=" ")
    print(a)
