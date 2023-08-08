a = int(input())
A = set(map(int,input().split()))

b = int(input())
B = list(map(int, input().split()))
answer = []
for i in B:
    if i in A:
        answer.append(1)
    else:
        answer.append(0)

for i in answer:
    print(i)