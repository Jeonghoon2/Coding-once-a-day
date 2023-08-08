# 문제를 읽었을 때 Binary Search가 가장 먼저 생각난다.
# 제한 조건 1 ≤ m ≤ n ≤ 100,000 , 최악의 상황 O(n^2) = 10,000,000,000 시간 초과,해결 방안 O(n) 또는 O(nlogn)

# 테케 3개 시간 초과
def solution(n, m, section):
    answer = 0

    # 왼쪽 방문
    l_visit = []
    # 오른쪽 방문
    r_visit = []

    lp, rp = 0, n

    while True:
        if lp > rp or rp < lp:
            break
        # left
        # 이미 칠해져있을 때
        if lp not in section:
            l_visit.append(lp)
            lp += 1
        else:
            for i in range(m):
                l_visit.append(lp)
                lp += 1
            answer += 1

        # right
        # 이미 칠해져있을 때
        if rp not in section:
            r_visit.append(rp)
            rp -= 1
        else:
            if rp < lp:
                break
            for i in range(m):
                r_visit.append(rp)
                rp -= 1
            answer += 1

    return answer


# 두번째 쉽게 생각 하자구
def solution2(n, m, section):
    answer = 0
    p = 0
    for i in section:
        if p > i:
            pass
        else:
            p = i + m
            answer += 1

    return answer


n = 8
m = 4
select = [2, 3, 6]

print(solution2(n, m, select))
