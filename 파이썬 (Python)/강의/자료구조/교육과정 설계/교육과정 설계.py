import sys
from collections import deque

sys.stdin = open('in5.txt', 'r')

necessary_subject = list(input())

n = int(input())

for i in range(n):

    subject = deque(list(input()))
    rule = 0
    answer = 'YES'

    while subject:

        cur = subject.popleft()

        if cur not in necessary_subject:
            continue
        else:
            if necessary_subject[rule] == cur:
                rule += 1
            else:
                answer = 'NO'
                break

    if rule < len(necessary_subject):
        answer = 'NO'

    print(f'#{i + 1} {answer}')
