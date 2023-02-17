def solution(cards1, cards2, goal):

    idx = 0
    while goal:
        # 첫 단어가 Cards1에 있을 때
        w = goal.pop(0)

        if w in cards1 and cards1[0] == w:
            cards1.pop(0)
            idx += 1
        elif w in cards2 and cards2[0] == w:
            cards2.pop(0)
            idx += 1
        else: return "No"

    return "Yes"


i = [[["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]]
    , [["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]]
     ]

for s in i:
    print(solution(s[0], s[1], s[2]))
