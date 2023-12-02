def solution(sequence, k):
    answer = []
    sum = 0
    s, e = 0, -1

    while True:
        if sum < k:
            e += 1
            if e >= len(sequence):
                break
            sum += sequence[e]
        else:
            sum -= sequence[s]
            if s >= len(sequence):
                break
            s += 1

        if sum == k:
            answer.append([s, e])

    return answer


print(solution([1, 1, 1, 2, 3, 4, 5], 5))
