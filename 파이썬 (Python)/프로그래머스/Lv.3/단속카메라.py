# 1<=len(routes)<=10,000
# -30,000 <= 진입 지점, 진출 지점 <= 30,000

def solution(routes):
    answer = 0
    routes.sort(key = lambda x:x[1])

    now = -30001
    for route in routes:
        if (now < route[0]):
            now = route[1]
            answer += 1

    return answer

routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
print(solution(routes))