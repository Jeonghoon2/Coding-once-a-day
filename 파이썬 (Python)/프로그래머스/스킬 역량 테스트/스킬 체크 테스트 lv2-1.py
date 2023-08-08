import re
from itertools import permutations


def calculate(num1, num2, operator):
    if operator == '+':
        return str(int(num1) + int(num2))
    if operator == '-':
        return str(int(num1) - int(num2))
    if operator == '*':
        return str(int(num1) * int(num2))


def oper(expression, op):
    result = re.split('(\D)', expression)

    for o in op:
        stack = []
        while len(result) != 0:
            tmp = result.pop(0)
            if tmp == o:
                stack.append(calculate(stack.pop(), result.pop(0), o))
            else:
                stack.append(tmp)
        result = stack

    return abs(int(result[0]))


def solution(expression):
    answer = 0

    # 모든 연산자 정의
    operation = ['+', '-', '*']

    # 모든 연산자 우선 순위 케이스 생성
    case_op = list(permutations(operation, 3))

    # 각 우선 순위로 계산
    for op in case_op:
        answer = max(oper(expression, op),answer)

    return answer


print(solution("100-200*300-500+20"))
