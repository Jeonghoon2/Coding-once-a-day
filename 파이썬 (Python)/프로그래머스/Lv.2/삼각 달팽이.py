# 하 -> 우 -> 상
def solution(n):
    answer = []

    snail = [[0] * i for i in range(1, n + 1)]
    x, y = -1, 0
    num = 1

    for i in range(n):
        for _ in range(i, n):
            # 하
            if i % 3 == 0:
                x += 1
            # 우
            elif i % 3 == 1:
                y += 1
            # 대각선 위
            elif i % 3 == 2:
                x -= 1
                y -= 1

            snail[x][y] = num
            num += 1

    for i in snail:
        answer += i

    return answer


n = 6
print(solution(n))
