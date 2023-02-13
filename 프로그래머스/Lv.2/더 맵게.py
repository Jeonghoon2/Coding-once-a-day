# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    if scoville[0] > K:
        return answer

    while scoville:
        if len(scoville) == 1:
            break
        low_scoville = heapq.heappop(scoville)
        if low_scoville < K:
            answer += 1
            heapq.heappush(scoville, low_scoville + int(heapq.heappop(scoville)*2))
        else:
            break

    if scoville[0] < K:
        return -1
    return answer


print(solution([1, 2, 3], 11))
