# 1 <= n <= 200

from collections import deque


def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]

    def bfs(idx):

        d = deque()
        d.append(idx)
        visited[idx] = True

        while d:
            cur_p = d.popleft()

            for i, bo in enumerate(computers[cur_p]):
                if not visited[i]:
                    if bo == 1:
                        d.append(i)
                        visited[i] = True

    for i in range(n):
        if not visited[i]:
            answer += 1
            bfs(i)

    return answer


n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n, computers))
