import sys

sys.stdin = open('in4.txt', 'r')

def dfs(l):
    if arr[l] > 0:
        return arr[l]
    if l == 1 or l == 2:
        return l
    else:
        arr[l] = dfs(l-1) + dfs(l-2)
        return arr[l]



if __name__ == '__main__':
    n = int(input())

    arr = [0] * (n + 1)

    print(dfs(n))

