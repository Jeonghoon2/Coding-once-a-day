def check(s):
    d = {']': '[',
         ')': '(',
         '}': '{'
         }
    st1, st2 = [], []
    for i in s:
        if i in ['[', '(', '{']:
            st1.append(i)
        else:
            ans = d.get(i)
            if ans in st1:
                for z in range(len(st1)):
                    cur_st1_pop = st1.pop(-1)
                    if cur_st1_pop == ans and z == 0:
                        st1 += st2
                        st2.clear()
                        break
                    else:
                        st2.append(cur_st1_pop)
            else:
                return False

    if len(st1) > 0:
        return False

    return True


def solution(s):
    answer = 0

    if len(s) % 2 == 1:
        return 0

    s = list(s)

    for _ in range(len(s)):
        ans = check(s)
        if ans:
            answer += 1
        s.append(s.pop(0))

    return answer


print(solution("}]()[{"))
