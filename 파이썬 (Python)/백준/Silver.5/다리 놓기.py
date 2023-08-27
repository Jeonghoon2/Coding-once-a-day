def factorial(n):
    num = 1
    for i in range(1, n + 1):
        num *= i
    return num

for _ in range(int(input())):

    N, M = map(int, input().split())

    bridge = factorial(M) // (factorial(N) * factorial(M-N))

    print(bridge)