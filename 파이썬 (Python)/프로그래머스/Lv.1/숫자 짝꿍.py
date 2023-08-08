def solution(X, Y):
    answer = []

    # 중복되는 수를 구한다.
    S = set(sorted(list(Y), reverse=True)) & set(sorted(list(X), reverse=True))
    # 중복 되는 수의 최소 개수를 구해서 최소 개수 만큼 반복 시키고 반복 될때 마다 answer에 append를 해준다.
    for i in list(S):
        for j in range(min(X.count(i), Y.count(i))):
            answer.append(i)
    
    answer = sorted(answer,reverse=True)
    # len(answer)의 개수가 0일때 returne -1을 해준다.
    if len(answer) == 0:
        return "-1"

    # answer[0]이란 것은 정렬을 했을때 오로지 0 뿐이라는 것이기 때문에 0이 다수가 있어도 0 하나면 리턴 되도록 한다.
    if answer[0] == "0":
        return "0"

    return ''.join(sorted(answer,reverse=True))

print(solution("100","123450"))