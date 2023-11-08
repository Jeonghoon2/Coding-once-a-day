import sys

sys.stdin = open('in1.txt', 'r')

if __name__ == '__main__':

    for tc in range(1, int(input())+1):
        n = int(input())

        arr = [list(map(int, input())) for _ in range(n)]
        rst = 0

        s, e = n // 2, n // 2

        for i in range(n):
            for j in range(s, e + 1):
                rst += arr[i][j]

            if i < n // 2:
                s, e = s - 1, e + 1
            else:
                s, e = s + 1, e - 1

        print(f'#{tc} {rst}')
