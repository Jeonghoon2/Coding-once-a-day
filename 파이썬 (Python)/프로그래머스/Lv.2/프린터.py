# 대기 목록 1 <= N <= 100개
from collections import deque
def solution(priorities, location):
    answer = 0

    deq = deque([(v, i) for i, v in enumerate(priorities)])

    while deq:
        i = deq.popleft()
        if deq and max(deq)[0] > i[0]:
            deq.append(i)
        else:
            answer += 1
            if i[1] == location:
                break

    return answer


print(solution([1, 1, 9, 1, 1, 1], 0))
