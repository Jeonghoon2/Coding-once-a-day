class Solution:
    def twoSum(self, nums, target):

        b = {}

        for i, n in enumerate(nums):
            if (target - n) in b:
                return [b.get(target - n), i]
            else:
                b[n] = i
        return [0, 0]


nums = [2, 7, 11, 15]
target = 9
print(Solution().twoSum(nums, target))
