# 9063번

n = int(input())
x_tmp = []
y_tmp = []
for _ in range(n):
    x, y = map(int, input().split())
    x_tmp.append(x)
    y_tmp.append(y)

x_d = max(x_tmp) - min(x_tmp)
y_d = max(y_tmp) - min(y_tmp)
print(x_d * y_d)
