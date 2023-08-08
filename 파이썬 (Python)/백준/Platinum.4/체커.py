from collections import deque
import sys
sys.setrecursionlimit(10**7)
move = [[1, 0], [-1, 0], [0, 1], [0, -1]]

t = int(input())

position = []

d = deque()
answer = [0]
for _ in range(t):
    in_x, in_y = map(int, input().split())
    d.append([in_x, in_y])


def dfs(x, y, visit, cnt):
    if [x, y] == d[0]:
        return cnt

    for mx, my in move:
        nx, ny = x + mx, y + my

        if [nx, ny] not in visit and 0 <= nx < 1000000 and 0 <= ny < 1000000:
            visit.append([nx, ny])
            dfs(nx, ny, visit, cnt + 1)


while d:
    start_x, start_y = d.popleft()
    dfs(start_x, start_y, [[start_x, start_y]], 0)
