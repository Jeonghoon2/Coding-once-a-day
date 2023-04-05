# Constraints
#  1<= nums.length <= 100 ⭐️ O(n),O(logn),O(n^2)

class Solution:
    def nextPermutation(self, nums):

        y = sorted(nums)
        arrs = []

        def dfs(arr, position):
            if len(arr) == len(y):
                if arr in arrs:
                    return
                else:
                    arrs.append(arr)
                    return
            for idx, n in enumerate(y):
                if idx in position:
                    continue
                else:
                    dfs(arr + [n], position + [idx])

        dfs([], [])

        p = arrs.index(nums)
        if p + 1 > len(nums):
            nums = arrs[0]
        else:
            nums = arrs[p + 1]
        return nums


# in-place
# 사이트에서 주어지는 Test Case 말고 [1,3,5,4,2] 또는 다른 Test Case를 생각 해보면 된다.
class Solution2:
    def nextPermutation(self, nums):
        low_point = len(nums) - 2
        while 0 <= low_point and nums[low_point] >= nums[low_point + 1]:
            low_point -= 1

        if low_point > -1:
            high_point = len(nums) - 1
            while 0 <= high_point and nums[low_point] >= nums[high_point]:
                high_point -= 1
            nums[low_point], nums[high_point] = nums[high_point], nums[low_point]
            start, end = low_point + 1, len(nums) - 1
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start, end = start + 1, end - 1

        else:
            nums.reverse()

        return nums


nums = [3,2,1]
print(Solution2().nextPermutation(nums))
