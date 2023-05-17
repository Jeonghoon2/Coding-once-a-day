N = int(input())

for i in range(1,N+1):
    s = str(i)
    cnt = 0
    for n in s:
        if n in ['3', '6', '9']:
            cnt += 1
    if cnt > 1:
        print("-" * 2, end=' ')
        continue
    elif cnt > 0:
        print("-", end=' ')
        continue
    else:
        print(s, end= ' ')