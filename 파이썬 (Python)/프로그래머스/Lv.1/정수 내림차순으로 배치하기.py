def solution(n):
    l = list(str(n))
    l.sort(reverse=True)
    answer = int("".join(l))
    return answer