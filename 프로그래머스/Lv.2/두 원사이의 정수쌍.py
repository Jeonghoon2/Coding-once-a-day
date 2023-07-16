def solution(r1, r2):
    answer = 0

    min_y, max_y = r1, r2

    for i in range(0, r2):
        # max를 줄여서 범위 줄이기
        while r2 ** 2 < max_y ** 2 + i ** 2:
            max_y -= 1
        # min을 줄여서 범위 늘리기
        # 1사분면 위의 점들만 count해야 하기 때문에 min_y은 양수로 유지 되어야 한다.
        while min_y-1 and r1 ** 2 <= (min_y - 1) ** 2 + i ** 2:
            min_y -= 1
        answer += max_y - min_y + 1
    return answer * 4


print(solution(2, 3))
