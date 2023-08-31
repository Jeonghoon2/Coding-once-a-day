class Solution:
    def getRow(self, rowIndex):
        pascal = [[] for _ in range(rowIndex+1)]

        pascal[0] = [1]
        if rowIndex+1 == 1:
            return pascal[rowIndex]

        pascal[1] = [1, 1]
        if rowIndex+1 == 2:
            return pascal[rowIndex]
        else:
            for i in range(2, rowIndex+1):
                pascal[i] += [1]
                for j in range(0, i - 1):
                    pascal[i] += [pascal[i - 1][j + 1] + pascal[i - 1][j]]
                pascal[i] += [1]

        return pascal[rowIndex]

print(Solution().getRow(0))