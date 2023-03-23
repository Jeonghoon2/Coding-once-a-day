# 10진법	124 나라  |	10진법	124 나라
#   1	        1	  |     6	   14
#   2	        2	  |     7	   21
#   3	        4	  |     8	   22
#   4	        11	  |     9	   24
#   5	        12	  |     10	   41
# n은 50,000,000이하의 자연수 입니다.
# 3진법 사용하여 문제 해결 가능

# 효율성 실패
from collections import deque

def solution(n):
    answer = ''
    s = deque()
    d = {
        3: 4,
        5: 12,
        6: 14,
        7: 21,
        8: 22,
        9: 24,
        10: 41
    }
    i = 1

    while True:
        if n <= 2:
            s.appendleft(n)
            break
        else:
            if 3 * i >= n:
                j = n - ((i - 1) * 3)
                n = i - 1
                if j in d:
                    s.appendleft(d.get(j))
                    i = 1
                else:
                    s.appendleft(j)
                    i = 1
            else:
                i += 1

    for i in s:
        if 0 < i:
            answer += str(i)
    return answer


# 재귀 방식
def sol(n):
    if n <= 3:
        return '124'[n-1]
    else:
        q,r = divmod(n-1,3)
        return sol(q) + '124'[r]




print(sol(50000000))
