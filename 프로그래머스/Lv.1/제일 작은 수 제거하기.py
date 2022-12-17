def solution(arr):
    answer = []
    tmp = 1e9
    for i in range(len(arr)):
        if tmp >i:
            tmp = i
    return answer