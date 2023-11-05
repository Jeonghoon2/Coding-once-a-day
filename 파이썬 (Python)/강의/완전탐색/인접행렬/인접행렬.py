import sys

sys.stdin = open('in1.txt', 'r')

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = [[0] * 6 for _ in range(n)]
    for _ in range(m):
        a, b, d = map(int, input().split())

        arr[a-1][b-1] = d

    for i in arr:
        print(*i)
