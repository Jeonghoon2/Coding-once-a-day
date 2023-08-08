def solution(survey, choices):
    answer = ''

    survey_dict = {
        'R': 0, 'T': 0,
        'C': 0, 'F': 0,
        'J': 0, 'M': 0,
        'A': 0, 'N': 0
    }

    point_dict = {1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 3}

    for s, c in zip(survey, choices):
        if c > 4:
            survey_dict[s[1:2]] += point_dict.get(c)
        else:
            survey_dict[s[0]] += point_dict.get(c)

    tmp = []
    for idx, (k, v) in enumerate(survey_dict.items()):

        if idx%2 != 0:
            tmp.append([k,v])
            if (tmp[0])[1] >= (tmp[1])[1]:
                answer += (tmp[0])[0]
                tmp.clear()
            # elif (tmp[0])[1] == (tmp[1])[1]:
            #     answer += (tmp[0])[0]
            else:
                answer += (tmp[1])[0]
                tmp.clear()
        else:
            tmp.append([k,v])

    return answer


i = [["TR", "RT", "TR"], [7,1,3]]
print(solution(i[0], i[1]))
