# 시간 초과....

import sys

sys.stdin = open('in5.txt', 'r')

def dfs(t):
    if len(t) == n:
        tmp.append(t)
        return
    else:
        for j in range(1, n + 1):
            if len(t) == 0:
                dfs(t + [j])
            else:
                if j not in t:
                    dfs(t + [j])


if __name__ == '__main__':
    n, m = map(int, input().split())

    tmp = []

    # 초기 순열 구하기
    dfs([])

    visit = []

    for arr in tmp:
        guess_ans = arr
        while len(arr) > 1:
            sub_tmp = []

            if arr in visit:
                break
            for i in range(len(arr) - 1):
                num = arr[i] + arr[i + 1]
                if num > m:
                    break
                sub_tmp.append(num)
                if sub_tmp not in visit:
                    visit.append(sub_tmp)
            arr = sub_tmp.copy()

        if sub_tmp[0] == m:
            print(guess_ans)
            sys.exit(0)
