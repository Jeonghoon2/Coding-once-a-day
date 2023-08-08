def solution(record):
    answer = []

    user = dict()
    user_e_log = []

    for i in record:
        i = list(i.split())
        status, uid = i[0], i[1]

        if status == 'Leave':
            user_e_log.append((uid, status))
            continue
        if status == 'Change':
            user[uid] = i[2]
            continue

        if uid not in user:
            user[uid] = i[2]
            user_e_log.append((uid, status))
        else:
            user[uid] = i[2]
            user_e_log.append((uid, status))


    for uid, status in user_e_log:
        message = str(user.get(uid)) + "님이 "
        if status == "Enter":
            message += "들어왔습니다."
        else:
            message += "나갔습니다."
        answer.append(message)

    return answer


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
print(solution(record))
