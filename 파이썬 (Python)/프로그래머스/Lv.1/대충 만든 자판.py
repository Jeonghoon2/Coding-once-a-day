def solution(keymap, targets):

    answer = []
    t_idx = 0
    s_idx = 0

    cnt = []

    while True:

        if len(targets) == t_idx:
            break

        # 첫번째 단어 저장
        target = targets[t_idx]

        # 단어 한글자 씩
        a = target[s_idx]

        # 길이 저장
        a_d = []
        for i in keymap:
            if a in i:
                a_d.append(int(i.find(a)) + 1)
        s_idx += 1


        # 최소 길이 저장
        if len(a_d) != 0:
            cnt.append(min(a_d))
        else:
            cnt.append(-1)

        if len(target) == s_idx:
            t_idx += 1
            s_idx = 0
            if sum(cnt) < 0:
                answer.append(-1)
            else:
                answer.append(sum(cnt))
            cnt.clear()

    return answer


keymap = ["ABACD", "BCEFD"]
keymap2 = ["AA"]
targets = ["ABCD", "AABB"]
targets2 = ["B"]
print(solution(keymap2, targets2))
