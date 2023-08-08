def solution(a, b, n):
    answer = 0
    while n >= a:
        s,e = n%a, (int(n/a))*b
        n = s + e
        answer += e
    return answer
print(solution(2, 1, 20))