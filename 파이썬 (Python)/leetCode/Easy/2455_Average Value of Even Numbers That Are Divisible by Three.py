class Solution:
    def averageValue(nums):
        add_nums = []
        for num in nums:
            if num %3 == 0 and num %2 == 0:
                add_nums.append(num)
        
        if len(add_nums) == 0:
            answer = 0
        else:
            answer = sum(add_nums)/(len(add_nums))
    
        return int(answer)
    

print(Solution.averageValue([1,3,6,10,12,15]))
