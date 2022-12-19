# 나의 풀이 ( 시간 초과 )
def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    e = []
    
    while True:

        if len(e) == m:
            answer += e.pop(-1) * m
            e.clear()

        if len(score) == 0:
            break

        e.append(score.pop(0))
    
    return answer


# 2차 시도 ( 성공 )
def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    e = []
    
    for i in score:
        e.append(i)
        if len(e) == m:
            answer += e.pop(-1) * m
            e.clear()
        if len(score) == 0:
            break
    return answer

print(solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))