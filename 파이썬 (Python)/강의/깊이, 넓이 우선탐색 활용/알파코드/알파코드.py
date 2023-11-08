import sys

sys.stdin = open("in1.txt", 'r')


def dfs(l, p):
    global cnt
    if l == n:
        cnt += 1
        for j in range(p):
            print(chr(tmp[j]+64), end=' ')

        print()

    else:
        for i in range(1, 27):
            if s[l] == i:
                tmp[p] = i
                dfs(l + 1, p + 1)
            elif i >= 10 and s[l] == i // 10 and s[l + 1] == i % 10:
                tmp[p] = i
                dfs(l + 2, p + 1)


if __name__ == '__main__':
    s = list(map(int, input()))
    n = len(s)
    s.append(-1)

    tmp = [0] * (n + 3)
    cnt = 0

    dfs(0, 0)



