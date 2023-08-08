# 사람은 1~N번,
# i번 사람이 돌을 인출하는데 걸리는 시간은 P[i]분

import heapq

N = int(input())
time = list(map(int, input().split()))
time_tmp = []
heapq.heapify(time)

for i in range(len(time)):
    if i == 0:
        time_tmp.append(heapq.heappop(time))
        continue
    else:
        time_tmp.append(time_tmp[i-1] + heapq.heappop(time))

print(sum(time_tmp))


