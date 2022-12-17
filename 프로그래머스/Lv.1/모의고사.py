def solution(answers):
    answer =[]
    supo1 = [1,2,3,4,5]
    supo2 = [2,1,2,3,2,2,4,2,5]
    supo3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0,0,0]
    rank = {}

    for i in range(len(answers)):
        if supo1[i] == answers[i % len(supo1)] : score[0] += 1
        if supo2[i] == answers[i % len(supo2)] : score[1] += 1
        if supo3[i] == answers[i % len(supo3)] : score[2] += 1

    for i in range(len(score)):
        if score[i] == 0:
            continue
        if score[i] >= 1:
            rank[i+1] = score[i]
        
    answer = sorted(rank)    
    return answer


# 다른 풀이

def solution(answers):
    answer =[]
    supo1 = [1,2,3,4,5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [ 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0,0,0]
    rank = []

    pt = 0
    for i in range(len(answers)):
        if supo1[pt % len(supo1)] == answers[i] : score[0] += 1
        if supo2[pt % len(supo2)] == answers[i] : score[1] += 1
        if supo3[pt % len(supo3)] == answers[i] : score[2] += 1
        pt += 1

    max_val = 0
    for i in range(len(score)):
        if score[i] != 0:
            max_val = max(score[i], max_val)
            rank.append((score[i], i + 1))
            
    return sorted([person for score, person in rank if score == max_val])
    
print(solution([1,2,3,4,5]))