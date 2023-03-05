class Solution:
    def sumOfUnique(nums):

        Unique_dict = {}

        for n in nums:
            if n in Unique_dict:
                Unique_dict[n] = Unique_dict.get(n) + 1
            else:
                Unique_dict[n] = 1

        s = [k for k,v in Unique_dict.items() if min(Unique_dict.values()) == v]

        if len(Unique_dict) == 1 and len(nums) >= 2:
            return 0
        else:
            return sum(s)
    
print(Solution.sumOfUnique([10]))