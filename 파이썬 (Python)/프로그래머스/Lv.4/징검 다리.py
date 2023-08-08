def solution(distance, rocks, n):

    answer = 0
    start, end = 0, distance

    rocks.sort()

    while start <= end:
        mid = (start+end) // 2
        remove_stone = 0
        pre_stone = 0

        for rock in rocks:
            if rock - pre_stone < mid:
                remove_stone += 1
            else:
                pre_stone = rock

            if remove_stone > n:
                break

        if remove_stone > n:
            end = mid -1
        else:
            answer = mid
            start = mid + 1

    return answer


print(solution(25, [2, 14, 11, 21, 17], 2))
