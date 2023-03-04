from collections import deque


# bfs
class Solution:

    def numIslands(self, grid):
        cn = 0
        visited = [[False]*len(grid[0]) for _ in range(len(grid))]

        def bfs(y, x):
            dy = [-1, 1, 0, 0]
            dx = [0, 0, -1, 1]
            visited[y][x] = True
            queue = deque()
            queue.append((y, x))
            while queue:
                cur_y, cur_x = queue.popleft()

                for i in range(4):
                    next_y = cur_y + dy[i]
                    next_x = cur_x + dx[i]
                    # Grid의 범위를 넘는 좌표 또는 0인 Vertex 방지
                    if next_x >= 0 and next_x < len(grid[0]) and next_y >= 0 and next_y < len(grid):
                        if grid[next_y][next_x] == "1" and not visited[next_y][next_x]:
                            visited[next_y][next_x] = True
                            queue.append((next_y, next_x))
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "1" and not visited[y][x]:
                    bfs(y, x)
                    cn += 1
        return cn


grid1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

grid2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
print(Solution().numIslands(grid2))
