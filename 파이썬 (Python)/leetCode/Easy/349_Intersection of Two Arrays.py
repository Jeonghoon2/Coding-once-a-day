# BS 풀이
class Solution:
    def intersection(self, nums1, nums2):
        nums1 = set(nums1)
        nums2 = list(sorted(nums2))
        answer = set()

        for n in nums1:
            start, end = 0, len(nums2)

            while start <= end:
                mid = (start + end) // 2

                if len(nums2) == mid:
                    break

                if nums2[mid] == n:
                    answer.add(n)
                    break

                if nums2[mid] > n:
                    end = mid - 1
                else:
                    start = mid + 1
        return list(answer)


print(Solution().intersection([1], [1,2]))
print(Solution().intersection([1, 2, 2, 1], [2, 2]))
print(Solution().intersection([4, 9, 5], [9, 4, 9, 8, 4]))
