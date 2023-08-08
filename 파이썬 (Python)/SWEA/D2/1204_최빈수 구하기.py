T = int(input())

for idx in range(1, T+1):
    i = int(input())
    n_list = list(map(int, input().split()))

    set_list = set(n_list)
    max_n = [1, 0]
    for n in set_list:
        cnt = n_list.count(n)
        if max_n[1] < cnt:
            max_n[0], max_n[1] = n, cnt

    print("#{} {}".format(idx, max_n[0]))
