from collections import deque
import sys

sys.stdin = open('in5.txt', 'r')

n, k = map(int, input().split())

q = deque(range(1,n+1))

tmp = []
while q:
    for _ in range(k-1):
        cur = q.popleft()
        q.append(cur)
    q.popleft()

    if len(q) == 1:
        print(cur)
        break
