import sys

sys.stdin = open('in5.txt', 'r')


def dfs(t):
    if len(t) == m:
        tmp.append(t)
        return
    else:
        for j in range(1,n+1):
            if len(t) == 0:
                dfs(t + [j])
            else:
                if j not in t:
                    dfs(t + [j])


if __name__ == '__main__':
    n, m = map(int, input().split())
    tmp = []
    dfs([])

    for i in tmp:
        print(*i)

    print(len(tmp))
