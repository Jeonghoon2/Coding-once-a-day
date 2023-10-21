import sys
from collections import deque

sys.stdin = open('in5.txt', 'r')

n, m = map(int, input().split())

p = list(map(int, input().split()))

d = deque()

for i, k in enumerate(p):
    d.append((i, k))

cnt = 1
while True:
    cur_i, cur_p = d.popleft()

    warring_point = max(d, key=lambda x: x[1])[1]

    if cur_p < warring_point:
        d.append((cur_i, cur_p))
        continue
    else:
        if m == cur_i:
            print(cnt)
            break
    cnt += 1
