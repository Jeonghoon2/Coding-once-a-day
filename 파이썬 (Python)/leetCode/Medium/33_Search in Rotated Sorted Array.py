
class Solution:
    def search(self, nums, target):

        # 시작
        nst = nums.index(min(nums))

        start, end = 0, len(nums)

        while start <= end:
            mid = (start + end) // 2

            ac_mid = (nst + mid) % len(nums)
            print(nums[ac_mid])

            if nums[ac_mid] == target:
                return ac_mid
            elif nums[ac_mid] < target:
                start = mid +1
            else:
                end = mid -1

        return -1


print(Solution().search([4, 5, 6, 7, 0, 1, 2], 5))
