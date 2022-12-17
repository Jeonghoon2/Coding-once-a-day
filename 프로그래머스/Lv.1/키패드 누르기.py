from turtle import right


def solution(numbers, hand):
    answer = ''
    print(numbers)
    left_key = [1,4,7]
    right_key = [3,6,9]
    ju_hand = ''
    
    if hand == 'right':
        ju_hand = 'R'
    else: ju_hand = 'L'
    for i in range(len(numbers)):
        #

        # left_key에 있는지 검사
        if numbers[i] in left_key:
            answer += 'L'
            continue
        # rigtht_key에 있는지 검사
        if numbers[i] in right_key:
            answer += 'R'
            continue
        

        # 최초로 눌렀을 경우
        if i == 0:
            answer += ju_hand

        #  둘다 없다면 현재값 -1 +1을 해서 이전에 누른값과 비교해서 있다면 최신에 누른 값을 적는다.
        if numbers[i]-1 == numbers[i-1]:
            answer+='L'
        elif numbers[i]+1 == numbers[i-1]:
            answer +='R'
        else:
            answer += ju_hand
        

        # 위 조건이 일치 하지 않을 경우 주손을 적는다.
        
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))