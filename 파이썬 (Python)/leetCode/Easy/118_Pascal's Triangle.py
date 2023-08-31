class Solution:
    def generate(self, numRows):
        pascal = [[] for _ in range(numRows)]

        pascal[0] = [1]
        if numRows == 1:
            return pascal

        pascal[1] = [1, 1]
        if numRows == 2:
            return pascal
        else:
            for i in range(2, numRows):
                pascal[i]+=[1]
                for j in range(0, i - 1):
                    pascal[i] += [pascal[i-1][j + 1] + pascal[i-1][j]]
                pascal[i]+=[1]

        return pascal


print(Solution().generate(5))
