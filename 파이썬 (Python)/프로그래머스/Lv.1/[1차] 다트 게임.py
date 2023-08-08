# "점수|보너스|[옵션]"으로 이루어진 문자열 3세트.
# S,D,T 

def solution(dartResult):
    point_li = []
    dartResult = list(dartResult)
    for i in range(len(dartResult)):
        if dartResult[i] == '*' or dartResult[i] =='#':
            
        point_li.append(i)
        
    answer = 0
    return answer

print(solution("1S2D*3T"))