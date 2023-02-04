
def solution(n, words):
    answer = []

    check_word = []
    previous_word = ''
    l = ''
    n_turn = 0
    a_turn = 0

    for i,current_word in enumerate(words):
        
        # 최초 단어 등록
        if previous_word == '':
            check_word.append(current_word)
            previous_word = current_word
            l = current_word[-1]
            a_turn += 1
            continue
        else:
            # 이전 단어의 끝 글자와 현재 단어의 첫 글자가 다를 때
            if l != current_word[0]:
                break
            elif current_word in check_word:
                break

            # 맨 마지막 단어 검사
            elif i == (len(words)-1):
                l = current_word[-1]
                a_turn += 1
                break
                
            # 이전 단어 끝 글자와 현재 단어의 첫글자가 같을 때
            else:
                check_word.append(current_word)
                l = current_word[-1]
                a_turn += 1
            

        if a_turn == n:
            a_turn = 0
            n_turn += 1
                
    if a_turn == n:
        answer.append(0)
        answer.append(0)
        
    else:
        answer.append(a_turn+1)
        answer.append(n_turn+1)

    return answer

print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))