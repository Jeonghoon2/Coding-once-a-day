import heapq

T = int(input())
A, B = list(map(int, input().split())), list(map(int, input().split()))

r_A = sorted(A, reverse=True)

heapq.heapify(B)
count = 0
for i in range(T):
    count += r_A[i] * heapq.heappop(B)



print(count)