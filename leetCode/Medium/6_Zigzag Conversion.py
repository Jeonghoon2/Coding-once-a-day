class Solution:
    def convert(self, s, numRows):
        answer = ''
        if numRows == 1:
            return s
        zigzag = [[] * i for i in range(numRows)]

        status, m = 0, 1

        for st in s:
            zigzag[status].append(st)
            if status == 0:
                m = 1
            elif status == numRows-1:
                m = -1
            status = status + m

        for i in zigzag:
            cur_str = ''.join(st for st in i)
            answer += cur_str

        return answer




s = "AB"
numRows = 1
print(Solution().convert(s, numRows))
