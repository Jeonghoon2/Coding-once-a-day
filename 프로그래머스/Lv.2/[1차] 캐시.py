# 캐시에 대한 이해도가 있어야 풀수 있는 문제

def solution(cacheSize, cities):
    answer = 0
    cache = []
    for i in cities:
        i = i.lower()
        # cacheSize가 0이 아닐때
        if cacheSize >= 1:
            # cache에 i가 안들어 있을 때
            if i not in cache:
                # cache가 꽉 찼을 경우
                if len(cache) == cacheSize:
                    cache.pop(0)
                cache.append(i)
                answer += 5
            else:
                cache.pop(cache.index(i))
                cache.append(i)
                answer += 1
        else:
            answer += 5
    return answer


cacheSize = 3
cities = ["Jeju", "Pangyo", "NewYork", "newyork"]
print(solution(cacheSize, cities))
