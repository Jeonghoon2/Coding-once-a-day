T = int(input())

for idx in range(1, T + 1):
    day = int(input())
    answer = 0
    prices = list(map(int, input().split()))
    s_price = 0

    for p in prices[::-1]:
        if s_price <= p:
            s_price = p
        else:
            answer += s_price - p

    print("#{} {}".format(idx, answer))
