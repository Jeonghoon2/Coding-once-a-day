import math
import time

# 나의 풀기 ( 성공 + 시간 초과 )
# def solution(number, limit, power):
#     answer = 0
#     p = []

#     for i in range(1, int(number ** 0.5) + 1):
#         count = 0
#         for j in range(1, i+1):
#             if i%j == 0:
#                 count += 1
#         p.append(count)

#     for i in p:
#         if i > limit:
#             answer += power   
#         else:
#             answer += i
#     return answer


# 다른 사람 풀이
def get_cds(n, limit , power):
    cnt = 0
    for i in range(1, int(n**(1/2))+1):
        if n%i == 0:
            if i == n//i: 
                cnt += 1
            else:
                cnt += 2 
        if cnt > limit:  
            return power 
    return cnt

    
def solution(number, limit, power):
    total = 1
    for i in range(2, number+1):
        len_cds = get_cds(i, limit, power)
        total += len_cds

    return total


start = time.time()
math.factorial(100000)
print(solution(10, 3, 2), "시간 = ", time.time())

