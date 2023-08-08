def mv(park, startX, startY, status, cnt):
    mv_rule = {'N': [-1, 0],
               'S': [1, 0],
               'W': [0, -1],
               'E': [0, 1]
               }
    tmpX, tmpY = startX, startY
    mx, my = mv_rule.get(status)
    for _ in range(cnt):
        nx, ny = startX + mx, startY + my
        if 0 <= nx < len(park) and 0 <= ny < len(park[0]):
            if park[nx][ny] == 'X':
                return tmpX, tmpY
            else:
                startX, startY = nx, ny
        else:
            return tmpX, tmpY
    return startX, startY


def check_st(park):
    for x in range(len(park)):
        for y in range(len(park[0])):
            if park[x][y] == 'S':
                return x, y


from collections import deque


def solution(park, routes):
    answer = []
    start_x, start_y = check_st(park)

    d = deque()
    d.append((start_x, start_y))
    while d:
        cur_x, cur_y = d.popleft()
        m_status, m_cnt = routes.pop(0).split()
        n_x, n_y = mv(park, cur_x, cur_y, m_status, int(m_cnt))
        if len(routes) == 0:
            answer=[n_x, n_y]
            break
        d.append((n_x, n_y))

    return answer


park = ["SOO", "OOO", "OOO"]
routes = ["E 2", "S 2", "W 1"]
print(solution(park, routes))
