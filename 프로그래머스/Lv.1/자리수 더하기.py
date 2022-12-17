def solution(n):
    answer = 0
    n = list(map(int, str(n)))
    answer = sum(n)
    return answer

print(solution(int(input())))