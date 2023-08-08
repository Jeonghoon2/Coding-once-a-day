class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sd = {}
        td = {}
        idx = 0

        for i in range(0, len(s)):
            if not (s[i] in sd) and not (t[i] in td):
                sd[s[i]] = idx
                td[t[i]] = idx
                idx += 1
            elif (s[i] in sd and t[i] in td):
                if (sd[s[i]] != td[t[i]]):
                    return False
            else:
                return False

        return True


input = [["egg", "add"], ["foo", "bar"], ["paper", "title"]]

for i in input:
    print(Solution().isIsomorphic(i[0], i[1]))
