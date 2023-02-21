def solution(board, moves):
    answer = 0
    basket = []


    for i in moves:

        for j in range(len(board)):
            if board[j][i-1] != 0:
                basket.append(board[j][i-1])
                board[j][i-1] = 0
                break
        c_b = len(basket)
        if c_b > 1:
            if basket[c_b-1] == basket[c_b-2]:
                for _ in range(2):
                    basket.pop()
                answer += 2
    return answer


i = [[[0, 0, 0, 0, 0],
      [0, 0, 1, 0, 3],
      [0, 2, 5, 0, 1],
      [4, 2, 4, 4, 2],
      [3, 5, 1, 3, 1]
      ],
     [1, 5, 3, 5, 1, 2, 1, 4]]
print(solution(i[0], i[1]))
