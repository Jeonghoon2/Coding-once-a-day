from collections import deque


# 예제 1에서만 적용 되는 식 완전 오답.. 정신 차려라...
def solution(bridge_length, weight, truck_weights):
    answer = 0
    de = deque([i for i in truck_weights])
    bridge_clear = []
    bridge = deque()

    while True:

        if len(bridge) == 0 and len(de) == 0:
            break

        if len(bridge) == 0:
            bridge.append(de.popleft())
            answer += 1
            continue

        else:
            if len(de) == 0:
                bridge_clear.append(bridge.popleft())
                answer += 1
                continue
            elif sum(bridge) + de[0] > weight:
                bridge_clear.append(bridge.popleft())
                answer += 1
                continue
            elif sum(bridge) + de[0] <= weight:
                bridge.append(de.popleft())
                answer += 1

    return answer


def solution2(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    while bridge:
        answer += 1
        bridge.pop(0)
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
    return answer


print(solution2(2, 10, [7, 4, 5, 6]))
