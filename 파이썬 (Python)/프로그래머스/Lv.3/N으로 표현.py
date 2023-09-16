# 1<= N <= 9

def solution2(N, number):
    if number == 1:
        return 1

    set_list = []

    for cnt in range(1, 9):
        tmp_set = set()
        tmp_set.add(int(str(N) * cnt))

        for i in range(cnt - 1):
            for op1 in set_list[i]:
                for op2 in set_list[-i - 1]:
                    tmp_set.add(op1 + op2)
                    tmp_set.add(op1 * op2)
                    tmp_set.add(op1 - op2)
                    if op2 != 0:
                        tmp_set.add(op1 / op2)
        if number in tmp_set:
            return cnt
        set_list.append(tmp_set)
    return -1


N = 5
number = 12
print(solution(N, number))
