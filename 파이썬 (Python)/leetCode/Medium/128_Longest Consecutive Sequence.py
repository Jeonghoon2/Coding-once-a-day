# You must write an algorithm that runs in O(n) time.

class Solution:
    def longestConsecutive(self, nums):
        nums = {i: 0 for i in nums}
        nums = dict(sorted(nums.items()))
        cs = []
        count = 0

        for k,v in nums.items():
            if k+1 in nums:
                count += 1
            else:
                cs.append(count+1)
                count = 0

        if len(cs) == 0:
            return 0

        return max(cs)








nums = [100, 4, 200, 1, 3, 2]
print(Solution().longestConsecutive(nums))
