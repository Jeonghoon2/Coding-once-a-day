def solution(x):
    l = list(map(int, str(x)))
    if x%sum(l) == 0: 
        answer = True
    else:
        answer = False
    return answer