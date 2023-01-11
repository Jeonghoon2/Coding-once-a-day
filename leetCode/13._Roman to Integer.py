class Solution:
    def romanToInt(s: str) -> int:
        answer = 0
        Symbol_dict = {"M":1000, "D":500, "C":100, "L": 50, "X": 10, "V":5, "I":1}

        for i in range(len(s)-1):
            if Symbol_dict[s[i]] < Symbol_dict[s[i+1]]:
                answer -= Symbol_dict[s[i]]
            else:
                answer +=Symbol_dict[s[i]]
        return answer + Symbol_dict[s[-1]]

