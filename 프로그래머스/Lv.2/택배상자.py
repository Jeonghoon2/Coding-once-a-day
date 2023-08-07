# 택배 순서 대로 박스를 싣을 려 한다.


def solution(order):
    assist = []
    i = 1
    cnt = 0
    while i != len(order) + 1:
        assist.append(i)
        while assist and assist[-1] == order[cnt]:
            cnt += 1
            assist.pop()

        i += 1
    return cnt


order = [4, 3, 1, 2, 5]
order2 = [5, 4, 3, 2, 1]

print(solution(order))
