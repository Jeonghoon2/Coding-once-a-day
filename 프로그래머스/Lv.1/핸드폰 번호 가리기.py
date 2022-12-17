def solution(phone_number):
    length = len(phone_number)
    phone_number = list(phone_number)

    for i in range(len(phone_number) -4):
        phone_number[i] = '*'

    
    answer = ''.join(phone_number)
    return answer

def addEndNumber(s):
    return '*' * (len(s) - 4) + s[-4:]

print(solution('01033334444'))
print(addEndNumber('027778888'))