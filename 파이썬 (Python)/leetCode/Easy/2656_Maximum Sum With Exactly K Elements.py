class Solution:
    def maximizeSum(self, nums, k):
        m = max(nums)
        total = 0

        for _ in range(k):
            total += m
            m += 1
        return total


nums = [5,5,5]
k = 2

print(Solution().maximizeSum(nums, k))
