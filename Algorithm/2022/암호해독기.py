import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().rstrip().split()))
word = input().rstrip()

for w in word:
    if w.isupper():
        if ord(w)-64 in lst:
            lst.remove(ord(w)-64)
    elif w.islower():
        if ord(w)-70 in lst:
            lst.remove(ord(w)-70)
    else:
        if 0 in lst:
            lst.remove(0)

if lst:
    print('n')
else:
    print('y')
