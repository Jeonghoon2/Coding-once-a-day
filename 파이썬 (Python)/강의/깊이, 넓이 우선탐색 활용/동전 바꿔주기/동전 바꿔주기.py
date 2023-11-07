import sys

sys.stdin = open('in5.txt', 'r')


def dfs(l, s):
    global rst
    if s == t:
        rst += 1
        return

    if s > t or l == k:
        return
    else:
        cur_n, cur_c = p[l]

        for i in range(cur_c + 1):
            dfs(l + 1, s + (cur_n * i))


if __name__ == '__main__':
    t = int(input())
    k = int(input())
    p = []
    for _ in range(k):
        p.append(list(map(int, input().split())))
    p.sort(key=lambda x: x[1])
    rst = 0

    dfs(0, 0)

    print(rst)