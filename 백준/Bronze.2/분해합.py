n = int(input())

for i in range(1, n + 1):
    s_i = sum(map(int, str(i)))
    ss_i = i + s_i
    if ss_i == n:
        print(i)
        break
    if i == n:
        print(0)
