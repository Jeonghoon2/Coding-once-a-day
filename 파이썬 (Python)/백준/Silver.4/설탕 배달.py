# 봉지 종류 3Kg, 5Kg
# N = 4

N = int(input())
answer = 0

while N >= 0:
    if N%5 == 0:
        answer += int(N//5)
        print(answer)
        break
    N -= 3
    answer +=1
else:
    print(-1)



