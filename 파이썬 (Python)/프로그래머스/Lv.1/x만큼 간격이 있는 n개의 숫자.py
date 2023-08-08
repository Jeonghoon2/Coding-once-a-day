def solution(x, n):
    answer = [0]*n
    for i in range(int(n)):
        answer[i] = answer[i-1] + x
    return answer

print(solution(2,5))