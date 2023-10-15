N, D = map(int, input().split())
p = sorted(list(map(int, input().split())))

start, end = 0,0
length = 0

while start <N and end <N:

    if p[end] - p[start] <= D:
        length = max(length, end-start + 1)
        end +=1
    else:
        start += 1

print(N-length)
