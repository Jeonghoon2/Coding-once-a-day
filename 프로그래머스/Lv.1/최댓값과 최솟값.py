def solution(s):
    s.replace(' ','')
    return min(s),max(s)
    
print(solution("1 2 3 4"))