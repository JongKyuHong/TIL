import sys
input = sys.stdin.readline

word = input().rstrip()
alphas = [0 for _ in range(27)]
odds = 0
oddsindex = -1

for w in word:
    alphas[ord(w)-65] += 1

for i in range(27):
    if alphas[i] % 2 == 1:
        odds += 1
        oddsindex = i
        if odds == 2:
            print("I'm Sorry Hansoo")
            exit()

alphas[oddsindex] -= 1
for i in range(len(alphas)):
    for _ in range(alphas[i]//2):
        print(chr(i+65), end='')
if oddsindex != -1:
    print(chr(oddsindex+65), end='')
for i in range(len(alphas)-1, -1, -1):
    for _ in range(alphas[i]//2):
        print(chr(i+65), end='')         
