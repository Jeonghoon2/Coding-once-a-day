from collections import deque

# 몇번 실행 할지 입력
t = int(input())
for _ in range(t):
    # 명령어 입력
    p = input()
    n = int(input())
    x = input()[1:-1].split(',')
    x = deque(x)

    st_rs = 0

    if not n:
        x = deque()

    for i in p:
        if i == 'R':
            st_rs += 1
        elif i == 'D':
            if len(x) == 0:
                break
            if st_rs % 2 == 0:
                x.popleft()
            else:
                x.pop()

    if len(x) == 0:
        print('error')
        continue

    if st_rs % 2 == 0:
        print('[' + ','.join(x) + ']')
    else:
        x.reverse()
        print('[' + ','.join(x) + ']')
