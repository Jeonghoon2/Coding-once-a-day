def solution(lottos, win_nums):
    answer = []
    rank = [6,5,4,3,2,1]
    correct = 0
    guessNum = lottos.count(0)
    
    for i in lottos:
        if i != 0:
            correct += win_nums.count(i)
    
    min = rank.index(correct)
    max = rank.index(correct+guessNum)
    
    
    answer.append(max+1)
    answer.append(min+1)
    
    
    return answer


print(solution([45, 4, 35, 20, 3, 9],[20, 9, 3, 45, 4, 35]))