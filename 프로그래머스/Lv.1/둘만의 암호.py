def bycrypt(i, ignore, idx):
    tmp = []
    count = 0

    w = ord(i)
    while True:

        if count > idx:
            break

        count += 1

        if chr(w) in ignore:
            count -= 1
            w += 1
        else:
            tmp.append(chr(w))
            w += 1

        if w == 123:
            w = 97



    return tmp[-1]


def solution(s, skip, index):
    answer = ''

    for i in s:
        answer += bycrypt(i, skip, index)

    return answer


i = ["aukks", "wbqd", 5]

print(solution(i[0], i[1], i[2]))
