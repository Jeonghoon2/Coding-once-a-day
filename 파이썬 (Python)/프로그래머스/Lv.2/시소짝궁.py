from collections import Counter


def solution(weights):
    answer = 0

    count = Counter(weights)

    # 1 : 1 Case
    for w, c in count.items():
        if c > 1:
            answer += c * (c - 1) // 2

    # Distinct Weight
    weights = list(set(weights))

    for w in weights:
        for check in [2 / 3, 3 / 4, 2 / 4]:
            if w * check in weights:
                answer += count[w] * count[w * check]

    return answer


weight = [100, 180, 360, 100, 270]

print(solution(weight))
