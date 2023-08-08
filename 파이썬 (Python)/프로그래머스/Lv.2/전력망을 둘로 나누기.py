from collections import deque


def solution(n, wires):
    answer = 0

    grap = [[] for _ in range(n + 1)]

    for a, b in wires:
        grap[a].append(b)
        grap[b].append(a)

    def bfs(start):
        visit = [0] * (n + 1)
        q = deque([start])
        visit[start] = 1
        cnt = 1
        while q:
            s = q.popleft()

            for i in grap[s]:
                if not visit[i]:
                    q.append(i)
                    visit[i] = 1
                    cnt += 1

        return cnt

    answer = n
    for a, b in wires:
        grap[a].remove(b)
        grap[b].remove(a)

        answer = min(abs(bfs(a) - bfs(b)), answer)

        grap[a].append(b)
        grap[b].append(a)

    return answer


print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
