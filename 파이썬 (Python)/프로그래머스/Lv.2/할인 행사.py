from collections import Counter


def solution(want, number, discount):
    answer = 0
    buy_item = {}

    for item, count in zip(want, number):
        if item not in buy_item:
            buy_item[item] = count

    for i in range(len(discount) - 9):
        cur_point = Counter(discount[i:i + 10])
        if cur_point == buy_item:
            answer += 1

    return answer


want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana",
            "apple", "banana"]
discount2 = ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]

print(solution(want, number, discount))
