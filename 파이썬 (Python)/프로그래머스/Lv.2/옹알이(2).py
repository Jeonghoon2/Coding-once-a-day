def solution(babbling):
    answer = 0
    babble = ["aya", "ye", "woo", "ma"]
    for b in babbling:
        for text in babble:
            if text * 2 not in b:
                b = b.replace(text, ' ')
        if b.strip() == '':
            answer += 1
    return answer


babbling = ["mama", "yeye", "woowoo", "ayaaya"]
print(solution(babbling))
