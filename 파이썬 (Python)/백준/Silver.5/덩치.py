N = int(input())

size = dict()
answer = []
for i in range(N):
    size[i] = list(map(int, input().split()))


def op(n):
    cur_weight, cur_height = size.get(n)
    cnt = 1
    for i in range(len(size)):
        if i == n:
            continue
        else:
            sub_weight, sub_height = size.get(i)

            if cur_weight < sub_weight and cur_height < sub_height:
                cnt += 1
            else:
                continue

    return cnt


for i in range(N):
    answer.append(op(i))

for i in answer:
    print(i, end=" ")
