# @알파벳이 N회 이상 나타나지만 한구역에만 있는 경우  = 외톨이 알파벳 X
# @알파벳이 N회 이상 나타나지만 N구역에 나뉘어 있는 경우 = 외톨이 알파벳
# 외톨이 알파벳이 없다면 N 반환


def solution(input_string):
    answer = ''
    alone_char = set()
    regi_char = dict()

    for r, char in enumerate(input_string):

        # char가 등록 되지 않은 경우
        if char not in regi_char:
            regi_char[char] = r
        else:
            # char가 등록 되어 있지만 r-1이 같은 char인 경우
            if input_string[r - 1] == char:
                pass
            else:
                alone_char.add(char)

    if len(alone_char) == 0:
        return 'N'
    else:
        alone_char = list(alone_char)
        alone_char.sort()
        for i in alone_char:
            answer+=i
    return answer


print(solution("zbzbz"))
