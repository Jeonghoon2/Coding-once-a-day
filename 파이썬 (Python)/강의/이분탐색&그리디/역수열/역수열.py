import sys

sys.stdin = open('in2.txt', 'r')


def solution():
    # input
    n = int(input())
    nums = list(map(int, input().split()))

    # setup
    arr = [0] * n
    # position operator
    for i in range(n):
        position = nums[i]

        for j in range(n):
            if arr[j] == 0:
                if position == 0:
                    arr[j] = str(i + 1)
                    break
                position -= 1

    ans = ' '.join(arr)

    return ans


print(solution())


