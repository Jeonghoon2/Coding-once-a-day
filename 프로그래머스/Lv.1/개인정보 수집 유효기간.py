# privacies dict 변환
def change_privacies(privacies):
    dic_privacies = {}

    for i in privacies:
        s = list(i.split())
        dic_privacies[s[0]] = s[1]

    return dic_privacies

# privacies dict 변환
def change_terms(terms):
    dic_terms = {}

    for i in terms:
        s = list(i.split())
        dic_terms[s[0]] = s[1]

    return dic_terms

# time operation
def time_operation(date):
    time = (int(date[0])*12*28) + (int(date[1])*28) + int(date[2])
    return time


def solution(today, terms, privacies):
    answer = []

    # dict 변환 privacies ( O(N) )
    privacies = change_privacies(privacies)

    # dict 변환 terms ( O(N) )
    terms = change_terms(terms)

    # today list 변환
    today = list(today.split('.'))

    # 오늘 날짜 시간 계산 ( O(1) )
    today_total = time_operation(today)

    for i,(k,v) in enumerate((privacies.items())):
        date = list(k.split('.'))
        term = int(terms.get(v)) * 28
        date_total = time_operation(date)
        term_date = today_total - date_total

        if term <= term_date:
            answer.append(i+1)

    return answer


i = ["2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C", "2021.05.02 A"]]

print(solution(i[0], i[1], i[2]))


# 테스트 케이스 10, 12, 13, 15 ~ 20 실패
# 예상 오류
# 1. 현재 privacies에 데이터를 dictionary로 저장 하였느데 같은 날짜에 다른 약관 종류가 들어온다면 인지하지 못한다.
# 2. 예상 해결 방법 - 이차월 배열로 계산을 할예정