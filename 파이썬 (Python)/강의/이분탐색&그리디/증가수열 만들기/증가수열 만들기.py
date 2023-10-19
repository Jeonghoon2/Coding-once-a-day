import sys

sys.stdin = open('in5.txt', 'r')

n = int(input())

nums = list(map(int, input().split()))

ans = ''
s, e = 0, n - 1
lst_n = 0
while True:
    tmp = []
    l_n, r_n = nums[s], nums[e]

    if lst_n < l_n:
        tmp.append((l_n, 'L'))
    if lst_n < r_n:
        tmp.append((r_n, 'R'))

    if len(tmp) == 0:
        break

    tmp.sort(key=lambda x: x[0])

    ans += tmp[0][1]
    lst_n = tmp[0][0]

    if tmp[0][1] == 'L':
        nums.pop(0)
    else:
        nums.pop()

    e -= 1

print(ans)
