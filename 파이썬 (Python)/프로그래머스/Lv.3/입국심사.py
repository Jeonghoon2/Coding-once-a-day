def solution(n, times):
    answer = 0

    # right는 최악의 수
    left, right = 1, max(times) * n

    while left <= right:
        mid = (left + right) // 2
        people = 0

        for time in times:

            people += mid//time

            # 모든 심사를 하지 않아도 mid분 동안 n명 이상의 심사를 할 수 있을 때
            if people >= n:
                break

        # 심사한 사람의 수가 심사 받아야할 사람의 수(n) 보다 많거나 같은 경우
        if people >= n:
            answer = mid
            right = mid - 1
        # 심사한 사람의 수가 심사 받아야할 사람의 수(n)보다 적은 경우
        elif people < n:
            left = mid + 1

    return answer


print(solution(6, [7, 10]))
