import sys

sys.stdin = open('in5.txt', 'r')

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    dy = [0] * n

    dy[0] = 1

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j]:
                dy[i] = max(dy[j] + 1, dy[i])
            else:
                dy[i] = max(dy[i], 1)

    print(max(dy))
