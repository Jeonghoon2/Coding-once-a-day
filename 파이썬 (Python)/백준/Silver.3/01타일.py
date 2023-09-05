def solution(n):
    arr = [0] * 1000001
    arr[1] = 1
    arr[2] = 2
    if n > 2:
        for i in range(3, n + 1):
            arr[i] = (arr[i - 1] + arr[i - 2]) % 15746

    return arr[n]

print(solution(int(input())))
