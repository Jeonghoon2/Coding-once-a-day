# n은 할수 있는 작업량
# works 남은 작업량
# n의 수만큼 works의 작업을 줄인다.
# Solution 1. works의 가장 큰수 부터 줄인다.
# 1 <= works <= 20,000, works <= 50,000
# N <= 1,000,000
import heapq


def solution(n, works):
    answer = 0

    for i in range(len(works)):
        works[i] *= -1


    heapq.heapify(works)

    for i in range(n):
        max_work = heapq.heappop(works)

        if max_work >= 0:
            break
        max_work += 1
        heapq.heappush(works,max_work)

    for i in works:
        i *= -1
        answer += i*i

    return answer


n, works = 3, [1, 1]
print(solution(n, works))
