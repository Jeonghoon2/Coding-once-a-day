from collections import deque
import sys

sys.setrecursionlimit(100000)


def solution(n, m, x, y, r, c, k):
    visit, miro = [[''] * m for _ in range(n)], [['.'] * m for _ in range(n)]
    x, y, r, c = x - 1, y - 1, r - 1, c - 1
    miro[x][y], miro[r][c] = 'S', 'E'

    z = k - abs(x - r) + abs(y - c)
    if z < 0 or z % 2 != 0:
        return 'impossible'

    move = [[1, 0, 'd'], [0, -1, 'l'], [0, 1, 'r'], [-1, 0, 'u']]

    d = deque()
    d.append((x, y,0))
    f_s = ''
    sub_s = ''

    while d:
        cur_x, cur_y, cnt = d.popleft()
        if miro[cur_x][cur_y] == 'E':
            for mx, my, cmd in move:
                nx = cur_x + mx
                ny = cur_y + my
                if 0 <= nx < n and 0 <= ny < m:
                    sub_s = cmd+(visit[cur_x][cur_y])[-1]
                    break

            f_s = visit[cur_x][cur_y]
            break
        for mx, my, cmd in move:
            nx = cur_x + mx
            ny = cur_y + my

            if 0 <= nx < n and 0 <= ny < m and len(visit[nx][ny]) == 0:
                visit[nx][ny] = visit[cur_x][cur_y] + cmd
                cnt += 1
                # k보다 클때
                if cnt > k:
                    return
                d.append((nx, ny, cnt))
                break

    if len(f_s) > 0:
        if len(sub_s) > 0:
            for i in range((z//2)-1):
                f_s+=sub_s
            return f_s

    return 'impossible'


print(solution(3, 4, 2, 3, 3, 1, 5))
print(solution(2, 2, 1, 1, 2, 2, 2))
