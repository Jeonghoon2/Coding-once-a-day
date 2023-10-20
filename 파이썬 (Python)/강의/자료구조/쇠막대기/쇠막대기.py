import sys

sys.stdin = open('in2.txt', 'r')

n = list(input())

st = []
ans = 0

for i in range(len(n)):
    if n[i] == '(':
        st.append(n[i])
    else:
        st.pop()
        if n[i-1] == '(':
            ans += len(st)
        else:
            ans += 1
print(ans)
