from pickle import TRUE


def solution(num):
    answer = 0
    while TRUE:
        if num == 1:
            break
        if num%2==0:
            num = num/2
            answer += 1
        else:
            num = (num * 3) + 1
            answer += 1
    return answer

print(solution(6))