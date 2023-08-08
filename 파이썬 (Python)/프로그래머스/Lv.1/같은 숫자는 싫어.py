from queue import Empty


def solution(arr):
    answer =[]
    j = 0
    for i in arr:
        if len(answer) == 0:
            answer.append(i)
            j += 1
        elif answer[j-1] != i:
            answer.append(i)
            j += 1
    return answer

print(solution([1,1,3,3,0,1,1]))