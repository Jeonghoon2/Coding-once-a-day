def solution(babbling):
    answer = 0
    return answer


baby = ["aya", "ye", "woo", "ma"]
babbling = ["ayayeu"]

# 우선 단어들의 위치를 찾는다
for i in babbling:
    for j in range(len(baby)):
        print(i.find(j))
    
# 찾은 단어들의 위치가 곂치지 않는지 검사한다.

# 겹치지 않는다면 올바른 단어 인지 검사한다.

# 검사다 통과 되면 return


