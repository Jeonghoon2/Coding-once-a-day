import sys

sys.stdin = open('in5.txt', 'r')


def dfs(idx, sum):
    if idx == n:
        if sum == (total - sum):
            print('Yes')
            sys.exit(0)
    else:
        dfs(idx + 1, sum + arr[idx])
        dfs(idx + 1, sum)


if __name__ == "__main__":
    n = int(input())

    arr = list(map(int, input().split()))
    total = sum(arr)
    dfs(0,0)
    print('No')
