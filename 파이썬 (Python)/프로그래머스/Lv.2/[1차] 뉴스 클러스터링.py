import math


def mk_set(st):
    tmp = []

    for i in range(len(st) - 1):
        cur_set = st[i:i + 2]

        if cur_set.isalpha():
            tmp.append(cur_set)

    return tmp


def solution(str1, str2):

    str1, str2 = Counter(mk_set(str1.lower())), Counter(mk_set(str2.lower()))

    inter, union = list((str1 & str2).elements()), list((str1 | str2).elements())
    if len(inter) == 0 and len(union) == 0:
        return 65536
    else:
        return int(len(inter)/len(union)*65536)


from collections import Counter


def solution2(str1, str2):
    str1_low = str1.lower()
    str2_low = str2.lower()

    str1_lst = []
    str2_lst = []

    for i in range(len(str1_low) - 1):
        if str1_low[i].isalpha() and str1_low[i + 1].isalpha():
            str1_lst.append(str1_low[i] + str1_low[i + 1])
    for j in range(len(str2_low) - 1):
        if str2_low[j].isalpha() and str2_low[j + 1].isalpha():
            str2_lst.append(str2_low[j] + str2_low[j + 1])

    Counter1 = Counter(str1_lst)
    Counter2 = Counter(str2_lst)

    inter = list((Counter1 & Counter2).elements())
    union = list((Counter1 | Counter2).elements())

    if len(union) == 0 and len(inter) == 0:
        return 65536
    else:
        return int(len(inter) / len(union) * 65536)

str1 = "aa1+aa2"
str2 = "AAAA12"

print(solution(str1, str2))
