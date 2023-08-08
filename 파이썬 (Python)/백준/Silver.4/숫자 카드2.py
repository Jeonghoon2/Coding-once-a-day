# Sol.1 시간 1044ms
def sol1():
    N = int(input())
    n = sorted(list(map(int, input().split())))
    M = int(input())
    m = list(map(int, input().split()))

    answer = []

    n_dic = dict()

    for i in n:
        if i in n_dic:
            n_dic[i] += 1
        else:
            n_dic[i] = 1

    for j in m:
        if j in n_dic:
            answer.append(n_dic.get(j))
        else:
            answer.append(0)

    for a in answer:
        print(a, end=' ')


# Sol.2 848ms
def sol2():
    N = int(input())
    n = list(map(int, input().split()))
    n_dic = {}

    def bs(arr):
        start = 0
        end = N - 1

        while True:

            if arr[start] in n_dic:
                n_dic[arr[start]] += 1
            else:
                n_dic[arr[start]] = 1

            start += 1

            if arr[end] in n_dic:
                n_dic[arr[end]] += 1
            else:
                n_dic[arr[end]] = 1

            if start == end:
                return

            end -= 1

    bs(n)

    M = int(input())
    m = list(map(int, input().split()))
    answer = []
    for i in m:
        if i in n_dic:
            answer.append(n_dic.get(i))
        else:
            answer.append(0)

    for a in answer:
        print(a, end=' ')


sol2()
