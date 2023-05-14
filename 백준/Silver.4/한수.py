N = int(input())

cnt = 0

for i in range(1, N+1):
    n_list = list(map(int, str(i)))
    # 100 보다 작으면 무조건 한수
    if i < 100:
        cnt += 1
    # 1000보다 작거나의 조건으로 인해 N의 자리수는 3자리 이 조건에만 만족
    elif n_list[0]-n_list[1] == n_list[1]-n_list[2]:
        cnt += 1
print(cnt)