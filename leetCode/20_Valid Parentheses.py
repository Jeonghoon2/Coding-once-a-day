# v 가 Key 일 때 i+1 이 value 값이면 True

# 틀린닶 
# s={[]} 일때 만족하지 못함
class Solution:
    def isValid(s: str) -> bool:

        ans = True

        sym_dict= {
            '(':')',
            '{':'}',
            '[':']'
            }

        prev = ''
        for i, v in enumerate(s):
            # v가 sym_dict에 있을 경우
            if v in sym_dict:
                ans = s[i+1:i+2] == sym_dict.get(v) # 검사 하는 문자와 value가 일치 하면 true
                prev = v
            # v가 value일 경우 이전 문자가 key값인지 검사 후 아닐시 False 반환
            elif s[i-1:i] == prev and sym_dict.get(prev) == v:
                continue
            else:
                return False
        
        return ans

# 2차 시도

class Solution2:
    def isValid(s: str) -> bool:

        ar = []

        sym_dict= {
            ')':'(',
            '}':'{',
            ']':'['
            }

        for i in s:
            if i in sym_dict.values():
                ar.append(i)
            else:
                if ar and sym_dict[i]==ar[-1]:
                    ar.pop()
                else:
                    return False
        
        if ar:
            return False
        return True

        return ans


s = "{[]}"
print(Solution2.isValid(s))