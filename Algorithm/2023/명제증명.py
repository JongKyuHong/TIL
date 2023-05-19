import sys
input = sys.stdin.readline
INF = float('inf')

N = int(input())
lst = [[INF]*(52) for _ in range(52)]

for _ in range(N):
    a, b, c = input().split()
    if 65 <= ord(a) < 97:
        a_num = ord(a)-65
    elif 97 <= ord(a) <= 122:
        a_num = ord(a)-97+26
    if 65 <= ord(c) < 97:
        c_num = ord(c)-65
    elif 97 <= ord(c) <= 122:
        c_num = ord(c)-97+26
    lst[a_num][c_num] = 1

for k in range(52):
    for i in range(52):
        for j in range(52):
            if i == k or j == k or i == j:
                continue
            else:
                lst[i][j] = min(lst[i][j], lst[i][k]+lst[k][j])

ans = []

for i in range(52):
    for j in range(52):
        if i == j:
            continue
        if lst[i][j] != INF:
            tmp = ''
            if 0 <= i < 26:
                tmp += chr(i+65) + ' '
            else:
                tmp += chr(i+97-26) + ' '
            tmp += '=> '
            if 0 <= j < 26:
                tmp += chr(j+65)
            else:
                tmp += chr(j+97-26)
            ans.append(tmp)

print(len(ans))
for i in ans:
    print(i)