op = list(input().split('-'))
answer = 0
for i in range(0, len(op)):
    arr = op[i].split('+')
    sums = 0
    for j in arr:
        sums += int(j)

    if i == 0:
        op[i] = sums
        continue

    sums = str(sums * -1)
    op[i] = sums


for i in op:
    answer += int(i)

print(answer)