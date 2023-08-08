# A번 참가자와 B번 참가자는 서로 붙게 되기 전까지 항상 이긴다고 가정합니다.
# N : 참가자 수

# 첫번째 시간초과... Too Many..
def solution(n, a, b):
    answer = 0
    # 게임 순서
    game_trun = 0
    # 대진 우승자
    game_winner = []
    # 게이머
    gammer = []

    # 대진표 제작
    for i in range(1, int(n / 2) + 1):
        i = i * 2
        gammer.append([i - 1, i])

    while True:

        game_trun += 1

        # 게임 우승자에 A와 B가 있을 경우
        if [a, b] in gammer:
            return game_trun
        else:
            for i in gammer:
                if a in i:
                    idx = i.index(a)
                    game_winner.append(i[idx])
                elif b in i:
                    idx = i.index(b)
                    game_winner.append(i[idx])
                else:
                    game_winner.append(i.pop())

        gammer = []

        for i in range(int(len(game_winner) / 2)):
            f = game_winner.pop(0)
            s = game_winner.pop(0)
            gammer.append([f, s])

    return answer


# 두번째 시도 27번 부터 시간 초과
def solution2(n, a, b):
    gammer = []
    turn = 0
    for i in range(1, n + 1):
        gammer.append(i)

    while True:
        turn += 1

        for i in range(int(len(gammer) / 2)):
            f = gammer.pop(0)
            s = gammer.pop(0)

            if f == a and s == b:
                return turn
            elif s == a and f == b:
                return turn
            else:
                if f == a or s == a:
                    gammer.append(a)
                elif f == b or s == b:
                    gammer.append(b)
                else:
                    gammer.append(f)
    return turn


# 세번째 시도 누가 이기나 해보자..
# 문제를 제대로 읽자..
# 각 게임에서 이긴 사람은 다음 라운드에 진출할 수 있습니다.
# 이때, 다음 라운드에 진출할 참가자의 번호는 다시 1번부터 N/2번을 차례대로 배정받습니다.
# 처음 라운드에서 A번을 가진 참가자는 경쟁자로 생각하는 B번 참가자와 몇 번째 라운드에서 만나는지


def solution3(n, a, b):
    turn = 0
    while a != b:
        turn += 1
        a, b = (a + 1) // 2, (b + 1) // 2
    return turn


print(solution3(8, 1, 4))
