# terms를 dictionary로 변환
def term_dict(terms):
    d_tmp = {}
    for i in terms:
        i = i.split(' ')
        # month * 28 = 총 일수
        d_tmp[i[0]] = int(i[1])*28

    return d_tmp

def _operation(date):

    date = list(date.split('.'))
    return int(date[0])*12*28 + int(date[1])*28 + int(date[2])

def _privacies(privacies):
    a_tmp = []
    for privacy in privacies:
        privacy = list(privacy.split(' '))
        privacy[0] = _operation(privacy[0])
        a_tmp.append(privacy)
    return a_tmp


# 어렵게 생각하지 않고...
def solution2(today, terms, privacies):
    answer = []

    terms = term_dict(terms)
    privacies = _privacies(privacies)
    today = _operation(today)

    for i,(x,y) in enumerate(privacies):
        term = terms.get(y)

        if today - x >= term:
            answer.append(i+1)


    return answer


i = ["2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C", "2021.05.02 A"]]

print(solution2(i[0], i[1], i[2]))


# 테스트 케이스 10, 12, 13, 15 ~ 20 실패
# 예상 오류
# 1. 현재 privacies에 데이터를 dictionary로 저장 하였느데 같은 날짜에 다른 약관 종류가 들어온다면 인지하지 못한다.
# 2. 예상 해결 방법 - 이차원 배열로 계산을 할예정 ( 해결 )