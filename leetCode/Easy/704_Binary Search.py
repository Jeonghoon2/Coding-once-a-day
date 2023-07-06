class Solution:
    def search(self, nums, target):
        start, end = 0, len(nums)

        while start <= end:
            mid = (start + end) // 2

            if mid > len(nums)-1:
                return -1
            if nums[mid] == target:
                return mid
            else:
                if nums[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1
        return -1


print(Solution().search([-1, 0, 3, 5, 9, 12], 13))
