# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

def solution(answers):
    answer = []
    counts = [0,0,0]
    first = [1,2,3,4,5] * 2000
    second = [2,1,2,3,2,4,2,5] * 1250
    thrid = [3,3,1,1,2,2,4,4,5,5] * 1000


    # 
    for i in range(len(answers)):
        if first[i] == answers[i]:
            counts[0] += 1
        if second[i] == answers[i]:
            counts[1] += 1
        if thrid[i] == answers[i]:
            counts[2] += 1
    
    for i in range(len(counts)):
        if counts[i] == max(counts):
            answer.append(i+1)
    

    return answer

print(solution([1,3,2,4,2]))