from collections import deque


def find(N, K):
    answer = 0
    visit = [0] * 100001
    if N == K:
        return 0
    d = deque()
    d.append(N)

    while d:
        cur_n = d.popleft()

        for next_n in (cur_n - 1, cur_n + 1, cur_n * 2):
            if next_n == K:
                return visit[cur_n] +1
            if 0 <= next_n <= 100000 and visit[next_n] == 0:
                d.append(next_n)
                visit[next_n] = visit[cur_n] + 1

    return answer


# 수빈이가 있는 위치 N, 동생이 있는 위치 K
N, K = map(int, input().split())

print(find(N, K))
