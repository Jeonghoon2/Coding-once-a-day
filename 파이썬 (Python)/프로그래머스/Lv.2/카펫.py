# 테스트케이스 4,6,7 실패
def solution(brown, yellow):
    
    answer = []
    check_pettern = []
    sum_b_y = brown + yellow

    for i in range(1,int(sum_b_y/2)):
        if len(answer) == 0:
            answer = [i,sum_b_y]
            check_pettern.append(sorted([i,int(sum_b_y/i)]))
            continue
        
        if sum_b_y%i == 0:
            if sorted([i,int(sum_b_y/i)]) in check_pettern:
                continue
            else:
                answer = [i, int(sum_b_y/i)]
                check_pettern.append(sorted([i,int(sum_b_y/i)]))
                continue
    
    answer = answer[::-1]
    return answer


# 참고
def solution2(brown, yellow):
    
    answer = []
    sum_b_y = brown + yellow

    for i in range(1,int(sum_b_y/2)):
        if(sum_b_y / i) % 1 == 0:
            a = sum_b_y / i
            if a>= i:
                if 2*a + 2*i == brown + 4:
                    return [int(a),i]
    return answer

print(solution2(24, 24))