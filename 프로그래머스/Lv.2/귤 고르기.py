
# Counter 함수를 사용하여 총 개수(total)을 0으로 지정해준다.
# count 에는 tangerine을 개수 별로 정리 한다.
# enumerate를 사용하여 value를 기준으로 오름차순을 해서 index each로 나눈다.


def solution(k, tangerine):
    from collections import Counter
    total, count = 0, Counter(tangerine)
    for index, each in enumerate(sorted(count.values(), reverse=True)):
        total += each
        if total >= k:
            return index + 1
    return k

print(solution(6,[1, 3, 2, 5, 4, 5, 2, 3]))