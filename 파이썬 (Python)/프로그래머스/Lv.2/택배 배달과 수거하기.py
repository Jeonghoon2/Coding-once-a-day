# n개의 집에 택배를 배달
# 모두 크기가 같은 재활용 택배 상자에 담아 배달
# 배달을 다니면서 빈 재활용 택배 상자들을 수거

def solution(cap, n, deliveries, pickups):
    i, j = n - 1, n - 1

    while i >= 0 and deliveries[i] == 0:
        i -= 1

    while j >= 0 and deliveries[j] == 0:
        j -= 1

    answer = 0

    while i >= 0 or j >= 0:
        answer += (max(i, j) + 1) * 2
        # 배달
        cur = cap
        if deliveries[i] > cur:
            deliveries[i] -= cur
        else:
            cur -= deliveries[i]
            deliveries[i] = 0
            while i >= 0 and deliveries[i] == 0:
                i -= 1

        # 수거
        cur = cap
        if pickups[j] > cur:
            pickups[j] -= cur
        else:
            cur -= pickups[j]
            pickups[j] = 0
            while j >= 0 and pickups[j] == 0:
                j -= 1

    return answer


cap = 4
n = 5
deliveries = [1, 0, 3, 1, 2]
pickups = [0, 3, 0, 4, 0]

print(solution(cap, n, deliveries, pickups))
