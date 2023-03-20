import sys
sys.setrecursionlimit(1000000)
def solution(elements):
    l = len(elements)
    v = set()
    v.add(sum(elements))
    elements = elements * 2
    c = 0
    x = 1
    while True:
        i = 0 + x
        cur_v = set()
        if i == l:
            break

        for j in range(l):
            # print(str(elements[j:i]) + ': sum : ' + str(sum(elements[j:i])))
            cur_v.add(sum(elements[j:i]))
            i += 1

        v.update(cur_v)
        x, c = x + 1, c + 1

    # print(sorted(v,reverse=False))

    return len(v)


p = [7, 9, 1, 1, 4]
print(solution(p))
