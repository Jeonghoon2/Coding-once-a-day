# price 의 각 가격은 1 <= price<= 10,000
#

from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)

    while prices:
        price = prices.popleft()
        sec = 0

        for i in prices:
            sec += 1
            if price > i:
                break
        answer.append(sec)

    return answer


print(solution([1, 2, 3, 2, 3]))
