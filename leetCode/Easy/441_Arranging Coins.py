# 등차수열 합공식 ( k*(k+1)/2   )
# k = mid

class Solution:
    def arrangeCoins(self, n):
        start, end = 0, n

        while start <= end:
            mid = (start + end) // 2
            c = mid*(mid+1)//2

            # 완전한 계단을 이룰 때
            if c == n:
                return mid

            #  부족할 경우
            if c > n:
                end = mid-1
            # 초과 할 경우
            else:
                start = mid +1
        return end


print(Solution().arrangeCoins(5))
