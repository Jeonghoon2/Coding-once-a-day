from collections import deque
# 오답
def solution(people, limit):
    
    current_kg= 0
    boat = 0

    people = sorted(people)

    for i in people:
        if i >= limit:
            boat+=1


        # ck + i가 100이면 클리어 후 clear
        if current_kg + i == limit:
            boat+=1
            current_kg = 0
        # ck + i가 100을 넘었을 경우 boat +1 해주고 ck를 i로 변환
        elif current_kg + i > limit:
            boat+=1
            current_kg = i
        else:
            current_kg+= i


    if current_kg != 0:
        return boat+1
    else:
        return boat



# 참고 Greedy  Two-Point
def solution2(people, limit):
    
    boat = 0
    people = deque(sorted(people, reverse = True))

    while len(people)>1:
        if people[0] + people[-1] <= limit:
            boat += 1
            people.pop()
            people.popleft()
        else:
            answer+=1
            people.popleft()
    
    if people:
        boat+=1
    
    return boat


    
    

print(solution2([70, 50, 80, 50], 130))