class Solution:
    def kItemsWithMaximumSum(self, numOnes, numZeros, numNegOnes, k):
        if k < numOnes:
            return k
        if k < numOnes + numZeros:
            return numOnes
        k -= numOnes + numZeros
        return numOnes - k


numOnes = 3
numZeros = 2
numNegOnes = 0
k = 4

print(Solution().kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k))
