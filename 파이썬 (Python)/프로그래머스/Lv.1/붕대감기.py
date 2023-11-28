import copy

def solution(bandage, health, attacks):
    att = dict()
    max_h = copy.deepcopy(health)

    # 중복이 안되므로 바로 변수 지정 가능
    for t, d in attacks:
        att[t] = d

    # 초당 회복 연속 횟수
    s_h_c = 0
    for i in range(1, (attacks[-1])[0] + 1):

        # 공격 받을 때
        if i in att:
            health -= att.get(i)
            s_h_c = 0

            if health <= 0:
                return -1

        else:
            s_h_c += 1

            health += bandage[1]
            if s_h_c == bandage[0]:
                health += bandage[2]
                s_h_c = 0

            if health > max_h:
                health = max_h
    return health


print(solution([5, 1, 5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]]))
