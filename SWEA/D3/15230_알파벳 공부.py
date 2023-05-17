T = int(input())
answer = "abcdefghijklmnopqrstuvwxyz"
for idx in range(1, T+1):

    st = input()
    cnt = 0

    for i, s in enumerate(st):
        if s == answer[i]:
            cnt += 1
        else:
            break

    print("#{} {}".format(idx, cnt))
