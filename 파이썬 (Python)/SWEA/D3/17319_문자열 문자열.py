for tc in range(1, int(input()) + 1):

    n = int(input())
    s = input()
    f = True
    if n % 2 == 0:
        for i in range(0, n // 2):
            if s[i] != s[i + n // 2]:
                f = False
                break

        if f:
            print("#%d" % tc, "Yes")
        else:
            print("#%d" % tc, "No")

    else:
        print("#%d" % tc, "No")
        continue
