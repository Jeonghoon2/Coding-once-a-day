def solution(s):
    s = s.split()
    arr = []
    for i in s:
        arr.append(int(i))
        
    minmax = "{} {}".format(min(arr),max(arr))
    return s

print(solution("-1 -2 -3 -4"))