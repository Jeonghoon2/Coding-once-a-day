# X : 게임 이긴횟수, Y : 이긴 게임
# Z = (Y*100)/X

x, y = map(int, input().split())
z = (y * 100) // x

l, r = 0, x
res = x

if z >= 99:
    print(-1)
else:
    while l <= r:
        mid = (l + r) // 2
        if 100 * (y + mid) // (x + mid) > z:
            res = mid
            r = mid - 1
        else:
            l = mid + 1
    print(res)
