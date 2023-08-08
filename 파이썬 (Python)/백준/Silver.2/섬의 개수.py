from collections import deque


def check_island(island, visit, cur_x, cur_y):
    move = [[1, 0],  # 상
            [-1, 0],  # 하
            [0, -1],  # 좌
            [0, 1],  # 우
            [1, -1],  # 상좌
            [1, 1],  # 상우
            [-1, -1],  # 하좌
            [-1, 1]  # 하우
            ]
    d = deque()
    d.append((cur_x, cur_y))
    visit.append([cur_x,cur_y])

    while d:
        # 현재 좌표
        cur_x, cur_y = d.popleft()


        for mx, my in move:
            nx, ny = mx + cur_x, my + cur_y

            # 지정 좌표의 범위를 벗어 나지 않고 방문하지 않은 좌표일 경우
            if 0 <= nx < h and 0 <= ny < w and [nx, ny] not in visit:
                if island[nx][ny] == 1:
                    d.append((nx, ny))
                    visit.append([nx, ny])

    return visit


while True:
    w, h = map(int, input().split())

    # 테스트 케이스 종료
    if w == 0 and h == 0:
        break

    answer = 0
    #  섬 변수
    island = []

    for _ in range(h):
        island.append(list(map(int, input().split())))

    visit = []

    for x in range(h):
        for y in range(w):
            if island[x][y] == 1 and [x, y] not in visit:
                visit = check_island(island, visit, x, y)
                answer += 1

    print(answer)
