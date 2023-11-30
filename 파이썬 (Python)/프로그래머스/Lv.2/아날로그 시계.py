def cal_sec(h, m, s):
    return (h * 60 * 60) + (m * 60) + s


def cal_angle(sec_time):
    hour_sec_angle = 30.0 / 60 / 60
    min_sec_angle = 6.0 / 60
    sec_angle = 6.0

    return [(sec_time * hour_sec_angle) % 360, (sec_time * min_sec_angle) % 360, (sec_time * sec_angle) % 360]


def solution(h1, m1, s1, h2, m2, s2):
    answer = 0

    start_time, end_time = cal_sec(h1, m1, s1), cal_sec(h2, m2, s2)
    prev_hour_angle, prev_min_angle, prev_sec_angle = cal_angle(start_time)

    if prev_sec_angle == prev_min_angle and prev_sec_angle == prev_hour_angle:
        answer += 1

    for i in range(start_time+1, end_time+1):
        cur_hour_angle, cur_min_angle, cur_sec_angle = cal_angle(i)

        # 초침이 분침 또는 시침과 완전히 일치 하는 경우
        if cur_hour_angle == cur_sec_angle and cur_min_angle == cur_sec_angle:
            answer += 1
            prev_hour_angle = cur_hour_angle
            prev_min_angle = cur_min_angle
            prev_sec_angle = cur_sec_angle
            continue

        # 시침이 1~2 사이의 1.x이 되어 초침과 중간에 겹치는 경우
        if (prev_sec_angle < prev_hour_angle) and (cur_sec_angle >= cur_hour_angle):
            answer += 1
        elif (prev_sec_angle < prev_hour_angle) and cur_sec_angle == 0:
            answer += 1

        # 분침이 1~2 사이의 1.x이 되어 초침과 중간에 겹치는 경우
        if (prev_sec_angle < prev_min_angle) and (cur_sec_angle >= cur_min_angle):
            answer += 1
        elif (prev_sec_angle < prev_min_angle) and cur_sec_angle == 0:
            answer += 1

        prev_hour_angle = cur_hour_angle
        prev_min_angle = cur_min_angle
        prev_sec_angle = cur_sec_angle
    return answer


print(solution(1, 5, 5, 1, 5, 6))
