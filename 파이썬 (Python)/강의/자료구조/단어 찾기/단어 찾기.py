import sys

sys.stdin = open('in5.txt', 'r')

n = int(input())

words = dict()

for _ in range((n*2)-1):
    w = input()
    words[w] = words.get(w, 0) + 1

ans = ''
for k, v in words.items():
    if v == 1:
        ans = k

print(ans)
