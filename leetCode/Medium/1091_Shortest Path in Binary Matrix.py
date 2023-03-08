# 상하 좌우 대각선으로 움직여야 한다.
# 출발지 top-left 맨위 좌측 끝
# 도착지 bottom-right 맨아래 우측 끝

# BFS로 풀이

from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid):
        shortest_path_len = -1
        row, col = len(grid), len(grid[0])

        if grid[0][0] != 0: return -1
        visited = [[False] * col for _ in range(row)]

        d = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        q = deque()
        q.append((0, 0, 1))
        visited[0][0] = True

        while q:
            cur_r, cur_c, cur_count = q.popleft()

            if row-1 == cur_r and col-1 == cur_c:
                shortest_path_len = cur_count
                break
            for dr, dc in d:
                next_r = cur_r + dr
                next_c = cur_c + dc

                if 0 <= next_r < row and 0 <= next_c < col:
                    if grid[next_r][next_c] == 0 and not visited[next_r][next_c]:
                        q.append((next_r, next_c, cur_count + 1))
                        visited[next_r][next_c] = True

        return shortest_path_len


grid1 = [[0, 1], [1, 0]]
grid2 = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
print(Solution().shortestPathBinaryMatrix(grid2))
