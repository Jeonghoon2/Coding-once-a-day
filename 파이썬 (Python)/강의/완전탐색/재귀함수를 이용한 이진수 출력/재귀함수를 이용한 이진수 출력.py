import sys

sys.stdin = open('in5.txt', 'r')


def dfs(n, str):
    if n == 1:
        str = '1' + str
        print(str)
        return
    else:
        c, d = divmod(n, 2)
        str = f'{d}' + str
        dfs(c, str)


dfs(int(input()), '')
