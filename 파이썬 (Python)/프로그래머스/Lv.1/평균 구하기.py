from audioop import avg

def solution(arr):
    answer = sum(arr) / len(arr)
    return answer

arr = map(int, input().split())