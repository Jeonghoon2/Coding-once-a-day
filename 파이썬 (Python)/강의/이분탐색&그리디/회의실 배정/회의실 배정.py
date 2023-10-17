import sys

sys.stdin = open('in2.txt', 'r')

n = int(input())

meetings = []

for _ in range(n):
    meetings.append(list(map(int, input().split())))

meetings.sort(key=lambda x: (x[1], x[0]))

end_time = 0
cnt = 0
for s, e in meetings:
    if end_time <= s:
        cnt += 1
        end_time = e

print(cnt)
