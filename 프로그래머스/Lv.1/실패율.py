from itertools import count


def solution(N, stages):
    answer =[]

    dic = {}
    allPlayer = len(stages)
    for i in range(1,N+1):
        notclearPlay = stages.count(i)
        failRate = notclearPlay/allPlayer
        dic[i] = failRate
        allPlayer -= notclearPlay

    dicSort = sorted(dic.items(), key = lambda x : x[1],reverse=True)
    return [dicSort[i][0] for i in range(len(dicSort))]

def solution2(N, stages):
    
    result = {}
    playerCount = len(stages)
    for i in range(1, N+1):
        if playerCount != 0:
            clear = stages.count(i)
            result[i] = clear/playerCount
            playerCount -= clear
        else:
            result[i] = 0
    return sorted(result, key=lambda x : result[x], reverse= True)
        
    
print(solution2(5, [2, 1, 2, 6, 2, 4, 3, 3]))