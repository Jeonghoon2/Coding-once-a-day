def solution(nums):
    nums = sorted(nums)
    nums =set(nums)
    return len(nums)

print(solution([3,1,2,3]))