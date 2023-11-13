import sys
from collections import deque

sys.stdin = open('in5.txt', 'r')


def bfs(x, y):
    global s
    d = deque()
    d.append((x, y, 0))

    visit = [[x, y]]

    m = [[1, 0],
         [-1, 0],
         [0, -1],
         [0, 1]]

    while d:
        cur_x, cur_y, cur_l = d.popleft()

        # 마지막 레벨일 경우
        if cur_l == (n // 2):
            continue

        for mx, my in m:
            nx, ny = cur_x + mx, cur_y + my

            if 0 <= nx < n and 0 <= ny < n and [nx, ny] not in visit:
                s += arr[nx][ny]
                visit.append([nx, ny])
                d.append((nx, ny, cur_l + 1))


if __name__ == '__main__':

    n = int(input())

    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    s = arr[n//2][n//2]
    bfs(n // 2, n // 2)
    print(s)
