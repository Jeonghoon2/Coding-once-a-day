def makeToFood(foodList):
    result = ""
    for s in foodList:
        if s == 0:
            continue
        result += str(s)
    return result.strip()

def solution(food):
    answer = ''
    
    dic = {}
    first = []
    middle = '0'

    for i in range(1,len(food)):
        
        # 짝수로 만들기
        while food[i]%2 != 0:
            food[i] -= 1

        # 음식 개수 재정의
        dic[i] = int(food[i]/2)
    
    # 음식 순열 찍기
    for i in range(1, len(dic)+1):
        for j in range(dic[i]):
            first.append(i)
    

    first_str = makeToFood(first)
    first.reverse()
    second_str = makeToFood(first)

    return first_str+'0'+second_str

print(solution([1,7,1,2]))