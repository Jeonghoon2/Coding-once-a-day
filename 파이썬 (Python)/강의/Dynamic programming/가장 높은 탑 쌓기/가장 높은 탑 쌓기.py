import sys

sys.stdin = open('in5.txt', 'r')

if __name__ == '__main__':
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    # 밑면이 좁은 벽돌 위에 밑면 넓은 벽돌은 놓을 수 없다.
    arr.sort(key=lambda x: x[0], reverse=True)

    # 넓이, 높이, 무게
    a, h, w = [], [], []

    for ai, hi, wi in arr:
        a.append(ai)
        h.append(hi)
        w.append(wi)
    dp = [0] * n
    dp[0] = h[0]

    for i in range(1, n):
        for j in range(0, i):

            # 무게가 무거운 벽돌을 무게가 가벼운 벽돌 위에 놓을 수 없다.
            if w[i] > w[j]:
                dp[i] = max(h[i], dp[i])
            else:
                dp[i] = max(dp[i], dp[j] + h[i])

    print(max(dp))
