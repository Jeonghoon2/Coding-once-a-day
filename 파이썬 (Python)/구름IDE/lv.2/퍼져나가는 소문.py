from collections import deque

d = dict()


def bfs():
    de = deque()

    for i in d.get(1):
        de.append(i)

    visit = [1]

    while de:
        cur_i = de.popleft()
        visit.append(cur_i)
        for j in d.get(cur_i):
            if j not in visit:
                if j not in de:
                    de.append(j)

    return len(visit)


def relation(u, v):
    if u not in d:
        s = set()
        s.add(v)
        d[u] = s
    else:
        s = d.get(u)
        s.add(v)
        d[u] = s

    if v not in d:
        s = set()
        s.add(u)
        d[v] = s
    else:
        s = d.get(v)
        s.add(u)
        d[v] = s


def sol():
    N = int(input())
    M = int(input())

    if N == 1:
        return 1

    for _ in range(M):
        u, v = map(int, input().split())
        relation(u, v)

    return bfs()

print(sol())

