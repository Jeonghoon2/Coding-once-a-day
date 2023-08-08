from dataclasses import replace


def solution(s):
    arr = []
    zero_count = 0
    change_count = 0

    while True:
        if s == '1':
            break
        zero_count += s.count('0')
        s = s.replace('0','')
        s = format(len(s), 'b')
        change_count += 1
        
    arr.append(change_count)
    arr.append(zero_count)

    return arr

print(solution("0111010"))