def solution(price, money, count):
    num = 0
    for i in range(1, count+1):
        num += i * price
    if num - money < 0:
        return 0
    else:
        return num - money    

print(solution(3,20,4))