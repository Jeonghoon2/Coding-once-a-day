# 빨간색과 초록생의 차이는 거의 느끼지 못한다.
# N * M - 빨강, 초록, 파랑 중 하나를 색칠한 그림

from collections import deque
import sys

sys.setrecursionlimit(1000000)

n = int(input())
arr = []
visit = []
for _ in range(n):
    arr.append(list(input().rstrip()))

move = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def common(px, py, color):
    d = deque()
    d.append((px, py))
    visit.append([px, py])

    while d:
        cx, cy = d.popleft()
        for mx, my in move:
            nx, ny = cx + mx, cy + my
            if 0 <= nx < len(arr) and 0 <= ny < len(arr[0]):
                if [nx, ny] not in visit and arr[nx][ny] == color:
                    d.append((nx, ny))
                    visit.append([nx, ny])


cnt = 0
c_cnt = 0

for i in range(len(arr)):
    for j in range(len(arr[0])):
        if [i, j] not in visit:
            common(i, j, arr[i][j])
            c_cnt += 1

visit = []
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] == 'R':
            arr[i][j] = 'G'

for i in range(len(arr)):
    for j in range(len(arr[0])):
        if [i, j] not in visit:
            common(i, j, arr[i][j])
            cnt += 1

print(c_cnt, cnt)
