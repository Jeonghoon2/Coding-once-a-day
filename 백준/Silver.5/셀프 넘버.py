nums = set(range(1, 10001))
s_nums = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    s_nums.add(i)

self_num = sorted(nums - s_nums)

for i in self_num:
    print(i)
