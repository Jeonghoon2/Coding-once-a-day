# 1. n의 다음 큰 숫자는 N보다 큰 자연수 입니다.
# 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.

def solution(n):
    answer = 0
    n_count = (format(n, 'b').count('1'))
    while True:
        n += 1
        if (format(n, 'b')).count('1') == n_count:
            answer = n
            break

    return answer

print(solution(78))