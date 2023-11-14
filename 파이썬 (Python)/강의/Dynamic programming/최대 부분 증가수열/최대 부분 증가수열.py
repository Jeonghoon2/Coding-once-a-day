import sys

sys.stdin = open('in5.txt', 'r')

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    dy = [0] * n

    dy[0] = 1

    for i in range(1, n):
        sub = i - 1
        while True:

            if sub < 0:
                break
            else:
                if arr[i] > arr[sub]:
                    dy[i] = max(dy[i], dy[sub] + 1)
                    sub -= 1
                else:
                    dy[i] = max(dy[i], 1)
                    sub -= 1

    print(max(dy))