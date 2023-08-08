# I 숫자 : 삽입
# D 1   : 큐에서 최댓값을 삭제
# D -1  : 큐에서 최솟값을 삭제
import heapq


def solution(operations):
    answer = []
    heapq.heapify(answer)

    for i in operations:
        command, num = i.split()

        if command == 'I':
            heapq.heappush(answer, int(num))
        else:
            if len(answer) == 0:
                continue
            if num == '-1':
                heapq.heappop(answer)
            elif num == '1':
                answer.pop(-1)

    if len(answer) == 0:
        return [0, 0]
    return [max(answer), min(answer)]


operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
print(solution(operations))
