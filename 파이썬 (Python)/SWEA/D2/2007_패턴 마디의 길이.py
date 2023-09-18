# 마디의 최대 길이는 10이다.
# 각 문자열은 30이다.

for t in range(1,int(input())+1):
    s = input()
    ans = 0

    for i in range(1,10):
        if s[0] != s[i] or s[1] != s[i+1]:
            ans += 1
        else:
            break

    print("#%d" %t, ans+1)



