# 2로 나누어가면서
# 2로 안나누어 지면 점프 = 건전지 1사용

def solution(n):
    ans = 0
    
    while n > 0:
        ans += n % 2
        n //= 2
    return ans

print(solution(5000))