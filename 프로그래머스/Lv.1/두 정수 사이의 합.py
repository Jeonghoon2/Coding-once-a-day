def solution(a, b):
    if a > b:
        tmp = b
        b = a
        a = tmp
    answer = 0
    for i in range(a,b+1):
        answer += i    
    return answer