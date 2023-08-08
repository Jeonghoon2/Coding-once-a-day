T = int(input())

nums_list = []
answer = []
for _ in range(T):
    nums_list.append(list(map(int, input().split())))

for nums in nums_list:
    sums = 0
    for n in nums:
        if n % 2 != 0:
            sums += n

    answer.append(sums)

for idx, a in enumerate(answer):
    print("#" + str(idx + 1), end=" ")
    print(a)
