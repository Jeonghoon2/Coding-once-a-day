from collections import deque


def solution(s):
    answer = True
    stack = deque()
    for i in s:
        # 스택에 아무것도 없는 스택에 '('만 남았을 경우
        if i == ')' and not stack:
            return False
        #  i가 닫는 괄호 이면서 스택에 맨 맨 처음이 열린 괄호일때
        elif i ==')' and stack[-1]=='(':
            stack.pop()
        else:
            if i == '(':
                stack.append(i)
    # 비어 있다면 True를 반환 하고 비어 있지 않으면 False를 반환
    return True if not stack else False

print(solution("(()("))