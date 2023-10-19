import sys

sys.stdin = open('in3.txt', 'r')

n = int(input())

p = []

for _ in range(n):
    p.append(list(map(int, input().split())))

p.sort(key=lambda x: -x[0])

height, weight = 0, 0
cnt = 0
for h, w in p:
    if height == 0:
        height, weight = h, w
        cnt += 1
    else:
        if height < h or weight < w:
            cnt += 1
            height, weight = h, w

print(cnt)