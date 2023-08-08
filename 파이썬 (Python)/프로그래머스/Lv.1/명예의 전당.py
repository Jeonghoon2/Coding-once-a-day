def solution(k, score):
    
    answer = []
    print_score = []
    for i in range(len(score)):
    
        print_score.append(score[i])
        
        if print_score[0] > score[i]:
            del print_score[-1]

        if len(print_score) == k+1:
            del print_score[0]

        print_score.sort(reverse=False)
        answer.append(print_score[0])
        
    return answer


# 2차 시도
def solution2(k,score):
    answer = []
    print_score = []

    for i in score:
        # 배열이 비어 있을 경우
        if len(print_score) < k:
            print_score.append(i)
        else:
            if min(print_score) <i:
                print_score.remove(min(print_score))
                print_score.append(i)
        
        answer.append(min(print_score))
    return answer

print(solution2(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000] ))