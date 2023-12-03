n1 = int(input())
n2 = input()
sub_n2 = list(map(int, n2))

for n in range(len(sub_n2)-1,-1, -1):
    print(n1 * sub_n2[n])

print(n1 * int(n2))
