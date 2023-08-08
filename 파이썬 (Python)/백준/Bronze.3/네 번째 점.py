x_position = []
y_position = []
for _ in range(3):
    x, y = map(int, input().split())
    x_position.append(x)
    y_position.append(y)

x, y = 0, 0
for i in range(3):
    if x_position.count(x_position[i]) == 1:
        x = x_position[i]
    if y_position.count(y_position[i]) == 1:
        y = y_position[i]

print(x, y)
