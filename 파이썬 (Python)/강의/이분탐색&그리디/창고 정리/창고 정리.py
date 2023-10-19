import sys

sys.stdin = open('in1.txt', 'r')

n = int(input())

l = list(map(int, input().split()))

m = int(input())

l.sort()

print(l)

for _ in range(m):
    l[0] += 1
    l[-1] -= 1

    l.sort()

print(max(l) - min(l))
