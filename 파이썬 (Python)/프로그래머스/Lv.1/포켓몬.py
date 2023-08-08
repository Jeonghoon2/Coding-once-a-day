def solution(nums):
    N = int(len(nums) / 2)
    nums = set(nums)
    answer = min(len(nums), N)
    return answer

print(solution([3,1,2,3]))