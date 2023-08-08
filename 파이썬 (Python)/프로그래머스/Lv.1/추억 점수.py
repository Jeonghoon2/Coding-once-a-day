def solution(name, yearning, photo):

    d = dict()
    for s, n in zip(name,yearning):
        d[s] = n


    answer = []

    for names in photo:
        point = 0
        for i in names:
            if i in name:
                point += d.get(i)

        answer.append(point)


    return answer

name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may"],["kein", "deny", "may"], ["kon", "coni"]]

print(solution(name,yearning,photo))