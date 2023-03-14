def solution(wallpaper):
    v = []

    lx, ly = 51, 51
    rx, ry = 0, 0

    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                v.append((i, j))

    for x, y in v:
        if x < lx:
            lx = x
        if y < ly:
            ly = y
        if x > rx:
            rx = x
        if y > ry:
            ry = y

    return [lx, ly, rx + 1, ry + 1]

# 다른 풀이
def solution2(wallpaper):
    x = []
    y = []

    lx, ly = 51, 51
    rx, ry = 0, 0

    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                x.append(i)
                y.append(j)

    return [min(x), min(y), max(x)+1, max(y)+1]



wallpaper = [".#...", "..#..", "...#."]
print(solution2(wallpaper))
