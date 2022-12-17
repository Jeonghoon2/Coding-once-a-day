import random, time

def genBigRandList(n):
    while 1:
        ran_i = random.randrange(0,n)
        if ran_i not in R_list:
            R_list.append(ran_i)
        if len(R_list) == n:
            break


def printListSample(L):
    for i in range(0,20):
        print(R_list[i],' ',end = '')
        if i == 9:
            print()
    print()
    print(".................")
    print()
    for j in range(len(L)-20,len(L)):
        print(R_list[j],' ', end = '')
        if j == len(L)-11:
            print()

def merge_sort(L):
    if len(L) <= 1:
        return L
    L_mid = len(L)//2
    L_left = L[:L_mid]
    L_right = L[L_mid:]
    
    return merge(merge_sort(L_left),merge_sort(L_right))


def merge(L1,L2):
    L_r = []
    L1index = 0
    L2index = 0
    while L1index <len(L1) and L2index <len(L2):
        if L1[L1index] < L2[L2index]:
            L_r.append(L1[L1index])
            L1index += 1
        else:
            L_r.append(L2[L2index])
            L2index += 1
    if L1index == len(L1):
        while L2index < len(L2):
            L_r.append(L2[L2index])
            L2index += 1
    if L2index == len(L2):
        while L1index < len(L1):
            L_r.append(L1[L1index])
            L1index += 1
    return L_r

while 1:
    x = int(input())
    if x == 0:
        break
    R_list = []
    genBigRandList(x)
    print("before mergeSort of:")
    printListSample(R_list)
    print()
    print("After mergeSort of:")
    time1 = time.time()
    merge_sort(R_list)

    # 시간 관련 Code
    time2 = time.time()
    time_dif = time2-time1
    printListSample(R_list)
    print()
    print("걸린 시간:",time_dif)