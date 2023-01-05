def solution(t, p):
    answer = 0

    t_list = []

    for i in range(len(list(t)) - len(list(p))+1):
        t_list.append(t[i:i+len(list(p))])

    for i in t_list:
        if int(i) <= int(p):
            answer += 1

    return answer

print(solution("500220839878", "7"))