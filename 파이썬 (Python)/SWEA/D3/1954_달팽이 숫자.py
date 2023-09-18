for tc in range(1, int(input()) + 1):
    n = int(input())

    arr = [[0] * n for _ in range(n)]

    mv = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    m = 0

    sx, sy, cnt = 0, -1, 1

    while cnt <= (n * n):
        nx, ny = sx + mv[m][0], sy + mv[m][1]

        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0:
            arr[nx][ny] = cnt
            cnt += 1
            sx, sy = nx, ny
        else:
            m = (m+1) % 4

    print("#%d" %tc)
    for sn in arr:
        print(*sn)

