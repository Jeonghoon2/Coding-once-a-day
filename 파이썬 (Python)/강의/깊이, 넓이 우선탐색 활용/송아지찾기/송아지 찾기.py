import sys
from collections import deque

sys.stdin = open('in5.txt', 'r')


def bfs(s, e):
    global rst
    d = deque()
    d.append((s, 0))
    visit = []
    visit.append(s)

    while d:
        cur_p, cur_c = d.popleft()

        if cur_p == e:
            rst =  cur_c
            break
        for i in m:
            np = cur_p + i
            if np not in visit and 1 <= np <= 10000:
                d.append((np, cur_c + 1))


if __name__ == '__main__':
    s, e = map(int, input().split())

    m = [1, -1, 5]

    rst = int(1e9)

    bfs(s, e)

    print(rst)
