# LZW 압축
# 길이가 1인 모든 단어를 포함하도록 사전을 초기화한다.
# 사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾는다.
# w에 해당하는 사전의 색인 번호를 출력하고, 입력에서 w를 제거한다.
# 입력에서 처리되지 않은 다음 글자가 남아있다면(c), w+c에 해당하는 단어를 사전에 등록한다.
# 단계 2로 돌아간다.

# 97~122

def dictionary_alpha():
    alpha = dict()
    for i, ac in enumerate(range(97, 123)):
        alpha[chr(ac)] = i + 1

    return alpha


def solution(msg):
    answer = []
    msg = msg.lower()
    d_l_num = 27
    alpha = dictionary_alpha()
    search = ''
    i = 0
    while i < len(msg):
        search += msg[i]

        if search in alpha:
            i += 1
            continue
        else:
            alpha[search] = d_l_num
            d_l_num += 1

            s = search[:-1]
            answer.append(alpha[s])
            search = ''

    answer.append(alpha[search])
    return answer


msg = "KAKAO"
print(solution(msg))
