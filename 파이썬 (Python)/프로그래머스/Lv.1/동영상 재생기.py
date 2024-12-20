from datetime import timedelta


# 동영상 재생기

# command
# prev = -10, next =  +10
# op_start <= pos < op_end 일 경우 op_end로 이동
# 0 <= mm <= 59, 0 <= ss <= 59

def solution(video_len, pos, op_start, op_end, commands):
    def str_to_timedelta(time_str):
        minutes, seconds = map(int, time_str.split(":"))
        return timedelta(minutes=minutes, seconds=seconds)

    # 현재 위치가 오프닝 구간에 있는지 검사
    def check_opening(cur_time, op_start, op_end):
        if op_start_td <= cur_time <= op_end_td:
            return op_end_td
        else:
            return cur_time

    # 시간 정보를 timedelta로 변환
    video_len_td = str_to_timedelta(video_len)
    pos_td = str_to_timedelta(pos)
    op_start_td = str_to_timedelta(op_start)
    op_end_td = str_to_timedelta(op_end)

    pos_td = check_opening(pos_td, op_start_td, op_end_td)

    for command in commands:
        if command == 'next':
            pos_td += timedelta(seconds=10)

            # 현재 분과 초가 video_len -10초 <= video_len 일 경우
            if video_len_td - timedelta(seconds=10) < pos_td:
                pos_td = video_len_td
        if command == 'prev':
            # 현재 초가 10초 미만이고, 분이 0일 경우 0분 00초로 초기화
            if pos_td < timedelta(minutes=0, seconds=10):
                pos_td = timedelta(minutes=0, seconds=0)
            else:
                pos_td -= timedelta(seconds=10)

        pos_td = check_opening(pos_td, op_start_td, op_end_td)

    return str(pos_td)[2:]


video_len = "10:00"
pos = "00:03"
op_start = "00:00"
op_end = "00:05"
command = ["prev", "next"]

print(solution(video_len, pos, op_start, op_end, command))
