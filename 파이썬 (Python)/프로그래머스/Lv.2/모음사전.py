# word : 1<= word <= 5
# 순서  'A', 'E', 'I', 'O', 'U'
# DFS 사용

def solution(word):

    v = []
    alpha = "AEIOU"

    def combination_word(w, cnt):
        if cnt == 5:
            return None

        for i in range(len(alpha)):

            v.append(w + alpha[i])
            combination_word(w + alpha[i], cnt + 1)

    combination_word('', 0)

    return v.index(word) + 1


print(solution("AAAAA"))
