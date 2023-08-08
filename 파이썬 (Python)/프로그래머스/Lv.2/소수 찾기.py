# 1 <= lne(numbers) <= 7
from itertools import permutations


def sd(n):
    if n <= 1:
        return False
    for j in range(2, int(n ** (1 / 2)) + 1):
        if n % j == 0:
            return False
    return True


def solution(numbers):
    answer = set()
    numbers = list(numbers)

    for i in range(1, len(numbers) + 1):
        nums = list(map(''.join, permutations(numbers, i)))

        for n in nums:
            n = int(n)
            if sd(n):
                answer.add(n)

    return len(answer)


numbers = "0131"
print(solution(numbers))
