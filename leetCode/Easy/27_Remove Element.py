from typing import List

class Solution:
    def removeElement(nums: List[int], val: int) -> int:
        
        while nums.count(val):
            nums.remove(val)

        return len(nums)

print(Solution.removeElement(nums=[3,2,2,3],val=3))