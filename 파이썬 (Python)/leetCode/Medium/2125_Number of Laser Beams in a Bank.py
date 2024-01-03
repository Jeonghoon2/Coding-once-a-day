class Solution:
    def numberOfBeams(self, bank):
        answer = 0
        prev = 0

        for x in bank:
            cnt = x.count('1')
            if not cnt:
                continue
            answer += prev * cnt
            prev = cnt

        return answer



bank = ["011001", "000000", "010100", "001000"]
print(Solution().numberOfBeams(bank))
