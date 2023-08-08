a = map(int, input().split())

# 체스 규격
chess_set = [1, 1, 2, 2, 2, 8]

for idx, c in enumerate(a):
    print(chess_set[idx] - c, end=' ')


