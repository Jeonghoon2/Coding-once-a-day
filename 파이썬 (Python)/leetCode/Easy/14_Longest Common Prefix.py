from typing import List

class Solution:
    def longestCommonPrefix(strs: List[str]) -> str:
        ans = []
       
        for i, ch in enumerate(strs[0]):
            for string in strs[1:]:
                if len(string) <= i or ch != string[i]:
                    return ''.join(ans)
            ans.append(ch)
        return ''.join(ans)

print(Solution.longestCommonPrefix(["flower","flow","flight"]))