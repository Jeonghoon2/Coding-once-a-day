# nums1 = list
# nums2 = list
# n, m = int

# 함수 사용 풀이
class Solution:
    def merge(nums1, m, nums2, n):
    
        del nums1[m:]
        nums1 += nums2[0:n]
        nums1.sort()

        return nums1


# 최소 시간
class Solution2:
    def merge(nums1, m, nums2, n):

        i1 = m - 1
        i2 = n - 1
        f = n + m -1

        while i2 >= 0:
            if i1 >= 0 and nums1[i1] > nums2[i2]:
                nums1[f] = nums1[i1]
                i1 -= 1
                f -= 1
            else:
                nums1[f] = nums2[i2]
                f -= 1
                i2 -= 1

        return nums1


print(Solution2.merge([1,2,3,0,0,0], 3, [2,5,6], 3))