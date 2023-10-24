import sys

sys.stdin = open('in2.txt', 'r')


def solution():
    n = int(input())

    arr = [i for i in range(1, n + 1)]

    ans = []

    def dfs(lst, idx, a):
        if idx == n:
            ans.append(a)
            return
        else:
            cur_n = lst[idx]

            # O
            dfs(lst, idx + 1, a + [cur_n])
            # X
            dfs(lst, idx + 1, a)

    dfs(arr, 0, [])

    return ans


answer = solution()

for i in answer:

    if len(i) != 0:
        print(*i)
