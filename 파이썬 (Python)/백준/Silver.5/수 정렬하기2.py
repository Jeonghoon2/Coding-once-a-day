import heapq

N = int(input())
n_list = []

for _ in range(N):
    n_list.append(int(input()))

heapq.heapify(n_list)

for _ in range(N):
    print(heapq.heappop(n_list))
