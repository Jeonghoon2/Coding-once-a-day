import sys

sys.stdin = open('in3.txt', 'r')

n, m = map(int, input().split())

st = []

n = list(str(n))

while n:
    cur_n = n.pop(0)

    while st:

        if st[-1] < cur_n:
            if m == 0:
                st.append(cur_n)
                break
            st.pop()
            m -= 1
        else:
            st.append(cur_n)
            break
    if len(st) == 0:
        st.append(cur_n)


st = st + n
rst = ''.join(st[0:len(st)-m])

print(int(rst))
