import sys

sys.stdin = open('in1.txt', 'r')

if __name__ == '__main__':
    n = int(input())

    arr = [0] * (n + 1)
    arr[1] = 1
    arr[2] = 2

    for i in range(3, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]

    print(arr[n])
