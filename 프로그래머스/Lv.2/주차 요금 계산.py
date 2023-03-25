# 주차 요금 계산법
# 기본 요금 + ((누적 주차 시간-180) /10) * 600
# 누적 주차 시간이 기본시간 이하 라면 기본 요금 부여
import math
from datetime import datetime


def time_operation(in_time, out_time):
    in_time = datetime.strptime(in_time, "%H:%M")
    out_time = datetime.strptime(out_time, "%H:%M")
    op_time = out_time - in_time
    return int(op_time.seconds / 60)


def solution(fees, records):
    answer = []


    car_numbers = {}
    car_operation = {}

    # Out이 있는 주차 번호 계산
    for i in records:
        time, car_number, status = i.split()
        if status == 'IN':
            car_numbers[car_number] = time
        else:
            in_time = car_numbers.get(car_number)
            if car_number not in car_operation:
                car_operation[car_number] = time_operation(in_time, time)
                del car_numbers[car_number]
            else:
                car_operation[car_number] = car_operation.get(car_number) + time_operation(in_time, time)
                del car_numbers[car_number]

    # 나간 기록이 없는 차량 정산
    for car_number, in_time in car_numbers.items():
        if car_number in car_operation:
            car_operation[car_number] = car_operation.get(car_number) + time_operation(in_time, "23:59")
        else:
            car_operation[car_number] = time_operation(in_time, "23:59")

    for car_number, total_time in sorted(car_operation.items()):
        if total_time <= int(fees[0]):
            answer.append(fees[1])
        else:
            total_time = math.ceil((total_time -fees[0])/fees[2])
            total_time = total_time * fees[3]
            total_time = total_time + fees[1]

            answer.append(total_time)

    return answer


fees = [120, 0, 60, 591]
record = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]
print(solution(fees, record))
