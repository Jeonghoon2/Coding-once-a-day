# high rank 와 low rank 를 구해야한다.
# 0인 부분은 high rank 일 경우 모두 정답처리
# Low 인 경우에는 모두 오답 처리

def solution(lottos, win_nums):
    correct_cnt = 0
    zero_cnt = lottos.count(0)

    rank = [6, 6, 5, 4, 3, 2, 1]

    for i in lottos:
        if i in win_nums:
            correct_cnt += 1

    return [rank[zero_cnt+correct_cnt], rank[correct_cnt]]


lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
print(solution(lottos, win_nums))
