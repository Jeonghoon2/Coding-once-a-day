# 탑다운 [메모이제이션]

d = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]


print(fibo(3))

# 보텀업
# 1003번
for _ in range(int(input())):
    d = [0] * 100
    d[1] = 1
    d[2] = 1
    n = int(input())

    for i in range(3,n+1):
        d[i] = d[i-1]+ d[i-2]

    if n == 0:
        print(1,0)
    else:
        print(d[n-1],d[n])
