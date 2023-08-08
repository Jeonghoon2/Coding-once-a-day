from typing import List

# Binary Search

class Solution:
    def searchInsert(nums: List[int], target: int) -> int:
        
        left=0
        right=len(nums)-1

        while left<=right:

            # 중간 분기점
            mid=(left+right)//2
            
            # nums[mid]가 target보다 클 때
            if nums[mid]>target:
                right=mid-1
            # nums[mid]가 target보다 작을 때
            elif nums[mid]<target:
                left=mid+1   
            else: 
                return mid
        
        return left 

print(Solution.searchInsert([1,3,5,6], 7))