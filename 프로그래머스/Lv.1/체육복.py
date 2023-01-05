def solution(n, lost, reserve):

    _reverse = set(reserve) - set(lost)
    _lost = set(lost) - set(reserve)
    
    for i in _reverse:

        if i-1 in _lost:
            _lost.remove(i-1)
        elif i+1 in _lost:
            _lost.remove(i+1)


    return n - len(_lost)

print(solution(5, [2,4], [1,3,5]))