# 나의 풀이
def solution(n, arr1, arr2):
    answer = []
    tmp = []
    for i in range(n):
        tmp.append(format(arr1[i] | arr2[i],'b'))
    
    print(tmp)
    for i in tmp:
        st =''
        for j in i:
            if j == '1':
                st += '#'
            else: st += ' '
        answer.append(st)
    return answer

# 다른 사람 풀이

def solution2(n, arr1, arr2):
    answer =[]
    for i in range(n):
        tmp = bin(arr1[i] | arr2[i])
        tmp = tmp[2:].zfill(n)
        tmp = tmp.replace('1','#').replace('0',' ')
        answer.append(tmp)
    return answer

print(solution2(6,[46, 33, 33 ,22, 31, 50],[27 ,56, 19, 14, 14, 10]))