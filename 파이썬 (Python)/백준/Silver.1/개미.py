import sys

input = sys.stdin.readline

ans = []

for _ in range(int(input())):
    length, ant_cnt = map(int, input().split())

    ants = []

    min_time, max_time = 0, 0
    for _ in range(ant_cnt):
        p = int(input())

        sht, lng = min(p, length - p), max(p, length - p)

        min_time, max_time = max(min_time, sht), max(max_time, lng)

    ans.append([min_time, max_time])

for answer in ans:
    print(*answer)
