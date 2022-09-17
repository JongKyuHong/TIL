import sys
input = sys.stdin.readline

S = input().rstrip()
ans = ''.join(a[0].upper() for a in S.split())
S += ans
space = int(input())
alpha = list(map(int, input().split()))
prev = ''
for i in S:
    if prev == i:
        continue
    if i == ' ':
        space -= 1
        if space < 0:
            print(-1)
            exit()
        prev = ' '
    else:
        target = ord(i.lower())-97
        print(i, target,'tt')
        if alpha[target] == 0:
            print(-1)
            exit()
        alpha[target] -= 1
        prev = i
print(ans)
