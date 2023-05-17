# 8 x 8 크기의 체스판
# 각 칸에는 최대 1개의 룩을 놓을 수 있으므로, 체스판 위에는 0개 이상 64개 이하의 룩이 놓여 있는 것이다.
# 정확히 8개의 룩이 있어야 한다.
# 즉, 서로 다른 두 룩은 같은 열에 있거나 같은 행에 있으면 안 된다.

T = int(input())

for idx in range(1,T+1):
    maps = []
    visit_row = []
    for _ in range(8):
        maps.append(list(input()))

    def check():
        for i in range(8):
            if maps[i].count('O') > 1 or maps[i].count('.') == 8:
                return False
            for j in range(8):
                if maps[i][j] == 'O':
                    if j in visit_row:
                        return False
                    visit_row.append(j)
                    break
        return True

    if check():
        print('#'+ str(idx) +' '+ "yes")
    else:
        print('#' + str(idx) + ' ' + "no")



