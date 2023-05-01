# 1. 호텔 예약 시간 정렬

from heapq import heappush, heappop

def solution(book_time):
    answer = 0
    book_time = [(int(f[:2]) * 60 + int(f[3:]), int(s[:2]) * 60 + int(s[3:])) for f, s in book_time]
    book_time.sort()

    heap = []

    for f, s in book_time:
        # 최초에만 실행
        if not heap:
            heappush(heap, s+10)
            answer +=1
            continue
        # heap에 최소 시간이 입장 시간보다 작거나 같을 때
        if heap[0] <= f:
            heappop(heap)
        # 겹칠 때
        else:
            answer += 1
        heappush(heap, s + 10)

    return answer





book_time = [["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]
print(solution(book_time))
