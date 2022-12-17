# 스파이는 매일 다른 옷을 입어야 한다.
# 옷을 종류별로 구분하여 몇개의 조합이 가능한지 계산한다.


from collections import Counter
from functools import reduce


def solution(clothes):
    # 1. 옷을 종륩별로 구분한다.
    hash_map = {}
    for clothe, type in clothes:
        hash_map[type] = hash_map.get(type, 0) + 1

    # 2. 입지 않는 경우를 계산하여 모든 조합을 계산한다.
    answer = 1
    for type in hash_map:
        answer *= hash_map[type] + 1

    # 3. 아무 종류의 옷도 입지 않은 경우를 제외 한다.
    return answer - 1


def solution2(clothes):
    counte = Counter([type for clothe, type in clothes])
    return reduce(lambda acc, cur : acc * (cur + 1), counte.values() ,1) -1
print(solution2([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])) 