# 시간 초과..
def solution(n, l, r):
    answer = 0
    canto_r = [1]
    c_idx = 0
    for _ in range(n):
        s = canto_r[c_idx]
        b = ""

        for i in str(s):
            if i == '1':
                b += '11011'
            else:
                b += '00000'
        canto_r.append(b)
        c_idx += 1

    answer = (canto_r[-1])[l - 1:r].count('1')
    return answer


i = [2, 4, 17]

print(solution(i[0], i[1], i[2]))
