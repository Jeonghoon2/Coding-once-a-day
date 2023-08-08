from collections import deque


def solution(x, y, n):
    if x == y:
        return 0

    visit = [0] * int(y + 1)
    d = deque()
    d.append(x)
    visit[x] = 0

    while d:
        cur_n = d.popleft()

        for i in (cur_n + n, cur_n * 2, cur_n * 3):
            if i == y:
                return visit[cur_n] + 1
            if 1000000 > i >= 0 and i <= y and not visit[i]:
                d.append(i)
                visit[i] += visit[cur_n] + 1
    return -1


x, y, n = 10, 40, 5
print(solution(x, y, n))
