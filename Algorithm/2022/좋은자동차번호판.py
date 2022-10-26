import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    word = input().rstrip()
    answer = 0
    idx = 2
    for w in word[:3]:
        answer += (ord(w)-65)*(26**idx)
        idx -= 1
    ans = int(word[4:])
    target = abs(answer-ans)
    if target > 100:
        print('not nice')
    else:
        print('nice')