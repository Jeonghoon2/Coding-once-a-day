def solution(ingredient):
    answer = 0

    # 햄버거
    recipe = [1, 2, 3, 1]
    hambuger = []

    for i in ingredient:
        hambuger.append(i)
        if hambuger[-4:] == recipe:
            answer += 1
            for _ in range(4):
                hambuger.pop()

    return answer


print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))
