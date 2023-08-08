# 화패단위 500, 100, 50, 10

class Solution:
    def 거스름돈(self, num):
        count = 0
        type = [500, 100, 50, 10]

        for i in type:
            a, b = divmod(num, i)
            count += a
            num = b

        return count


num = 1260
print(Solution().거스름돈(num))
