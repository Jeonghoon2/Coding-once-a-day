import itertools


def is_prime_num(num):
    if num == 0 or num ==1:
        return False
    else:
        for n in range(2, (num//2)+1):
            if num%n == 0:
                return False
        return True


def solution(nums):
    answer = 0

    com = list(itertools.combinations(nums, 3))
    for c_p in com:
        if is_prime_num(sum(c_p)):
            answer += 1

    return answer


nums = [1,2,7,6,4]
print(solution(nums))
