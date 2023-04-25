# 1085번

x, y, w, h = map(int, input().split())
print(min(x, y, w - x, h - y))
