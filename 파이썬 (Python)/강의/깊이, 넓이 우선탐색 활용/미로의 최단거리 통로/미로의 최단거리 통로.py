import sys
from collections import deque

sys.stdin = open('in5.txt', 'r')


def bfs(x, y):
    ans = -1

    d = deque()
    d.append((x, y, 0))

    visit = [[x, y]]

    move = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    while d:
        cur_x, cur_y, cur_c = d.popleft()

        if cur_x == 6 and cur_y == 6:
            return cur_c

        for mx, my in move:
            nx, ny = cur_x + mx, cur_y + my

            if 0 <= nx < 7 and 0 <= ny < 7:
                if miro[nx][ny] == 0 and [nx, ny] not in visit:
                    d.append((nx, ny, cur_c + 1))
                    visit.append([nx,ny])

    return ans


if __name__ == '__main__':

    miro = []

    for _ in range(7):
        miro.append(list(map(int, input().split())))

    print(bfs(0, 0))
