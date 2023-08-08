# EX
# n = 234
#  Product of digits = 2 * 3 * 4 = 24
#  Sum of digits = 2 + 3 + 4 = 9
#  Result = 24 - 9 = 15

import math

# 런타임 Up 메모리 Down
class Solution:
    def subtractProductAndSum(n):
        
        n = list(map(int,str(n)))
        return math.prod(n) - sum(n)

# 런타임 Down 메모리 Up
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = list(str(n))
        a = []
        for i in n:
            a.append(int(i))

        return math.prod(a) - sum(a)

print(Solution.subtractProductAndSum(234))

