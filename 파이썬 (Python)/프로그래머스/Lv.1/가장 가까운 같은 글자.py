def solution(s):
    answer = []
    
    spells = {}


    for idx, spelling in enumerate(list(s)):
        if spelling not in spells:
            answer.append(-1)
            spells[spelling] = idx
        else:
            answer.append(idx - spells[spelling])
            spells[spelling] = idx

print(solution("banana"))