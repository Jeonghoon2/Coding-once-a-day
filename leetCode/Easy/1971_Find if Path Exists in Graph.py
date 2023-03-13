from collections import deque


class Solution:
    def validPath(self, n, edges, source, destination):
        connect = dict()
        d = deque()

        if len(edges) == 0:
            return True

        for p, next_p in edges:
            if p not in connect:
                connect[p] = {next_p}
                if next_p not in connect:
                    connect[next_p] = {p}
                else:
                    connect[next_p].add(p)
            else:
                connect[p].add(next_p)
                if next_p not in connect:
                    connect[next_p] = {p}
                else:
                    connect[next_p].add(p)


        def bfs(i):
            visit = [False] * n
            d.append(i)

            while d:
                cur_p = d.popleft()

                if cur_p in connect and not visit[cur_p]:
                    for i in connect[cur_p]:
                        if i == destination:
                            return True
                        if not visit[i]:
                            d.append(i)
                visit[cur_p] = True

            return False

        return bfs(source)


n = 10
edges = [[0,7],[0,8],[6,1],[2,0],[0,4],[5,8],[4,7],[1,3],[3,5],[6,5]]
source = 7
destination = 5

print(Solution().validPath(n, edges, source, destination))
