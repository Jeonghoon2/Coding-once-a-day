n, m = map(int, input().split())
matrix = [input() for i in range(n)]

w_board = [
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW"
]

b_board = [
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB"
]


def valid(i, j):
    w_count, b_count = 0, 0

    for di in range(8):
        for dj in range(8):
            ni, nj = i + di, j + dj
            if matrix[ni][nj] != w_board[di][dj]:
                w_count += 1
            if matrix[ni][nj] != b_board[di][dj]:
                b_count += 1
    return min(w_count, b_count)


answer = 100000
for i in range(n - 7):
    for j in range(m - 7):
        answer = min(answer, valid(i, j))
print(answer)
