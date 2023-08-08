# 한 유저가 하루에 한 번씩 탐험할 수 있는 던전이 여러개 있다.
# 최대한 많이 탐험
# 최소 필요 필로도는 소모 피로도와 같거나 크다.
# 던전 개수 1=<K<=8 시간 복잡도 O(n^2) 가능

from itertools import permutations


def solution(k, dungeons):
    answer = -1
    st_k = k
    for i in permutations(dungeons, len(dungeons)):

        cnt = 0
        for j in i:
            c_k, c_u = j
            if c_k <= k:
                k -= c_u
                cnt += 1

        if cnt > answer:
            answer = cnt
        k = st_k

    return answer


k = 80
dungeons = [[80, 20], [50, 40], [30, 10]]
print(solution(k, dungeons))
