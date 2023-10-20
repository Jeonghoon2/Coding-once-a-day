import sys

sys.stdin = open('in1.txt', 'r')

a = input()
st = []

res = ''

for x in a:
    if x.isdecimal():
        res += x
    else:
        if x == '(':
            st.append(x)
        elif x == '*' or x == '/':
            while st and (st[-1] == '*' or st[-1] == '/'):
                res += st.pop()
            st.append(x)
        elif x == '+' or x == '-':
            while st and st[-1] != '(':
                res += st.pop()
            st.append(x)
        elif x == ')':
            while st and st[-1] != '(':
                res += st.pop()
            st.pop()

while st:
    res += st.pop()

print(res)