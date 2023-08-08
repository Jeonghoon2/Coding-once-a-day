N = int(input())
rooms = []
answer = 0

for _ in range(N):
    rooms.append(list(map(int, input().split())))

rooms.sort(key=lambda a: (a[1], a[0]))

l_t = 0

for s, l in rooms:
    if s >= l_t:
        answer += 1
        l_t = l

print(answer)
