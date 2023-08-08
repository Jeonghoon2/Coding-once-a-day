from itertools import permutations


# 첫번째 방법
# 시간 초과
def solution(num):
    p_nums = list(permutations(num, len(num)))
    list_permute = [''.join(map(str, i)) for i in p_nums]
    answer = max(list_permute)

    return answer

# 참조
def solution2(num):
    num = list(map(str,num))
    num.sort(key=lambda x : x*3, reverse=True)
    return str(int(''.join(num)))


print(solution([6, 20, 10, 2]))
