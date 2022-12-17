def solution(a, b):
    answer =0
    day = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
    months = [31, 29, 31, 30, 31, 30,31, 31, 30, 31, 30, 31]
    
    for i in range(a-1):
        answer += months[i]
    
    answer += b-3
    answer = answer%7

    return day[answer]

print(solution(5,24))