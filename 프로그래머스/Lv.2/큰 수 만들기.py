# number는 2자리 이상, 1,000,000자리 이하인 숫자입니다. ⭐️️️⭐️️️⭐️️️⭐️️️

def solution(number, k):
    answer = []  # Stack

    for num in number:
        if not answer:
            answer.append(num)
            continue
        if k > 0:
            while answer[-1] < num:
                answer.pop()
                k -= 1
                if not answer or k <= 0:
                    break
        answer.append(num)

    answer = answer[:-k] if k > 0 else answer
    return ''.join(answer)

number = "4177252841"
k = 4
print(solution(number,k))