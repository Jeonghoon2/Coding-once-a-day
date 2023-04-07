# 0 <= digit <= 4 0일때 예외 처리 해줘야한다.
# digit[i]의 원소는 2~9까지

class Solution:
    def letterCombinations(self, digits):
        answer = []
        if len(digits) == 0:
            return answer
        nums_alpha = {"2": "abc", "3": "def",
                      "4": "ghi", "5": "jkl",
                      "6": "mno", "7": "pqrs",
                      "8": "tuv", "9": "wxyz"
                      }

        def dfs(d_idx, st):
            # 모든 번호를 눌렀을 경우
            if len(st) == len(digits):
                answer.append(st)
                return
            next_number = nums_alpha[digits[d_idx]]
            for s in next_number:
                dfs(d_idx + 1, st + s)

        dfs(0, '')
        return answer


digits = "2"
print(Solution().letterCombinations(digits))
