# 택배 순서 대로 박스를 싣을 려 한다.


def solution(order):
    answer = 0

    sub_container = []
    i = 1

    while i != len(order) + 1:
        sub_container.append(i)
        while sub_container and sub_container[-1] == order[answer]:
            answer += 1
            sub_container.pop()
        i += 1

    return answer


order = [4, 3, 1, 2, 5]
order2 = [5, 4, 3, 2, 1]

print(solution(order2))
