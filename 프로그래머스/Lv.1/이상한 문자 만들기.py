def solution(s):
    list = s.split(' ')
    answer = ''

    for i in list:
        for j in range(len(i)):
            if j%2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer += ' '
    return answer[0:-1]



print(solution("try hello world"))
