from gettext import find


def solution(s):
    s = s.lower()
    if s.count('p') == s.count('y'):
        answer = True
    else:
        answer = False
    return answer


print(solution(input()))
