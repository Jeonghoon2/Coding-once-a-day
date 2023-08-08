from collections import defaultdict

def solution(id_list, report, k):
    answer = []

    # 신고 중복 제거
    report = list(set(report))
    # id = defaultdict
    id = defaultdict(set)
    # 신고 당한 사람 횟수
    report_count = defaultdict(int)

    # 신고
    for i in report:
        i = list(i.split())
        user, r = i[0], i[1]

        id[user].add(r)
        report_count[r] += 1

    for i in id_list:
        b = id.get(i)
        cnt = 0
        if b == None:
            answer.append(0)
            continue
        for j in b:
            if report_count[j] >= k:
               cnt +=1
        answer.append(cnt)

    return answer

i = [["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2]
print(solution(i[0], i[1], i[2]))
