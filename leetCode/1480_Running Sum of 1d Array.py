class Solution:
    def runningSum(nums):
        answer =[]

        for i in nums:
            if len(answer) == 0:
                answer.append(i)
            else:
                answer.append(answer[-1]+i)

        return answer


print(Solution.runningSum([1,2,3,4]))