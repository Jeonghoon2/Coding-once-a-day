# 1 <= n <= 10,000
# 1 < = s <= 1,000,000,000 (Two Pointer)
# s를 n으로 나누고 나눈 값을 배열로 n만큼 늘린다.
# 그리고 남은 값만큼 1씩 나눠서 더한다.
def solution(n, s):
    answer = []

    if s < n:
        return [-1]

    for _ in range(n):
        answer.append(s // n)

    indexs = len(answer)-1

    for i in range(s - sum(answer)):
        answer[indexs] += 1
        indexs -= 1
    return answer


def solution2(n, s):
    answer = []

    if n > s:
        return [-1]

    p, q = divmod(s, n)
    answer = [p] * n

    for i in range(q):
        answer[i] += 1

    return sorted(answer)


n, s = 2, 9
print(solution2(n,s))