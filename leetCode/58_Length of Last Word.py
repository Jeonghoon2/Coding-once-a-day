class Solution:
    def lengthOfLastWord(s: str) -> int:
        s = s.split(' ')
        
        answer = 0
        idx = len(s)-1
        while True:

            if s[idx] == '':
                idx -= 1
                continue
            else:
                answer = len(s[idx])
                return answer


print(Solution.lengthOfLastWord("   fly me   to   the moon  "))