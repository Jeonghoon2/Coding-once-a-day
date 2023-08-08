# 총 10개의 테스트 케이스
for i in range(1, 11):
    answer = 0
    # 건물의 개수를 입력 받는다.
    building_cnt = int(input())
    # 빌딩의 높이 입력
    buildings_height = list(map(int, input().split()))

    for b_n in range(building_cnt):
        left, right = 0, 0
        tmp = []
        for _ in range(2):
            left -= 1
            right += 1

            if 0 <= b_n + left:
                tmp.append(buildings_height[b_n + left])
            if b_n+ right < building_cnt:
                tmp.append(buildings_height[b_n + right])

        if max(tmp) < buildings_height[b_n]:
            answer += buildings_height[b_n] - max(tmp)

    print("#{} {}".format(i,answer))
