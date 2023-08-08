# 5<=s<=1,000,000

def solution(s):
    answer = []
    s = s[2:-2]
    s = list(s.split("},{"))
    s.sort(key=len)
    for i in s:
        i = i.split(',')
        for j in i:
            j = int(j)
            if j not in answer:
                answer.append(j)

    return answer


s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
print(solution(s))
