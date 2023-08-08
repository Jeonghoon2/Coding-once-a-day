def solution(numbers):
    answer = 0
    a = [0,1,2,3,4,5,6,7,8,9,0]
    for i in a:
        if int(i) not in numbers  :
         answer += i
    return answer

solution([1,2,3,4,6,7,8,0])