from typing import List

class Solution:
    def plusOne(digits: List[int]) -> List[int]:
        
        digits_str = ''
        answer = []
        # 문자열로 변환
        for i in digits:
            digits_str += str(i)
        
        digits_str = str(int(digits_str) + 1)

        for i in digits_str:
            answer.append(int(i))
        return answer

        

print(Solution.plusOne([1,2,3]))